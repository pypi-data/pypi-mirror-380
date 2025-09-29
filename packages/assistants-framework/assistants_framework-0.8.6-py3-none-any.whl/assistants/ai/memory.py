"""
This module provides the `MemoryMixin` class, which handles memory-related functionality
for managing conversations.

Classes:
    - MemoryMixin: Mixin class to handle memory-related functionality, including remembering
        messages, truncating memory, and loading/saving conversations from/to a database.
"""

import json
import uuid
from abc import abstractmethod
from copy import deepcopy
from datetime import datetime
from typing import Optional, cast

import tiktoken

from assistants.ai.types import (
    ConversationManagementInterface,
    MessageData,
    MessageDict,
    MessageInput,
)
from assistants.config import environment
from assistants.user_data.sqlite_backend.conversations import (
    Conversation,
    get_conversations_table,
)
from assistants.user_data.sqlite_backend.message import (
    Message,
    get_messages_table,
)

encoding = tiktoken.encoding_for_model("gpt-4o-mini")


class ConversationHistoryMixin(ConversationManagementInterface):
    """Implements conversation management functionality."""

    def __init__(
        self, max_tokens: int = environment.DEFAULT_MAX_HISTORY_TOKENS
    ) -> None:
        """
        Initialise the MemoryMixin instance.

        :param max_tokens: Maximum number of messages to retain in memory.
        """
        self.memory: list[MessageInput] = []
        self.max_history_tokens = max_tokens
        self.conversation_id: str | None = None

    def truncate_memory(self):
        """
        Use the tiktoken library to truncate memory if it exceeds the maximum token limit.
        """
        while (
            self.memory
            and self.max_history_tokens
            and self.max_history_tokens < self._get_token_count()
        ):
            self.memory.pop(0)

    async def remember(self, message: MessageDict, audio: Optional[bool] = False):
        """
        Remember a new message.

        :param message: The message to remember.
        """
        conversation: Optional[Conversation]

        if self.conversation_id is None:
            conversation = Conversation(
                id=uuid.uuid4().hex,
                last_updated=datetime.now(),
            )
            await conversation.save()
            self.conversation_id = conversation.id
        else:
            conversation = await get_conversations_table().get(id=self.conversation_id)
            if not conversation:
                # If the conversation doesn't exist, create a new one
                conversation = Conversation(
                    id=self.conversation_id,
                    last_updated=datetime.now(),
                )
            conversation.last_updated = datetime.now()
            await conversation.save()

        self.memory.append(message)
        db_message = Message(
            role=message["role"],
            content=message["content"] or "",
            conversation_id=str(self.conversation_id),
        )
        await db_message.save()
        self.truncate_memory()

    async def load_conversation(
        self,
        conversation_id: Optional[str] = None,
    ) -> None:
        """
        Load the last conversation from the database.

        Args:
            conversation_id: Optional ID of the conversation to load.
        """
        if conversation_id:
            await self._load_specific_conversation(conversation_id)
        else:
            await self._load_latest_conversation()

    async def _load_specific_conversation(self, conversation_id: str):
        """Load a conversation with a specific ID or create it if it doesn't exist."""
        conversation = await get_conversations_table().get(id=conversation_id)
        if not conversation:
            # Create a new conversation if it doesn't exist
            conversation = Conversation(
                id=str(conversation_id),
                last_updated=datetime.now(),
            )
            await conversation.save()

        messages = await get_messages_table().get_by_conversation_id(conversation_id)
        self._load_memory_from_messages(messages)
        self.conversation_id = conversation_id

    async def _load_latest_conversation(self):
        """Load the most recent conversation or create a new one if none exists."""
        latest = await get_conversations_table().get_last_conversation()

        if not latest:
            # Create a new conversation if none exists
            self.conversation_id = uuid.uuid4().hex
            latest = Conversation(
                id=self.conversation_id,
                last_updated=datetime.now(),
            )
            await latest.save()
        else:
            self.conversation_id = latest.id

            messages = await get_messages_table().get_by_conversation_id(latest.id)
            self._load_memory_from_messages(messages)

    def _load_memory_from_messages(self, messages: list[Message]) -> None:
        """Convert database message objects to memory format."""
        self.memory = [
            MessageDict(role=message.role, content=message.content)
            for message in messages
        ]
        self.truncate_memory()

    def _convert_system_messages_to_instructions(
        self, instructions_understood_message: str
    ):
        """Convert system messages to user/assistant pairs."""
        temp_memory: list[MessageInput] = []
        for message in self.memory:
            if message["role"] == "system":
                temp_memory.extend(
                    [
                        MessageDict(role="user", content=cast(str, message["content"])),
                        MessageDict(
                            role="assistant", content=instructions_understood_message
                        ),
                    ]
                )
            else:
                temp_memory.append(message)
        self.memory = temp_memory

    async def async_get_conversation_id(self):
        if not self.conversation_id:
            await self.load_conversation()
        return self.conversation_id

    async def get_last_message(self) -> Optional[MessageData]:
        """
        Get the last message from the conversation or None if no message exists.
        Conversation must have already been loaded.

        :return: MessageData with the last message and current conversation_id.
        """
        if not self.memory:
            return None
        return MessageData(
            text_content=cast(str, self.memory[-1]["content"]) or "",
            thread_id=self.conversation_id,
        )

    @abstractmethod
    async def converse(
        self, user_input: str, thread_id: Optional[str] = None
    ) -> Optional[MessageData]:
        raise NotImplementedError

    async def get_whole_thread(self) -> list[MessageInput]:
        """
        Get the whole thread of messages.
        :return: List of messages in the thread.
        """
        return self.memory

    def _get_token_count(self):
        return len(encoding.encode(json.dumps(self.memory)))

    def clean_audio_messages(self):
        temp_memory = deepcopy(self.memory)
        for item in temp_memory:
            if "audio" in item:
                del item["audio"]
            if item["content"].startswith("[AUDIO TRANSCRIPTION] "):
                item["content"] = item["content"].replace("[AUDIO TRANSCRIPTION]: ", "")
        return temp_memory
