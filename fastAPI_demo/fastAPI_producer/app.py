from fastapi import FastAPI
import pika
import json

app = FastAPI()

def send_to_queue(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
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
    return {"message": "FastAPI is running"}

@app.post("/send")
def send_task(data: dict):
    send_to_queue(data)
    return {"status": "Task sent to RabbitMQ", "data": data}
