
from lcu_driver import Connector

connector = Connector()

"""
@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')


@connector.close
async def disconnect(connection):
    print('Finished task')

connector.start()

connector = Connector()
"""

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    print(await summoner.json())

connector.start()


