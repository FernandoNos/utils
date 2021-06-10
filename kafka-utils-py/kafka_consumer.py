from kafka import KafkaConsumer
from confluent_kafka import Consumer, KafkaError

def config_kafka_consumer():
    return {
        'bootstrap.servers': 'dev-events-broker-id-1.dev-sicredi.in:9092',
        'group.id': 'test-1234',
        # 'client.id': 'client-12',
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
        # 'default.topic.config': {'auto.offset.reset': 'smallest'}
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
