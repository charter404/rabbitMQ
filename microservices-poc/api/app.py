from fastapi import FastAPI
import pika
import json
import time

app = FastAPI()

def get_connection():
    # Retry logic (important in Docker)
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready, retrying...")
            time.sleep(3)

def send_to_queue(message):
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    connection.close()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/send")
def send_task(data: dict):
    send_to_queue(data)
    return {"status": "Task sent", "data": data}
