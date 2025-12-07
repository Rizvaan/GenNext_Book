import logging
from logging.handlers import RotatingFileHandler
import sys
import os
from datetime import datetime
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Callable, Dict, Any
import traceback
from functools import wraps

# Configure logging
def setup_logging():
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create a custom logger
    logger = logging.getLogger("textbook_api")
    logger.setLevel(logging.DEBUG)
    
    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)  # Console handler
    f_handler = RotatingFileHandler(
        f"{log_dir}/textbook_api.log", 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )  # File handler with rotation
    
    # Set levels for handlers
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)
    
    # Create formatters and add them to handlers
    c_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    f_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)
    
    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    
    return logger

# Initialize logger
logger = setup_logging()

# Error handling middleware
async def error_handler_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except HTTPException as e:
        logger.error(f"HTTPException: {e.status_code} - {e.detail}")
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail}
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"}
        )

# Log requests
async def log_requests_middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).total_seconds()
    
    logger.info(f"{request.method} {request.url} - {response.status_code} - {process_time:.4f}s")
    
    return response

# Decorator for logging function calls
def log_function_call(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        logger.info(f"Calling function: {func.__name__}")
        try:
            result = await func(*args, **kwargs)
            logger.info(f"Function {func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise
    return wrapper

# Centralized error response function
def create_error_response(error_type: str, message: str, status_code: int = 500) -> Dict[str, Any]:
    return {
        "error": {
            "type": error_type,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
    }

# Log a custom message with context
def log_with_context(context: str, message: str, level: str = "info"):
    getattr(logger, level)(f"[{context}] {message}")

# Initialize logging when module is loaded
logger.info("Logging infrastructure initialized")