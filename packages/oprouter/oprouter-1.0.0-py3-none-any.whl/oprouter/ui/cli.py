"""Interactive CLI interface for OpRouter."""

import asyncio
import sys
from typing import Optional, List
from datetime import datetime

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich.syntax import Syntax

from ..services.api_client import OpenRouterClient, APIResponse
from ..storage.conversation import Conversation, ConversationManager, MessageRole
from ..core.config import get_config, ensure_directories
from ..core.logger import logger
from .emoji_utils import emoji


class OpRouterCLI:
    """Interactive CLI for OpRouter."""
    
    def __init__(self):
        self.console = Console()
        self.config = get_config()
        self.conversation_manager = ConversationManager()
        self.client: Optional[OpenRouterClient] = None
        self.running = True
        
        # Ensure directories exist
        ensure_directories()
    
    async def initialize(self):
        """Initialize the CLI."""
        self.client = OpenRouterClient()
        
        # Health check
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task("Checking API connection...", total=None)
            
            if not await self.client.health_check():
                self.console.print(f"[red]{emoji.get('error')} Failed to connect to OpenRouter API[/red]")
                self.console.print("[yellow]Please check your API key and internet connection[/yellow]")
                return False

            progress.update(task, description=f"{emoji.get('success')} Connected to OpenRouter API")
        
        return True
    
    def show_welcome(self):
        """Show welcome message."""
        welcome_text = f"""
# {emoji.get('robot')} OpRouter - Advanced AI Chat Client

Welcome to OpRouter, your advanced AI chat interface with robust retry logic and conversation management.

**Features:**
- {emoji.get('retry')} Intelligent retry with exponential backoff
- {emoji.get('chat')} Conversation persistence and management
- {emoji.get('target')} Rate limiting and concurrent request control
- {emoji.get('stats')} Token usage and cost tracking
- {emoji.get('art')} Rich formatting and syntax highlighting

Type `/help` for available commands or start chatting!
        """
        
        self.console.print(Panel(
            Markdown(welcome_text),
            title="OpRouter",
            border_style="blue"
        ))
    
    def show_help(self):
        """Show help information."""
        help_table = Table(title="Available Commands")
        help_table.add_column("Command", style="cyan", no_wrap=True)
        help_table.add_column("Description", style="white")
        
        commands = [
            ("/help", "Show this help message"),
            ("/new", "Start a new conversation"),
            ("/list", "List all conversations"),
            ("/load <id>", "Load a conversation by ID"),
            ("/save", "Save current conversation"),
            ("/export", "Export conversation to text"),
            ("/clear", "Clear current conversation"),
            ("/title <title>", "Set conversation title"),
            ("/model <model>", "Change AI model"),
            ("/models", "List available models"),
            ("/stats", "Show conversation statistics"),
            ("/quit", "Exit the application"),
        ]
        
        for cmd, desc in commands:
            help_table.add_row(cmd, desc)
        
        self.console.print(help_table)
    
    def show_conversation_stats(self):
        """Show current conversation statistics."""
        if not self.conversation_manager.current_conversation:
            self.console.print("[yellow]No active conversation[/yellow]")
            return
        
        conv = self.conversation_manager.current_conversation
        
        stats_table = Table(title=f"Conversation Statistics: {conv.title}")
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="white")
        
        stats = [
            ("ID", conv.id),
            ("Model", conv.model),
            ("Messages", str(conv.metadata.message_count)),
            ("Total Tokens", str(conv.metadata.total_tokens)),
            ("Total Cost", f"${conv.metadata.total_cost:.4f}"),
            ("Created", conv.metadata.created_at.strftime("%Y-%m-%d %H:%M:%S")),
            ("Updated", conv.metadata.updated_at.strftime("%Y-%m-%d %H:%M:%S")),
        ]
        
        for metric, value in stats:
            stats_table.add_row(metric, value)
        
        self.console.print(stats_table)
    
    def list_conversations(self):
        """List all conversations."""
        conversations = self.conversation_manager.list_conversations()
        
        if not conversations:
            self.console.print("[yellow]No saved conversations found[/yellow]")
            return
        
        table = Table(title="Saved Conversations")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="white")
        table.add_column("Model", style="green")
        table.add_column("Messages", style="blue")
        table.add_column("Updated", style="magenta")
        
        for conv in conversations[:20]:  # Show last 20
            table.add_row(
                conv.id[:8] + "...",
                conv.title,
                conv.model,
                str(conv.message_count),
                conv.updated_at.strftime("%m-%d %H:%M")
            )
        
        self.console.print(table)
    
    async def list_models(self):
        """List available models."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task("Fetching models...", total=None)
            
            response = await self.client.get_models()
            
            if not response.success:
                self.console.print(f"[red]Failed to fetch models: {response.error}[/red]")
                return
            
            models = response.data.get('data', [])
            
            table = Table(title="Available Models")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="white")
            table.add_column("Context", style="blue")
            table.add_column("Pricing", style="green")
            
            for model in models[:20]:  # Show first 20
                table.add_row(
                    model.get('id', 'N/A'),
                    model.get('name', 'N/A'),
                    str(model.get('context_length', 'N/A')),
                    f"${model.get('pricing', {}).get('prompt', 'N/A')}"
                )
            
            self.console.print(table)
    
    def format_message(self, role: MessageRole, content: str, timestamp: Optional[datetime] = None) -> Panel:
        """Format a message for display."""
        if timestamp:
            time_str = timestamp.strftime("%H:%M:%S")
        else:
            time_str = datetime.now().strftime("%H:%M:%S")
        
        if role == MessageRole.USER:
            title = f"{emoji.get('user')} You ({time_str})"
            border_style = "blue"
        else:
            title = f"{emoji.get('robot')} Assistant ({time_str})"
            border_style = "green"
        
        # Try to render as markdown if it looks like markdown
        if any(marker in content for marker in ['```', '**', '*', '#', '`']):
            try:
                formatted_content = Markdown(content)
            except:
                formatted_content = content
        else:
            formatted_content = content
        
        return Panel(
            formatted_content,
            title=title,
            border_style=border_style,
            padding=(0, 1)
        )
    
    async def send_message(self, content: str) -> bool:
        """Send a message and get response."""
        if not self.conversation_manager.current_conversation:
            self.conversation_manager.create_conversation()
        
        conv = self.conversation_manager.current_conversation
        
        # Add user message
        conv.add_message(MessageRole.USER, content)
        
        # Display user message
        self.console.print(self.format_message(MessageRole.USER, content))
        
        # Get messages for API
        messages = conv.get_context_window(max_tokens=4000)
        
        # Send request with progress indicator
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task("Thinking...", total=None)
            
            try:
                response = await self.client.chat_completion(messages, model=conv.model)
                
                if not response.success:
                    self.console.print(f"[red]Error: {response.error}[/red]")
                    return False
                
                # Extract response
                assistant_content = response.data['choices'][0]['message']['content']
                usage = response.usage or {}
                
                # Add assistant message
                conv.add_message(
                    MessageRole.ASSISTANT, 
                    assistant_content,
                    tokens=usage.get('total_tokens'),
                    cost=self._calculate_cost(usage)
                )
                
                # Display assistant message
                self.console.print(self.format_message(MessageRole.ASSISTANT, assistant_content))
                
                # Show token usage
                if usage.get('total_tokens'):
                    self.console.print(f"[dim]Tokens used: {usage['total_tokens']}[/dim]")
                
                return True
                
            except Exception as e:
                self.console.print(f"[red]Unexpected error: {e}[/red]")
                logger.error(f"Send message error: {e}")
                return False
    
    def _calculate_cost(self, usage: dict) -> float:
        """Calculate approximate cost (placeholder implementation)."""
        # This is a simplified cost calculation
        # In reality, you'd need to use the actual pricing from the model
        prompt_tokens = usage.get('prompt_tokens', 0)
        completion_tokens = usage.get('completion_tokens', 0)
        
        # Approximate pricing (adjust based on actual model pricing)
        prompt_cost = prompt_tokens * 0.000001  # $1 per 1M tokens
        completion_cost = completion_tokens * 0.000002  # $2 per 1M tokens
        
        return prompt_cost + completion_cost

    async def handle_command(self, command: str) -> bool:
        """Handle CLI commands."""
        parts = command.strip().split()
        cmd = parts[0].lower()

        if cmd == "/help":
            self.show_help()

        elif cmd == "/new":
            title = " ".join(parts[1:]) if len(parts) > 1 else None
            self.conversation_manager.create_conversation(title=title)
            self.console.print(f"[green]{emoji.get('success')} Started new conversation[/green]")

        elif cmd == "/list":
            self.list_conversations()

        elif cmd == "/load":
            if len(parts) < 2:
                self.console.print("[red]Usage: /load <conversation_id>[/red]")
                return True

            conv_id = parts[1]
            # Try to find conversation by partial ID
            conversations = self.conversation_manager.list_conversations()
            matching = [c for c in conversations if c.id.startswith(conv_id)]

            if not matching:
                self.console.print(f"[red]Conversation not found: {conv_id}[/red]")
                return True

            if len(matching) > 1:
                self.console.print(f"[yellow]Multiple matches found. Please be more specific.[/yellow]")
                for conv in matching[:5]:
                    self.console.print(f"  {conv.id[:12]}... - {conv.title}")
                return True

            conv = self.conversation_manager.load_conversation(matching[0].id)
            if conv:
                self.console.print(f"[green]{emoji.get('success')} Loaded conversation: {conv.title}[/green]")
                # Show recent messages
                for msg in conv.messages[-3:]:
                    self.console.print(self.format_message(msg.role, msg.content, msg.timestamp))
            else:
                self.console.print(f"[red]Failed to load conversation[/red]")

        elif cmd == "/save":
            if not self.conversation_manager.current_conversation:
                self.console.print("[yellow]No active conversation to save[/yellow]")
                return True

            if self.conversation_manager.current_conversation.save():
                self.console.print(f"[green]{emoji.get('success')} Conversation saved[/green]")
            else:
                self.console.print("[red]Failed to save conversation[/red]")

        elif cmd == "/export":
            if not self.conversation_manager.current_conversation:
                self.console.print("[yellow]No active conversation to export[/yellow]")
                return True

            conv = self.conversation_manager.current_conversation
            filename = f"conversation_{conv.id[:8]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(conv.export_to_text())
                self.console.print(f"[green]{emoji.get('success')} Exported to {filename}[/green]")
            except Exception as e:
                self.console.print(f"[red]Export failed: {e}[/red]")

        elif cmd == "/clear":
            if not self.conversation_manager.current_conversation:
                self.console.print("[yellow]No active conversation to clear[/yellow]")
                return True

            if Confirm.ask("Are you sure you want to clear the conversation?"):
                self.conversation_manager.current_conversation.clear()
                self.console.print(f"[green]{emoji.get('success')} Conversation cleared[/green]")

        elif cmd == "/title":
            if not self.conversation_manager.current_conversation:
                self.console.print("[yellow]No active conversation[/yellow]")
                return True

            if len(parts) < 2:
                self.console.print("[red]Usage: /title <new_title>[/red]")
                return True

            title = " ".join(parts[1:])
            self.conversation_manager.current_conversation.set_title(title)
            self.console.print(f"[green]{emoji.get('success')} Title updated to: {title}[/green]")

        elif cmd == "/model":
            if len(parts) < 2:
                self.console.print("[red]Usage: /model <model_name>[/red]")
                return True

            model = parts[1]
            if self.conversation_manager.current_conversation:
                self.conversation_manager.current_conversation.model = model
                self.console.print(f"[green]{emoji.get('success')} Model changed to: {model}[/green]")
            else:
                self.client.model = model
                self.console.print(f"[green]{emoji.get('success')} Default model changed to: {model}[/green]")

        elif cmd == "/models":
            await self.list_models()

        elif cmd == "/stats":
            self.show_conversation_stats()

        elif cmd == "/quit" or cmd == "/exit":
            self.running = False
            return False

        else:
            self.console.print(f"[red]Unknown command: {cmd}[/red]")
            self.console.print("Type [cyan]/help[/cyan] for available commands")

        return True

    async def run(self):
        """Main CLI loop."""
        self.show_welcome()

        if not await self.initialize():
            return

        # Create initial conversation
        self.conversation_manager.create_conversation()

        self.console.print("\n[dim]Type your message or use /help for commands[/dim]")

        while self.running:
            try:
                # Get user input
                user_input = Prompt.ask("\n[bold blue]You[/bold blue]", console=self.console)

                if not user_input.strip():
                    continue

                # Handle commands
                if user_input.startswith('/'):
                    if not await self.handle_command(user_input):
                        break
                    continue

                # Send message
                await self.send_message(user_input)

            except KeyboardInterrupt:
                if Confirm.ask("\nAre you sure you want to quit?"):
                    break
                else:
                    self.console.print("Continuing...")
            except EOFError:
                break
            except Exception as e:
                self.console.print(f"[red]Unexpected error: {e}[/red]")
                logger.error(f"CLI error: {e}")

        # Cleanup
        if self.client:
            await self.client.close()

        self.console.print(f"\n[blue]{emoji.get('goodbye')} Goodbye![/blue]")


@click.command()
@click.option('--api-key', help='OpenRouter API key')
@click.option('--model', help='AI model to use')
@click.option('--conversation', help='Load specific conversation ID')
def main(api_key: Optional[str], model: Optional[str], conversation: Optional[str]):
    """OpRouter - Advanced AI Chat Client with robust retry logic."""

    try:
        cli = OpRouterCLI()

        # Override configuration if provided
        if api_key:
            cli.config.openrouter_api_key = api_key
        if model:
            cli.config.default_model = model

        # Load specific conversation if requested
        if conversation:
            conv = cli.conversation_manager.load_conversation(conversation)
            if not conv:
                click.echo(f"Error: Conversation {conversation} not found")
                return

        # Run the CLI
        asyncio.run(cli.run())

    except KeyboardInterrupt:
        click.echo("\nGoodbye!")
    except Exception as e:
        click.echo(f"Error: {e}")
        logger.error(f"Main error: {e}")


if __name__ == "__main__":
    main()
