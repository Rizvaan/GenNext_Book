from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from services.auth import get_current_user
from models.database import User
import os

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running
    """
    return {"status": "healthy", "service": "textbook-api"}

@router.get("/config")
async def get_config(current_user: dict = Depends(get_current_user)):
    """
    Get configuration settings for the frontend
    """
    return {
        "api_version": "1.0.0",
        "supported_languages": ["en", "ur-PK"],
        "rag_enabled": True,
        "personalization_enabled": True,
        "user_preferences": {
            "preferred_language": getattr(current_user, 'preferred_language', 'en')
        }
    }