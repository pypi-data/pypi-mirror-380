from dataclasses import asdict
from typing import Callable
from core.soda_client import SodaClient


class SodaProducer:

    def __init__(self, topic: str, client: SodaClient):
        self.topic = topic
        self.soda_client = client
        client.connect()

    def produce(self, message):

        if message is dict:
            d = message
        else:
            d = asdict(message)

        self.soda_client.send_message(self.topic, d)
