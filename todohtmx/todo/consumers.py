import json
from channels.generic.websocket import WebsocketConsumer


# TODO complete the implementation
class ChatConsumer(WebSocketConsumer):
    def connect(self):
        pass

    def disconnect(self):
        pass

    def receive(self, text_data):
        pass

    def chat_messsage(self, event):
        pass
