import os

import requests

GATEWAY_BORDER_HOST = "https://run.mocky.io"


def send_request(listen_port, path, token):
    # url = GATEWAY_BORDER_HOST + ":" + str(listen_port) + path
    url = GATEWAY_BORDER_HOST  + path
    response = requests.get(url, headers={'X-DC-AUTH': token})
    return response.json()


def request_token(host, port, ssl, description):
    api_url = "https://run.mocky.io/v3/233b3171-2b9e-494d-8101-a92395949182"
    body = {"host": host, "port": port, "ssl": ssl, "description": "debug " + description}

    response = requests.post(api_url, json=body)
    print("Gateway Boder response: "+str(response.json()))

    return response.json()
