# celery_app.py
from __future__ import annotations
import os
from celery import Celery
from env import REDIS_URL, MONGO_URI, RUN_ON_NET

RESULT_MONGO_DB = (
    "concordium_mainnet" if RUN_ON_NET == "mainnet" else "concordium_testnet"
)
RESULT_MONGO_COLLECTION = os.getenv("RESULT_MONGO_COLLECTION", "celery_taskmeta")

app = Celery("ccd")
app.conf.update(
    broker_url=REDIS_URL,
    result_backend=MONGO_URI,
    mongodb_backend_settings={
        "database": RESULT_MONGO_DB,
        "taskmeta_collection": RESULT_MONGO_COLLECTION,
    },
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_acks_late=True,
    task_acks_on_failure_or_timeout=False,
    broker_transport_options={
        "visibility_timeout": int(os.getenv("VISIBILITY_TIMEOUT", "3600")),
    },
    worker_prefetch_multiplier=int(os.getenv("PREFETCH", "1")),
)
