from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_name: str = "exercise-service"
    port: int = 8002
    
    nats_url: str = "nats://nats:4222"
    
    database_url: str = "postgresql+psycopg://postgres:postgres@postgres-exercises:5432/exercises"
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()