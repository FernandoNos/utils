from confluent_kafka import Consumer, KafkaError
from kafka_config import get_config


def config_kafka_consumer():
    host = get_config('host')
    return {
        'bootstrap.servers': host,
        'group.id': 'test-1234',
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
    }


def init_kafka_consumer(configs):
    try:
        c = Consumer(configs)
        print("Connected!")
        c.subscribe(['conecta-manual-notification-message'])
        print("Subscribed!")
        while True:
            msg = c.poll(0.1)
            if msg is None:
                continue
            elif not msg.error():
                print('Received message: {0}'.format(msg.value()))
            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'
                      .format(msg.topic(), msg.partition()))
            else:
                print('Error occured: {0}'.format(msg.error().str()))

    except KeyboardInterrupt:
        return
