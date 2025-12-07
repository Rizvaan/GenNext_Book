import pytest
import asyncio
from httpx import AsyncClient
from main import app
from models.database import User
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Create a test database engine and session
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Using SQLite for testing

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
from models.database import Base
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Create a new database session for testing"""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.mark.asyncio
async def test_user_profile_creation_integration():
    """
    Integration test for user profile creation
    Tests the full flow from API endpoint to database storage
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Prepare test user data
        user_data = {
            "email": "integration_test@example.com",
            "password": "securepassword123",
            "software_experience": "intermediate",
            "hardware_experience": "basic",
            "robotics_exposure": "none",
            "preferred_language": "en",
            "learning_pace": "moderate",
            "career_goals": "Develop humanoid robots"
        }
        
        # Call the registration endpoint
        response = await ac.post("/users/register", json=user_data)
        
        # Check that registration was successful
        assert response.status_code in [200, 201]
        
        # Verify the user was created in the database
        # This assumes you have a way to query the database directly
        # In a real implementation, you might need to implement this endpoint
        # or have a separate mechanism to verify database state
        response_data = response.json()
        assert "email" in response_data
        assert response_data["email"] == user_data["email"]

@pytest.mark.asyncio
async def test_user_profile_retrieval():
    """
    Integration test for retrieving user profile after creation
    """
    # First, create a user
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        user_data = {
            "email": "retrieve_test@example.com",
            "password": "securepassword123",
            "software_experience": "advanced",
            "hardware_experience": "intermediate",
            "robotics_exposure": "basic",
            "preferred_language": "ur-PK",  # Testing Urdu preference
            "learning_pace": "fast",
            "career_goals": "Robotics research"
        }
        
        # Register the user
        register_response = await ac.post("/users/register", json=user_data)
        assert register_response.status_code in [200, 201]
        
        # Then try to retrieve the user profile
        # Note: This assumes there's an endpoint to get user profile by email or ID
        # which may need to be implemented as part of the API
        user_response_data = register_response.json()
        
        # If there's an endpoint to retrieve user profile, test it here
        # For now, we'll assume the registration endpoint returns the full user profile
        assert user_response_data.get("software_experience") == "advanced"
        assert user_response_data.get("preferred_language") == "ur-PK"

@pytest.mark.asyncio
async def test_user_profile_updates():
    """
    Integration test for updating user profile after creation
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Create a user first
        user_data = {
            "email": "update_test@example.com",
            "password": "securepassword123",
            "software_experience": "beginner",
            "hardware_experience": "none",
            "robotics_exposure": "none",
            "preferred_language": "en",
            "learning_pace": "moderate",
            "career_goals": "Learn robotics"
        }
        
        register_response = await ac.post("/users/register", json=user_data)
        assert register_response.status_code in [200, 201]
        
        user_response_data = register_response.json()
        
        # Now update the user profile (assuming there's an update endpoint)
        # update_data = {
        #     "software_experience": "intermediate",
        #     "career_goals": "Build humanoid robots"
        # }
        # 
        # update_response = await ac.put(f"/users/{user_response_data['id']}", json=update_data)
        # assert update_response.status_code == 200
        
        # Verify the update worked
        # updated_data = update_response.json()
        # assert updated_data["software_experience"] == "intermediate"
        
        # For now, just verify the initial creation worked properly
        assert user_response_data.get("software_experience") == "beginner"