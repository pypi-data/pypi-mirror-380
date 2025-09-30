"""Storage interfaces for OpRouter."""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any


class ConversationStorageInterface(ABC):
    """Interface for conversation storage implementations."""

    @abstractmethod
    def save_conversation(self, conversation_id: str, data: Dict[str, Any]) -> bool:
        """Save conversation data."""
        pass

    @abstractmethod
    def load_conversation(self, conversation_id: str) -> Optional[Dict[str, Any]]:
        """Load conversation data."""
        pass

    @abstractmethod
    def delete_conversation(self, conversation_id: str) -> bool:
        """Delete conversation."""
        pass

    @abstractmethod
    def list_conversations(self) -> List[Dict[str, Any]]:
        """List all conversations."""
        pass

    @abstractmethod
    def conversation_exists(self, conversation_id: str) -> bool:
        """Check if conversation exists."""
        pass


class MessageStorageInterface(ABC):
    """Interface for message storage implementations."""

    @abstractmethod
    def add_message(self, conversation_id: str, message: Dict[str, Any]) -> bool:
        """Add message to conversation."""
        pass

    @abstractmethod
    def get_messages(self, conversation_id: str) -> List[Dict[str, Any]]:
        """Get all messages for a conversation."""
        pass

    @abstractmethod
    def update_message(self, conversation_id: str, message_id: str, data: Dict[str, Any]) -> bool:
        """Update a specific message."""
        pass

    @abstractmethod
    def delete_message(self, conversation_id: str, message_id: str) -> bool:
        """Delete a specific message."""
        pass