"""Text formatting utilities for OpRouter."""

import re
from typing import List, Tuple
from datetime import datetime, timedelta


class TextFormatter:
    """Text formatting utilities."""

    @staticmethod
    def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
        """Truncate text to maximum length."""
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix

    @staticmethod
    def extract_code_blocks(text: str) -> List[Tuple[str, str]]:
        """Extract code blocks from markdown text."""
        pattern = r'```(\w+)?\n(.*?)\n```'
        matches = re.findall(pattern, text, re.DOTALL)
        return [(lang or "text", code.strip()) for lang, code in matches]

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text by removing extra whitespace and normalizing."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove leading/trailing whitespace
        text = text.strip()
        return text

    @staticmethod
    def format_timestamp(dt: datetime, format_type: str = "relative") -> str:
        """Format timestamp in various ways."""
        if format_type == "relative":
            now = datetime.now()
            diff = now - dt

            if diff.days > 0:
                return f"{diff.days} days ago"
            elif diff.seconds > 3600:
                hours = diff.seconds // 3600
                return f"{hours} hours ago"
            elif diff.seconds > 60:
                minutes = diff.seconds // 60
                return f"{minutes} minutes ago"
            else:
                return "Just now"

        elif format_type == "short":
            return dt.strftime("%m/%d %H:%M")

        elif format_type == "long":
            return dt.strftime("%Y-%m-%d %H:%M:%S")

        else:
            return dt.isoformat()


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations."""
    # Remove or replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')

    # Limit length
    if len(filename) > 200:
        filename = filename[:200]

    return filename.strip()


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format."""
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1

    return f"{size_bytes:.1f} {size_names[i]}"