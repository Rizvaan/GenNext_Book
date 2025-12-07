import logging
import sys
from datetime import datetime
from typing import Dict, Any

# Set up module-specific logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler and set level
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)

# Add handlers to logger
if not logger.handlers:
    logger.addHandler(console_handler)

def log_user_action(user_id: str, action: str, details: Dict[str, Any] = None):
    """
    Log user actions for analytics and debugging
    """
    details_str = f" - Details: {details}" if details else ""
    logger.info(f"User {user_id} performed action: {action}{details_str}")

def log_api_request(request_method: str, request_path: str, user_id: str = None, response_time: float = None):
    """
    Log API requests
    """
    user_info = f" by User {user_id}" if user_id else " by Anonymous"
    time_info = f" in {response_time:.4f}s" if response_time else ""
    logger.info(f"API Request: {request_method} {request_path}{user_info}{time_info}")

def log_personalization_action(user_id: str, action: str, details: Dict[str, Any] = None):
    """
    Log specific personalization-related actions
    """
    details_str = f" - Details: {details}" if details else ""
    logger.info(f"Personalization - User {user_id} {action}{details_str}")

def log_error(error_type: str, error_message: str, context: str = None):
    """
    Log errors with context
    """
    context_str = f" in context '{context}'" if context else ""
    logger.error(f"Error of type {error_type}{context_str}: {error_message}")