import pika
import json
import time

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"[x] Processing: {data}")

    # simulate work
    time.sleep(2)

    print("[✔] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue='task_queue',
    on_message_callback=callback
)

print(" [*] Waiting for tasks...")
channel.start_consuming()
