from fastapi import APIRouter
from app.sensor.model import SensorModel

sensor_router = APIRouter(tags=["sensors"])


@sensor_router.post("/sensor_udpate")
async def send_readings(sensor_data: SensorModel):
    print(sensor_data.dict())
