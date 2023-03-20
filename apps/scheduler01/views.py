from django.shortcuts import render
from apps.websocket01.routing import application
from channels.testing import WebsocketCommunicator
import asyncio
# Create your views here.
async def task(request):
    print("Se ejecutó correctamente.")
    my_view(request)
    return render(request, 'scheduler.html', {})

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
async def my_view(self):
    channel_layer = get_channel_layer()
    print("chan_layer", channel_layer)

    communicator = WebsocketCommunicator(application, path='ws://localhost:8000/ws/echo/')

    connected, subprotocol = await communicator.connect()
    #self.assertTrue(connected)
    print("Connected", connected)
    if connected:
        print("----> ", "Connected")
        # send a message through the WebSocket connection
        await communicator.send_json_to({'type': 'my_message_type', 'data': 'Hello, World!'})
        
        # close the WebSocket connection
        await communicator.disconnect()
    """
    async_to_sync(channel_layer.send)('currenttime_channel', {'type': 'websocket.connect'})
    # send a message through the WebSocket connection
    async_to_sync(channel_layer.group_send)('currenttime_group', {'type': 'websocket.send', 'text': 'Hello, World!'})
    # close the WebSocket connection
    #async_to_sync(channel_layer.group_send)('currenttime_channel', {'type': 'disconnect'})
    """