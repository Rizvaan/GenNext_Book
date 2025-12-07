from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Application settings
    app_name: str = "AI-Native Textbook API"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: str = "development"  # development, staging, production
    
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/textbook_db")
    database_pool_size: int = int(os.getenv("DATABASE_POOL_SIZE", "5"))
    
    # Qdrant settings
    qdrant_host: str = os.getenv("QDRANT_HOST", "localhost")
    qdrant_port: int = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_collection_name: str = os.getenv("QDRANT_COLLECTION_NAME", "textbook_content")
    
    # OpenAI settings
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Authentication settings
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # CORS settings
    allowed_origins: str = os.getenv("ALLOWED_ORIGINS", "http://localhost,http://localhost:3000")
    
    # Content settings
    max_content_size: int = int(os.getenv("MAX_CONTENT_SIZE", "1000000"))  # 1MB in bytes
    supported_formats: str = os.getenv("SUPPORTED_FORMATS", "text/markdown,text/plain,application/pdf")
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()

# Create a global instance
settings = get_settings()