from redis import Redis
from rq import Queue

from tasks import add, slow_task

conn = Redis.from_url("redis://localhost:6379/0")

default_q = Queue("default", connection=conn)
slow_q = Queue("slow", connection=conn)

job1 = default_q.enqueue(add, 2, 3)
job2 = slow_q.enqueue(slow_task, 10, depends_on=job1)

print("job1:", job1.id)
print("job2:", job2.id, "(waiting on job1)")
