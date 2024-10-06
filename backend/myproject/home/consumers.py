import json
from channels.generic.websocket import AsyncWebsocketConsumer
import random
import asyncio
from urllib.parse import parse_qs

class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Parse query parameters
        query_params = parse_qs(self.scope['query_string'].decode())
        self.loop_count = int(query_params.get('loop_count', [10])[0])
        self.data_size = int(query_params.get('data_size', [100])[0])
        
        await self.accept()
        self.is_connected = True
        asyncio.create_task(self.send_random_numbers())

    async def disconnect(self, close_code):
        self.is_connected = False

    async def send_random_numbers(self):
        for _ in range(self.loop_count):
            if not self.is_connected:
                break
            
            binary_data = [random.randint(0, 1) for _ in range(self.data_size)]
            await self.send(text_data=json.dumps({
                'binary_data': binary_data,
            }))
            await asyncio.sleep(1)  # Send a number every second
