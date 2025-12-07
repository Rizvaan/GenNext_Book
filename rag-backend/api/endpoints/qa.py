from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

from ..database import get_db
from ..agents.rag_agent import rag_agent
from ..services.progress_service import ProgressService

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    context: Optional[str] = None  # Optional context to limit search scope
    user_id: Optional[int] = None  # Optional user ID to personalize response

class QuestionWithContextRequest(BaseModel):
    question: str
    selected_text: str
    user_id: Optional[int] = None

@router.post("/ask")
async def ask_question(request: QuestionRequest, db: Session = Depends(get_db)):
    """
    Ask a question about the textbook content
    """
    try:
        # Use RAG agent to answer the question
        answer = rag_agent.answer_question(request.question)
        
        # If user ID is provided, we could potentially track this interaction
        if request.user_id:
            # In a real implementation, we might log this interaction for analytics
            pass
        
        return {
            "question": request.question,
            "answer": answer,
            "source": "AI-Native Textbook Knowledge Base"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question: {str(e)}"
        )

@router.post("/ask-from-selection")
async def ask_from_selection(request: QuestionWithContextRequest, db: Session = Depends(get_db)):
    """
    Ask a question about selected text
    """
    try:
        # In a real implementation, we would provide the selected text as context
        # For now, we'll just include it in the question
        full_query = f"Regarding this text: '{request.selected_text}', {request.question}"
        
        # Use RAG agent to answer the question with context
        answer = rag_agent.answer_question(full_query)
        
        return {
            "question": request.question,
            "selected_text": request.selected_text,
            "answer": answer,
            "source": "AI-Native Textbook Knowledge Base"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question: {str(e)}"
        )

@router.get("/history/{user_id}")
async def get_qa_history(user_id: int, db: Session = Depends(get_db)):
    """
    Get the Q&A history for a user
    """
    try:
        # In a real implementation, we would retrieve the Q&A history from a database
        # For now, we'll return an empty list
        history = []
        
        return {
            "user_id": user_id,
            "history": history
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving Q&A history: {str(e)}"
        )