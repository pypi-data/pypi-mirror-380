"""
Simple chat module without Claude Code SDK for testing
"""

from typing import Optional, List
from rich.console import Console
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pathlib import Path
import json
import os

class SimpleChat:
    """Simple chat interface without Claude Code SDK for testing"""

    def __init__(self, history_file: Optional[str] = None):
        """Initialize the simple chat"""
        self.console = Console()

        # Set up history file
        if history_file is None:
            home = Path.home()
            history_dir = home / '.navam'
            history_dir.mkdir(exist_ok=True)
            history_file = str(history_dir / 'chat_history')

        self.session = PromptSession(
            history=FileHistory(history_file),
            auto_suggest=AutoSuggestFromHistory()
        )

    def display_welcome(self):
        """Display welcome message"""
        welcome = Panel.fit(
            "[bold cyan]Navam Simple Chat[/bold cyan]\n"
            "[dim]Testing Mode - No Claude Code SDK[/dim]\n\n"
            "Commands:\n"
            "  [yellow]/help[/yellow]    - Show available commands\n"
            "  [yellow]/tools[/yellow]   - List available MCP tools\n"
            "  [yellow]/clear[/yellow]   - Clear the screen\n"
            "  [yellow]/exit[/yellow]    - Exit the chat\n\n"
            "Type your question to test the interface!",
            title="Welcome",
            border_style="bright_blue"
        )
        self.console.print(welcome)

    def handle_command(self, command: str) -> bool:
        """Handle special commands"""
        command = command.strip().lower()

        if command in ['/exit', '/quit', '/q']:
            self.console.print("[yellow]Goodbye![/yellow]")
            return False

        elif command == '/help':
            help_text = """
[bold]Available Commands:[/bold]
  /help     - Show this help message
  /tools    - List MCP tools (simulated)
  /clear    - Clear the screen
  /exit     - Exit the chat

[bold]This is a simple test interface.[/bold]
The full Navam chat will integrate with Claude Code SDK.
            """
            self.console.print(Panel(help_text, title="Help", border_style="green"))

        elif command == '/tools':
            tools_text = """
[bold]MCP Tools (Simulated):[/bold]
  • mcp__stock-analyzer__analyze_stock
  • mcp__company-research__get_company_profile
  • mcp__news-analyzer__get_company_news

[dim]Full tool integration available with Claude Code SDK[/dim]
            """
            self.console.print(Panel(tools_text, title="Tools", border_style="cyan"))

        elif command == '/clear':
            self.console.clear()
            self.display_welcome()

        else:
            self.console.print(f"[red]Unknown command: {command}[/red]")

        return True

    def process_query(self, prompt: str):
        """Process a query (simulated)"""
        self.console.print(f"\n[bold cyan]You:[/bold cyan] {prompt}")

        # Simulate response based on keywords
        response = ""
        if any(word in prompt.lower() for word in ['stock', 'aapl', 'analyze']):
            response = """
**Stock Analysis Simulation**

This is a simulated response. The full Navam system would:
1. Use Claude Code SDK to process your query
2. Access MCP tools for real stock data
3. Provide comprehensive analysis with current data

To test with real functionality, ensure Claude Code SDK is properly configured.
            """
        elif 'hello' in prompt.lower() or 'hi' in prompt.lower():
            response = "Hello! I'm Navam. In full mode, I'd help you with stock analysis using live data."
        else:
            response = f"You asked: '{prompt}'\n\nThis is a test response. The full system would use Claude Code SDK to provide intelligent analysis."

        self.console.print(Panel(
            response,
            title="[bold green]Navam (Test Mode)[/bold green]",
            border_style="green",
            padding=(1, 2)
        ))

    def run(self):
        """Run the simple chat loop"""
        self.display_welcome()

        while True:
            try:
                # Get user input
                user_input = self.session.prompt("\n[Navam-Test] > ")

                if not user_input.strip():
                    continue

                # Handle commands
                if user_input.startswith('/'):
                    should_continue = self.handle_command(user_input)
                    if not should_continue:
                        break
                else:
                    # Process regular query
                    self.process_query(user_input)

            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use /exit to quit[/yellow]")
            except EOFError:
                break
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/red]")


def main():
    """Main entry point for simple chat"""
    chat = SimpleChat()
    chat.run()

if __name__ == "__main__":
    main()