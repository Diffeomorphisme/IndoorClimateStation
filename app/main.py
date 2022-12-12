from fastapi import FastAPI, Depends
from app.sensor.endpoints import sensor_router
from app.core.auth import api_key_auth

app = FastAPI(
    title="Indoor Climate Monitoring",
    dependencies=[Depends(api_key_auth)]
)
app.include_router(sensor_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_level='info',
        reload=True
    )
