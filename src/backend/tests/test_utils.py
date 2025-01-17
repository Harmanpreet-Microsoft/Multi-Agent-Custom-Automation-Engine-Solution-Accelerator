import pytest
import os
from unittest.mock import patch, AsyncMock

# Mock all required environment variables globally before importing utils
with patch.dict(os.environ, {
    "COSMOSDB_ENDPOINT": "https://mock-cosmosdb.documents.azure.com:443/",
    "COSMOSDB_KEY": "mock_key",
    "AZURE_OPENAI_ENDPOINT": "https://mock-openai-endpoint.azure.com/",
    "AZURE_OPENAI_API_VERSION": "2024-05-01-preview",
    "AZURE_OPENAI_DEPLOYMENT_NAME": "mock-deployment",
    "COSMOSDB_DATABASE": "mock_database",
    "COSMOSDB_CONTAINER": "mock_container"
}):
    from utils import (
        initialize_runtime_and_context,
        runtime_dict,
        rai_success,  # Ensure rai_success is imported
    )

from uuid import uuid4


@pytest.mark.asyncio
@patch("utils.SingleThreadedAgentRuntime")
@patch("utils.CosmosBufferedChatCompletionContext")
@patch("utils.ToolAgent.register")
async def test_initialize_runtime_and_context_new_session(
    mock_tool_agent_register, mock_context, mock_runtime
):
    session_id = None  # Test session creation
    user_id = "test-user-id"

    # Use AsyncMock for asynchronous methods
    mock_runtime.return_value = AsyncMock()
    mock_context.return_value = AsyncMock()

    runtime, context = await initialize_runtime_and_context(
        session_id=session_id, user_id=user_id
    )

    assert runtime is not None
    assert context is not None
    assert len(runtime_dict) > 0


@pytest.mark.asyncio
@patch("utils.SingleThreadedAgentRuntime")
@patch("utils.CosmosBufferedChatCompletionContext")
@patch("utils.ToolAgent.register")
async def test_initialize_runtime_and_context_reuse_existing_session(
    mock_tool_agent_register, mock_context, mock_runtime
):
    session_id = str(uuid4())
    user_id = "test-user-id"

    # Mock existing runtime and context in global runtime_dict
    mock_runtime_instance = AsyncMock()
    mock_context_instance = AsyncMock()
    runtime_dict[session_id] = (mock_runtime_instance, mock_context_instance)

    runtime, context = await initialize_runtime_and_context(
        session_id=session_id, user_id=user_id
    )

    assert runtime is mock_runtime_instance
    assert context is mock_context_instance


@pytest.mark.asyncio
async def test_initialize_runtime_and_context_user_id_none():
    # Assert ValueError is raised when user_id is None
    with pytest.raises(ValueError, match="The 'user_id' parameter cannot be None. Please provide a valid user ID."):
        await initialize_runtime_and_context(session_id="test-session-id", user_id=None)


@patch("utils.requests.post")
@patch("utils.DefaultAzureCredential")
def test_rai_success_true(mock_credential, mock_post):
    # Mock Azure token
    mock_credential.return_value.get_token.return_value.token = "mock_token"

    # Mock API response
    mock_post.return_value.json.return_value = {
        "choices": [{"message": {"content": "FALSE"}}]
    }

    result = rai_success("This is a valid description.")
    assert result is True


@patch("utils.requests.post")
@patch("utils.DefaultAzureCredential")
def test_rai_success_false(mock_credential, mock_post):
    # Mock Azure token
    mock_credential.return_value.get_token.return_value.token = "mock_token"

    # Mock API response for content filter
    mock_post.return_value.json.return_value = {
        "error": {"code": "content_filter"}
    }

    result = rai_success("Invalid description with rule violation.")
    assert result is False