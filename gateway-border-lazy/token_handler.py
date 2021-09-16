import os


def save_token(access_token):
    try:
    #Replaces whatever's in the file with the incoming token
        with open("access_token.txt","r") as access_token_file:
            access_token_file.seek(0)
            access_token_file.write(access_token)
            access_token_file.truncate()

    except IOError:
        access_token_file = open("access_token.txt", "w")
        access_token_file.write(access_token)
        access_token_file.close()

    #Sets the token as an env variable
    os.environ["DEVCONSOLE_TOKEN"] = access_token


def update_token():
    # pegar o token no devconsole
    access_token = input("Type your access token:")
    save_token(access_token)