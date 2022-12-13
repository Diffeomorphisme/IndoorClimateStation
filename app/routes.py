from fastapi import APIRouter
from app.sensor.endpoints import sensor_router


api_router = APIRouter(prefix="/api")
api_router.include_router(sensor_router)
