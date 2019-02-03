import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare("hello")


def callback(ch, method, properties, body):
    print(f" [x]: Received {body}")
    time.sleep(body.count(b"."))
    print(f" [x]: processing done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue="hello")

print("[x] Waiting for messages")

channel.start_consuming()
