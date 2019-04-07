from kafka import KafkaConsumer
import configHandler

# To consume latest messages and auto-commit offsets

def configMenu(configs):
    result = ''
    for index,config in enumerate(configs,start=0):
        result = result + '{} - {}\n'.format(index,config)
    return result

availableConfigs = configHandler.availableConfigs()

print configMenu(availableConfigs)
configIndex = raw_input('Selecione o ambiente :')

environmentConfig = availableConfigs[int(configIndex)]
envConfig = configHandler.getEnvConfig(environmentConfig)

bootstrap_server = envConfig.bootstrapServer
topic = envConfig.topics
messageFilter = raw_input("Digite as strings pela qual filtrar (separadas por ','):")

print 'connecting...'
consumer = KafkaConsumer(topic,
                         group_id='my-group',
                         bootstrap_servers=[bootstrap_server])
print 'connected!'
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    
    if any(filterString in message.value for filterString in messageFilter.split(',')):
        f=open("messageFile.txt", "a+")
        f.write(message.value+"\n")
        f.close()
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to a regex topic pattern
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')

