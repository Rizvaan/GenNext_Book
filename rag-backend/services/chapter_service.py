from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.user_profile import Chapter, UserProgress
from ..schemas.chapter import ChapterCreate, ChapterUpdate
from ..utils.logging import log_with_context, logger


class ChapterService:
    def __init__(self, db: Session):
        self.db = db

    def get_chapter(self, chapter_id: int) -> Optional[Chapter]:
        """Get chapter by ID"""
        return self.db.query(Chapter).filter(Chapter.id == chapter_id).first()

    def get_chapters_by_module(self, module_id: int) -> List[Chapter]:
        """Get all chapters for a specific module"""
        return self.db.query(Chapter).filter(Chapter.module_id == module_id).order_by(Chapter.order_in_module).all()

    def get_chapters_by_difficulty(self, difficulty_level: str) -> List[Chapter]:
        """Get all chapters with a specific difficulty level"""
        return self.db.query(Chapter).filter(Chapter.difficulty_level == difficulty_level).all()

    def get_chapters_by_user_level(self, user_skill_level: str) -> List[Chapter]:
        """Get chapters appropriate for a user's skill level"""
        # Map user skill level to acceptable difficulty levels
        level_mapping = {
            "beginner": ["beginner"],
            "intermediate": ["beginner", "intermediate"],
            "advanced": ["beginner", "intermediate", "advanced"]
        }

        acceptable_levels = level_mapping.get(user_skill_level, ["beginner"])
        return self.db.query(Chapter).filter(Chapter.difficulty_level.in_(acceptable_levels)).all()

    def create_chapter(self, chapter_data: ChapterCreate) -> Chapter:
        """Create a new chapter"""
        db_chapter = Chapter(
            title=chapter_data.title,
            content=chapter_data.content,
            module_id=chapter_data.module_id,
            order_in_module=chapter_data.order_in_module,
            difficulty_level=chapter_data.difficulty_level,
            tags=chapter_data.tags
        )
        self.db.add(db_chapter)
        self.db.commit()
        self.db.refresh(db_chapter)
        return db_chapter

    def update_chapter(self, chapter_id: int, chapter_data: ChapterUpdate) -> Optional[Chapter]:
        """Update a chapter"""
        db_chapter = self.get_chapter(chapter_id)
        if db_chapter:
            for field, value in chapter_data.dict(exclude_unset=True).items():
                setattr(db_chapter, field, value)

            self.db.commit()
            self.db.refresh(db_chapter)
        return db_chapter

    def delete_chapter(self, chapter_id: int) -> bool:
        """Delete a chapter"""
        db_chapter = self.get_chapter(chapter_id)
        if db_chapter:
            self.db.delete(db_chapter)
            self.db.commit()
            return True
        return False

    def get_personalized_chapter(self, chapter_id: int, user_id: int) -> Optional[Chapter]:
        """Get a chapter personalized for a specific user"""
        chapter = self.get_chapter(chapter_id)
        if not chapter:
            return None

        # In a real implementation, this would integrate with the personalization service
        # to adapt the chapter content based on the user's profile
        return chapter

    def apply_difficulty_filter(self, chapters: List[Chapter], user_skill_level: str) -> List[Chapter]:
        """Apply difficulty-based filtering to a list of chapters"""
        logger.info(f"Applying difficulty filter for user level: {user_skill_level}")

        # Map user skill level to acceptable difficulty levels
        level_mapping = {
            "beginner": ["beginner"],
            "intermediate": ["beginner", "intermediate"],
            "advanced": ["beginner", "intermediate", "advanced"]
        }

        acceptable_levels = level_mapping.get(user_skill_level, ["beginner"])

        filtered_chapters = [ch for ch in chapters if ch.difficulty_level in acceptable_levels]

        log_with_context("difficulty_filter", f"Filtered {len(chapters)} to {len(filtered_chapters)} chapters for level {user_skill_level}")

        return filtered_chapters

    def mark_chapter_completed(self, user_id: int, chapter_id: int, module_id: int) -> bool:
        """Mark a chapter as completed for a user"""
        # Check if progress record already exists
        existing_progress = self.db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.chapter_id == chapter_id
        ).first()

        if existing_progress:
            # Update existing record
            existing_progress.completed = True
            existing_progress.completion_percentage = 100
        else:
            # Create new progress record
            new_progress = UserProgress(
                user_id=user_id,
                chapter_id=chapter_id,
                module_id=module_id,
                completed=True,
                completion_percentage=100
            )
            self.db.add(new_progress)

        try:
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def get_user_chapter_progress(self, user_id: int, chapter_id: int) -> Optional[UserProgress]:
        """Get user's progress for a specific chapter"""
        return self.db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.chapter_id == chapter_id
        ).first()