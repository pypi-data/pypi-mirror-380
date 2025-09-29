from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

ping_router = APIRouter(prefix="/ping")

class PingResponse(BaseModel):
    status: int
    message: Optional[str] = None

@ping_router.get("", response_model=PingResponse)
async def ping_endpoint():
    return PingResponse(status=200)