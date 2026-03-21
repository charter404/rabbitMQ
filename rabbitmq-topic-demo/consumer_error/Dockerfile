FROM python:3.9
WORKDIR /app
COPY consumer_error.py .
RUN pip install pika
CMD ["python", "consumer_error.py"]
