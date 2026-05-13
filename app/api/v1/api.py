from fastapi import APIRouter
from app.api.v1.endpoints import heart_deasies

api_router = APIRouter()
api_router.include_router(heart_deasies.router, tags=["heart_disease"])