FROM python:3.13-slim

WORKDIR /app

COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./worker/worker.py ./tasks.py ./

CMD ["python", "worker.py"]
