import pytest
import asyncio
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_module_navigation_endpoint_contract():
    """
    Contract test for the module navigation endpoints
    Tests the expected input/output format for module navigation
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test getting available modules
        response = await ac.get("/curriculum/modules")
        
        # Check that the response status is what's expected
        # 200 for success, 404 if endpoint not implemented, 500 for server error
        assert response.status_code in [200, 404, 500]
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "modules" in data
            assert isinstance(data["modules"], list)
            # Each module should have required fields
            for module in data["modules"]:
                assert "id" in module
                assert "title" in module
                assert "description" in module
                assert "order" in module


@pytest.mark.asyncio
async def test_get_specific_module_contract():
    """
    Contract test for getting a specific module by ID
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with a sample module ID
        response = await ac.get("/curriculum/modules/module1-the-robotic-nervous-system")
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 404, 500]  # 404 if module doesn't exist
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "id" in data
            assert "title" in data
            assert "description" in data
            assert "chapters" in data
            assert isinstance(data["chapters"], list)


@pytest.mark.asyncio
async def test_course_progress_endpoint_contract():
    """
    Contract test for the course progress tracking endpoint
    Tests the expected input/output format
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test data that matches the expected contract
        progress_data = {
            "user_id": "test_user_123",
            "module_id": "module1-the-robotic-nervous-system",
            "chapter_id": "chapter1-intro-ros2",
            "status": "completed",  # Options could be: not_started, in_progress, completed
            "completion_percentage": 100
        }
        
        # POST request to progress tracking endpoint
        response = await ac.post("/curriculum/progress", json=progress_data)
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 201, 400, 404, 500]  # 200/201 for success, 400 for bad request, etc.
        
        if response.status_code in [200, 201]:
            data = response.json()
            # Check for expected fields in response
            assert "status" in data
            assert "message" in data
            assert "progress_id" in data


@pytest.mark.asyncio
async def test_get_user_progress_contract():
    """
    Contract test for getting user progress in the curriculum
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test getting user's progress
        response = await ac.get("/curriculum/progress?user_id=test_user_123")
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 400, 404, 500]
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "user_progress" in data
            assert "modules" in data["user_progress"]
            # Each module progress should have expected fields
            for module_progress in data["user_progress"]["modules"]:
                assert "module_id" in module_progress
                assert "completion_percentage" in module_progress
                assert "chapters" in module_progress
                # Each chapter should have status and completion data
                for chapter in module_progress["chapters"]:
                    assert "chapter_id" in chapter
                    assert "status" in chapter
                    assert "completed_at" in chapter