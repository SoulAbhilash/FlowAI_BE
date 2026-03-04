from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://admin:admin@localhost:5432/flow_ai"


settings = Settings()
