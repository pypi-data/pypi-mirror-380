"""Configuration management for OpRouter."""

import os
from pathlib import Path
from typing import Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config(BaseSettings):
    """Application configuration."""

    # API Configuration
    openrouter_api_key: Optional[str] = Field(None, env="OPENROUTER_API_KEY")
    default_model: str = Field("x-ai/grok-4-fast:free", env="DEFAULT_MODEL")
    base_url: str = Field("https://openrouter.ai/api/v1", env="BASE_URL")
    
    # Rate Limiting
    max_requests_per_minute: int = Field(60, env="MAX_REQUESTS_PER_MINUTE")
    max_concurrent_requests: int = Field(5, env="MAX_CONCURRENT_REQUESTS")
    
    # Retry Configuration
    max_retries: int = Field(5, env="MAX_RETRIES")
    base_delay: float = Field(1.0, env="BASE_DELAY")
    max_delay: float = Field(60.0, env="MAX_DELAY")
    backoff_multiplier: float = Field(2.0, env="BACKOFF_MULTIPLIER")
    
    # Logging
    log_level: str = Field("INFO", env="LOG_LEVEL")
    log_file: str = Field("oprouter.log", env="LOG_FILE")
    enable_logging: bool = Field(True, env="ENABLE_LOGGING")

    # UI Configuration
    use_emojis: bool = Field(True, env="USE_EMOJIS")

    # Conversation Management
    conversation_history_limit: int = Field(100, env="CONVERSATION_HISTORY_LIMIT")
    auto_save_conversations: bool = Field(True, env="AUTO_SAVE_CONVERSATIONS")
    conversations_dir: str = Field("conversations", env="CONVERSATIONS_DIR")
    storage_type: str = Field("file", env="STORAGE_TYPE")  # 'file', 'memory', or future: 'database', 'cloud'

    @validator('storage_type')
    def validate_storage_type(cls, v):
        """Validate storage type.

        Current supported types: 'file', 'memory'
        Future types could include: 'database', 'cloud', 'encrypted', 'redis', 'sqlite'

        To add a new storage type:
        1. Add it to valid_types list below
        2. Add corresponding is_<type>_storage() method
        3. Update ConversationManager and Conversation classes to handle the new type
        """
        valid_types = ['file', 'memory']
        if v.lower() not in valid_types:
            raise ValueError(f"storage_type must be one of {valid_types}, got '{v}'")
        return v.lower()

    def is_memory_storage(self) -> bool:
        """Check if using memory storage."""
        return self.storage_type == 'memory'

    def is_file_storage(self) -> bool:
        """Check if using file storage."""
        return self.storage_type == 'file'

    class Config:
        env_file = ".env"
        case_sensitive = False


def get_config() -> Config:
    """Get application configuration."""
    return Config()


def ensure_directories():
    """Ensure required directories exist."""
    config = get_config()
    conversations_path = Path(config.conversations_dir)
    conversations_path.mkdir(exist_ok=True)
    
    logs_path = Path(config.log_file).parent
    if logs_path != Path("."):
        logs_path.mkdir(exist_ok=True)
