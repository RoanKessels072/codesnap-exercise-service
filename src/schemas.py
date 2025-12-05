from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class ExerciseBase(BaseModel):
    name: str
    description: str
    difficulty: int
    starter_code: str
    language: str
    function_name: str
    test_cases: List[Any]
    reference_solution: Optional[str] = None

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[int] = None
    starter_code: Optional[str] = None
    language: Optional[str] = None
    function_name: Optional[str] = None
    test_cases: Optional[List[Any]] = None
    reference_solution: Optional[str] = None

class ExerciseResponse(ExerciseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True