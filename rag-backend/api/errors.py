from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging
import sys
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class TextbookException(Exception):
    """
    Base exception class for the textbook application
    """
    def __init__(self, message: str, status_code: int = 500, details: Dict[str, Any] = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)

class UserNotFoundException(TextbookException):
    """
    Raised when a user is not found
    """
    def __init__(self, user_id: str):
        super().__init__(
            message=f"User with id {user_id} not found",
            status_code=404
        )

class ContentNotFoundException(TextbookException):
    """
    Raised when requested content is not found
    """
    def __init__(self, content_id: str):
        super().__init__(
            message=f"Content with id {content_id} not found",
            status_code=404
        )

class RAGException(TextbookException):
    """
    Raised when there's an error with RAG functionality
    """
    def __init__(self, message: str):
        super().__init__(
            message=f"RAG error: {message}",
            status_code=500
        )

def setup_error_handlers(app: FastAPI):
    """
    Set up error handlers for the FastAPI application
    """
    
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "HTTP Exception",
                "message": str(exc.detail),
                "status_code": exc.status_code
            }
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"Validation Error: {exc.errors()}")
        return JSONResponse(
            status_code=422,
            content={
                "error": "Validation Error",
                "message": "Invalid input data",
                "details": exc.errors()
            }
        )
    
    @app.exception_handler(TextbookException)
    async def textbook_exception_handler(request: Request, exc: TextbookException):
        logger.error(f"Textbook Exception: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": "Textbook Exception",
                "message": exc.message,
                "status_code": exc.status_code,
                "details": exc.details
            }
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"General Exception: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "An unexpected error occurred"
            }
        )

# Set up logging utility functions
def log_user_action(user_id: str, action: str, details: Dict[str, Any] = None):
    """
    Log user actions for analytics and debugging
    """
    details_str = f" - Details: {details}" if details else ""
    logger.info(f"User {user_id} performed action: {action}{details_str}")

def log_api_request(request: Request, response_time: float):
    """
    Log API requests
    """
    logger.info(f"API Request: {request.method} {request.url} - Response time: {response_time}s")