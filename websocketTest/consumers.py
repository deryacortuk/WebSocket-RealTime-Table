from channels.generic.websocket import AsyncWebsocketConsumer

class RealTimeData(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'realTimeDataTable'

        await self.channel_layer.group_add(

            self.group_name,
            self.channel_name
        )
        await self.accept()
    
    async def receive(self,text_data):

        await self.channel_layer.group_send(
            self.group_name,{
                'type':'dataFunction',
                'value':text_data,
            }
        )
    
    async def dataFunction(self, event):

        print(event['value'])
        await self.send(event['value'])

    async def close(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )