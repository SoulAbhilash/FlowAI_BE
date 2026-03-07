# start cmd >> uvicorn app.main:app --host 0.0.0.0 --port 8000
# todays access token >> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBhcHAuY29tIiwiZXhwIjoxNzcyOTUxMjM1fQ.K1baUGaWdn-tFWvSa-gHXAz45oOia9-yfxQuzyOpJgk

from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.base import Base
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


app.include_router(api_router, prefix="/api/v1")
