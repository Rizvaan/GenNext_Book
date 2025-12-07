from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory
from alembic.runtime.environment import EnvironmentContext
import os
from .settings import settings

# Database URL
DATABASE_URL = settings.database_url

# Create synchronous engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def get_db():
    """
    Dependency to get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Initialize the database by creating all tables
    """
    # Import all models to ensure they're registered with Base
    from ..models.user_profile import User, UserProfile, Chapter, Module, Curriculum, UserProgress
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

def check_db_connection():
    """
    Check if the database connection is working
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

# Initialize database if needed
if __name__ == "__main__":
    init_db()