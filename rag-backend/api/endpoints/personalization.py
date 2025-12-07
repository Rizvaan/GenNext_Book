from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging

from .. import crud, models, schemas
from ..database import get_db
from ..utils.logging import log_with_context, logger
from ..services.user_profile_service import UserProfileService
from ..services.chapter_service import ChapterService

router = APIRouter()

@router.post("/profile", response_model=schemas.UserProfileResponse)
def create_user_profile(
    profile: schemas.UserProfileCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new user profile
    """
    try:
        service = UserProfileService(db)
        db_profile = service.create_user_profile(profile.user_id, profile)
        log_with_context("personalization", f"Created profile for user {profile.user_id}")
        return db_profile
    except Exception as e:
        logger.error(f"Error creating user profile: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user profile"
        )

@router.get("/profile/{user_id}", response_model=schemas.UserProfileResponse)
def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a user's profile
    """
    try:
        service = UserProfileService(db)
        db_profile = service.get_user_profile(user_id)
        if db_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )
        return db_profile
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting user profile: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting user profile"
        )

@router.put("/profile/{user_id}", response_model=schemas.UserProfileResponse)
def update_user_profile(
    user_id: int,
    profile_update: schemas.UserProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Update a user's profile
    """
    try:
        service = UserProfileService(db)
        db_profile = service.update_user_profile(user_id, profile_update)
        if db_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )
        log_with_context("personalization", f"Updated profile for user {user_id}")
        return db_profile
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating user profile: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating user profile"
        )

@router.post("/personalize-content", response_model=str)
def get_personalized_content(
    user_id: int,
    content: str,
    db: Session = Depends(get_db)
):
    """
    Get personalized content for a user
    """
    try:
        service = UserProfileService(db)
        personalized_content = service.get_personalized_content(user_id, content)
        log_with_context("personalization", f"Personalized content for user {user_id}")
        return personalized_content
    except Exception as e:
        logger.error(f"Error getting personalized content: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting personalized content"
        )

@router.get("/recommended-content/{user_id}")
def get_recommended_content(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Get recommended content based on user profile
    """
    try:
        service = UserProfileService(db)
        profile = service.get_user_profile(user_id)
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )
        
        # In a real implementation, this would use the profile to recommend content
        recommendations = {
            "next_modules": [],
            "focus_areas": [],
            "difficulty_level": profile.skill_level
        }
        
        log_with_context("personalization", f"Got recommendations for user {user_id}")
        return recommendations
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting recommendations: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting recommendations"
        )