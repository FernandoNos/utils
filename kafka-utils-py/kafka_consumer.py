from confluent_kafka import Consumer, KafkaError
from kafka_config import get_config, get_topics


def config_kafka_consumer():
    host = get_config('host')
    return {
        'bootstrap.servers': host,
        'group.id': 'group',
        'enable.auto.commit': True,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    }


def select_topics_to_consume():
    topics = get_topics()
    menu = "Select one or more topics (0,1,2):\n"

    index = 0
    for topic in topics:
        menu += "{0}. {1}\n".format(format(index), topic)
        index += 1

    menu += "Indexes:"

    selected_topics_string_indexes = input(menu).split(',')
    selected_topics_indexes = list(map(int, selected_topics_string_indexes))
    topics = get_topics()
    selected_topics = list(map(lambda i: topics[i], selected_topics_indexes))
    return selected_topics


def init_kafka_consumer(configs):
    try:
        c = Consumer(configs)
        print("Connected!")
        topics = select_topics_to_consume()
        c.subscribe(topics)
        print("Subscribed!")
        while True:
            msg = c.poll(0.1)
            if msg is None:
                continue
            elif not msg.error():
                print('Received message: {0}'.format(msg.value().decode('UTF-8')))
            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'
                      .format(msg.topic(), msg.partition()))
            else:
                print('Error occured: {0}'.format(msg.error().str()))

    except KeyboardInterrupt:
        return
