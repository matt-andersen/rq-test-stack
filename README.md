# RQ Test Stack: Redis + Workers

## Run

```bash
docker compose up --build
```

This starts Redis plus two workers, one consuming the `default` queue, one
consuming `slow`.

Then, start up a separate RQ Dashboard instance:

```bash
rq-dashboard --redis-url redis://localhost:6379/0 --port 9181
```

## Enqueue Test Jobs

From your host (after activating `venv` and running `pip install -r requirements.txt`):

```bash
python queue_jobs.py
```

This enqueues one job on `default` and a second on `slow` that depends on the
first. You'll see it sit as "deferred" in the dashboard until the first job
finishes.

Then open your RQ Dashboard URL to observe job progress.