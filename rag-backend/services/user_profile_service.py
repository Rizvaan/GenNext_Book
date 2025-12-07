from typing import Optional
from sqlalchemy.orm import Session
from ..models.user_profile import UserProfile, User
from ..schemas.user_profile import UserProfileCreate, UserProfileUpdate

class UserProfileService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_profile(self, user_id: int) -> Optional[UserProfile]:
        """Get user profile by user ID"""
        return self.db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

    def create_user_profile(self, user_id: int, profile_data: UserProfileCreate) -> UserProfile:
        """Create a new user profile"""
        db_profile = UserProfile(
            user_id=user_id,
            skill_level=profile_data.skill_level,
            background=profile_data.background,
            learning_preferences=profile_data.learning_preferences,
            preferred_language=profile_data.preferred_language
        )
        self.db.add(db_profile)
        self.db.commit()
        self.db.refresh(db_profile)
        return db_profile

    def update_user_profile(self, user_id: int, profile_data: UserProfileUpdate) -> Optional[UserProfile]:
        """Update user profile"""
        db_profile = self.get_user_profile(user_id)
        if db_profile:
            for field, value in profile_data.dict(exclude_unset=True).items():
                setattr(db_profile, field, value)
            
            self.db.commit()
            self.db.refresh(db_profile)
        return db_profile

    def get_personalized_content(self, user_id: int, content: str) -> str:
        """Apply personalization to content based on user profile"""
        profile = self.get_user_profile(user_id)
        if not profile:
            return content  # Return original content if no profile exists

        # In a real implementation, this would call the personalization engine
        # to adapt the content based on user profile
        adapted_content = self._adapt_content(content, profile)
        return adapted_content

    def _adapt_content(self, content: str, profile: UserProfile) -> str:
        """Private method to adapt content based on profile"""
        # This is a simplified example
        # In reality, this would interact with the personalization engine
        if profile.skill_level == "beginner":
            return f"[Beginner Level] {content}"
        elif profile.skill_level == "intermediate":
            return f"[Intermediate Level] {content}"
        elif profile.skill_level == "advanced":
            return f"[Advanced Level] {content}"
        else:
            return content