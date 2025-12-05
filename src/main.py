from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database import Base, engine
from src import handlers
from src.nats_client import nats_client

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await nats_client.connect()
    
    await nats_client.subscribe("exercises.list", handlers.list_exercises)
    await nats_client.subscribe("exercises.create", handlers.create_exercise)
    await nats_client.subscribe("exercises.get", handlers.get_exercise)
    await nats_client.subscribe("exercises.update", handlers.update_exercise)
    await nats_client.subscribe("exercises.delete", handlers.delete_exercise)
    
    yield
    
    await nats_client.close()

app = FastAPI(lifespan=lifespan)