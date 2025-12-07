from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

from models.database import User, AISession
from api.errors import UserNotFoundException
from config import get_config
from api.dependencies import get_db, get_current_user
from api.logging_util import log_user_action

router = APIRouter()

@router.get("/")
async def get_chat_history(
    session_id: Optional[str] = Query(None, description="Specific session ID to retrieve"),
    user_id: Optional[str] = Query(None, description="User ID to retrieve history for"),
    limit: int = Query(50, ge=1, le=100, description="Number of messages to return"),
    from_time: Optional[datetime] = Query(None, description="Get messages from this time onwards"),
    current_user: Optional[User] = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve chat history for a user or specific session.
    If session_id is provided, returns history for that specific session.
    If user_id is provided (or derived from auth), returns history for that user across sessions.
    """
    try:
        # Determine the effective user ID
        effective_user_id = current_user.id if current_user else user_id
        
        if not effective_user_id and not session_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Either user identification or session ID is required"
            )
        
        # Build query based on parameters
        query = db.query(AISession)
        
        if session_id:
            # Filter for specific session
            query = query.filter(AISession.session_id == session_id)
            
            # Verify the session belongs to the correct user
            if effective_user_id:
                query = query.filter(AISession.user_id == effective_user_id)
        else:
            # Filter for specific user
            query = query.filter(AISession.user_id == effective_user_id)
        
        # Apply time filter if provided
        if from_time:
            query = query.filter(AISession.timestamp >= from_time)
        
        # Order by timestamp (most recent first) and limit
        sessions = query.order_by(AISession.timestamp.desc()).limit(limit).all()
        
        # Log the history retrieval
        log_user_action(effective_user_id or "system", "retrieved chat history", {
            "session_count": len(sessions),
            "limit": limit,
            "session_id_filter": session_id
        })
        
        # Format response
        history = []
        for session in sessions:
            history.append({
                "id": session.id,
                "session_id": session.session_id,
                "user_id": session.user_id,
                "query": session.query,
                "response": session.response,
                "timestamp": session.timestamp.isoformat(),
                "source_content_ids": session.source_content_ids
            })
        
        return {
            "status": "success",
            "history": history,
            "count": len(history),
            "user_id": effective_user_id,
            "session_id": session_id
        }
        
    except Exception as e:
        user_id_to_log = effective_user_id or (current_user.id if current_user else 'unknown')
        log_user_action(user_id_to_log, "chat_history_error", {"error": str(e)})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving chat history: {str(e)}"
        )


@router.delete("/{session_id}")
async def delete_session(
    session_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a specific chat session.
    Only the owner of the session can delete it.
    """
    try:
        # Find the session
        session = db.query(AISession).filter(
            AISession.session_id == session_id,
            AISession.user_id == current_user.id
        ).first()
        
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found or you don't have permission to delete it"
            )
        
        # Log the deletion
        log_user_action(current_user.id, "deleted chat session", {"session_id": session_id})
        
        # Delete the session
        db.delete(session)
        db.commit()
        
        return {
            "status": "success",
            "message": "Session deleted successfully",
            "session_id": session_id
        }
        
    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        log_user_action(current_user.id, "delete_session_error", {
            "error": str(e),
            "session_id": session_id
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting session: {str(e)}"
        )


@router.get("/sessions")
async def get_user_sessions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    limit: int = Query(20, ge=1, le=50, description="Number of sessions to return")
):
    """
    Get a list of all chat sessions for the authenticated user.
    Returns session metadata without the full conversation content.
    """
    try:
        # Query for sessions belonging to the user
        sessions = db.query(AISession).filter(
            AISession.user_id == current_user.id
        ).order_by(AISession.timestamp.desc()).limit(limit).all()
        
        # Group sessions by session_id to get session summaries
        session_summaries = {}
        for session in sessions:
            session_id = session.session_id
            if session_id not in session_summaries:
                session_summaries[session_id] = {
                    "session_id": session_id,
                    "first_message_time": session.timestamp,
                    "last_message_time": session.timestamp,
                    "message_count": 0,
                    "first_query_preview": session.query[:100] if session.query else ""
                }
            
            # Update the last message time and count
            if session.timestamp > session_summaries[session_id]["last_message_time"]:
                session_summaries[session_id]["last_message_time"] = session.timestamp
            session_summaries[session_id]["message_count"] += 1
        
        # Convert to list and sort by last message time
        session_list = list(session_summaries.values())
        session_list.sort(key=lambda x: x["last_message_time"], reverse=True)
        
        # Log the session list retrieval
        log_user_action(current_user.id, "retrieved session list", {
            "session_count": len(session_list),
            "limit": limit
        })
        
        return {
            "status": "success",
            "sessions": session_list,
            "count": len(session_list),
            "user_id": current_user.id
        }
        
    except Exception as e:
        log_user_action(current_user.id, "get_sessions_error", {"error": str(e)})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving session list: {str(e)}"
        )


@router.delete("/")  # Delete all sessions for user (with confirmation)
async def clear_user_history(
    confirm: bool = Query(..., description="Must be true to confirm deletion of all history"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Clear all chat history for the authenticated user.
    Requires explicit confirmation to prevent accidental data loss.
    """
    if not confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Confirmation required to clear all chat history"
        )
    
    try:
        # Count sessions to be deleted
        session_count = db.query(AISession).filter(
            AISession.user_id == current_user.id
        ).count()
        
        # Delete all sessions for this user
        deleted_count = db.query(AISession).filter(
            AISession.user_id == current_user.id
        ).delete(synchronize_session=False)
        
        db.commit()
        
        # Log the history clearing
        log_user_action(current_user.id, "cleared all chat history", {
            "sessions_deleted": deleted_count
        })
        
        return {
            "status": "success",
            "message": f"Cleared {deleted_count} chat sessions",
            "sessions_cleared": deleted_count,
            "user_id": current_user.id
        }
        
    except Exception as e:
        log_user_action(current_user.id, "clear_history_error", {"error": str(e)})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error clearing chat history: {str(e)}"
        )