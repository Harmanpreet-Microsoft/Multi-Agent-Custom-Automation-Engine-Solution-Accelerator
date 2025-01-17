import pytest
from unittest.mock import patch, AsyncMock
from httpx import AsyncClient

# Mock environment variables globally
MOCK_ENV_VARS = {
    "COSMOSDB_ENDPOINT": "https://mock-cosmosdb.documents.azure.com:443/",
    "COSMOSDB_DATABASE": "mock_database",
    "COSMOSDB_CONTAINER": "mock_container",
    "AZURE_OPENAI_DEPLOYMENT_NAME": "mock-deployment",
    "AZURE_OPENAI_API_VERSION": "2024-05-01-preview",
    "AZURE_OPENAI_ENDPOINT": "https://mock-openai-endpoint.azure.com/",
    "AZURE_OPENAI_API_KEY": "mock-api-key",
    "AZURE_TENANT_ID": "mock-tenant-id",
    "AZURE_CLIENT_ID": "mock-client-id",
    "AZURE_CLIENT_SECRET": "mock-client-secret",
}

# Patch environment variables for the entire module
with patch.dict("os.environ", MOCK_ENV_VARS):
    from app import app  # Import after setting env vars

@pytest.mark.asyncio
async def test_get_agent_tools():
    """Test the /api/agent-tools endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/agent-tools")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list


@pytest.mark.asyncio
async def test_get_all_messages():
    """Test the /messages endpoint."""
    # Mock the CosmosBufferedChatCompletionContext.get_all_messages method
    with patch("app.CosmosBufferedChatCompletionContext.get_all_messages", AsyncMock(return_value=[{"id": "1", "content": "Message"}])):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get("/messages")
    assert response.status_code == 200
    assert response.json() == [{"id": "1", "content": "Message"}]  # Match mock response


@pytest.mark.asyncio
async def test_delete_all_messages():
    """Test the /messages DELETE endpoint."""
    # Mock the CosmosBufferedChatCompletionContext.delete_all_messages method
    with patch("app.CosmosBufferedChatCompletionContext.delete_all_messages", AsyncMock()):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.delete("/messages")
    assert response.status_code == 200
    assert response.json() == {"status": "All messages deleted"}