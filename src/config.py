from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    NATS_URL: str = "nats://nats:4222"

    class Config:
        env_file = ".env"

settings = Settings()