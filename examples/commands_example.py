#!/usr/bin/env python3

import asyncio
from hbotrc import BotListener, BotCommands


async def run_commands(client):
    resp = client.start()
    print(f'Start Command Response: {resp}')
    resp = client.import_strategy('conf_pure_mm')
    print(f'Import Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.import_strategy('conf_pure_mm_1')
    print(f'Import Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.start()
    print(f'Start Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.stop()
    print(f'Stop Command Response: {resp}')
    await asyncio.sleep(1)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('Give instance_id argument')
    _id = sys.argv[1]
    client = BotCommands(
        host='localhost',
        port=1883,
        username='',
        password='',
        bot_id=_id,
    )
    asyncio.new_event_loop().run_until_complete(run_commands(client))
