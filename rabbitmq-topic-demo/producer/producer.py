import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
ch = conn.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

messages = [
    ('app.error', 'App crashed'),
    ('app.info', 'App started'),
    ('db.error', 'DB connection failed'),
    ('db.info', 'DB connected'),
    ('payment.success', 'Payment completed'),
    ('payment.failed', 'Payment declined')
]

for key, msg in messages:
    ch.basic_publish(
        exchange='topic_logs',
        routing_key=key,
        body=msg
    )
    print(f"Sent [{key}] {msg}")
    time.sleep(1)

conn.close()
