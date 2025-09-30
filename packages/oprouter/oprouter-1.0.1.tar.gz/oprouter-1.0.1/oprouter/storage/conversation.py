"""Conversation management system for OpRouter."""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

from ..core.config import get_config
from ..core.logger import logger


class MessageRole(Enum):
    """Message roles."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class Message:
    """Chat message."""
    role: MessageRole
    content: str
    timestamp: datetime
    tokens: Optional[int] = None
    cost: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "role": self.role.value,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
            "tokens": self.tokens,
            "cost": self.cost
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create from dictionary."""
        return cls(
            role=MessageRole(data["role"]),
            content=data["content"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
            tokens=data.get("tokens"),
            cost=data.get("cost")
        )
    
    def to_api_format(self) -> Dict[str, str]:
        """Convert to API format."""
        return {
            "role": self.role.value,
            "content": self.content
        }


@dataclass
class ConversationMetadata:
    """Conversation metadata."""
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    model: str
    total_tokens: int = 0
    total_cost: float = 0.0
    message_count: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        data = asdict(self)
        # Convert datetime objects to ISO format strings
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversationMetadata':
        """Create from dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            model=data["model"],
            total_tokens=data.get("total_tokens", 0),
            total_cost=data.get("total_cost", 0.0),
            message_count=data.get("message_count", 0)
        )


class Conversation:
    """Conversation management."""
    
    def __init__(self, conversation_id: Optional[str] = None, title: Optional[str] = None, model: Optional[str] = None):
        self.config = get_config()
        self.id = conversation_id or str(uuid.uuid4())
        self.title = title or f"Conversation {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        self.model = model or self.config.default_model
        
        self.messages: List[Message] = []
        self.metadata = ConversationMetadata(
            id=self.id,
            title=self.title,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            model=self.model
        )
        
        # Ensure conversations directory exists
        self.conversations_dir = Path(self.config.conversations_dir)
        self.conversations_dir.mkdir(exist_ok=True)
        
        logger.info(f"Initialized conversation: {self.id}")
    
    def add_message(self, role: MessageRole, content: str, tokens: Optional[int] = None, cost: Optional[float] = None):
        """Add a message to the conversation."""
        message = Message(
            role=role,
            content=content,
            timestamp=datetime.now(),
            tokens=tokens,
            cost=cost
        )
        
        self.messages.append(message)
        self._update_metadata(tokens, cost)
        
        # Auto-save if enabled
        if self.config.auto_save_conversations:
            self.save()
        
        logger.debug(f"Added {role.value} message with {len(content)} characters")
    
    def _update_metadata(self, tokens: Optional[int] = None, cost: Optional[float] = None):
        """Update conversation metadata."""
        self.metadata.updated_at = datetime.now()
        self.metadata.message_count = len(self.messages)
        
        if tokens:
            self.metadata.total_tokens += tokens
        if cost:
            self.metadata.total_cost += cost
    
    def get_messages_for_api(self, limit: Optional[int] = None) -> List[Dict[str, str]]:
        """Get messages in API format."""
        messages = self.messages
        if limit:
            messages = messages[-limit:]
        
        return [msg.to_api_format() for msg in messages]
    
    def get_context_window(self, max_tokens: int = 4000) -> List[Dict[str, str]]:
        """Get messages that fit within token limit."""
        # Simple approximation: 4 characters per token
        current_tokens = 0
        context_messages = []
        
        for message in reversed(self.messages):
            message_tokens = len(message.content) // 4
            if current_tokens + message_tokens > max_tokens:
                break
            
            context_messages.insert(0, message.to_api_format())
            current_tokens += message_tokens
        
        return context_messages
    
    def save(self) -> bool:
        """Save conversation based on storage type configuration."""
        if self.config.is_memory_storage():
            # Store in memory (handled by ConversationManager)
            return True
        elif self.config.is_file_storage():
            try:
                file_path = self.conversations_dir / f"{self.id}.json"

                data = {
                    "metadata": self.metadata.to_dict(),
                    "messages": [msg.to_dict() for msg in self.messages]
                }

                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                logger.info(f"Saved conversation to {file_path}")
                return True

            except Exception as e:
                logger.error(f"Failed to save conversation: {e}")
                return False
        # TODO: Add new storage types here
        # elif self.config.storage_type == 'database':
        #     return self._save_to_database()
        # elif self.config.storage_type == 'cloud':
        #     return self._save_to_cloud()
        else:
            logger.error(f"Unsupported storage type: {self.config.storage_type}")
            return False
    
    @classmethod
    def load(cls, conversation_id: str) -> Optional['Conversation']:
        """Load conversation from file."""
        try:
            config = get_config()

            # If using memory storage, this will be handled by ConversationManager
            if config.is_memory_storage():
                logger.warning("Cannot load individual conversations when using memory storage")
                return None

            file_path = Path(config.conversations_dir) / f"{conversation_id}.json"

            if not file_path.exists():
                logger.warning(f"Conversation file not found: {file_path}")
                return None

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Create conversation instance
            metadata = ConversationMetadata.from_dict(data["metadata"])
            conversation = cls(
                conversation_id=metadata.id,
                title=metadata.title,
                model=metadata.model
            )
            conversation.metadata = metadata

            # Load messages
            conversation.messages = [
                Message.from_dict(msg_data)
                for msg_data in data["messages"]
            ]

            logger.info(f"Loaded conversation: {conversation_id}")
            return conversation

        except Exception as e:
            logger.error(f"Failed to load conversation {conversation_id}: {e}")
            return None
    
    def export_to_text(self) -> str:
        """Export conversation to text format."""
        lines = [
            f"Conversation: {self.title}",
            f"ID: {self.id}",
            f"Model: {self.model}",
            f"Created: {self.metadata.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Messages: {self.metadata.message_count}",
            f"Total Tokens: {self.metadata.total_tokens}",
            f"Total Cost: ${self.metadata.total_cost:.4f}",
            "=" * 50,
            ""
        ]
        
        for message in self.messages:
            timestamp = message.timestamp.strftime('%H:%M:%S')
            role = message.role.value.upper()
            lines.append(f"[{timestamp}] {role}:")
            lines.append(message.content)
            lines.append("")
        
        return "\n".join(lines)
    
    def clear(self):
        """Clear all messages."""
        self.messages.clear()
        self._update_metadata()
        logger.info("Cleared conversation messages")
    
    def set_title(self, title: str):
        """Set conversation title."""
        self.title = title
        self.metadata.title = title
        self._update_metadata()
        logger.info(f"Updated conversation title to: {title}")


class ConversationManager:
    """Manage multiple conversations."""
    
    def __init__(self):
        self.config = get_config()
        self.conversations_dir = Path(self.config.conversations_dir)
        self.current_conversation: Optional[Conversation] = None

        # In-memory storage for conversations
        self._memory_conversations: Dict[str, Conversation] = {}

        # Only create directory if using file storage
        if self.config.is_file_storage():
            self.conversations_dir.mkdir(exist_ok=True)
    
    def create_conversation(self, title: Optional[str] = None, model: Optional[str] = None) -> Conversation:
        """Create a new conversation."""
        conversation = Conversation(title=title, model=model)
        self.current_conversation = conversation

        # Store in memory if using memory storage
        if self.config.is_memory_storage():
            self._memory_conversations[conversation.id] = conversation

        return conversation
    
    def load_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Load and set as current conversation."""
        if self.config.is_memory_storage():
            # Load from memory
            conversation = self._memory_conversations.get(conversation_id)
            if conversation:
                self.current_conversation = conversation
            return conversation
        elif self.config.is_file_storage():
            # Load from file
            conversation = Conversation.load(conversation_id)
            if conversation:
                self.current_conversation = conversation
            return conversation
        else:
            logger.error(f"Unsupported storage type: {self.config.storage_type}")
            return None
    
    def list_conversations(self) -> List[ConversationMetadata]:
        """List all saved conversations."""
        conversations = []

        if self.config.is_memory_storage():
            # List from memory
            for conversation in self._memory_conversations.values():
                conversations.append(conversation.metadata)
        elif self.config.is_file_storage():
            # List from files
            for file_path in self.conversations_dir.glob("*.json"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    metadata = ConversationMetadata.from_dict(data["metadata"])
                    conversations.append(metadata)

                except Exception as e:
                    logger.warning(f"Failed to load conversation metadata from {file_path}: {e}")
        else:
            logger.error(f"Unsupported storage type: {self.config.storage_type}")

        # Sort by updated_at descending
        conversations.sort(key=lambda x: x.updated_at, reverse=True)
        return conversations
    
    def delete_conversation(self, conversation_id: str) -> bool:
        """Delete a conversation."""
        try:
            if self.config.is_memory_storage():
                # Delete from memory
                if conversation_id in self._memory_conversations:
                    del self._memory_conversations[conversation_id]
                    logger.info(f"Deleted conversation from memory: {conversation_id}")

                    # Clear current conversation if it's the deleted one
                    if self.current_conversation and self.current_conversation.id == conversation_id:
                        self.current_conversation = None

                    return True
                else:
                    logger.warning(f"Conversation not found in memory: {conversation_id}")
                    return False
            elif self.config.is_file_storage():
                # Delete from file
                file_path = self.conversations_dir / f"{conversation_id}.json"
                if file_path.exists():
                    file_path.unlink()
                    logger.info(f"Deleted conversation: {conversation_id}")

                    # Clear current conversation if it's the deleted one
                    if self.current_conversation and self.current_conversation.id == conversation_id:
                        self.current_conversation = None

                    return True
                else:
                    logger.warning(f"Conversation file not found: {conversation_id}")
                    return False
            else:
                logger.error(f"Unsupported storage type: {self.config.storage_type}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to delete conversation {conversation_id}: {e}")
            return False
