import asyncio
from commlib.node import Node
from commlib.transports.mqtt import ConnectionParameters
from typing import Any, List, Optional, Tuple, Callable

from .msgs import *
from .spec import TopicSpecs, CommandTopicSpecs


class BotCommands(Node):
    def __init__(self,
                 bot_id: str,
                 host: str = 'localhost',
                 port: int = 1883,
                 username: str = '',
                 password: str = '',
                 namespace: str = 'hbot',
                 **kwargs
                 ):
        self._bot_id = bot_id
        self._ns = namespace

        topic_prefix = TopicSpecs.PREFIX.format(
            namespace=self._ns,
            instance_id=self._bot_id
        )
        self._start_uri = f'{topic_prefix}{TopicSpecs.COMMANDS.START}'
        self._stop_uri = f'{topic_prefix}{TopicSpecs.COMMANDS.STOP}'
        self._import_uri = f'{topic_prefix}{TopicSpecs.COMMANDS.IMPORT}'

        conn_params = ConnectionParameters(
            host=host,
            port=int(port),
            username=username,
            password=password
        )

        super().__init__(
            node_name=f'{self._ns}.{self._bot_id}',
            connection_params=conn_params,
            heartbeats=False,
            debug=True,
            **kwargs
        )
        self._init_clients()
        self.run()

    def _init_clients(self):
        self._start_cmd = self.create_rpc_client(msg_type=StartCommandMessage,
                                                 rpc_name=self._start_uri)
        print(f'[*] Created RPC client for start command @ {self._start_uri}')
        self._stop_cmd = self.create_rpc_client(msg_type=StopCommandMessage,
                                                rpc_name=self._stop_uri)
        print(f'[*] Created RPC client for stop command @ {self._stop_uri}')
        self._import_cmd = self.create_rpc_client(msg_type=ImportCommandMessage,
                                                  rpc_name=self._import_uri)
        print(f'[*] Created RPC client for import command @ {self._import_uri}')

    def start(self,
              log_level: str = None,
              script: str = None,
              async_backend: bool = False
              ):
        resp = self._start_cmd.call(
            StartCommandMessage.Request(
                log_level=log_level,
                script=script,
                async_backend=async_backend
            )
        )
        return resp

    def stop(self,
             skip_order_cancellation: bool = False,
             async_backend: bool = False
             ):
        resp = self._stop_cmd.call(
            StopCommandMessage.Request(
                skip_order_cancellation=skip_order_cancellation,
                async_backend=async_backend
            )
        )
        return resp

    def import_strategy(self,
                        strategy: str,
                        ):
        resp = self._import_cmd.call(
            ImportCommandMessage.Request(strategy=strategy)
        )
        return resp
