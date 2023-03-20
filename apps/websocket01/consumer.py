from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_name = 'currenttime_channel'
        self.channel_group = 'currenttime_group'
        print(self.channel_name)
        await self.channel_layer.group_add(
            self.channel_group,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.channel_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.channel_name,
            {
                'type': 'send_message',
                'message': text_data,
            }
        )

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=message)