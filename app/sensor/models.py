from pydantic import BaseModel
from datetime import datetime


class BaseAppModel(BaseModel):
    def get(self, key):
        return getattr(self, key, None)


class SensorLogModel(BaseAppModel):
    key: str
    temperature: float
    humidity: float
    time: datetime


class SensorModel(BaseAppModel):
    key: str
    name: str


class NewSensorModel(SensorModel):
    id: int
