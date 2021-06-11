from confluent_kafka import Producer
from kafka_config import *


def send_messages():
    try:
        host = get_config('host')
        topic = select_topic()
        while True:
            message = input("Type in your message: ")
            p = Producer({'bootstrap.servers': host})
            p.produce(topic, value=message)
            p.flush(30)
    except KeyboardInterrupt:
        return


def select_topic():
    topics = get_topics()
    menu = "Select one topic: \n"

    index = 0
    for topic in topics:
        menu += "{0}. {1}\n".format(str(index), topic)
        index += 1

    menu += "Index: "

    selected_index = int(input(menu))
    return topics[selected_index]