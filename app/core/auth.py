from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from app.core.config import settings

server_key = settings.API_KEY


def api_key_auth(api_key: str = Security(
        APIKeyHeader(name='x-api-key', auto_error=False))):
    if api_key != server_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
