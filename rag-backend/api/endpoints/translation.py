from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
import asyncio
import sys
import os

# Add the project root directory to sys.path to access the src directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from ..database import get_db
from src.translation.engine import TranslationEngine

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "en"
    target_lang: str = "ur"

class ContentTranslationRequest(BaseModel):
    content_id: int
    target_lang: str = "ur"

# Initialize translation engine
translation_engine = TranslationEngine()

@router.post("/translate")
async def translate_text(request: TranslationRequest):
    """
    Translate text between supported languages
    """
    try:
        if request.source_lang not in translation_engine.get_supported_languages():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Source language '{request.source_lang}' not supported"
            )

        if request.target_lang not in translation_engine.get_supported_languages():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Target language '{request.target_lang}' not supported"
            )

        translated_text = await translation_engine.translate(
            request.text,
            request.source_lang,
            request.target_lang
        )

        return {
            "original_text": request.text,
            "translated_text": translated_text,
            "source_lang": request.source_lang,
            "target_lang": request.target_lang
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error translating text: {str(e)}"
        )

@router.post("/translate/chapter")
async def translate_chapter_content(request: ContentTranslationRequest):
    """
    Translate chapter content
    """
    try:
        # In a real implementation, this would fetch the chapter content from the database
        # For now, we'll simulate the process
        original_content = f"This is the original content of chapter {request.content_id} in English."

        translated_content = await translation_engine.translate(
            original_content,
            "en",  # source is always English for textbook content
            request.target_lang
        )

        return {
            "content_id": request.content_id,
            "original_content": original_content,
            "translated_content": translated_content,
            "target_lang": request.target_lang
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error translating chapter content: {str(e)}"
        )

@router.get("/supported-languages")
async def get_supported_languages():
    """
    Get list of supported languages
    """
    languages = translation_engine.get_supported_languages()
    return {"supported_languages": languages}