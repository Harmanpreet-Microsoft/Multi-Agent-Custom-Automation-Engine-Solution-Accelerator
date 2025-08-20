"""
Configuration settings for the Magentic Employee Onboarding system.
Handles Azure OpenAI, MCP, and environment setup.
"""

import os

from common.config.app_config import config
from semantic_kernel.agents.orchestration.magentic import MagenticOrchestration
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion, OpenAIChatPromptExecutionSettings)
from v3.magentic_agents.magentic_agent_factory import (cleanup_all_agents,
                                                       get_agents)
from v3.orchestration.manager import init_orchestration


class AzureConfig:
    """Azure OpenAI and authentication configuration."""

    def __init__(self):
        self.endpoint = config.AZURE_OPENAI_ENDPOINT
        self.reasoning_model = config.REASONING_MODEL_NAME
        self.standard_model = config.AZURE_OPENAI_DEPLOYMENT_NAME
        self.bing_connection_name = config.AZURE_BING_CONNECTION_NAME

        # Create credential
        self.credential = config.get_azure_credentials()

    def create_chat_completion_service(self, use_reasoning_model=False):
        """Create Azure Chat Completion service."""
        model_name = (
            self.reasoning_model if use_reasoning_model else self.standard_model
        )

        return AzureChatCompletion(
            deployment_name=model_name,
            endpoint=self.endpoint,
            ad_token_provider=config.get_access_token(),
        )

    def create_execution_settings(self):
        """Create execution settings for OpenAI."""
        return OpenAIChatPromptExecutionSettings(max_tokens=4000, temperature=0.1)


class MCPConfig:
    """MCP server configuration."""

    def __init__(self):
        self.url = "http://127.0.0.1:8000/mcp/"
        self.name = "MCPGreetingServer"
        self.description = "MCP server with greeting and planning tools"

    def get_headers(self, token):
        """Get MCP headers with authentication token."""
        return (
            {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            if token
            else {}
        )
    
class OrchestrationConfig:
    """Configuration for orchestration settings."""

    def __init__(self):
        self._orchestrations = {}

    async def get_current_orchestration(self, user_id: str) -> MagenticOrchestration:
        """Initialize or get existing orchestration instance."""
        if user_id not in self._orchestrations:
            agents = await get_agents()
            self._orchestrations[user_id] = await init_orchestration(agents)
        return self._orchestrations[user_id]


# Global config instances
azure_config = AzureConfig()
mcp_config = MCPConfig()
orchestration_config = OrchestrationConfig()
