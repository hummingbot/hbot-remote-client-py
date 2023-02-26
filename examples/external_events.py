#!/usr/bin/env python3

import asyncio
import time
from hbotrc import BotEventEmitter, ExternalEvent as EEvent


async def send_commands(client):
    event = EEvent(
        name='test.a',
        data={'a': 1, "b": 'b'}
    )
    while True:
        client.send(event)
        await asyncio.sleep(1)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('Give instance_id argument')
    _id = sys.argv[1]
    client = BotEventEmitter(
        host='localhost',
        port=1883,
        username='',
        password='',
        bot_id=_id,
    )
    asyncio.new_event_loop().run_until_complete(send_commands(client))
