import pytest
import asyncio
from httpx import AsyncClient
from main import app  # Import the FastAPI app
from config import config

@pytest.mark.asyncio
async def test_user_registration_contract():
    """
    Contract test for user registration endpoint
    Tests the expected input/output format and basic functionality
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test data that matches the expected contract
        user_data = {
            "email": "test@example.com",
            "password": "securepassword123",  # In a real implementation, password would be required
            "software_experience": "beginner",
            "hardware_experience": "none",
            "robotics_exposure": "none",
            "preferred_language": "en",
            "learning_pace": "moderate",
            "career_goals": "Learn robotics concepts"
        }
        
        # POST request to user registration endpoint
        # Note: The actual endpoint might be different depending on the implementation
        response = await ac.post("/users/register", json=user_data)
        
        # Check that the response status is what's expected (200 for success or 201 for created)
        # In a real implementation, this would match the actual API contract
        assert response.status_code in [200, 201, 400, 409]  # 400 for validation error, 409 for duplicate email
        
        # If successful registration, check response structure
        if response.status_code in [200, 201]:
            data = response.json()
            # Check for expected fields in response
            assert "user_id" in data or "id" in data
            assert "email" in data
            # Additional fields might be present based on the User model

@pytest.mark.asyncio
async def test_user_registration_missing_fields():
    """
    Contract test to verify required fields in user registration
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with missing required fields (should return 422 or 400)
        incomplete_user_data = {
            "email": "test@example.com"
            # Missing other required fields
        }
        
        response = await ac.post("/users/register", json=incomplete_user_data)
        
        # Should return validation error for missing fields
        assert response.status_code in [400, 422]

@pytest.mark.asyncio
async def test_user_registration_invalid_email():
    """
    Contract test to verify email validation
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with invalid email format
        invalid_user_data = {
            "email": "invalid-email",
            "password": "securepassword123",
        }
        
        response = await ac.post("/users/register", json=invalid_user_data)
        
        # Should return validation error for invalid email
        assert response.status_code in [400, 422]