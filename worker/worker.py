import os

from redis import Redis
from rq import Queue, Worker

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
QUEUE_NAME = os.environ.get("QUEUE_NAME", "default")

if __name__ == "__main__":
    conn = Redis.from_url(REDIS_URL)
    queue = Queue(QUEUE_NAME, connection=conn)
    worker = Worker([queue], connection=conn)
    worker.work(with_scheduler=True)
