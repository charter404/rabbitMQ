import pika
import json
import time

def get_connection():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Waiting for RabbitMQ...")
            time.sleep(3)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"[x] Processing: {data}")

    # simulate work
    time.sleep(2)

    print("[✔] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = get_connection()
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# fair dispatch
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue='task_queue',
    on_message_callback=callback
)

print(" [*] Worker waiting for tasks...")
channel.start_consuming()
