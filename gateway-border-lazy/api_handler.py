# salvar em arquivo o token
# solicitar a api que quer chamar
# extrair o host - e gerar o token + host no gateway border
# salvar o token, com o horário para validação de 30 mins
import re
import time
from datetime import datetime

from gateway_border_client import request_token, send_request

API_TOKENS = {}


def request_api():
    api_endpoint = "https://run.mocky.io/v3/de37863a-4710-433f-9422-ad6c3f97a7dd"

    # api_endpoint = input("Endpoint:")
    (host, path, port) = extract_host(api_endpoint)
    (token, listen_port) = get_token(host, port)

    response = send_request(listen_port, path, token)
    print("#################################")
    print(response)


def get_token(host, port):

    if host not in API_TOKENS:
        (token, listen_port) = request_new_gateway_token(host, port)
        save_tokens(host, token, listen_port)
    else:
        api_details = API_TOKENS[host]
        creation_date = api_details[2]
        difference_from_now = datetime.now() - creation_date
        difference_in_minutes = difference_from_now.total_seconds() / 60

        if difference_in_minutes >= 30:
            (token, listen_port) = request_new_gateway_token(host, port)
            save_tokens(host, token, listen_port)
        else:
            token = api_details[0]
            listen_port = api_details[1]

    return token, listen_port

def request_new_gateway_token(host, port):
    response = request_token(host, port, "true", host)
    token = response['token']
    listen_port = response['listenPort']
    return token, listen_port

def save_tokens(host, token, listen_port):
    API_TOKENS[host] = (token, listen_port, datetime.now())


def extract_host(api_endpoint):
    pattern = r"(https?)://([\w\.]+)([\:0-9]+)?(.*)"
    if re.match(pattern, api_endpoint):
        api_protocol = re.search(pattern, api_endpoint).group(1)

        api_host = re.search(pattern, api_endpoint).group(2)
        api_port = re.search(pattern, api_endpoint).group(3)
        api_path = re.search(pattern, api_endpoint).group(4)
        api_port = extract_port(api_protocol, api_port)

        return api_host, api_path, api_port

    else:
        print("Invalid endpoint format!")
        return ()


def extract_port(protocol, port):
    if port:
        return port.replace(':', '')
    if protocol == 'http':
        return "8080"
    if protocol == 'https':
        return "443"
    return ""
