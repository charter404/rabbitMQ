FROM python:3.9
WORKDIR /app
COPY consumer_payment.py .
RUN pip install pika
CMD ["python", "consumer_payment.py"]
