from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import init_db
from src import handlers
from src.nats_client import nats_client
from src.seed_data import seed_exercises 
from src.seed_data import seed_exercises 
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Exercise Service...")
    
    init_db()
    
    try:
        print("Running seed data...")
        seed_exercises()
    except Exception as e:
        print(f"Seeding failed: {e}")
    
    await nats_client.connect()
    
    await nats_client.subscribe("exercises.list", handlers.list_exercises)
    await nats_client.subscribe("exercises.create", handlers.create_exercise)
    await nats_client.subscribe("exercises.get", handlers.get_exercise)
    await nats_client.subscribe("exercises.update", handlers.update_exercise)
    await nats_client.subscribe("exercises.delete", handlers.delete_exercise)
    
    print("Exercise Service ready!")
    
    yield
    
    print("Shutting down Exercise Service...")
    await nats_client.close()

app = FastAPI(title="Exercise Service", lifespan=lifespan)

Instrumentator().instrument(app).expose(app)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "exercise-service"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)