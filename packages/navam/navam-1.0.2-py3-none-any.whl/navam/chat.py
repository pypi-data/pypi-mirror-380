"""
Interactive chat module using Claude Code SDK
"""

import anyio
from typing import Optional, Dict, List, Any
from claude_code_sdk import (
    ClaudeSDKClient, ClaudeCodeOptions,
    AssistantMessage, SystemMessage, ResultMessage,
    TextBlock, ThinkingBlock, ToolUseBlock, ToolResultBlock
)
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from pathlib import Path
import os
import json
from datetime import datetime
from dotenv import load_dotenv

class NotificationManager:
    """Manages persistent notification history for the chat interface"""

    def __init__(self, console: Console):
        self.console = console
        self.notification_count = 0

    def show_notification(self, content: str, title: str, border_style: str = "white", timestamp: bool = True):
        """Show a persistent notification that remains in the scrollable history"""
        self.notification_count += 1

        # Add timestamp to title if requested
        if timestamp:
            current_time = datetime.now().strftime("%H:%M:%S")
            title_with_time = f"{title} [{current_time}]"
        else:
            title_with_time = title

        # Print the notification panel
        panel = Panel(
            content,
            title=title_with_time,
            border_style=border_style,
            padding=(1, 2)
        )
        self.console.print(panel)

    def show_status(self, content: str, timestamp: bool = True):
        """Show a status notification"""
        self.show_notification(content, "[bold yellow]StockAI Status[/bold yellow]", "yellow", timestamp)

    def show_thinking(self, content: str, timestamp: bool = True):
        """Show a thinking notification"""
        self.show_notification(content, "[bold blue]Claude Thinking[/bold blue]", "blue", timestamp)

    def show_tool_execution(self, content: str, timestamp: bool = True):
        """Show a tool execution notification"""
        self.show_notification(content, "[bold cyan]Tool Execution[/bold cyan]", "cyan", timestamp)

    def show_agent_execution(self, content: str, timestamp: bool = True):
        """Show an agent execution notification"""
        self.show_notification(content, "[bold magenta]Agent Execution[/bold magenta]", "magenta", timestamp)

    def show_multi_agent_execution(self, content: str, timestamp: bool = True):
        """Show a multi-agent execution notification"""
        self.show_notification(content, "[bold magenta]Multi-Agent Parallel Execution[/bold magenta]", "magenta", timestamp)

    def show_completion(self, content: str, success: bool = True, timestamp: bool = True):
        """Show a completion notification"""
        if success:
            self.show_notification(content, "[bold green]Completed[/bold green]", "green", timestamp)
        else:
            self.show_notification(content, "[bold red]Failed[/bold red]", "red", timestamp)

    def show_response(self, content: str, timestamp: bool = True):
        """Show a response notification"""
        self.show_notification(content, "[bold green]Claude Response[/bold green]", "green", timestamp)

    def show_session_complete(self, content: str, timestamp: bool = True):
        """Show a session completion notification"""
        self.show_notification(content, "[bold green]Session Complete[/bold green]", "green", timestamp)

