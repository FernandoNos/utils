import configparser

class EnvConfig:
  def __init__(self, bootstrapServer, topics):
    self.bootstrapServer = bootstrapServer
    self.topics = topics

def readConfig():
    config = configparser.ConfigParser()
    config.read('envConfigs.ini')
    return config

def availableConfigs():
    config = readConfig()
    return config.sections()

def getEnvConfig(environment):
    config = readConfig()
    bootstrapServer = config['DEV']['BootstrapServer']
    topics = config['DEV']['Topics']
    envConfig = EnvConfig(bootstrapServer,topics)
    print envConfig.topics
    return envConfig