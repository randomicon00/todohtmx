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
        # Leave room group
        self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        sender = data["sender"]

        self.channel_layer.group_add(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            },
        )

    def chat_messsage(self, event):
        pass
