        
from core.soda_client import SodaClient


class SodaConsumer:
    
    def __init__(self, topic: str, client: SodaClient):
        self.soda_client = client
        self.topic = topic
        client.connect()
        
    # 使SodaConsumer类可迭代，可以在for循环中消费消息
    def __iter__(self):
        # 假设有一个队列来存储接收到的消息
        if not hasattr(self, "_message_queue"):
            import queue
            self._message_queue = queue.Queue()

            def on_message(message):
                self._message_queue.put(message)
            # 这里默认订阅一个topic，需要在实例化时指定或传参
            if hasattr(self, "topic"):
                topic = self.topic
            else:
                raise AttributeError("请先设置self.topic为要订阅的topic")
            self.soda_client.subscribe(topic, on_message)

        return self

    def __next__(self):
        # 阻塞直到有新消息
        message = self._message_queue.get()
        return message