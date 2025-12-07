from typing import Optional, List
from sqlalchemy.orm import Session
from ..models.user_profile import UserProgress, Chapter, Module
from ..schemas.progress import ProgressCreate, ProgressUpdate

class ProgressService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_progress(self, user_id: int, chapter_id: int) -> Optional[UserProgress]:
        """Get user's progress for a specific chapter"""
        return self.db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.chapter_id == chapter_id
        ).first()

    def get_user_module_progress(self, user_id: int, module_id: int) -> List[UserProgress]:
        """Get user's progress for all chapters in a specific module"""
        return self.db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.module_id == module_id
        ).all()

    def get_user_curriculum_progress(self, user_id: int) -> List[UserProgress]:
        """Get user's progress for the entire curriculum"""
        return self.db.query(UserProgress).filter(
            UserProgress.user_id == user_id
        ).all()

    def create_progress_record(self, progress_data: ProgressCreate) -> UserProgress:
        """Create a new progress record"""
        db_progress = UserProgress(
            user_id=progress_data.user_id,
            chapter_id=progress_data.chapter_id,
            module_id=progress_data.module_id,
            completed=progress_data.completed,
            completion_percentage=progress_data.completion_percentage,
            time_spent_seconds=progress_data.time_spent_seconds
        )
        self.db.add(db_progress)
        self.db.commit()
        self.db.refresh(db_progress)
        return db_progress

    def update_progress(self, user_id: int, chapter_id: int, progress_data: ProgressUpdate) -> Optional[UserProgress]:
        """Update user's progress for a specific chapter"""
        db_progress = self.get_user_progress(user_id, chapter_id)
        if db_progress:
            for field, value in progress_data.dict(exclude_unset=True).items():
                setattr(db_progress, field, value)
            
            self.db.commit()
            self.db.refresh(db_progress)
        return db_progress

    def mark_chapter_completed(self, user_id: int, chapter_id: int, module_id: int) -> UserProgress:
        """Mark a chapter as completed"""
        progress = self.get_user_progress(user_id, chapter_id)
        if progress:
            # Update existing record
            progress.completed = True
            progress.completion_percentage = 100
            self.db.commit()
            self.db.refresh(progress)
        else:
            # Create new record
            progress = UserProgress(
                user_id=user_id,
                chapter_id=chapter_id,
                module_id=module_id,
                completed=True,
                completion_percentage=100
            )
            self.db.add(progress)
            self.db.commit()
            self.db.refresh(progress)
        
        return progress

    def calculate_module_completion(self, user_id: int, module_id: int) -> float:
        """Calculate completion percentage for a module"""
        module_chapters = self.db.query(Chapter).filter(Chapter.module_id == module_id).all()
        if not module_chapters:
            return 0.0

        completed_chapters = 0
        for chapter in module_chapters:
            progress = self.get_user_progress(user_id, chapter.id)
            if progress and progress.completed:
                completed_chapters += 1

        return (completed_chapters / len(module_chapters)) * 100

    def calculate_curriculum_completion(self, user_id: int) -> float:
        """Calculate completion percentage for the entire curriculum"""
        all_chapters = self.db.query(Chapter).all()
        if not all_chapters:
            return 0.0

        completed_chapters = 0
        for chapter in all_chapters:
            progress = self.get_user_progress(user_id, chapter.id)
            if progress and progress.completed:
                completed_chapters += 1

        return (completed_chapters / len(all_chapters)) * 100