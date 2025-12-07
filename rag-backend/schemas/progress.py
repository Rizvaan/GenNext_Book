from pydantic import BaseModel
from typing import Optional

class ProgressBase(BaseModel):
    user_id: int
    chapter_id: int
    module_id: int
    completed: bool = False
    completion_percentage: int = 0
    time_spent_seconds: int = 0

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(BaseModel):
    completed: Optional[bool] = None
    completion_percentage: Optional[int] = None
    time_spent_seconds: Optional[int] = None

class ProgressResponse(ProgressBase):
    id: int
    
    class Config:
        from_attributes = True