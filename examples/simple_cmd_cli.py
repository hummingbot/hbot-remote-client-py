#!/usr/bin/env python3

from hbotrc import BotCommands


if __name__ == "__main__":
    import sys
    import json
    if len(sys.argv) < 2:
        print('Give instance_id argument')
        sys.exit(1)
    if len(sys.argv) < 3:
        print('Give command argument')
        sys.exit(1)
    if len(sys.argv) < 4:
        print('Give command parameters')
        sys.exit(1)
    _id = sys.argv[1]
    _cmd = sys.argv[2]
    _params = json.loads(sys.argv[3])
    client = BotCommands(
        host='localhost',
        port=1883,
        username='',
        password='',
        bot_id=_id,
    )
    if _cmd == 'stop':
        resp = client.stop(**_params)
    elif _cmd == 'start':
        resp = client.start(**_params)
    elif _cmd == 'import':
        resp = client.import_strategy(**_params)
    elif _cmd == 'config':
        resp = client.config(**_params)
    elif _cmd == 'status':
        resp = client.status(**_params)
    print(f'[*] Response -> {resp}')
