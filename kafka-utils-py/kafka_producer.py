from confluent_kafka import Producer
from kafka_config import get_config


def send_messages():
    try:
        host = get_config('host')
        while True:
            message = input("Type in your message: ")
            p = Producer({'bootstrap.servers': host})
            p.produce('conecta-manual-notification-message', value=message)
            p.flush(30)
    except KeyboardInterrupt:
        return
