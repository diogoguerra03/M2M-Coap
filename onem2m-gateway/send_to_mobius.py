# send_to_mobius.py
import asyncio
from aiocoap import *

async def send():
    with open("sensor_data.txt", "r") as f:
        content = f.read()

    payload = {
        "m2m:cin": {
            "con": content
        }
    }

    json_payload = str(payload).replace("'", '"')  # JSON válido
    request = Message(code=POST,
                      uri="coap://<MOBIUS_IP>:5683/~/in-cse/in-name/GatewayMN/SensorData",
                      payload=json_payload.encode(),
                      content_format=50)  # 50 = application/json

    request.opt.uri_query = ("rcn=0",)
    request.opt.accept = 50
    request.opt.content_format = 50

    context = await Context.create_client_context()
    response = await context.request(request).response
    print("Resposta:", response.payload.decode())

if __name__ == "__main__":
    asyncio.run(send())
