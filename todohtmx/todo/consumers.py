from channels.generic.websocket import WebsocketConsumer
import json
from todo.utils import (
    get_room_name,
    get_client_type,
    add_to_group,
    remove_from_group,
    send_group_message,
)


class ChatConsumer(WebsocketConsumer):
    clients = {}

    def connect(self):
        self.room_name = get_room_name(self)
        self.room_group_name = f"chat_{self.room_name}"
        client_type = get_client_type(self)

        if not self.add_client(client_type):
            self.close()
            return

        add_to_group(self)
        self.accept()

    def disconnect(self, close_code):
        self.remove_client(self.get_client_type())
        remove_from_group(self)

    def receive(self, text_data):
        data = json.loads(text_data)
        message, sender = data.get("message"), data.get("sender")

        if message and sender:
            send_group_message(self, message, sender)

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


"""    def get_room_name(self):
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
        )"""
