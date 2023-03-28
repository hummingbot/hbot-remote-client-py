#!/usr/bin/env python3

import asyncio
from hbotrc import BotListener


def on_notification(msg):
    _text = msg.msg
    print(f'[NOTIFICATION] - {_text}')


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('Give instance_id argument')
    _id = sys.argv[1]
    client = BotListener(
        host='localhost',
        port=1883,
        username='',
        password='',
        bot_id=_id,
        notifications=True,
        events=True,
        logs=True,
        on_notification=on_notification
    )
    asyncio.new_event_loop().run_until_complete(client.run_forever())
