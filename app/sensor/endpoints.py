from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.sensor.models import SensorLogModel, NewSensorModel
from app.database.database import get_db
from app.sensor import crud

sensor_router = APIRouter(tags=["sensors"])


@sensor_router.post("/sensor_udpate")
async def send_readings(sensor_log: SensorLogModel,
                        db: Session = Depends(get_db)):
    print(sensor_log.dict())
    sensor = crud.get_sensor(key=sensor_log.key, db=db)
    if not sensor:
        raise HTTPException(
            status_code=400,
            detail="No sensor with this key"
        )
    crud.insert_data(sensor_log=sensor_log,
                     sensor_id=sensor.id,
                     db=db)


@sensor_router.post("/add_sensor")
async def add_sensor(new_sensor: NewSensorModel,
                     db: Session = Depends(get_db)):
    sensor = crud.get_sensor(key=new_sensor.key, db=db)
    if sensor:
        raise HTTPException(
            status_code=400,
            detail="Sensor already existing with this key"
        )
    sensor_added = crud.create_new_sensor(sensor=new_sensor, db=db)
    if not sensor_added:
        raise HTTPException(
            status_code=400,
            detail="Cannot create sensor with this id"
        )


@sensor_router.get("/get_sensors")
async def get_sensors(db: Session = Depends(get_db)):
    sensors = crud.get_sensors_list(db=db)
    return [sensor.name for sensor in sensors]
