"""Conversation analysis utilities for OpRouter."""

import re
from typing import List, Dict, Any
from datetime import datetime


class ConversationAnalyzer:
    """Analyze conversation patterns and statistics."""

    @staticmethod
    def analyze_conversation(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze conversation for insights."""
        if not messages:
            return {}

        user_messages = [msg for msg in messages if msg.get("role") == "user"]
        assistant_messages = [msg for msg in messages if msg.get("role") == "assistant"]

        # Basic statistics
        total_messages = len(messages)
        user_message_count = len(user_messages)
        assistant_message_count = len(assistant_messages)

        # Content analysis
        total_user_chars = sum(len(msg.get("content", "")) for msg in user_messages)
        total_assistant_chars = sum(len(msg.get("content", "")) for msg in assistant_messages)

        avg_user_length = total_user_chars / user_message_count if user_message_count > 0 else 0
        avg_assistant_length = total_assistant_chars / assistant_message_count if assistant_message_count > 0 else 0

        # Time analysis
        timestamps = [
            datetime.fromisoformat(msg["timestamp"])
            for msg in messages
            if "timestamp" in msg
        ]

        duration = None
        if len(timestamps) >= 2:
            duration = (max(timestamps) - min(timestamps)).total_seconds()

        # Token analysis
        total_tokens = sum(msg.get("tokens", 0) for msg in messages)
        total_cost = sum(msg.get("cost", 0.0) for msg in messages)

        return {
            "total_messages": total_messages,
            "user_messages": user_message_count,
            "assistant_messages": assistant_message_count,
            "total_characters": total_user_chars + total_assistant_chars,
            "avg_user_message_length": round(avg_user_length, 1),
            "avg_assistant_message_length": round(avg_assistant_length, 1),
            "conversation_duration_seconds": duration,
            "total_tokens": total_tokens,
            "total_cost": total_cost,
            "messages_per_minute": round(total_messages / (duration / 60), 2) if duration and duration > 0 else 0
        }

    @staticmethod
    def extract_topics(messages: List[Dict[str, Any]]) -> List[str]:
        """Extract potential topics from conversation."""
        # Simple keyword extraction - could be enhanced with NLP
        text = " ".join(msg.get("content", "") for msg in messages)

        # Remove common words and extract potential topics
        words = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())

        # Count word frequency
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Get top words (excluding very common ones)
        common_words = {
            "that", "this", "with", "have", "will", "from", "they", "been",
            "were", "said", "each", "which", "their", "time", "would", "there",
            "what", "about", "when", "where", "could", "should", "might"
        }

        topics = [
            word for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            if freq >= 2 and word not in common_words
        ]

        return topics[:10]  # Return top 10 topics