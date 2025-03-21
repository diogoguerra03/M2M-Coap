# coap_server.py
import asyncio
from aiocoap import resource, Message, Context

class SensorResource(resource.Resource):
    async def render_get(self, request):
        try:
            with open("sensor_data.txt", "r") as f:
                data = f.read()
        except FileNotFoundError:
            data = "Sem dados"
        return Message(payload=data.encode())

def main():
    root = resource.Site()
    root.add_resource(['sensor'], SensorResource())
    asyncio.run(Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
