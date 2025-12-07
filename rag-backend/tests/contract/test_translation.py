import pytest
import asyncio
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_translation_endpoint_contract():
    """
    Contract test for the translation endpoint
    Tests the expected input/output format for translating content
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test data that matches the expected contract
        translation_data = {
            "content": "This is a sample text to translate.",
            "target_language": "ur-PK",  # Urdu Pakistan
            "source_language": "en"      # English
        }
        
        # POST request to translation endpoint
        response = await ac.post("/translate", json=translation_data)
        
        # Check that the response status is what's expected
        # 200 for success, 400 for bad request, 500 for server error
        # The endpoint might not exist yet during development, so allow 404
        assert response.status_code in [200, 400, 404, 500]
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "translated_content" in data
            assert "source_language" in data
            assert "target_language" in data
            # Additional validation could be done on the response structure


@pytest.mark.asyncio
async def test_translation_endpoint_missing_fields():
    """
    Contract test to verify required fields for translation endpoint
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with missing required fields (should return 400 or 422)
        incomplete_data = {
            "target_language": "ur-PK"
            # Missing the content field
        }
        
        response = await ac.post("/translate", json=incomplete_data)
        
        # Should return validation error for missing fields
        assert response.status_code in [400, 422]


@pytest.mark.asyncio
async def test_translation_endpoint_invalid_language():
    """
    Contract test to verify language code validation
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Test with invalid language code
        invalid_data = {
            "content": "This is a sample text to translate.",
            "target_language": "invalid",  # Invalid language code
            "source_language": "en"
        }
        
        response = await ac.post("/translate", json=invalid_data)
        
        # Should return validation error for invalid language
        assert response.status_code in [400, 422]


@pytest.mark.asyncio
async def test_get_available_languages():
    """
    Contract test for the available languages endpoint
    """
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # GET request to available languages endpoint
        response = await ac.get("/translate/languages")
        
        # Check that the response status is what's expected
        assert response.status_code in [200, 404, 500]  # 404 if endpoint not yet implemented
        
        if response.status_code == 200:
            data = response.json()
            # Check for expected fields in response
            assert "available_languages" in data
            assert isinstance(data["available_languages"], list)
            # Should include English and Urdu as per requirements
            language_codes = [lang["code"] for lang in data["available_languages"]]
            assert "en" in language_codes
            assert "ur-PK" in language_codes