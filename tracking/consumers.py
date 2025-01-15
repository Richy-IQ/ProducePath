from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'tracking_updates'
        self.room_group_name = f'tracking_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        location = data['location']

        # Broadcast location to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_update',
                'location': location
            }
        )

    async def send_update(self, event):
        location = event['location']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'location': location
        }))
