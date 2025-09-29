# SodaMQ Client

SodaMQ客户端库，用于通过SignalR协议进行消息队列通信。

## 安装

```bash
pip install soda-mq-client
```

## 基本用法

### 创建客户端

```python
from core.soda_client import SodaClient

# 创建SodaMQ客户端
client = SodaClient("http://your-sodamq-server-url")

# 连接到服务器
client.connect()
```

### 发送消息

```python
# 向指定主题发送消息
client.send_message("your-topic", {"key": "value"})
```

### 订阅主题

```python
# 定义消息处理函数
def on_message(message):
    print(f"收到消息: {message}")

# 订阅主题
client.subscribe("your-topic", on_message)
```

### 断开连接

```python
# 断开连接
client.disconnect()
```

## 高级用法

请参考`core`目录下的`soda_producer.py`和`soda_consumer.py`文件了解更多高级用法。

## 许可证

MIT
