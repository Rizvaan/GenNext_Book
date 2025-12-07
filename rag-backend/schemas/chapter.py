from pydantic import BaseModel
from typing import Optional

class ChapterBase(BaseModel):
    title: str
    content: str
    module_id: int
    order_in_module: int
    difficulty_level: Optional[str] = "beginner"
    tags: Optional[str] = None

class ChapterCreate(ChapterBase):
    pass

class ChapterUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    module_id: Optional[int] = None
    order_in_module: Optional[int] = None
    difficulty_level: Optional[str] = None
    tags: Optional[str] = None

class ChapterResponse(ChapterBase):
    id: int
    
    class Config:
        from_attributes = True