# 🤖 OpRouter - OpenRouter SDK Client for Python

A Python library for chatting with AI models through OpenRouter. Simple to use, reliable, and feature-rich.

## What is OpRouter?

OpRouter makes it easy to build AI-powered applications by providing:
- **Simple API**: Chat with AI in just a few lines of code
- **Reliable**: Automatic retries when things go wrong
- **Smart**: Manages conversations and tracks usage
- **Interactive**: Beautiful command-line chat interface

Perfect for developers who want to integrate AI chat into their projects without dealing with API complexities.

## ✨ Key Features

- **Easy Integration**: Start chatting with AI in 3 lines of code
- **Automatic Retries**: Handles rate limits and network issues automatically
- **Conversation Memory**: Save and resume conversations
- **Multiple Models**: Works with any OpenRouter-supported AI model
- **Token Tracking**: Monitor usage and costs
- **Streaming Responses**: Get responses as they're generated
- **Interactive CLI**: Ready-to-use chat interface

## 🚀 Quick Start

### Installation

**Option 1: Install from PyPI (recommended)**
```bash
pip install oprouter
```

**Option 2: Install from source (for development)**
```bash
git clone https://github.com/DedInc/oprouter.git
cd oprouter
pip install -e .
```

### Get Your API Key

1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Get your [API key](https://openrouter.ai/settings/keys) from the dashboard
3. Set it as an environment variable:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```

### Start Chatting

**Option 1: Interactive CLI (after installation)**
```bash
# If installed with pip
oprouter

# Or using Python module
python -m oprouter
```

**Option 2: Development mode**
```bash
python main.py
```

**Option 3: Use in Your Code**
```python
import asyncio
from oprouter.api_client import OpenRouterClient

async def chat():
    async with OpenRouterClient() as client:
        response = await client.chat_completion([
            {"role": "user", "content": "Hello!"}
        ])
        print(response.data['choices'][0]['message']['content'])

asyncio.run(chat())
```

## 📚 Usage Examples

### 1. Simple Chat (3 lines!)

```python
import asyncio
from oprouter.api_client import OpenRouterClient

async def simple_chat():
    async with OpenRouterClient() as client:
        response = await client.chat_completion([
            {"role": "user", "content": "Explain Python in one sentence"}
        ])
        print(response.data['choices'][0]['message']['content'])

asyncio.run(simple_chat())
```

### 2. Conversation with Memory

```python
import asyncio
from oprouter.api_client import OpenRouterClient
from oprouter.conversation import Conversation, MessageRole

async def conversation_example():
    async with OpenRouterClient() as client:
        # Create a conversation that remembers context
        conversation = Conversation(title="My Chat")

        # Add messages and get responses
        messages = ["Hi, I'm learning Python", "What should I learn first?"]

        for user_msg in messages:
            conversation.add_message(MessageRole.USER, user_msg)

            # Get conversation context for API
            context = conversation.get_context_window()
            response = await client.chat_completion(context)

            if response.success:
                ai_msg = response.data['choices'][0]['message']['content']
                conversation.add_message(MessageRole.ASSISTANT, ai_msg)
                print(f"You: {user_msg}")
                print(f"AI: {ai_msg}\n")

        # Save conversation
        conversation.save()
        print(f"Conversation saved with ID: {conversation.id}")

asyncio.run(conversation_example())
```

### 3. Streaming Responses

```python
import asyncio
from oprouter.api_client import OpenRouterClient

async def streaming_example():
    async with OpenRouterClient() as client:
        messages = [{"role": "user", "content": "Write a short poem"}]

        print("AI: ", end="", flush=True)
        async for chunk in client.chat_completion_stream(messages):
            print(chunk, end="", flush=True)
        print()  # New line

asyncio.run(streaming_example())
```

### 4. Different Models

```python
import asyncio
from oprouter.api_client import OpenRouterClient

async def model_example():
    # Use a specific model
    async with OpenRouterClient(model="anthropic/claude-3-haiku") as client:
        response = await client.chat_completion([
            {"role": "user", "content": "Hello from Claude!"}
        ])
        print(response.data['choices'][0]['message']['content'])

asyncio.run(model_example())
```

### 5. Error Handling

```python
import asyncio
from oprouter.api_client import OpenRouterClient

async def safe_chat():
    async with OpenRouterClient() as client:
        response = await client.chat_completion([
            {"role": "user", "content": "Hello!"}
        ])

        if response.success:
            print("AI:", response.data['choices'][0]['message']['content'])
        else:
            print("Error:", response.error)

asyncio.run(safe_chat())
```

## 📖 CLI Commands

When using `python main.py`, you get an interactive chat with these commands:

| Command | Description |
|---------|-------------|
| `/help` | Show help message |
| `/new [title]` | Start new conversation |
| `/list` | List all conversations |
| `/load <id>` | Load conversation by ID |
| `/save` | Save current conversation |
| `/export` | Export conversation to text |
| `/clear` | Clear current conversation |
| `/title <title>` | Set conversation title |
| `/model <model>` | Change AI model |
| `/models` | List available models |
| `/stats` | Show conversation statistics |
| `/quit` | Exit application |

## ⚙️ Configuration

### Environment Variables

```bash
# Required
OPENROUTER_API_KEY=your_api_key_here

# Optional - customize behavior
DEFAULT_MODEL=anthropic/claude-3-haiku        # Which AI model to use
MAX_REQUESTS_PER_MINUTE=60                    # Rate limiting
MAX_CONCURRENT_REQUESTS=5                     # Parallel requests
MAX_RETRIES=5                                 # Retry failed requests

# Logging & UI
LOG_LEVEL=INFO                                # Logging detail (DEBUG, INFO, WARNING, ERROR)
ENABLE_LOGGING=true                           # Enable/disable logging
USE_EMOJIS=true                               # Enable/disable emojis (auto-detected on Windows)

# Storage
STORAGE_TYPE=file                             # Storage type: 'file' or 'memory'
CONVERSATIONS_DIR=conversations               # Directory for saved conversations (file storage)
AUTO_SAVE_CONVERSATIONS=true                  # Auto-save conversations
```

### Using Different Models

```python
# In your code
client = OpenRouterClient(model="anthropic/claude-3-sonnet")

# Or via environment
export DEFAULT_MODEL="openai/gpt-4"
```

Popular models:
- `anthropic/claude-sonnet-4` - Ultimate coding agent
- `x-ai/grok-4-fast:free` - Multimodal speed demon, 2M context
- `openai/gpt-5-codex` - Engineering powerhouse, structured outputs
- `deepseek/deepseek-chat-v3.1:free` - Hybrid reasoning beast, free mode
- `deepseek/deepseek-v3.2-exp` - Experimental sparse attention for long contexts

## 🔄 Reliability Features

OpRouter automatically handles common issues:

- **Rate Limits**: Waits and retries when you hit API limits
- **Network Issues**: Retries failed requests with smart delays
- **Concurrent Requests**: Manages multiple requests safely
- **Error Recovery**: Graceful handling of API errors

You don't need to worry about these - OpRouter handles them automatically!

## 🎛️ Advanced Configuration

### Windows Compatibility

OpRouter automatically detects Windows Command Prompt and disables emojis for better compatibility. If you're using Windows Terminal or want to force emoji usage:

```bash
export USE_EMOJIS=true
```

### Storage Types

**File Storage (default)**: Conversations saved to disk, persist between sessions
```bash
export STORAGE_TYPE=file
```

**Memory Storage**: Conversations only exist during the session, faster but temporary
```bash
export STORAGE_TYPE=memory
```

**Future Storage Types**: The system is designed to support additional storage types like:
- `database` - Store in SQL/NoSQL database
- `cloud` - Store in cloud services (AWS S3, Google Cloud, etc.)
- `encrypted` - Encrypted local storage

### Logging Control

**Enable logging** (default):
```bash
export ENABLE_LOGGING=true
export LOG_LEVEL=INFO
```

**Disable logging** for cleaner output:
```bash
export ENABLE_LOGGING=false
```

## 📊 Monitoring Usage

### Track Token Usage

```python
# After a conversation
print(f"Tokens used: {conversation.metadata.total_tokens}")
print(f"Estimated cost: ${conversation.metadata.total_cost:.4f}")
```

### Check API Health

```python
async with OpenRouterClient() as client:
    if await client.health_check():
        print("✅ API is working")
    else:
        print("❌ API issues")
```

## 🏗️ Project Structure

```
oprouter/
├── main.py              # Start the CLI chat
├── oprouter/
│   ├── api_client.py    # Main API client
│   ├── conversation.py  # Conversation management
│   ├── cli.py          # Interactive interface
│   └── config.py       # Configuration
├── examples/           # Usage examples
└── requirements.txt    # Dependencies
```

## 🆘 Troubleshooting

**"API key not found"**
```bash
export OPENROUTER_API_KEY="your_key_here"
```

**"Rate limit exceeded"**
OpRouter automatically handles this - just wait a moment.

**"Connection failed"**
Check your internet connection and try again.

**Emojis not showing on Windows?**
```bash
# Disable emojis
export USE_EMOJIS=false

# Or use Windows Terminal for better emoji support
```

**Want to disable logging?**
```bash
export ENABLE_LOGGING=false
```

**Want conversations in memory only?**
```bash
export STORAGE_TYPE=memory
```

**Need help?**
Check the logs in `oprouter.log` or open an issue on GitHub.

## 📄 License

MIT License - feel free to use in your projects!

## 🙏 Credits

- [OpenRouter](https://openrouter.ai/) for the AI API
- Built with Python, aiohttp, and Rich
