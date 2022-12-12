from pydantic import BaseModel
from datetime import datetime


class SensorModel(BaseModel):
    sensor_id: int
    sensor_key: str
    temperature: float
    humidity: float
    time: datetime
