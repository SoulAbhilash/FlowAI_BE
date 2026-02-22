from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://abhilr_odoo:root@localhost:5432/hard_not_bot"

settings = Settings()