# Copyright (c) Microsoft. All rights reserved.
""" Proxy agent that prompts for human clarification."""

import logging
import uuid
from collections.abc import AsyncIterable
from typing import AsyncIterator

from semantic_kernel.agents import (  # pylint: disable=no-name-in-module
    AgentResponseItem, AgentThread)
from semantic_kernel.agents.agent import Agent
from semantic_kernel.contents import AuthorRole, ChatMessageContent
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.history_reducer.chat_history_reducer import \
    ChatHistoryReducer
from semantic_kernel.exceptions.agent_exceptions import \
    AgentThreadOperationException
from typing_extensions import override


class DummyAgentThread(AgentThread):
    """Dummy thread implementation for proxy agent."""
    
    def __init__(self, chat_history: ChatHistory | None = None, thread_id: str | None = None):
        super().__init__()
        self._chat_history = chat_history if chat_history is not None else ChatHistory()
        self._id: str = thread_id or f"thread_{uuid.uuid4().hex}"
        self._is_deleted = False
        self.logger = logging.getLogger(__name__)
        
    @override
    async def _create(self) -> str:
        """Starts the thread and returns its ID."""
        return self._id
        
    @override
    async def _delete(self) -> None:
        """Ends the current thread."""
        self._chat_history.clear()

    @override
    async def _on_new_message(self, new_message: str | ChatMessageContent) -> None:
        """Called when a new message has been contributed to the chat."""
        if isinstance(new_message, str):
            new_message = ChatMessageContent(role=AuthorRole.USER, content=new_message)

        if (
            not new_message.metadata
            or "thread_id" not in new_message.metadata
            or new_message.metadata["thread_id"] != self._id
        ):
            self._chat_history.add_message(new_message)

    async def get_messages(self) -> AsyncIterable[ChatMessageContent]:
        """Retrieve the current chat history.

        Returns:
            An async iterable of ChatMessageContent.
        """
        if self._is_deleted:
            raise AgentThreadOperationException("Cannot retrieve chat history, since the thread has been deleted.")
        if self._id is None:
            await self.create()
        for message in self._chat_history.messages:
            yield message

    async def reduce(self) -> ChatHistory | None:
        """Reduce the chat history to a smaller size."""
        if self._id is None:
            raise AgentThreadOperationException("Cannot reduce chat history, since the thread is not currently active.")
        if not isinstance(self._chat_history, ChatHistoryReducer):
            return None
        return await self._chat_history.reduce()

class ProxyAgentResponseItem:
    """Response item wrapper for proxy agent responses."""
    
    def __init__(self, message: ChatMessageContent, thread: AgentThread):
        self.message = message
        self.thread = thread
        self.logger = logging.getLogger(__name__)

class ProxyAgent(Agent):
    """Simple proxy agent that prompts for human clarification."""
    
    def __init__(self):
        super().__init__(
            name="ProxyAgent", 
            description="""Call this agent when you need to clarify requests by asking the human user 
            for more information. Ask it for more details about any unclear requirements, missing information, 
            or if you need the user to elaborate on any aspect of the task."""
        )
        self.instructions = ""
    
    async def invoke(self, message: str,*, thread: AgentThread | None = None,**kwargs) -> AsyncIterator[ChatMessageContent]:
        """Ask human user for clarification about the message."""

        thread = await self._ensure_thread_exists_with_messages(
            messages=message,
            thread=thread,
            construct_thread=lambda: DummyAgentThread(),
            expected_type=DummyAgentThread,
        )
        # Replace with websocket call when available
        print(f"\n🤔 ProxyAgent: Another agent is asking for clarification about:")
        print(f"   Request: {message}")
        print("-" * 60)
        
        # Get human input
        human_response = input("Please provide clarification: ").strip()
        
        if not human_response:
            human_response = "No additional clarification provided."
        
        response = f"Human clarification: {human_response}"

        chat_message = ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            content=response,
            name=self.name,
            metadata={"thread_id": thread.id}
        )
        
        yield AgentResponseItem(
            message=chat_message,
            thread=thread
        )
    
    async def invoke_stream(self, messages, thread=None, **kwargs) -> AsyncIterator[ProxyAgentResponseItem]:
        """Stream version - handles thread management for orchestration."""

        thread = await self._ensure_thread_exists_with_messages(
            messages=messages,
            thread=thread,
            construct_thread=lambda: DummyAgentThread(),
            expected_type=DummyAgentThread,
        )

        # Extract message content
        if isinstance(messages, list) and messages:
            message = messages[-1].content if hasattr(messages[-1], 'content') else str(messages[-1])
        elif isinstance(messages, str):
            message = messages
        else:
            message = str(messages)

        # Replace with websocket call when available
        print(f"\nProxyAgent: Another agent is asking for clarification about:")
        print(f"   Request: {message}")
        print("-" * 60)
        
        # Get human input - replace with websocket call when available
        human_response = input("Please provide clarification: ").strip()
        
        if not human_response:
            human_response = "No additional clarification provided."
        
        response = f"Human clarification: {human_response}"
        
        chat_message = ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            content=response,
            name=self.name,
            metadata={"thread_id": thread.id}
        )
        
        yield AgentResponseItem(
            message=chat_message,
            thread=thread
        )

    async def get_response(self, chat_history, **kwargs):
        """Get response from the agent - required by Agent base class."""
        # Extract the latest user message
        latest_message = chat_history.messages[-1].content if chat_history.messages else ""
        
        # Use our invoke method to get the response
        async for response in self.invoke(latest_message, **kwargs):
            return response
        
        # Fallback if no response generated
        return ChatMessageContent(
            role=AuthorRole.ASSISTANT,
            content="No clarification provided."
        )

async def create_proxy_agent():
    """Factory function for human proxy agent."""
    return ProxyAgent()