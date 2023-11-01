import json
import django
import os
import pika

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def main():
    from convert import views
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='video', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        video_data = json.loads(body.decode())

        error = views.start_convert(video_data, ch)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue='video',
        on_message_callback=callback
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='video', on_message_callback=callback)

    channel.start_consuming()


main()
