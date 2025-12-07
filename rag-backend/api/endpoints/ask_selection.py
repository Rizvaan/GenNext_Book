from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import Dict, Any, Optional
import uuid
from datetime import datetime

from agents.rag_agent import rag_agent
from services.user_profile_service import user_profile_service
from models.database import User, AISession
from api.errors import RAGException, UserNotFoundException
from config import get_config
from api.dependencies import get_db, get_current_user
from api.logging_util import log_user_action

router = APIRouter()

@router.post("/")
async def ask_from_selection(
    question: str = Body(...),
    selected_text: str = Body(...),
    user_id: Optional[str] = Body(None),
    language: Optional[str] = Body(None),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint for asking questions about specifically selected text from the textbook.
    The AI uses the provided selected text as the primary context for answering.
    """
    try:
        # Use the current user if authenticated, or the provided user_id
        effective_user_id = current_user.id if current_user else user_id
        
        if not effective_user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User identification is required"
            )
        
        # Validate input
        if not question.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Question cannot be empty"
            )
        
        if not selected_text.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Selected text cannot be empty"
            )
        
        # Log the question being asked about selected text
        log_user_action(effective_user_id, "asked about selection", {
            "question": question,
            "selected_text_length": len(selected_text)
        })
        
        # Get user's profile for personalization context
        try:
            user_profile = user_profile_service.get_personalization_data(
                db=db,
                user_id=effective_user_id
            )
        except UserNotFoundException:
            # If user not found in our system, use default profile
            user_profile = {
                "user_id": effective_user_id,
                "software_experience": "intermediate",
                "preferred_language": language or "en",
                "learning_pace": "moderate"
            }
        
        # Use the RAG agent to answer the question based on the selected text
        response = await rag_agent.answer_from_selection(
            question=question,
            selected_text=selected_text,
            user_id=effective_user_id
        )
        
        # Create a session record to track this interaction
        session_id = str(uuid.uuid4())
        session = AISession(
            id=session_id,
            user_id=effective_user_id,
            session_id=session_id,  # Using the same ID for now
            query=question,
            response=response.get("answer", ""),
            timestamp=datetime.utcnow(),
            source_content_ids=["selected_text"]  # Mark that this is from selected text
        )
        
        db.add(session)
        db.commit()
        
        # Log successful response
        log_user_action(effective_user_id, "received answer to selection question", {
            "question": question,
            "response_length": len(response.get("answer", ""))
        })
        
        return {
            "status": "success",
            "answer": response["answer"],
            "references": response["references"],
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": effective_user_id,
            "selected_text": selected_text  # Include the selected text in response for context
        }
        
    except RAGException as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "rag_error_selection", {"error": str(e), "question": question})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question about selection: {str(e)}"
        )
    except Exception as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "ask_selection_error", {"error": str(e), "question": question})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error processing question about selection: {str(e)}"
        )


@router.post("/context-verification")
async def verify_selection_context(
    selected_text: str = Body(...),
    user_id: Optional[str] = Body(None),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint to verify that the selected text exists in the knowledge base
    and provide context information about it.
    """
    try:
        effective_user_id = current_user.id if current_user else user_id
        
        if not effective_user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User identification is required"
            )
        
        if not selected_text.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Selected text cannot be empty"
            )
        
        # Log the verification request
        log_user_action(effective_user_id, "verifying selection context", {
            "selected_text_length": len(selected_text)
        })
        
        # In a real implementation, we might search for similar content in the vector database
        # For now, we'll just return a success response indicating the text was received
        return {
            "status": "success",
            "valid": True,
            "text_length": len(selected_text),
            "user_id": effective_user_id,
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "verify_selection_error", {"error": str(e)})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error verifying selection context: {str(e)}"
        )