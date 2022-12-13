from sqlalchemy.orm import Session
from app.database.models import Sensor, Log, LOG_COLUMNS, SENSOR_COLUMNS
from app.sensor.models import SensorLogModel, SensorModel, NewSensorModel


def get_sensor(key: str, db: Session):
    return db.query(Sensor).filter(Sensor.key == key).first()


def insert_data(sensor_log: SensorLogModel, sensor_id, db: Session):
    log = Log(**{c: sensor_log.get(c) for c in LOG_COLUMNS})
    log.sensor_id = sensor_id
    db.add(log)
    db.commit()


def create_new_sensor(sensor: NewSensorModel, db: Session):
    # ids = [sensor.id for sensor in db.query(Sensor).all()]
    ids = db.query(Sensor.id)
    if sensor.id in ids:
        return
    sensor = Sensor(**{c: sensor.get(c) for c in SENSOR_COLUMNS})
    db.add(sensor)
    db.commit()
    return True


def get_sensors_list(db: Session) -> list[SensorModel]:
    sensors = db.query(Sensor).all()
    return [SensorModel(**sensor.get_dict()) for sensor in sensors]
