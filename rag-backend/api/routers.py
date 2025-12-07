from fastapi import APIRouter
from . import auth, personalization, qa, translation, curriculum

# Main API router
api_router = APIRouter()

# Include all API endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(personalization.router, prefix="/personalization", tags=["personalization"])
api_router.include_router(qa.router, prefix="/qa", tags=["question-answering"])
api_router.include_router(translation.router, prefix="/translation", tags=["translation"])
api_router.include_router(curriculum.router, prefix="/curriculum", tags=["curriculum"])

# Health check endpoint
@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy", "service": "AI-Native Textbook API"}