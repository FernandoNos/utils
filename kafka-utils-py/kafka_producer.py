from confluent_kafka import Producer


def send_messages():
    try:
        while True:
            message = input("Type in your message: ")
            p = Producer({'bootstrap.servers': 'dev-events-broker-id-1.dev-sicredi.in:9092'})
            p.produce('conecta-manual-notification-message', value=message)
            p.flush(30)
    except KeyboardInterrupt:
        return
