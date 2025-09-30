"""Emoji utilities for cross-platform compatibility."""

import os
import platform
from typing import Dict
from ..core.config import get_config


class EmojiManager:
    """Manages emoji display based on platform and configuration."""
    
    # Emoji mappings with text alternatives
    EMOJI_MAP = {
        # Status emojis
        'success': {'emoji': '✅', 'text': '[OK]'},
        'error': {'emoji': '❌', 'text': '[ERROR]'},
        'warning': {'emoji': '⚠️', 'text': '[WARNING]'},
        'info': {'emoji': 'ℹ️', 'text': '[INFO]'},
        
        # UI emojis
        'robot': {'emoji': '🤖', 'text': '[AI]'},
        'user': {'emoji': '👤', 'text': '[USER]'},
        'goodbye': {'emoji': '👋', 'text': '[BYE]'},
        
        # Feature emojis
        'retry': {'emoji': '🔄', 'text': '[RETRY]'},
        'chat': {'emoji': '💬', 'text': '[CHAT]'},
        'target': {'emoji': '🎯', 'text': '[TARGET]'},
        'stats': {'emoji': '📊', 'text': '[STATS]'},
        'art': {'emoji': '🎨', 'text': '[UI]'},
        'rocket': {'emoji': '🚀', 'text': '[START]'},
        'gear': {'emoji': '⚙️', 'text': '[CONFIG]'},
        'book': {'emoji': '📚', 'text': '[DOCS]'},
        'folder': {'emoji': '📁', 'text': '[FOLDER]'},
        'save': {'emoji': '💾', 'text': '[SAVE]'},
        'load': {'emoji': '📂', 'text': '[LOAD]'},
        'export': {'emoji': '📤', 'text': '[EXPORT]'},
        'clear': {'emoji': '🗑️', 'text': '[CLEAR]'},
        'title': {'emoji': '📝', 'text': '[TITLE]'},
        'model': {'emoji': '🧠', 'text': '[MODEL]'},
        'list': {'emoji': '📋', 'text': '[LIST]'},
        'help': {'emoji': '❓', 'text': '[HELP]'},
        'new': {'emoji': '✨', 'text': '[NEW]'},
        'spinner': {'emoji': '⠋', 'text': '[...]'},
    }
    
    def __init__(self):
        self.config = get_config()
        self._should_use_emojis = self._detect_emoji_support()
    
    def _detect_emoji_support(self) -> bool:
        """Detect if emojis should be used based on platform and config."""
        # Check config first
        if not self.config.use_emojis:
            return False
        
        # Auto-detect based on platform and terminal
        system = platform.system().lower()
        
        # Windows Command Prompt and PowerShell often have emoji issues
        if system == 'windows':
            # Check if we're in Windows Terminal (which supports emojis better)
            wt_session = os.environ.get('WT_SESSION')
            if wt_session:
                return True
            
            # Check terminal type
            term = os.environ.get('TERM', '').lower()
            if 'xterm' in term or 'color' in term:
                return True
            
            # Default to no emojis on Windows unless explicitly enabled
            return False
        
        # Unix-like systems generally support emojis
        return True
    
    def get(self, key: str) -> str:
        """Get emoji or text alternative based on configuration."""
        if key not in self.EMOJI_MAP:
            return key
        
        mapping = self.EMOJI_MAP[key]
        if self._should_use_emojis:
            return mapping['emoji']
        else:
            return mapping['text']
    
    def format_message(self, key: str, message: str) -> str:
        """Format a message with emoji/text prefix."""
        prefix = self.get(key)
        return f"{prefix} {message}"
    
    @property
    def use_emojis(self) -> bool:
        """Check if emojis are enabled."""
        return self._should_use_emojis


# Global emoji manager instance
emoji = EmojiManager()
