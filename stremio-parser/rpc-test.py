import asyncio
from jsonrpc_base import Server


async def routine():
    server = Server('https://api9.strem.io')
    server.foo()

    await server.send_message('')


# {"jsonrpc":"2.0","params":[{"authKey":null,"email":"eovxalkkkkfvyoytzq@wqcefp.com","password":"!"}],"method":"login","id":11759052}

asyncio.get_event_loop().run_until_complete(routine())
