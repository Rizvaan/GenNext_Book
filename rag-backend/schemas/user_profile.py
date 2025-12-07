from pydantic import BaseModel
from typing import Optional

class UserProfileBase(BaseModel):
    skill_level: Optional[str] = "beginner"
    background: Optional[str] = None
    learning_preferences: Optional[str] = None
    preferred_language: Optional[str] = "en"

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(BaseModel):
    skill_level: Optional[str] = None
    background: Optional[str] = None
    learning_preferences: Optional[str] = None
    preferred_language: Optional[str] = None

class UserProfileResponse(UserProfileBase):
    id: int
    user_id: int
    
    class Config:
        from_attributes = True