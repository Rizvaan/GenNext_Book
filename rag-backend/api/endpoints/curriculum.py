from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from ..database import get_db
from ..models.user_profile import Module, Chapter, Curriculum, UserProgress
from ..services.progress_service import ProgressService

router = APIRouter()

class ModuleResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    order_in_curriculum: int
    prerequisites: Optional[str]
    chapter_count: int

class CurriculumResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    modules: List[ModuleResponse]

class UserProgressResponse(BaseModel):
    module_id: int
    completed_chapters: int
    total_chapters: int
    completion_percentage: float

@router.get("/curriculum/{curriculum_id}", response_model=CurriculumResponse)
async def get_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    """
    Get curriculum with modules and chapter counts
    """
    curriculum = db.query(Curriculum).filter(Curriculum.id == curriculum_id).first()
    if not curriculum:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curriculum not found"
        )
    
    modules = db.query(Module).filter(Module.id == curriculum_id).order_by(Module.order_in_curriculum).all()
    
    module_responses = []
    for module in modules:
        chapters_count = db.query(Chapter).filter(Chapter.module_id == module.id).count()
        module_responses.append(ModuleResponse(
            id=module.id,
            title=module.title,
            description=module.description,
            order_in_curriculum=module.order_in_curriculum,
            prerequisites=module.prerequisites,
            chapter_count=chapters_count
        ))
    
    return CurriculumResponse(
        id=curriculum.id,
        name=curriculum.name,
        description=curriculum.description,
        modules=module_responses
    )

@router.get("/modules/{module_id}/chapters")
async def get_module_chapters(module_id: int, db: Session = Depends(get_db)):
    """
    Get all chapters for a specific module
    """
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )
    
    chapters = db.query(Chapter).filter(Chapter.module_id == module_id).order_by(Chapter.order_in_module).all()
    
    return {
        "module_id": module_id,
        "module_title": module.title,
        "chapters": [
            {
                "id": ch.id,
                "title": ch.title,
                "order_in_module": ch.order_in_module,
                "difficulty_level": ch.difficulty_level
            }
            for ch in chapters
        ]
    }

@router.get("/user/{user_id}/progress")
async def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    """
    Get user's progress across all modules in the curriculum
    """
    # Get all modules
    all_modules = db.query(Module).all()
    
    progress_list = []
    for module in all_modules:
        # Get all chapters in the module
        module_chapters = db.query(Chapter).filter(Chapter.module_id == module.id).all()
        total_chapters = len(module_chapters)
        
        # Get completed chapters for this user and module
        completed_chapters_count = 0
        for chapter in module_chapters:
            progress = db.query(UserProgress).filter(
                UserProgress.user_id == user_id,
                UserProgress.chapter_id == chapter.id,
                UserProgress.completed == True
            ).count()
            
            if progress > 0:
                completed_chapters_count += 1
        
        completion_percentage = (completed_chapters_count / total_chapters * 100) if total_chapters > 0 else 0
        
        progress_list.append(UserProgressResponse(
            module_id=module.id,
            completed_chapters=completed_chapters_count,
            total_chapters=total_chapters,
            completion_percentage=completion_percentage
        ))
    
    return {
        "user_id": user_id,
        "progress": progress_list
    }

@router.get("/user/{user_id}/next")
async def get_next_recommendation(user_id: int, db: Session = Depends(get_db)):
    """
    Get the next recommended module/chapter for the user
    """
    # Find the first incomplete module
    modules = db.query(Module).order_by(Module.order_in_curriculum).all()
    
    for module in modules:
        # Check if user has started this module
        progress_in_module = db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.module_id == module.id
        ).first()
        
        if not progress_in_module:
            # User hasn't started this module yet
            return {
                "recommended_type": "module",
                "module_id": module.id,
                "module_title": module.title,
                "message": "Start a new module"
            }
        
        # Get all chapters in the module
        module_chapters = db.query(Chapter).filter(Chapter.module_id == module.id).order_by(Chapter.order_in_module).all()
        
        # Find the first incomplete chapter
        for chapter in module_chapters:
            chapter_progress = db.query(UserProgress).filter(
                UserProgress.user_id == user_id,
                UserProgress.chapter_id == chapter.id
            ).first()
            
            if not chapter_progress or not chapter_progress.completed:
                # Found a chapter that hasn't been completed
                return {
                    "recommended_type": "chapter",
                    "module_id": module.id,
                    "module_title": module.title,
                    "chapter_id": chapter.id,
                    "chapter_title": chapter.title,
                    "message": "Continue with the next chapter"
                }
    
    return {
        "recommended_type": "complete",
        "message": "Congratulations! You've completed the entire curriculum."
    }