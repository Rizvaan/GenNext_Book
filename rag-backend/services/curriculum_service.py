from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.user_profile import Module, UserProgress
from ..services.progress_service import ProgressService

class CurriculumService:
    def __init__(self, db: Session):
        self.db = db

    def check_prerequisites_completed(self, user_id: int, module_id: int) -> bool:
        """
        Check if user has completed prerequisites for a module
        """
        # Get the module
        module = self.db.query(Module).filter(Module.id == module_id).first()
        if not module:
            return False

        # If no prerequisites, return True
        if not module.prerequisites:
            return True

        # Parse prerequisites (comma-separated module IDs)
        prerequisite_ids = [int(id.strip()) for id in module.prerequisites.split(",") if id.strip()]
        
        # Check if all prerequisites are completed
        for prereq_id in prerequisite_ids:
            if not self.is_module_completed(user_id, prereq_id):
                return False
        
        return True

    def is_module_completed(self, user_id: int, module_id: int) -> bool:
        """
        Check if a user has completed all chapters in a module
        """
        # Get all chapters in the module
        from ..models.user_profile import Chapter
        chapters = self.db.query(Chapter).filter(Chapter.module_id == module_id).all()
        
        if not chapters:
            # If no chapters in module, consider it complete
            return True
        
        # Check if all chapters are completed for the user
        completed_chapter_count = 0
        for chapter in chapters:
            progress = self.db.query(UserProgress).filter(
                UserProgress.user_id == user_id,
                UserProgress.chapter_id == chapter.id,
                UserProgress.completed == True
            ).count()
            
            if progress > 0:
                completed_chapter_count += 1
        
        # Module is completed if all chapters are completed
        return completed_chapter_count == len(chapters)

    def get_available_modules(self, user_id: int) -> List[int]:
        """
        Get a list of module IDs that the user is eligible to start
        """
        all_modules = self.db.query(Module).all()
        available_modules = []
        
        for module in all_modules:
            if self.check_prerequisites_completed(user_id, module.id):
                available_modules.append(module.id)
        
        return available_modules

    def get_next_module(self, user_id: int) -> Optional[int]:
        """
        Get the next module ID the user should work on based on curriculum order
        and prerequisite completion
        """
        # Get modules in curriculum order
        modules = self.db.query(Module).order_by(Module.order_in_curriculum).all()
        
        for module in modules:
            # Check if this module's prerequisites are met
            if self.check_prerequisites_completed(user_id, module.id):
                # Check if module is not already completed
                if not self.is_module_completed(user_id, module.id):
                    return module.id
        
        return None  # All modules completed