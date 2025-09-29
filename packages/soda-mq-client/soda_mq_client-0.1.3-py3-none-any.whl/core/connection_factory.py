from core.soda_client import SodaClient
from core.soda_consumer import SodaConsumer
from core.soda_producer import SodaProducer


class ClientFactory:
    
    def __init__(self, url: str):
        self.clients = {}
        self.url = url
    
    def create_soda_client(self, topic: str):
        client = self.clients.get(topic)
        if client is None:
            client = SodaClient(self.url)
            self.clients[topic] = client
        return client
    
    def create_soda_producer(self, topic: str):
        return SodaProducer(topic, self.create_soda_client(topic))
    
    def create_soda_consumer(self, topic: str):
        return SodaConsumer(topic, self.create_soda_client(topic))

    def _foo():
        pass