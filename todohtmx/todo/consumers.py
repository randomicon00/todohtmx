from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    clients = {}

    def connect(self):
        self.room_name = self.get_room_name()
        self.room_group_name = f"chat_{self.room_name}"
        client_type = self.get_client_type()

        if not self.add_client(client_type):
            self.close()
            return

        self.add_to_group()
        self.accept()

    def disconnect(self, close_code):
        self.remove_client(self.get_client_type())
        self.remove_from_group()

    def receive(self, text_data):
        data = json.loads(text_data)
        message, sender = data.get("message"), data.get("sender")

        if message and sender:
            self.send_group_message(message, sender)

    def chat_message(self, event):
        self.send_json(
            {
                "message": event["message"],
                "sender": event["sender"],
            }
        )

    def add_client(self, client_type):
        if client_type in ChatConsumer.clients:
            return False
        ChatConsumer.clients[client_type] = self.channel_name
        return True

    def remove_client(self, client_type):
        ChatConsumer.clients.pop(client_type, None)

    # Helper Methods
    def get_room_name(self):
        return self.scope["url_route"]["kwargs"]["room_name"]

    def get_client_type(self):
        return self.scope["url_route"]["kwargs"]["client_type"]

    def add_to_group(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

    def remove_from_group(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def send_group_message(self, message, sender):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            },
        )
