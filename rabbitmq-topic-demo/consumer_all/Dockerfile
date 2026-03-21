FROM python:3.9
WORKDIR /app
COPY consumer_all.py .
RUN pip install pika
CMD ["python", "consumer_all.py"]
