from src.database import SessionLocal
from src import crud, schemas

async def list_exercises(data: dict):
    db = SessionLocal()
    try:
        exercises = crud.get_all_exercises(db)
        return [schemas.ExerciseResponse.from_orm(e).dict() for e in exercises]
    finally:
        db.close()

async def create_exercise(data: dict):
    db = SessionLocal()
    try:
        exercise_in = schemas.ExerciseCreate(**data)
        new_exercise = crud.create_exercise(db, exercise_in)
        return schemas.ExerciseResponse.from_orm(new_exercise).dict()
    finally:
        db.close()

async def get_exercise(data: dict):
    exercise_id = data.get("id")
    if not exercise_id:
        return {"error": "Missing exercise ID"}

    db = SessionLocal()
    try:
        exercise = crud.get_exercise_by_id(db, exercise_id)
        if exercise:
            return schemas.ExerciseResponse.from_orm(exercise).dict()
        return {"error": "Exercise not found"}
    finally:
        db.close()

async def update_exercise(data: dict):
    exercise_id = data.get("id")
    if not exercise_id:
        return {"error": "Missing exercise ID"}

    db = SessionLocal()
    try:
        update_in = schemas.ExerciseUpdate(**data)
        updated = crud.update_exercise(db, exercise_id, update_in)
        if updated:
            return schemas.ExerciseResponse.from_orm(updated).dict()
        return {"error": "Exercise not found"}
    finally:
        db.close()

async def delete_exercise(data: dict):
    exercise_id = data.get("id")
    db = SessionLocal()
    try:
        success = crud.delete_exercise(db, exercise_id)
        if success:
            return {"status": "success", "message": "Deleted"}
        return {"error": "Exercise not found"}
    finally:
        db.close()