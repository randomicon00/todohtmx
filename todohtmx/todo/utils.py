from asgiref.sync import async_to_sync


# Helper Methods
def get_room_name(consumer):
    return consumer.scope["url_route"]["kwargs"]["room_name"]


def get_client_type(consumer):
    return consumer.scope["url_route"]["kwargs"]["client_type"]


def add_to_group(consumer):
    async_to_sync(consumer.channel_layer.group_add)(
        consumer.room_group_name, consumer.channel_name
    )


def remove_from_group(consumer):
    async_to_sync(consumer.channel_layer.group_discard)(
        consumer.room_group_name, consumer.channel_name
    )


def send_group_message(consumer, message, sender):
    async_to_sync(consumer.channel_layer.group_send)(
        consumer.room_group_name,
        {
            "type": "chat_message",
            "message": message,
            "sender": sender,
        },
    )
