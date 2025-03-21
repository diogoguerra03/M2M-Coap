# ble_reader.py
import asyncio
from bleak import BleakScanner
import datetime

TARGET_NAME = "SensorBLE"  # Nome definido no NRF Connect

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        if TARGET_NAME in d.name:
            data = f"{datetime.datetime.now()}: {d.name} ({d.address}) RSSI={d.rssi}"
            print("Found:", data)
            with open("sensor_data.txt", "w") as f:
                f.write(data)
            break
    else:
        print("Sensor BLE não encontrado.")

if __name__ == "__main__":
    asyncio.run(run())
