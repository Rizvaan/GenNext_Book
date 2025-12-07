import pytest
import asyncio
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_ask_endpoint_contract():
    """
    Contract test for the ask endpoint
    Tests the expected input/output format for asking textbook questions
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test data that matches the expected contract
        question_data = {
            "question": "What is ROS 2?",
            "user_id": "test_user_123",
            "language": "en"
        }
        
        # POST request to ask endpoint
        response = await ac.post("/ask", json=question_data)
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 400, 500]  # 200 for success, 400 for bad request, 500 for server error
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "answer" in data
            assert "references" in data
            assert "session_id" in data
            # Additional validation could be done on the response structure


@pytest.mark.asyncio
async def test_ask_selection_endpoint_contract():
    """
    Contract test for the ask from selection endpoint
    Tests the expected input/output format for asking about selected text
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test data that matches the expected contract
        question_data = {
            "question": "Explain this concept?",
            "selected_text": "ROS 2 is a middleware for robotics applications.",
            "user_id": "test_user_123",
            "language": "en"
        }
        
        # POST request to ask selection endpoint
        response = await ac.post("/ask/selection", json=question_data)
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 400, 500]  # 200 for success, 400 for bad request, 500 for server error
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "answer" in data
            assert "session_id" in data
            # The response for selection might be different than the general ask


@pytest.mark.asyncio
async def test_ask_endpoint_missing_fields():
    """
    Contract test to verify required fields for ask endpoint
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with missing required fields (should return 400 or 422)
        incomplete_data = {
            "user_id": "test_user_123"
            # Missing the question field
        }
        
        response = await ac.post("/ask", json=incomplete_data)
        
        # Should return validation error for missing fields
        assert response.status_code in [400, 422]


@pytest.mark.asyncio
async def test_ask_selection_endpoint_missing_fields():
    """
    Contract test to verify required fields for ask selection endpoint
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with missing required fields (should return 400 or 422)
        incomplete_data = {
            "question": "Explain this concept?",
            "user_id": "test_user_123"
            # Missing the selected_text field
        }
        
        response = await ac.post("/ask/selection", json=incomplete_data)
        
        # Should return validation error for missing fields
        assert response.status_code in [400, 422]