from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    clients = {}

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        client_type = self.scope["url_route"]["kwargs"]["client_type"]

        if not self.add_client(client_type):
            self.close()
            return

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        client_type = self.scope["url_route"]["kwargs"]["client_type"]
        self.remove_client(client_type)

        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message")
        sender = data.get("sender")

        if message and sender:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "sender": sender,
                },
            )

    def chat_message(self, event):
        self.send_json({
            "message": event["message"],
            "sender": event["sender"],
        })

    def add_client(self, client_type):
        if client_type in ChatConsumer.clients:
            return False
        ChatConsumer.clients[client_type] = self.channel_name
        return True

    def remove_client(self, client_type):
        ChatConsumer.clients.pop(client_type, None)
