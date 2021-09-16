from token_handler import update_token
from api_handler import request_api

def start():
    while True:
        update_token()
        request_api()
