from sqlalchemy import Column, Integer, Float
from sqlalchemy import String, ForeignKey, Identity, DateTime
from app.database.base import Base


SENSOR_COLUMNS = {
    "id",
    "key"
}

LOG_COLUMNS = {
    "id",
    "user_id",
    "address",
    "user"
}


class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    key = Column(String(30))

    def get_dict(self):
        return {c: getattr(self, c) for c in SENSOR_COLUMNS}


class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, Identity(), primary_key=True)
    sensor_id = Column(Integer, ForeignKey("sensor.id"), nullable=False)
    temperature = Column(Float)
    humidity = Column(Float)
    time = Column(DateTime)

    def get_dict(self):
        return {c: getattr(self, c) for c in LOG_COLUMNS}


sensor = Sensor()
log = Log()