class InteractiveChat:
    """Interactive chat interface for StockAI with Claude Code SDK integration"""

    def __init__(self,
                 history_file: Optional[str] = None,
                 mcp_servers: Optional[List[str]] = None,
                 allowed_tools: Optional[List[str]] = None,
                 permission_mode: str = "acceptEdits",
                 interactive_permissions: bool = True):
        """
        Initialize the interactive chat

        Args:
            history_file: Path to command history file
            mcp_servers: List of MCP server configurations to load
            allowed_tools: List of allowed tools for Claude to use
            permission_mode: Permission mode ('default', 'acceptEdits', 'bypassPermissions')
            interactive_permissions: Enable interactive permission prompts for tool usage
        """
        self.console = Console()
        self.notifications = NotificationManager(self.console)
        self.permission_mode = permission_mode
        self.interactive_permissions = interactive_permissions

        # Load environment variables from .env file
        load_dotenv()

        # Set up history file and permissions storage
        if history_file is None:
            home = Path.home()
            self.navam_dir = home / '.navam'
            self.navam_dir.mkdir(exist_ok=True)
            history_file = str(self.navam_dir / 'chat_history')
        else:
            self.navam_dir = Path.home() / '.navam'
            self.navam_dir.mkdir(exist_ok=True)

        # Initialize permissions storage
        self.permissions_file = self.navam_dir / 'permissions.json'
        self.default_permissions = self._load_default_permissions()

        self.session = PromptSession(
            history=FileHistory(history_file),
            auto_suggest=AutoSuggestFromHistory()
        )

        # Load MCP servers configuration
        self.mcp_servers = self._load_mcp_servers(mcp_servers)

        # Configure authentication and environment
        auth_info = self._configure_authentication()
        self.auth_method = auth_info['method']
        self.auth_source = auth_info['source']

        # Configure Claude Code options
        # For Pro/Max plans, don't set API key - let Claude Code SDK use authenticated session
        self.claude_options = ClaudeCodeOptions(
            allowed_tools=allowed_tools or self._get_default_tools(),
            permission_mode=self.permission_mode,
            system_prompt=self._get_system_prompt(),
            can_use_tool=self._handle_tool_permission if self.interactive_permissions else None
            # Note: No model or env specified - use Pro/Max plan defaults
        )

        # Initialize ClaudeSDKClient for conversation continuity
        self.client = ClaudeSDKClient(options=self.claude_options)
        self.client_connected = False
        self.turn_count = 0

        # Load investment commands from local filesystem immediately
        self.investment_commands = self._load_investment_commands()
        self.available_slash_commands = []  # System commands from Claude Code SDK

    async def _load_investment_command_prompt(self, command: str) -> Optional[str]:
        """Load the prompt content for an investment command"""
        # Extract command name (e.g., /invest:research-stock -> research-stock)
        command_parts = command.split(':')
        if len(command_parts) < 2:
            return None

        command_name = command_parts[1].split()[0]  # Get just the command name, ignore args
        command_args = ' '.join(command_parts[1].split()[1:]) if len(command_parts[1].split()) > 1 else ''

        # Try multiple locations in order of preference
        possible_locations = [
            Path(".claude/commands/invest") / f"{command_name}.md",  # Local development
            Path(__file__).parent / "commands" / "invest" / f"{command_name}.md",  # Package location
            Path.home() / ".navam" / "commands" / "invest" / f"{command_name}.md",  # User config
        ]

        for command_file in possible_locations:
            if command_file.exists():
                try:
                    prompt_content = command_file.read_text()
                    # If command has arguments, append them to the prompt
                    if command_args:
                        prompt_content = f"{prompt_content}\n\nUser specified: {command_args}"
                    return prompt_content
                except Exception as e:
                    self.console.print(f"[red]Error loading command {command_name}: {e}[/red]")
                    return None

        return None

    def _load_investment_commands(self) -> List[str]:
        """Load investment slash commands from .claude/commands/invest/ folder or package"""
        investment_commands = []

        # Try multiple locations in order of preference
        possible_locations = [
            Path(".claude/commands/invest"),  # Local development
            Path(__file__).parent / "commands" / "invest",  # Package location
            Path.home() / ".navam" / "commands" / "invest",  # User config
        ]

        for invest_folder in possible_locations:
            if invest_folder.exists():
                for md_file in invest_folder.glob("*.md"):
                    if md_file.name != "README.md":  # Skip README
                        # Convert filename to slash command format
                        command_name = f"invest:{md_file.stem}"
                        if command_name not in investment_commands:
                            investment_commands.append(command_name)

        return sorted(investment_commands)

    def _load_mcp_servers(self, server_names: Optional[List[str]] = None) -> Dict[str, Any]:
        """Load MCP server configurations from project"""
        servers = {}

        # Try to load from .mcp.json files
        mcp_files = ['.mcp.json', '.mcp-company.json']
        for mcp_file in mcp_files:
            if os.path.exists(mcp_file):
                with open(mcp_file, 'r') as f:
                    config = json.load(f)
                    if 'mcpServers' in config:
                        servers.update(config['mcpServers'])

        # Filter by server names if provided
        if server_names:
            servers = {k: v for k, v in servers.items() if k in server_names}

        return servers

    def _configure_authentication(self) -> Dict[str, Any]:
        """
        Configure authentication for Claude Code SDK

        Returns:
            Dictionary with authentication info including method, source, and env vars
        """
        # For Pro/Max plans, we NEVER set ANTHROPIC_API_KEY to avoid API charges
        # Claude Code SDK automatically uses the authenticated Pro/Max session

        auth_method = "Pro/Max Plan"
        auth_source = "Claude authenticated session"

        # Important: Do not set any API key environment variables
        # This ensures usage counts against Pro/Max plan allocation, not API billing

        return {
            'method': auth_method,
            'source': auth_source,
            'env_vars': {}  # Empty - no API key needed for Pro/Max
        }

    def _check_claude_desktop_auth(self) -> bool:
        """Check if Claude Desktop authentication is available"""
        # Look for Claude Desktop configuration or session files
        claude_config_path = Path.home() / "Library/Application Support/Claude"
        return claude_config_path.exists()

    def _check_system_claude_auth(self) -> bool:
        """Check if system-wide Claude authentication is available"""
        # Look for Claude CLI authentication
        claude_dir = Path.home() / ".claude"
        return claude_dir.exists()

    def _get_default_tools(self) -> List[str]:
        """Get default list of allowed tools"""
        return [
            "mcp__stock-analyzer__analyze_stock",
            "mcp__stock-analyzer__compare_stocks",
            "mcp__stock-analyzer__screen_stocks",
            "mcp__stock-analyzer__calculate_portfolio_value",
            "mcp__stock-analyzer__get_moving_averages",
            "mcp__stock-analyzer__find_trending_stocks",
            "mcp__company-research__get_company_profile",
            "mcp__company-research__get_company_financials",
            "mcp__company-research__get_company_filings",
            "mcp__company-research__get_insider_trading",
            "mcp__company-research__get_analyst_ratings",
            "mcp__company-research__compare_companies",
            "mcp__company-research__search_companies",
            "mcp__news-analyzer__search_news",
            "mcp__news-analyzer__get_trending_topics",
            "mcp__news-analyzer__analyze_sentiment",
            "mcp__news-analyzer__get_market_overview",
            "mcp__news-analyzer__summarize_news",
            "mcp__news-analyzer__get_company_news",
        ]

    def _get_system_prompt(self) -> str:
        """Get system prompt for Claude"""
        return """You are StockAI, an intelligent financial assistant with access to comprehensive stock market data and analysis tools.

        You have access to MCP tools for:
        - Stock analysis and comparisons
        - Company research and financials
        - Market news and sentiment analysis
        - Portfolio calculations
        - Technical indicators

        Provide accurate, data-driven insights while being helpful and conversational.
        When analyzing stocks or companies, use the available tools to fetch real-time data.
        Always cite the data sources and be transparent about any limitations."""

    def display_welcome(self):
        """Display welcome message"""
        welcome = Panel.fit(
            "[bold cyan]StockAI Enhanced Interactive Chat[/bold cyan]\n"
            "[dim]Powered by ClaudeSDKClient with Advanced Notifications[/dim]\n\n"
            "✨ [bold]New Features:[/bold]\n"
            "  🧠 Real-time thinking tokens display\n"
            "  🔧 Live MCP tool execution tracking\n"
            "  🤖 Agent usage progress indication\n"
            "  ⚡ Multi-agent parallel execution tracking\n"
            "  🔐 Interactive permission system with persistent settings\n"
            "  📜 Scrollable notification history with timestamps\n"
            "  📊 Session metrics and turn counting\n"
            "  💭 Conversation memory (Claude remembers context)\n"
            "  ⚡ Custom slash commands for investment workflows\n\n"
            "Commands:\n"
            "  [yellow]/help[/yellow]       - Show available commands\n"
            "  [yellow]/status[/yellow]     - Show conversation status\n"
            "  [yellow]/commands[/yellow]   - List all slash commands (built-in + investment)\n"
            "  [yellow]/new[/yellow]        - Start new conversation\n"
            "  [yellow]/tools[/yellow]      - List available MCP tools\n"
            "  [yellow]/servers[/yellow]    - Show loaded MCP servers\n"
            "  [yellow]/clear[/yellow]      - Clear the screen\n"
            "  [yellow]/exit[/yellow]       - Exit the chat\n\n"
            f"Type your question or use /{self.investment_commands[0] if self.investment_commands else 'invest:research-stock'} to start!",
            title="Welcome",
            border_style="bright_blue"
        )
        self.console.print(welcome)

    async def handle_command(self, command: str) -> bool:
        """
        Handle special commands

        Returns:
            True if should continue, False if should exit
        """
        command = command.strip().lower()

        if command in ['/exit', '/quit', '/q']:
            self.console.print("[yellow]Goodbye![/yellow]")
            return False

        elif command == '/help':
            help_text = f"""
[bold]Available Commands:[/bold]
  /help     - Show this help message
  /commands - List all slash commands (built-in + investment workflows)
  /tools    - List available MCP tools
  /servers  - Show loaded MCP servers
  /status   - Show conversation status and metrics
  /new      - Start a new conversation (clear context)
  /clear    - Clear the screen
  /exit     - Exit the chat

[bold]Investment Workflow Commands:[/bold]
  Use /commands to see available investment workflows
  Examples: /invest:research-stock, /invest:review-portfolio, /invest:plan-goals

[bold]Conversation Features:[/bold]
  • Context memory: Claude remembers previous messages
  • Turn tracking: Each exchange is numbered
  • Tool notifications: See real-time MCP tool usage
  • Thinking tokens: View Claude's reasoning process
  • Custom slash commands for investment workflows
  • Auto-approved file operations (Write, Edit, MultiEdit) for seamless analysis

[bold]Stock Analysis Examples:[/bold]
  "Analyze AAPL stock"
  "Compare MSFT and GOOGL"
  "Find trending tech stocks"
  "Get news sentiment for Tesla"
  "Show my portfolio value"
            """
            self.console.print(Panel(help_text, title="Help", border_style="green"))

        elif command == '/commands':
            # Show all available slash commands
            commands_text = "[bold]Built-in Chat Commands:[/bold]\n"
            built_in_commands = [
                "/help - Show help message",
                "/commands - List all slash commands",
                "/status - Show conversation status",
                "/new - Start new conversation",
                "/tools - List MCP tools",
                "/servers - Show MCP servers",
                "/clear - Clear screen",
                "/exit - Exit chat"
            ]
            commands_text += "\n".join([f"  • {cmd}" for cmd in built_in_commands])

            # Always show investment commands (loaded from filesystem)
            if self.investment_commands:
                commands_text += "\n\n[bold]Investment Workflow Commands:[/bold]\n"
                commands_text += "\n".join([f"  ⚡ /{cmd}" for cmd in self.investment_commands])
                commands_text += "\n\n[dim]💡 Investment commands run comprehensive multi-agent workflows[/dim]"
            else:
                commands_text += "\n\n[yellow]⚠️ No investment commands found in .claude/commands/invest/[/yellow]"

            self.console.print(Panel(commands_text, title="All Commands", border_style="cyan"))

        elif command == '/status':
            status_info = f"""
[bold]Conversation Status:[/bold]
  • Turns completed: {self.turn_count}
  • Client connected: {'Yes' if self.client_connected else 'No'}
  • Authentication: {self.auth_method} ({self.auth_source})
  • Context memory: Active (Claude remembers this conversation)

[bold]Features Active:[/bold]
  • Real-time tool notifications
  • Thinking token display
  • Session metrics tracking
  • Progressive status updates
            """
            self.console.print(Panel(status_info, title="Status", border_style="blue"))

        elif command == '/new':
            # Start new conversation by disconnecting and reconnecting
            if self.client_connected:
                await self.disconnect_client()

            previous_turns = self.turn_count
            self.turn_count = 0

            self.console.print(Panel(
                f"🔄 Started new conversation\n"
                f"Previous conversation: {previous_turns} turns\n"
                f"Claude's context has been cleared",
                title="[bold cyan]New Conversation[/bold cyan]",
                border_style="cyan",
                padding=(1, 2)
            ))

        elif command == '/tools':
            tools_list = "\n".join([f"  • {tool}" for tool in self.claude_options.allowed_tools])
            self.console.print(Panel(f"[bold]Available MCP Tools:[/bold]\n{tools_list}",
                                    title="Tools", border_style="cyan"))

        elif command == '/servers':
            if self.mcp_servers:
                servers_list = "\n".join([f"  • {name}" for name in self.mcp_servers.keys()])
                self.console.print(Panel(f"[bold]Loaded MCP Servers:[/bold]\n{servers_list}",
                                        title="Servers", border_style="cyan"))
            else:
                self.console.print("[yellow]No MCP servers loaded[/yellow]")

        elif command == '/clear':
            self.console.clear()
            self.display_welcome()

        else:
            self.console.print(f"[red]Unknown command: {command}[/red]")

        return True

    async def ensure_client_connected(self):
        """Ensure the Claude SDK client is connected"""
        if not self.client_connected:
            await self.client.connect()
            self.client_connected = True

    async def disconnect_client(self):
        """Disconnect the Claude SDK client"""
        if self.client_connected:
            await self.client.disconnect()
            self.client_connected = False

    async def process_query(self, prompt: str):
        """Process a query using ClaudeSDKClient with enhanced notifications"""
        self.console.print(f"\n[bold cyan]You (Turn {self.turn_count + 1}):[/bold cyan] {prompt}")

        # Ensure client is connected
        await self.ensure_client_connected()

        # Initialize tracking variables
        response_text = ""
        system_initialized = False
        tools_in_use = set()
        agents_in_use = {}  # Dict: agent_type -> {"status": "running"|"completed"|"failed", "task": description, "tool_use_id": id}
        thinking_content = ""
        session_metrics = {}

        # Show initial status notification
        self.notifications.show_status(f"🔄 Connecting to Claude (Turn {self.turn_count + 1})...")

        try:
            # Send query to Claude SDK Client
            await self.client.query(prompt)
            self.turn_count += 1

            # Process all messages in the response
            async for message in self.client.receive_messages():

                    # Handle SystemMessage (initialization/status)
                    if isinstance(message, SystemMessage):
                        if message.subtype == 'init':
                            system_initialized = True
                            data = message.data

                            # Extract session info
                            model_name = data.get('model', 'unknown')
                            connected_servers = []
                            tools_available = []

                            if 'mcp_servers' in data:
                                mcp_servers_status = data['mcp_servers']
                                connected_servers = [s['name'] for s in mcp_servers_status if s['status'] == 'connected']

                            if 'tools' in data:
                                tools_available = [t for t in data['tools'] if t.startswith('mcp__')]

                            # Note: We load investment commands from filesystem, not from system


                            # Show comprehensive status
                            status_lines = [
                                f"✅ Claude SDK Client connected (Turn {self.turn_count})",
                                f"🤖 Model: {model_name}",
                                f"🔐 Auth: {self.auth_method} ({self.auth_source})",
                                f"🔗 MCP Servers: {len(connected_servers)} connected ({', '.join(connected_servers)})",
                                f"🛠️  Financial Tools: {len(tools_available)} available",
                            ]

                            if self.investment_commands:
                                status_lines.append(f"⚡ Investment Commands: {len(self.investment_commands)} workflows available")

                            status_lines.append("💭 Processing your request...")

                            self.notifications.show_status("\n".join(status_lines))

                    # Handle AssistantMessage with different content blocks
                    elif isinstance(message, AssistantMessage):
                        for block in message.content:

                            # Handle text content
                            if isinstance(block, TextBlock):
                                response_text += block.text
                                content = Markdown(response_text) if response_text.strip() else "⏳ Generating response..."
                                self.notifications.show_response(content)

                            # Handle thinking tokens (if available)
                            elif isinstance(block, ThinkingBlock):
                                thinking_content = block.thinking
                                thinking_preview = thinking_content[:100] + "..." if len(thinking_content) > 100 else thinking_content

                                status_lines = [
                                    f"🧠 Thinking: {thinking_preview}",
                                    f"📝 Thinking tokens: {len(thinking_content.split())} words"
                                ]
                                if tools_in_use:
                                    status_lines.append(f"🔧 Tools active: {', '.join(tools_in_use)}")

                                self.notifications.show_thinking("\n".join(status_lines))

                            # Handle tool usage
                            elif isinstance(block, ToolUseBlock):
                                tool_name = block.name
                                tools_in_use.add(tool_name)

                                # Show tool usage details
                                tool_input = block.input
                                tool_description = self._get_tool_description(tool_name)

                                # Special handling for Task tool (agent execution)
                                if tool_name == "Task":
                                    agent_type = tool_input.get('subagent_type', 'unknown')
                                    task_description = tool_input.get('description', 'Unknown task')
                                    agent_description = self._get_agent_description(agent_type)

                                    # Track agent usage with detailed state
                                    agents_in_use[agent_type] = {
                                        "status": "running",
                                        "task": task_description,
                                        "tool_use_id": block.id,
                                        "description": agent_description
                                    }

                                    # Check if multiple agents are running in parallel
                                    running_agents = [agent for agent, info in agents_in_use.items()
                                                    if info["status"] == "running"]

                                    if len(running_agents) > 1:
                                        # Multi-agent parallel execution
                                        status_lines = [
                                            f"🤖 Multi-Agent Execution ({len(running_agents)} agents)",
                                            f"⚡ Latest: {agent_type} - {agent_description}",
                                            f"🎯 Task: {task_description}",
                                            "",
                                            "🔄 Active Agents:"
                                        ]
                                        for agent in running_agents:
                                            agent_info = agents_in_use[agent]
                                            status_lines.append(f"  • {agent}: {agent_info['task'][:40]}...")

                                        self.notifications.show_multi_agent_execution("\n".join(status_lines))
                                    else:
                                        # Single agent execution
                                        status_lines = [
                                            f"🤖 Launching Agent: {agent_type}",
                                            f"📋 Agent Role: {agent_description}",
                                            f"🎯 Task: {task_description}",
                                        ]

                                        self.notifications.show_agent_execution("\n".join(status_lines))
                                else:
                                    # Regular tool execution
                                    status_lines = [
                                        f"🔧 Executing: {tool_name}",
                                        f"📋 Purpose: {tool_description}",
                                    ]

                                    # Show relevant input parameters based on tool type
                                    if tool_name.startswith('mcp__'):
                                        # MCP tool parameters
                                        if 'symbol' in tool_input:
                                            status_lines.append(f"📊 Symbol: {tool_input['symbol']}")
                                        if 'query' in tool_input:
                                            status_lines.append(f"🔍 Query: {tool_input['query'][:50]}...")

                                    elif tool_name == "Write":
                                        # File writing operations
                                        if 'file_path' in tool_input:
                                            status_lines.append(f"📄 Writing to: {tool_input['file_path']}")
                                        if 'content' in tool_input:
                                            content_preview = tool_input['content'][:80].replace('\n', ' ')
                                            status_lines.append(f"✏️  Content: {content_preview}...")

                                    elif tool_name == "Edit":
                                        # File editing operations
                                        if 'file_path' in tool_input:
                                            status_lines.append(f"📝 Editing: {tool_input['file_path']}")
                                        if 'old_string' in tool_input:
                                            old_preview = tool_input['old_string'][:50].replace('\n', ' ')
                                            status_lines.append(f"🔍 Finding: {old_preview}...")

                                    elif tool_name == "Read":
                                        # File reading operations
                                        if 'file_path' in tool_input:
                                            status_lines.append(f"📖 Reading: {tool_input['file_path']}")
                                        if 'offset' in tool_input or 'limit' in tool_input:
                                            offset = tool_input.get('offset', 0)
                                            limit = tool_input.get('limit', 'all')
                                            status_lines.append(f"📏 Range: lines {offset}-{offset + limit if limit != 'all' else 'end'}")

                                    elif tool_name == "Bash":
                                        # Shell command execution
                                        if 'command' in tool_input:
                                            command = tool_input['command'][:60]
                                            status_lines.append(f"💻 Command: {command}...")
                                        if 'description' in tool_input:
                                            status_lines.append(f"📋 Action: {tool_input['description']}")

                                    elif tool_name == "TodoWrite":
                                        # Todo list management
                                        if 'todos' in tool_input:
                                            todos = tool_input['todos']
                                            if isinstance(todos, list):
                                                todo_count = len(todos)
                                                pending_count = len([t for t in todos if t.get('status') == 'pending'])
                                                completed_count = len([t for t in todos if t.get('status') == 'completed'])
                                                in_progress_count = len([t for t in todos if t.get('status') == 'in_progress'])
                                                status_lines.append(f"📝 Managing {todo_count} todos: {completed_count} done, {in_progress_count} active, {pending_count} pending")

                                    elif tool_name == "Glob":
                                        # File pattern matching
                                        if 'pattern' in tool_input:
                                            status_lines.append(f"🔍 Pattern: {tool_input['pattern']}")
                                        if 'path' in tool_input:
                                            status_lines.append(f"📂 Search in: {tool_input['path']}")

                                    elif tool_name == "Grep":
                                        # Text search in files
                                        if 'pattern' in tool_input:
                                            pattern = tool_input['pattern'][:40]
                                            status_lines.append(f"🔍 Searching: {pattern}...")
                                        if 'path' in tool_input:
                                            status_lines.append(f"📂 In: {tool_input['path']}")
                                        if 'glob' in tool_input:
                                            status_lines.append(f"📄 Files: {tool_input['glob']}")

                                    elif tool_name == "WebFetch":
                                        # Web content fetching
                                        if 'url' in tool_input:
                                            url = tool_input['url'][:50]
                                            status_lines.append(f"🌐 URL: {url}...")
                                        if 'prompt' in tool_input:
                                            prompt_preview = tool_input['prompt'][:40]
                                            status_lines.append(f"❓ Query: {prompt_preview}...")

                                    elif tool_name == "MultiEdit":
                                        # Multiple file edits
                                        if 'file_path' in tool_input:
                                            status_lines.append(f"📝 Multi-editing: {tool_input['file_path']}")
                                        if 'edits' in tool_input and isinstance(tool_input['edits'], list):
                                            edit_count = len(tool_input['edits'])
                                            status_lines.append(f"✏️  Operations: {edit_count} edits")

                                    self.notifications.show_tool_execution("\n".join(status_lines))

                            # Handle tool results
                            elif isinstance(block, ToolResultBlock):
                                if block.tool_use_id:
                                    # Try to identify which agent completed using tool_use_id
                                    completed_agent = None
                                    for agent_type, agent_info in agents_in_use.items():
                                        if agent_info.get("tool_use_id") == block.tool_use_id:
                                            completed_agent = agent_type
                                            break

                                    if completed_agent:
                                        # Update agent status
                                        agents_in_use[completed_agent]["status"] = "failed" if block.is_error else "completed"

                                        # Count running agents after this completion
                                        running_agents = [agent for agent, info in agents_in_use.items()
                                                        if info["status"] == "running"]
                                        completed_agents = [agent for agent, info in agents_in_use.items()
                                                          if info["status"] in ["completed", "failed"]]

                                        if len(agents_in_use) > 1:
                                            # Multi-agent scenario
                                            if block.is_error:
                                                status_text = f"❌ Agent {completed_agent} failed"
                                                title = "[bold red]Agent Failed[/bold red]"
                                                border_style = "red"
                                            else:
                                                status_text = f"✅ Agent {completed_agent} completed"
                                                title = "[bold green]Agent Complete[/bold green]"
                                                border_style = "green"

                                            # Add parallel execution summary
                                            status_lines = [status_text, ""]
                                            if running_agents:
                                                status_lines.append(f"🔄 Still running: {len(running_agents)} agents")
                                                for agent in running_agents[:3]:  # Show up to 3 running agents
                                                    status_lines.append(f"  • {agent}")
                                                if len(running_agents) > 3:
                                                    status_lines.append(f"  • ... and {len(running_agents) - 3} more")
                                            else:
                                                status_lines.append("🎉 All agents completed!")

                                            success = not block.is_error
                                            self.notifications.show_completion("\n".join(status_lines), success)
                                        else:
                                            # Single agent scenario
                                            if block.is_error:
                                                status_text = f"❌ Agent {completed_agent} failed"
                                                title = "[bold red]Agent Failed[/bold red]"
                                                border_style = "red"
                                            else:
                                                status_text = f"✅ Agent {completed_agent} completed"
                                                title = "[bold green]Agent Complete[/bold green]"
                                                border_style = "green"

                                            success = not block.is_error
                                            self.notifications.show_completion(status_text, success)
                                    else:
                                        # Regular tool completion (non-agent)
                                        completed_tool = "Tool"
                                        for tool in tools_in_use:
                                            if block.tool_use_id in str(block):
                                                completed_tool = tool
                                                break

                                        if block.is_error:
                                            status_text = f"❌ {completed_tool} failed"
                                            title = "[bold red]Tool Failed[/bold red]"
                                            border_style = "red"
                                        else:
                                            status_text = f"✅ {completed_tool} completed"
                                            title = "[bold green]Tool Complete[/bold green]"
                                            border_style = "green"

                                        success = not block.is_error
                                        self.notifications.show_completion(status_text, success)

                    # Handle ResultMessage (final metrics)
                    elif isinstance(message, ResultMessage):
                        session_metrics = {
                            'duration': message.duration_ms,
                            'api_duration': message.duration_api_ms,
                            'turns': message.num_turns,
                            'cost': message.total_cost_usd,
                            'success': not message.is_error
                        }

                        # Show final status with metrics
                        metrics_lines = [
                            f"🎯 Query completed (Turn {self.turn_count})",
                            f"⏱️  Duration: {message.duration_ms}ms (API: {message.duration_api_ms}ms)",
                            f"🔄 Conversation turns: {message.num_turns}",
                        ]

                        if message.total_cost_usd:
                            metrics_lines.append(f"💰 Cost: ${message.total_cost_usd:.4f}")

                        if tools_in_use:
                            metrics_lines.append(f"🛠️  Tools used: {', '.join(tools_in_use)}")

                        if agents_in_use:
                            agent_names = list(agents_in_use.keys())
                            completed_count = len([a for a, info in agents_in_use.items() if info["status"] == "completed"])
                            failed_count = len([a for a, info in agents_in_use.items() if info["status"] == "failed"])

                            if len(agent_names) > 1:
                                metrics_lines.append(f"🤖 Multi-Agent Execution: {len(agent_names)} agents")
                                metrics_lines.append(f"   ✅ Completed: {completed_count}, ❌ Failed: {failed_count}")
                            else:
                                metrics_lines.append(f"🤖 Agent used: {', '.join(agent_names)}")

                        self.notifications.show_session_complete("\n".join(metrics_lines))

                        # Break after ResultMessage
                        break

        except Exception as e:
            error_message = str(e)
            error_content = (
                f"❌ Error in Turn {self.turn_count}: {error_message}\n\n"
                "💡 Troubleshooting:\n"
                "• Connection issue - client will retry next turn\n"
                "• Check MCP server status: `navam test-connection`\n"
                "• Try `/clear` to reset or `/exit` to restart"
            )
            self.notifications.show_notification(error_content, "[bold red]Error[/bold red]", "red")

            # Reset connection on error
            await self.disconnect_client()

        # All notifications are now displayed during streaming - no need for post-processing

    async def _is_builtin_command(self, command: str) -> bool:
        """Check if a command is a built-in chat command"""
        builtin_commands = {
            '/help', '/status', '/commands', '/new', '/tools', '/servers',
            '/clear', '/exit', '/quit', '/q'
        }
        command_name = command.strip().lower().split()[0]
        return command_name in builtin_commands

    def _get_tool_description(self, tool_name: str) -> str:
        """Get a brief description of what a tool does"""
        descriptions = {
            "mcp__stock-analyzer__analyze_stock": "Stock analysis & metrics",
            "mcp__stock-analyzer__compare_stocks": "Compare multiple stocks",
            "mcp__stock-analyzer__screen_stocks": "Screen stocks by criteria",
            "mcp__company-research__get_company_profile": "Company information",
            "mcp__company-research__get_company_financials": "Financial statements",
            "mcp__news-analyzer__search_news": "News search & analysis",
            "mcp__news-analyzer__analyze_sentiment": "Sentiment analysis",
            "Bash": "Execute shell command",
            "Read": "Read file contents",
            "Write": "Write to file",
            "Task": "Execute specialized agent task",
        }
        return descriptions.get(tool_name, "Execute task")

    def _get_agent_description(self, agent_type: str) -> str:
        """Get a brief description of what an agent specializes in"""
        agent_descriptions = {
            "atlas-investment-strategist": "Chief Investment Strategist - Portfolio strategy & asset allocation",
            "quill-equity-analyst": "Equity Research Analyst - Company research & valuation",
            "macro-lens-strategist": "Market & Macro Strategist - Top-down analysis & sector allocation",
            "quant-portfolio-optimizer": "Portfolio Optimizer - Risk/return modeling & optimization",
            "risk-shield-manager": "Risk Manager - Portfolio risk monitoring & mitigation",
            "rebalance-bot": "Rebalancing Specialist - Portfolio drift control & rebalancing",
            "trader-jane-execution": "Execution Trader - Order routing & transaction cost analysis",
            "tax-scout": "Tax Optimization Specialist - Tax-loss harvesting & tax-aware strategies",
            "earnings-whisperer": "Earnings Analyst - Earnings analysis & guidance tracking",
            "news-sentry-market-watch": "Market News Analyst - Real-time signal detection & event monitoring",
            "screen-forge": "Idea Generation Specialist - Stock screening & candidate identification",
            "factor-scout": "Factor Analyst - Style exposure measurement & factor analysis",
            "ledger-performance-analyst": "Performance Analyst - Return calculation & attribution analysis",
            "compass-goal-planner": "Goal Planning Specialist - Financial planning & goal mapping",
            "compliance-sentinel": "Compliance Specialist - Regulatory compliance & risk controls",
            "notionist-librarian": "Research Librarian - Knowledge organization & thesis management",
            "hedge-smith-options": "Options Strategist - Hedging & protection strategies",
            "cash-treasury-steward": "Cash Manager - Treasury operations & liquidity management",
            "general-purpose": "General-Purpose Agent - Multi-step task execution",
        }
        return agent_descriptions.get(agent_type, f"Specialized agent ({agent_type})")

    async def run(self):
        """Run the interactive chat loop with ClaudeSDKClient"""
        self.display_welcome()

        try:
            while True:
                try:
                    # Get user input
                    user_input = await anyio.to_thread.run_sync(
                        self.session.prompt,
                        f"\n[StockAI] > "
                    )

                    if not user_input.strip():
                        continue

                    # Handle commands
                    if user_input.startswith('/'):
                        # Check if it's a built-in chat command
                        if await self._is_builtin_command(user_input):
                            should_continue = await self.handle_command(user_input)
                            if not should_continue:
                                break
                        # Check if it's an investment command
                        elif user_input.startswith('/invest:'):
                            # Parse command and arguments
                            full_command = user_input[1:]  # Remove leading /
                            command_prompt = await self._load_investment_command_prompt(user_input)
                            if command_prompt:
                                # For research-stock specifically, handle the stock symbol
                                if 'research-stock' in user_input and len(user_input.split()) > 1:
                                    stock_symbol = user_input.split()[-1]
                                    command_prompt = f"{command_prompt}\n\nStock to research: {stock_symbol}"
                                await self.process_query(command_prompt)
                            else:
                                self.console.print(f"[red]Investment command not found: {user_input}[/red]")
                        else:
                            # It's a Claude Code slash command - send it as a query
                            await self.process_query(user_input)
                    else:
                        # Process regular query with ClaudeSDKClient
                        await self.process_query(user_input)

                except KeyboardInterrupt:
                    self.console.print("\n[yellow]Use /exit to quit or /new to start fresh[/yellow]")
                except EOFError:
                    break
                except Exception as e:
                    self.console.print(f"[red]Chat error: {str(e)}[/red]")
                    self.console.print("[yellow]Connection will be reset on next interaction[/yellow]")

        finally:
            # Cleanup: Disconnect client and show session summary
            if self.client_connected:
                await self.disconnect_client()

            farewell = Panel.fit(
                f"[bold cyan]Session Complete[/bold cyan]\n\n"
                f"📊 Total conversation turns: {self.turn_count}\n"
                f"🔗 ClaudeSDKClient: Disconnected\n"
                f"💭 Context memory: Cleared\n\n"
                f"Thank you for using StockAI!\n"
                f"[dim]Enhanced with thinking tokens, tool tracking, and conversation memory[/dim]",
                title="Goodbye",
                border_style="green"
            )
            self.console.print(farewell)

    def _load_default_permissions(self) -> Dict[str, Any]:
        """Load default permission settings from JSON file"""
        try:
            if self.permissions_file.exists():
                with open(self.permissions_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            self.console.print(f"[yellow]Warning: Could not load permissions file: {e}[/yellow]")

        # Return simplified permissions structure
        # Note: File operations are auto-approved by acceptEdits mode
        return {
            "auto_allow": [      # Tools to always allow without prompting
                "Read",          # Reading files is safe
                "Glob",          # File pattern matching is safe
                "Grep",          # Text search is safe
            ],
            "auto_deny": [       # Tools to always deny without prompting
                # Add any tools that should never be allowed
            ],
            "remembered": {},    # Individual tool+input combinations with user decisions
        }

    def _save_default_permissions(self):
        """Save current permission settings to JSON file"""
        try:
            with open(self.permissions_file, 'w') as f:
                json.dump(self.default_permissions, f, indent=2)
        except Exception as e:
            self.console.print(f"[yellow]Warning: Could not save permissions file: {e}[/yellow]")

    async def _handle_tool_permission(self, tool_name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle tool permission requests for non-file operations

        Note: File operations (Write, Edit, MultiEdit) are auto-approved by acceptEdits mode.
        This callback only handles remaining tools that need manual approval.

        Returns:
            Dict with 'behavior' ('allow'|'deny') and optional 'updatedInput' or 'message'
        """
        # Check if this tool is in auto-allow list
        if tool_name in self.default_permissions.get("auto_allow", []):
            return {"behavior": "allow", "updatedInput": tool_input}

        # Check if this tool is in auto-deny list
        if tool_name in self.default_permissions.get("auto_deny", []):
            return {
                "behavior": "deny",
                "message": f"Tool {tool_name} is in auto-deny list"
            }

        # Special handling for potentially dangerous Bash commands
        if tool_name == "Bash" and "command" in tool_input:
            command = tool_input["command"]

            # Block dangerous commands
            dangerous_patterns = [
                "rm -rf",
                "sudo rm",
                "format",
                "mkfs",
                "dd if=",
                "curl | sh",
                "wget | sh",
                "> /dev/",
            ]

            for pattern in dangerous_patterns:
                if pattern in command.lower():
                    return {
                        "behavior": "deny",
                        "message": f"Dangerous command blocked: {pattern}"
                    }

        # Create a unique key for this specific tool+input combination
        tool_key = self._create_tool_key(tool_name, tool_input)
        remembered = self.default_permissions.get("remembered", {})

        # Check if we have a remembered decision for this exact scenario
        if tool_key in remembered:
            decision = remembered[tool_key]
            if decision == "allow":
                return {"behavior": "allow", "updatedInput": tool_input}
            else:
                return {"behavior": "deny", "message": "Previously denied by user"}

        # Show interactive permission prompt
        return await self._show_permission_prompt(tool_name, tool_input, tool_key)

    def _create_tool_key(self, tool_name: str, tool_input: Dict[str, Any]) -> str:
        """Create a unique key for tool+input combination for permission storage"""
        # For bash commands, include the command in the key
        if tool_name == "Bash" and "command" in tool_input:
            command = tool_input["command"]
            # Truncate very long commands
            if len(command) > 100:
                command = command[:100] + "..."
            return f"{tool_name}:{command}"

        # For file operations, include the file path
        elif tool_name in ["Read", "Write", "Edit"] and "file_path" in tool_input:
            file_path = tool_input["file_path"]
            return f"{tool_name}:{file_path}"

        # For other tools, just use the tool name
        else:
            return tool_name

    async def _show_permission_prompt(self, tool_name: str, tool_input: Dict[str, Any], tool_key: str) -> Dict[str, Any]:
        """Show interactive permission prompt to user"""

        # Create permission prompt panel
        prompt_lines = [
            f"🔧 [bold yellow]Tool Permission Request[/bold yellow]",
            f"   Tool: [cyan]{tool_name}[/cyan]",
            f"   Description: {self._get_tool_description(tool_name)}"
        ]

        # Add specific parameters based on tool type
        if tool_input:
            prompt_lines.append("   Parameters:")
            for key, value in tool_input.items():
                # Format value for display
                display_value = str(value)
                if len(display_value) > 80:
                    display_value = display_value[:80] + "..."
                prompt_lines.append(f"     {key}: {display_value}")

        # Show the permission request
        self.console.print(Panel(
            "\n".join(prompt_lines),
            title="[bold red]Permission Required[/bold red]",
            border_style="red",
            padding=(1, 2)
        ))

        # Get user decision
        while True:
            try:
                decision = await anyio.to_thread.run_sync(
                    lambda: input("\n   Choice: [y]es / [n]o / [A]lways allow / [D]eny always / [r]emember: ").lower().strip()
                )

                if decision in ['y', 'yes']:
                    self.console.print("   ✅ [green]Allowed[/green]\n")
                    return {"behavior": "allow", "updatedInput": tool_input}

                elif decision in ['n', 'no']:
                    self.console.print("   ❌ [red]Denied[/red]\n")
                    return {"behavior": "deny", "message": "User denied permission"}

                elif decision in ['a', 'always']:
                    # Add to auto-allow list
                    if tool_name not in self.default_permissions["auto_allow"]:
                        self.default_permissions["auto_allow"].append(tool_name)
                        self._save_default_permissions()
                    self.console.print(f"   ✅ [green]Always allowing {tool_name}[/green]\n")
                    return {"behavior": "allow", "updatedInput": tool_input}

                elif decision in ['d', 'deny']:
                    # Add to auto-deny list
                    if tool_name not in self.default_permissions["auto_deny"]:
                        self.default_permissions["auto_deny"].append(tool_name)
                        self._save_default_permissions()
                    self.console.print(f"   ❌ [red]Always denying {tool_name}[/red]\n")
                    return {"behavior": "deny", "message": "User set tool to always deny"}

                elif decision in ['r', 'remember']:
                    # Remember this specific tool+input combination
                    remember_decision = await anyio.to_thread.run_sync(
                        lambda: input("   Remember as [a]llow or [d]eny: ").lower().strip()
                    )

                    if remember_decision in ['a', 'allow']:
                        self.default_permissions["remembered"][tool_key] = "allow"
                        self._save_default_permissions()
                        self.console.print("   ✅ [green]Remembered as allow[/green]\n")
                        return {"behavior": "allow", "updatedInput": tool_input}
                    elif remember_decision in ['d', 'deny']:
                        self.default_permissions["remembered"][tool_key] = "deny"
                        self._save_default_permissions()
                        self.console.print("   ❌ [red]Remembered as deny[/red]\n")
                        return {"behavior": "deny", "message": "User remembered denial for this scenario"}
                    else:
                        self.console.print("   [yellow]Invalid choice, please try again[/yellow]")
                        continue

                else:
                    self.console.print("   [yellow]Invalid choice. Please enter y, n, A, D, or r[/yellow]")
                    continue

            except KeyboardInterrupt:
                self.console.print("\n   ❌ [red]Denied (interrupted)[/red]\n")
                return {"behavior": "deny", "message": "User interrupted permission prompt"}
            except EOFError:
                self.console.print("\n   ❌ [red]Denied (EOF)[/red]\n")
                return {"behavior": "deny", "message": "User cancelled permission prompt"}


def main():
    """Main entry point for interactive chat"""
    chat = InteractiveChat()
    anyio.run(chat.run)