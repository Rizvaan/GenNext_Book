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
async def ask_question(
    question: str = Body(..., embed=True),
    user_id: Optional[str] = Body(None),
    language: Optional[str] = Body(None),
    module_id: Optional[str] = Body(None),
    chapter_id: Optional[str] = Body(None),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Main endpoint for asking questions about textbook content.
    Uses RAG (Retrieval-Augmented Generation) to answer from textbook knowledge.
    """
    try:
        # Use the current user if authenticated, or the provided user_id
        effective_user_id = current_user.id if current_user else user_id
        
        if not effective_user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User identification is required"
            )
        
        # Log the question being asked
        log_user_action(effective_user_id, "asked question", {
            "question": question,
            "module_id": module_id,
            "chapter_id": chapter_id
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
        
        # Use the RAG agent to answer the question
        response = await rag_agent.answer_question(
            question=question,
            user_id=effective_user_id,
            module_id=module_id,
            chapter_id=chapter_id
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
            source_content_ids=[ref.get("content_id") for ref in response.get("references", [])[:5]]  # Top 5 references
        )
        
        db.add(session)
        db.commit()
        
        # Log successful response
        log_user_action(effective_user_id, "received answer", {
            "question": question,
            "response_length": len(response.get("answer", ""))
        })
        
        return {
            "status": "success",
            "answer": response["answer"],
            "references": response["references"],
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": effective_user_id
        }
        
    except RAGException as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "rag_error", {"error": str(e), "question": question})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question: {str(e)}"
        )
    except Exception as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "ask_error", {"error": str(e), "question": question})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error processing question: {str(e)}"
        )


@router.post("/askWithContext")
async def ask_question_with_context(
    question: str = Body(...),
    context: str = Body(...),
    user_id: Optional[str] = Body(None),
    language: Optional[str] = Body(None),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint for asking questions with explicit context provided by the client.
    This can be used when specific content context is already known.
    """
    try:
        effective_user_id = current_user.id if current_user else user_id
        
        if not effective_user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User identification is required"
            )
        
        # Log the question being asked with context
        log_user_action(effective_user_id, "asked question with context", {
            "question": question,
            "context_length": len(context)
        })
        
        # Use the RAG agent with the provided context
        # This is a simplified approach - in a full implementation, 
        # we might want to customize the agent behavior
        prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer based on the provided context."
        
        # For now, we'll simulate using the LLM directly with the context
        # In a full implementation, this would be handled by the RAG agent
        from openai import AsyncOpenAI
        from config import config
        
        client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)
        
        response = await client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are an AI assistant for a robotics textbook. Answer based on the provided context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        
        # Create a session record
        session_id = str(uuid.uuid4())
        session = AISession(
            id=session_id,
            user_id=effective_user_id,
            session_id=session_id,
            query=question,
            response=answer,
            timestamp=datetime.utcnow(),
            source_content_ids=["provided_context"]  # Mark as provided context
        )
        
        db.add(session)
        db.commit()
        
        return {
            "status": "success",
            "answer": answer,
            "references": [{"content_id": "provided_context", "source": "user_provided"}],
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": effective_user_id
        }
    except Exception as e:
        log_user_action(effective_user_id if 'effective_user_id' in locals() else 'unknown', 
                       "ask_with_context_error", {"error": str(e), "question": question})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing question with context: {str(e)}"
        )