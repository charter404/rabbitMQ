import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
ch = conn.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

q = ch.queue_declare(queue='', exclusive=True)
queue_name = q.method.queue

ch.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='*.error')

def callback(ch, method, properties, body):
    print(f"[ERROR] {method.routing_key}: {body.decode()}")

ch.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for error logs...")
ch.start_consuming()
