from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumer import EchoConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/echo/', EchoConsumer.as_asgi()),
    ]),
})