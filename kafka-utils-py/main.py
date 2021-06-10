
from kafka_consumer import *
from kafka_producer import *
from kafka_config   import *

if __name__ == '__main__':

    while True:
        environment = get_environment()
        print("\n ########## ENV: {0} ########## \n".format(environment))
        option = input("1. consume from topics\n"
                       "2. write to topic\n"
                       "3. change config\n"
                       "Choose an action: ")
        if option == '1':
            configs = config_kafka_consumer()
            init_kafka_consumer(configs)
        elif option == '2':
            send_messages()
        elif option == '3':
            init_config()
        else:
            print("Unknown option!")
    print("Finished")
