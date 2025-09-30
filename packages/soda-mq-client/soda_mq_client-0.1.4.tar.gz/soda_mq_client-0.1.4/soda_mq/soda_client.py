import asyncio
import logging
from typing import AsyncIterable

from signalrcore.hub_connection_builder import HubConnectionBuilder
from signalrcore.protocol.messagepack_protocol import MessagePackHubProtocol



class SodaClient:

    def __init__(self, server_url: str):
        self._server_url = server_url
        self._connected = False
        self.hub_connection = HubConnectionBuilder() \
            .with_url(hub_url=server_url) \
            .with_hub_protocol(MessagePackHubProtocol()) \
            .configure_logging(logging.DEBUG) \
            .build()

    @property
    def is_connected(self) -> bool:
        return self.hub_connection.transport and self.hub_connection.transport.is_running

    def connect(self):
        return self.hub_connection.start()

    def disconnect(self):
        return self.hub_connection.stop()

    def send_message(self, topic: str, message: dict) -> None:
        self.hub_connection.send("AppendOnTopic", [topic, message])

    def subscribe(self, topic: str, on_message):
        # self.hub_connection.on("ListenToTopic", on_message)
        x = self.hub_connection.stream(
            "ListenToTopic",
            [topic],
        )

        def next_call_back(message):
            # print("next_call_back", message)
            on_message(message)

        def error_call_back(error):
            print("error_call_back", error)

        def complete_call_back():
            print("complete_call_back")

        x.subscribe({
            "next": next_call_back,
            "error": error_call_back,
            "complete": complete_call_back
        })
