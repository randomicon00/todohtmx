import json
from channels.generic.websocket import WebsocketConsumer


# TODO complete the implementation
class ChatConsumer(WebSocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        self.channel_layer.group_add(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self):
        # TODO leave room group using channel_layer
        pass

    def receive(self, text_data):
        pass

    def chat_messsage(self, event):
        pass
