# hbot-remote-client-py
Package that implements a remote client for hummingbot in Python.

You can use this client to implement remote control and monitoring software of multi-bot
environments using the MQTT feature of hummingbot.

## Usage

### Commands

The `BotCommands` class provides methods for calling bot commands.
Each instance is bound to a specific bot instance.

```python
def __init__(self,
             bot_id: str,
             host: str = 'localhost',
             port: int = 1883,
             username: str = '',
             password: str = '',
             namespace: str = 'hbot',
             **kwargs
             ):

```

Below is an example of using the `BotCommands` class to send commands to a bot

```python
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
    resp = client.config([('bid_spread', 0.1), ('ask_spread', 0.1)])
    print(f'Config Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.start()
    print(f'Start Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.status()
    print(f'Status Command Response: {resp}')
    await asyncio.sleep(1)
    resp = client.history()
    print(f'History Command Response: {resp}')
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
```

### Monitoring Interfaces

The `BotListener` class provides methods for subscribing to notifications,
internal events (e.g. market events), logs and heartbeat messages for a specific
bot instance.

```python
    def __init__(self,
                 host: str = 'localhost',
                 port: int = 1883,
                 username: str = '',
                 password: str = '',
                 bot_id: str = 'bot1',
                 namespace: str = 'hbot',
                 notifications: bool = True,
                 events: bool = True,
                 logs: bool = True,
                 on_notification: Optional[Callable[[NotifyMessage], None]] = None,
                 on_event: Optional[Callable[[EventMessage], None]] = None,
                 on_log: Optional[Callable[[EventMessage], None]] = None,
                 **kwargs

```

Below is an example of using the `BotListener` class to listen to bot events and
notifications.

```python
import asyncio
from hbotrc import BotListener


def on_notification(msg):
    _text = msg.msg
    print(f'[NOTIFICATION] - {_text}')

def on_event(msg):
    print(f'[EVENT] - {event}')

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
        on_notification=on_notification,
        on_event=on_event
    )
    asyncio.new_event_loop().run_until_complete(client.run_forever())

```


## Examples

Head to the `./examples` directory for more examples.
