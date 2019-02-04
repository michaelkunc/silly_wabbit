import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare("task_queue", durable=True)


def callback(ch, method, properties, body):
    print(f" [x]: Received {body}")
    time.sleep(body.count(b"."))
    print(f" [x]: processing done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue="task_queue")

print("[x] Waiting for messages")

channel.start_consuming()
