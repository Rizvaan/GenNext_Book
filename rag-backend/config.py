import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to manage environment variables
    """
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", 
                                  "postgresql+asyncpg://username:password@localhost/dbname")
    DB_ECHO: bool = os.getenv("DB_ECHO", "false").lower() == "true"
    
    # Qdrant settings
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    
    # OpenAI settings
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", 
                                "your-super-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Application settings
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Physical AI & Humanoid Robotics Textbook API")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    
    # CORS settings
    BACKEND_CORS_ORIGINS: str = os.getenv("BACKEND_CORS_ORIGINS", 
                                          "http://localhost,http://localhost:3000,http://localhost:8080")
    
    # Content settings
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "400"))  # tokens
    OVERLAP_SIZE: int = int(os.getenv("OVERLAP_SIZE", "50"))  # tokens
    
    # Debug settings
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

# Create config instance
config = Config()

def get_config():
    """
    Get the configuration instance
    """
    return config