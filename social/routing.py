from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#import chat.routing
from chat.consumers import ChatConsumer
from django.conf.urls import url
from django.urls import re_path

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/chat/(?P<room_name>\w+)/', ChatConsumer),
            ]
        )
    ),
})
