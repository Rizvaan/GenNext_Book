from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import enum

Base = declarative_base()

class SoftwareExperience(enum.Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"

class HardwareExperience(enum.Enum):
    none = "none"
    basic = "basic"
    intermediate = "intermediate"
    advanced = "advanced"

class RoboticsExposure(enum.Enum):
    none = "none"
    basic = "basic"
    intermediate = "intermediate"
    advanced = "advanced"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    software_experience = Column(Enum(SoftwareExperience), default=SoftwareExperience.beginner)
    hardware_experience = Column(Enum(HardwareExperience), default=HardwareExperience.none)
    robotics_exposure = Column(Enum(RoboticsExposure), default=RoboticsExposure.none)
    preferred_language = Column(String, default="en")  # Supports "en", "ur-PK"
    learning_pace = Column(String, default="moderate")  # "slow", "moderate", "fast"
    career_goals = Column(Text)
    current_module = Column(String)  # References Module
    progress = Column(JSON)  # Stores progress by chapter as JSON

class Module(Base):
    __tablename__ = "modules"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    order = Column(Integer, nullable=False)  # For curriculum sequence
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(String, primary_key=True, index=True)
    module_id = Column(String, nullable=False)  # Foreign key to Module
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)  # Markdown format
    difficulty = Column(String)  # "beginner", "intermediate", "advanced"
    learning_outcomes = Column(JSON)  # List of learning outcomes
    tags = Column(JSON)  # List of tags for searchability
    version = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class AISession(Base):
    __tablename__ = "ai_sessions"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String)  # Foreign key to User (optional for anon users)
    session_id = Column(String, nullable=False)  # For tracking conversation context
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    source_content_ids = Column(JSON)  # List of content IDs used to generate response
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Translation(Base):
    __tablename__ = "translations"

    id = Column(String, primary_key=True, index=True)  # Format: "<chapter_id>:<language_code>"
    chapter_id = Column(String, nullable=False)  # Foreign key to Chapter
    language_code = Column(String, nullable=False)  # e.g., "ur-PK", "en"
    translated_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class ContentChunk(Base):
    __tablename__ = "content_chunks"

    id = Column(String, primary_key=True, index=True)
    chapter_id = Column(String, nullable=False)  # Foreign key to Chapter
    chunk_order = Column(Integer, nullable=False)  # For reassembly
    content = Column(Text, nullable=False)  # 300-500 token chunks
    metadata = Column(JSON)  # chapter, module, tags, difficulty, version
    embedding_id = Column(String)  # ID in vector database
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)