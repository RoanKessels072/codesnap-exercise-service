import nats
import json
from config import settings

class NATSClient:
    def __init__(self):
        self.nc = None
        
    async def connect(self):
        self.nc = await nats.connect(settings.NATS_URL)
        print(f"✓ Connected to NATS at {settings.NATS_URL}")
        
    async def close(self):
        if self.nc:
            await self.nc.close()

    async def subscribe(self, subject: str, handler):
        async def message_handler(msg):
            try:
                data = json.loads(msg.data.decode()) if msg.data else {}
                
                response = await handler(data)
                
                if msg.reply and response is not None:
                    await self.nc.publish(
                        msg.reply, 
                        json.dumps(response, default=str).encode()
                    )
            except Exception as e:
                print(f"Error handling message on {subject}: {e}")
                error_response = {"error": str(e)}
                if msg.reply:
                    await self.nc.publish(
                        msg.reply,
                        json.dumps(error_response).encode()
                    )
        
        await self.nc.subscribe(subject, cb=message_handler)
        print(f"Subscribed to {subject}")

nats_client = NATSClient()