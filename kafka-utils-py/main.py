
from kafka_consumer import *

if __name__ == '__main__':

    while True:
        print("\n ############################# \n")
        option = input("1. consume from topics\n"
                       "2. write to topic\n"
                       "3. add new configuration\n"
                       "Choose an action: ")
        if option == '1':
            configs = config_kafka_consumer()
            init_kafka_consumer(configs)
        elif option == '2':
            print("TODO WRITER")
        elif option == '3':
            print("TODO NEW CONFIG")
        else:
            print("Unknown option!")
    print("Finished")
