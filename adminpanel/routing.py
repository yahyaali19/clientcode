from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from adminapp.consumer import NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoseyConsumer),
    ])
})
