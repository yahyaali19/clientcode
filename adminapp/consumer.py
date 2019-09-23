import asyncio
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        # Echo the received payload
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


class NoseyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print("Added {} channel to notify".format(self.channel_name))

    # async def disconnect(self):
    #     await self.channel_layer.group_discard("gossip", self.channel_name)
    #     print("Removed {} channel to gossip".format(self.channel_name))

    async def user_gossip(self, event):
        await self.send_json(event)
        print("Got message {} at {}".format(event, self.channel_name))
