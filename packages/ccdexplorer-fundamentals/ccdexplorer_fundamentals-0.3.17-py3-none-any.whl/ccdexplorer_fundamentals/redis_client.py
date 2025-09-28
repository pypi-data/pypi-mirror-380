#!/usr/bin/env python3
from __future__ import annotations

import asyncio
import contextlib
import json
import os
import socket
import sys

from typing import Callable, Optional

from env import REDIS_URL, RUN_LOCAL, RUN_ON_NET
from pydantic import BaseModel, computed_field
from redis.asyncio import Redis
from redis.exceptions import ResponseError


class Settings(BaseModel):
    processor: str

    redis_url: Optional[str] = REDIS_URL

    stream_prefix: str = os.getenv("STREAM_PREFIX", "blocks")
    group_prefix: str = os.getenv("GROUP_PREFIX", "workers")

    block_ms: int = int(os.getenv("XREAD_BLOCK_MS", "5000"))
    count: int = int(os.getenv("XREAD_COUNT", "32"))
    reclaim_idle_ms: int = int(os.getenv("RECLAIM_MIN_IDLE_MS", "2000"))
    reclaim_batch: int = int(os.getenv("RECLAIM_BATCH", "200"))
    trim_maxlen: int = int(os.getenv("STREAM_TRIM_MAXLEN", "100000"))
    health_log_secs: int = int(os.getenv("HEALTH_LOG_SECS", "300"))
    test_xadd_on_boot: str = os.getenv("TEST_XADD_ON_BOOT", "false").lower()

    model_config = {"arbitrary_types_allowed": True}

    @computed_field
    @property
    def consumer(self) -> str:
        host = socket.gethostname()
        consumer: str = os.getenv(
            "CONSUMER", f"{RUN_ON_NET}-{self.processor}-{RUN_LOCAL}-{host}"
        )
        return consumer


class RedisClient:
    def __init__(self, processor: str):
        self.processor = processor
        self.settings = Settings(processor=processor)

        self.stream = (
            f"{self.settings.stream_prefix}:{self.settings.processor}:{RUN_ON_NET}"
        )
        self.group = (
            f"{self.settings.group_prefix}:{self.settings.processor}:{RUN_ON_NET}"
        )

        self.r: Redis = Redis.from_url(self.settings.redis_url, db=0, decode_responses=False)  # type: ignore
        self._health_task: Optional[asyncio.Task] = None

    async def __aenter__(self):
        try:
            await self.r.client_setname(
                f"worker:{self.stream}:{self.group}:{self.settings.consumer}"
            )
        except Exception:
            pass
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def ensure_group(self, start_id: str = "0-0") -> None:
        """Create the group once. Never SETID afterwards."""
        try:
            await self.r.xgroup_create(
                self.stream, self.group, id=start_id, mkstream=True
            )
            print(
                f"[{self.settings.processor}] group created (start_id={start_id})",
                file=sys.stderr,
            )
        except ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise

    async def _decode_payload(self, fields: dict[bytes, bytes]) -> dict:
        """Best-effort JSON decode from 'data' field; raise to keep message pending on failure."""
        raw = fields.get(b"data") or fields.get("data")  # type: ignore
        if raw is None:
            # If you want to treat missing payload as success, return {} instead.
            raise ValueError("missing 'data' field")
        if isinstance(raw, (bytes, bytearray)):
            s = raw.decode(
                "utf-8", errors="strict"
            )  # strict → fail fast; keeps at-least-once
        else:
            s = str(raw)
        return json.loads(s)

    async def _process_one(
        self,
        msg_id: bytes | str,
        fields: dict[bytes, bytes],
        handle_payload: Callable[[dict], "asyncio.Future"],
    ) -> bool:
        """
        Returns True if processed successfully (we will ACK),
        False on any error (we will NOT ACK → stays pending).
        """
        try:
            payload = await self._decode_payload(fields)
            await handle_payload(payload)
            return True
        except Exception as e:
            # At-least-once semantics: do NOT ack on failure.
            # Log context; keep concise to avoid log storms.
            print(
                f"[{self.settings.processor}] process error id={msg_id} err={e!r}",
                file=sys.stderr,
            )
            return False

    async def _read(self, streams: dict[str, str], *, count: int, block_ms: int):
        """Wrapper for XREADGROUP; returns [] on timeout."""
        try:
            return (
                await self.r.xreadgroup(
                    groupname=self.group,
                    consumername=self.settings.consumer,
                    streams=streams,  # type: ignore
                    count=count,
                    block=block_ms,
                )
                or []
            )
        except ResponseError as e:
            print(
                f"[{self.settings.processor}] xreadgroup error: {e!r}", file=sys.stderr
            )
            return []

    async def pump_once(
        self, handle_payload: Callable[[dict], "asyncio.Future"]
    ) -> int:
        """
        One cycle:
          1) Drain this consumer's PEL (start='0').
          2) Read new entries (start='>').
          ACK only on successful processing.
        """
        processed = 0

        # 1) Drain own PEL
        resp = await self._read(
            {self.stream: "0"}, count=self.settings.count, block_ms=1
        )
        if resp:
            _, entries = resp[0]
            for msg_id, fields in entries:
                ok = await self._process_one(msg_id, fields, handle_payload)
                if ok:
                    try:
                        await self.r.xack(self.stream, self.group, msg_id)
                    except Exception as e:
                        print(
                            f"[{self.settings.processor}] xack error id={msg_id} err={e!r}",
                            file=sys.stderr,
                        )
                processed += 1
            if processed:
                return processed

        # 2) Read new messages
        resp = await self._read(
            {self.stream: ">"},
            count=self.settings.count,
            block_ms=self.settings.block_ms,
        )
        if resp:
            _, entries = resp[0]
            for msg_id, fields in entries:
                ok = await self._process_one(msg_id, fields, handle_payload)
                if ok:
                    try:
                        await self.r.xack(self.stream, self.group, msg_id)
                    except Exception as e:
                        print(
                            f"[{self.settings.processor}] xack error id={msg_id} err={e!r}",
                            file=sys.stderr,
                        )
                processed += 1

        return processed

    async def run(self, handle_payload: Callable, health: bool = False) -> None:
        await self.ensure_group(start_id="0-0")
        if health:
            self.start_health()
        while True:
            await self.pump_once(handle_payload)

    async def health_log_task(self):
        while True:
            try:
                groups = await self.r.xinfo_groups(self.stream)
                consumers = await self.r.xinfo_consumers(self.stream, self.group)
                print(f"[health:{self.processor}] groups={groups}", file=sys.stderr)
                print(
                    f"[health:{self.processor}] consumers={consumers}", file=sys.stderr
                )
            except Exception as e:
                print(f"[health:{self.processor}] error: {e!r}", file=sys.stderr)
            await asyncio.sleep(30)

    def start_health(self) -> None:
        if not self._health_task:
            self._health_task = asyncio.create_task(self.health_log_task())

    async def close(self) -> None:
        if self._health_task:
            self._health_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self._health_task
        await self.r.aclose()
