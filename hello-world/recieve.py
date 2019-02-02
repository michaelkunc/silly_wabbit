import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare("hello")


def callback(ch, method, properties, body):
    print(f" [x]: Received {body}")


channel.basic_consume(callback, queue="hello", no_ack=True)

print("[x] Waiting for messages")

channel.start_consuming()
