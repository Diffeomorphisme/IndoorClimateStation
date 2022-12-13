from fastapi import FastAPI, Depends
from app.core.auth import api_key_auth
from app.routes import api_router

app = FastAPI(
    title="Indoor Climate Monitoring",
    dependencies=[Depends(api_key_auth)]
)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_level='info',
        reload=True
    )
