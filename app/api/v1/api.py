from fastapi import APIRouter
from app.api.v1.endpoints import auth, ai_flow

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(ai_flow.router, tags=["ai_flow"])
