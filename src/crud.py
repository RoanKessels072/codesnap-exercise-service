from sqlalchemy.orm import Session
from src.models import Exercise
from src.schemas import ExerciseCreate, ExerciseUpdate

def get_all_exercises(db: Session):
    return db.query(Exercise).all()

def get_exercise_by_id(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()

def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = Exercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def update_exercise(db: Session, exercise_id: int, exercise_data: ExerciseUpdate):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not db_exercise:
        return None
    
    update_data = exercise_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_exercise, key, value)
    
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def delete_exercise(db: Session, exercise_id: int):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not db_exercise:
        return False
    db.delete(db_exercise)
    db.commit()
    return True