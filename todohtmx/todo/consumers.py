from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    clients = {}

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        client_type = self.scope["url_route"]["kwargs"]["client_type"]

        # Restrict to one agent and one customer for one on one conversation
        if client_type == "agent":
            if "agent" in ChatConsumer.clients:
                self.close()
                return
            ChatConsumer.clients["agent"] = self.channel_name
        elif client_type == "customer":
            if "customer" in ChatConsumer.clients:
                self.close()
                return
            ChatConsumer.clients["customer"] = self.channel_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Remove from clients
        client_type = self.scope["url_route"]["kwargs"]["client_type"]
        if client_type in ChatConsumer.clients:
            del ChatConsumer.clients[client_type]

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        sender = data["sender"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            },
        )

    def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "sender": sender,
                }
            )
        )
