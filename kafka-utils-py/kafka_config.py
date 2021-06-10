import yaml

environment = 'DEV'
all_configs = {}
config = {}

with open('config.yml') as f:

    all_configs = yaml.load(f, Loader=yaml.FullLoader)
    environment = all_configs['DEFAULT']['default_environment']
    config = all_configs[environment]


def get_environment():
    global environment
    return environment


def get_config(config_path):
    global config
    global environment

    return all_configs[environment][config_path]


def init_config():
    change_environment()


def change_environment():
    global environment
    global config

    env = input("Choose the environment: \n"
                "1. DEV \n"
                "2. TST \n"
                "3. UAT\n"
                "Env: ")

    if env == '1':
        environment = 'DEV'
    elif env == '2':
        environment = 'TST'
    elif env == '3':
        environment = 'UAT'

    config = all_configs[environment]
