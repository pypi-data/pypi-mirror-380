"""
Interactive chat module using Claude Agent SDK
"""

import anyio
import time
from typing import Optional, Dict, List, Any
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions,
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

# Import session cache for performance optimization
from .cache_manager import SessionCache

class ProgressTracker:
    """Tracks long-running operations and provides periodic progress updates"""

    def __init__(self, console: Console):
        self.console = console
        self.active_operations = {}  # operation_id -> {"start_time": float, "description": str, "last_update": float}
        self.update_interval = 30  # Show progress every 30 seconds

    def start_operation(self, operation_id: str, description: str):
        """Start tracking a new operation"""
        current_time = time.time()
        self.active_operations[operation_id] = {
            "start_time": current_time,
            "description": description,
            "last_update": current_time
        }

    def update_operation(self, operation_id: str, force: bool = False) -> Optional[str]:
        """
        Check if operation needs a progress update.
        Returns progress message if update is needed, None otherwise.
        """
        if operation_id not in self.active_operations:
            return None

        operation = self.active_operations[operation_id]
        current_time = time.time()
        elapsed = current_time - operation["start_time"]
        since_last_update = current_time - operation["last_update"]

        # Only show update if interval has passed or forced
        if force or since_last_update >= self.update_interval:
            operation["last_update"] = current_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)

            if minutes > 0:
                time_str = f"{minutes}m {seconds}s"
            else:
                time_str = f"{seconds}s"

            return f"⏱️ {operation['description']} - Running for {time_str}..."

        return None

    def complete_operation(self, operation_id: str) -> str:
        """Mark operation as complete and return completion message"""
        if operation_id not in self.active_operations:
            return ""

        operation = self.active_operations[operation_id]
        elapsed = time.time() - operation["start_time"]
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)

        if minutes > 0:
            time_str = f"{minutes}m {seconds}s"
        else:
            time_str = f"{seconds}s"

        del self.active_operations[operation_id]
        return f"✅ {operation['description']} - Completed in {time_str}"

    def get_active_operations_summary(self) -> Optional[str]:
        """Get summary of all active operations"""
        if not self.active_operations:
            return None

        current_time = time.time()
        lines = ["📊 Active Operations:"]

        for op_id, operation in self.active_operations.items():
            elapsed = current_time - operation["start_time"]
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)

            if minutes > 0:
                time_str = f"{minutes}m {seconds}s"
            else:
                time_str = f"{seconds}s"

            lines.append(f"  • {operation['description']} ({time_str})")

        return "\n".join(lines)


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
        self.show_notification(content, "[bold yellow]Navam Status[/bold yellow]", "yellow", timestamp)

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
    """Interactive chat interface for Navam with Claude Code SDK integration"""

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
        self.progress_tracker = ProgressTracker(self.console)
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

        # Configure agent directories for Claude Code SDK
        agent_dirs = self._get_agent_directories()

        # Configure Claude Code options
        # For Pro/Max plans, don't set API key - let Claude Code SDK use authenticated session

        # Determine if we should provide permission callback
        # IMPORTANT: In acceptEdits mode, don't provide callback to let SDK auto-approve file operations
        should_use_permission_callback = (
            self.interactive_permissions and
            self.permission_mode not in ['acceptEdits', 'bypassPermissions']
        )

        self.claude_options = ClaudeAgentOptions(
            allowed_tools=allowed_tools or self._get_default_tools(),
            permission_mode=self.permission_mode,
            system_prompt=self._get_system_prompt(),
            mcp_servers=self.mcp_servers,  # Pass MCP server configurations
            add_dirs=agent_dirs,  # Add agent directories so Claude Code SDK can find them
            can_use_tool=self._handle_tool_permission if should_use_permission_callback else None,
            # Note: No model or env specified - use Pro/Max plan defaults
            # NEW: Add hooks for caching (Phase 1 - v1.5.0)
            hooks={
                'pre_tool_use': self._pre_tool_use_hook,
                'post_tool_use': self._post_tool_use_hook
            }
        )

        # Initialize ClaudeSDKClient for conversation continuity
        self.client = ClaudeSDKClient(options=self.claude_options)
        self.client_connected = False
        self.turn_count = 0

        # Initialize session cache for performance optimization
        self.session_cache = SessionCache(ttl_seconds=300, max_entries=100)
        self.cache_enabled = True  # Can be toggled for debugging

        # Track tool call patterns for cache effectiveness analysis
        self.tool_call_tracker = {}  # tool_name+args_hash -> {'count': N, 'first_seen': timestamp, 'results': []}

        # Track performance metrics
        self.performance_metrics = {
            'workflow_start': None,
            'last_activity': None,
            'tool_calls_made': 0,
            'operations': [],
            'permission_checks': 0,
            'permission_check_time': 0.0,
            'potential_cache_hits': 0,  # Duplicate tool calls that could have been cached
            'unique_tool_calls': 0,
            'cache_hits_actual': 0,  # Actual cache hits (tool execution skipped)
            'cache_misses_actual': 0  # Cache misses (tool executed)
        }

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

    def _get_agent_directories(self) -> List[Path]:
        """
        Get directories containing .claude/agents/ to be added to Claude Code SDK's accessible paths.
        This allows agents to be recognized when installed via PyPI.

        Claude Code SDK auto-detects subagents from `.claude/agents/*.md` directories.
        We need to ensure the SDK can find these regardless of where navam is installed.
        """
        agent_dirs = []

        # Check for local development .claude/agents (highest priority)
        if Path(".claude/agents").exists():
            # In development, add current directory so SDK finds ./.claude/agents/
            agent_dirs.append(Path.cwd())

        # Check for package installation - agents are in src/navam/agents/
        package_agents_dir = Path(__file__).parent / "agents"
        if package_agents_dir.exists() and package_agents_dir.is_dir():
            # For PyPI installation, we need to create a .claude/agents symlink structure
            # or copy agents to user's home directory on first run
            self._ensure_user_agents_dir(package_agents_dir)

        # Check for user-level agents in ~/.claude/agents/ (standard Claude Code location)
        user_claude_agents = Path.home() / ".claude" / "agents"
        if user_claude_agents.exists():
            # Add home directory so SDK finds ~/.claude/agents/
            agent_dirs.append(Path.home())

        return agent_dirs

    def _ensure_user_agents_dir(self, package_agents_dir: Path):
        """
        Ensure agents from package are available in user's ~/.claude/agents/ directory.
        This is a fallback for PyPI installations where .claude/agents/ doesn't exist locally.
        """
        user_claude_dir = Path.home() / ".claude"
        user_agents_dir = user_claude_dir / "agents"

        try:
            # Create ~/.claude/agents/ if it doesn't exist
            user_agents_dir.mkdir(parents=True, exist_ok=True)

            # Copy agent files from package to user directory if not already present
            for agent_file in package_agents_dir.glob("*.md"):
                dest_file = user_agents_dir / agent_file.name
                if not dest_file.exists():
                    # Copy agent file to user directory
                    import shutil
                    shutil.copy2(agent_file, dest_file)

        except Exception as e:
            # Silently fail if we can't set up user agents
            # The package will still work, just without agent support
            pass

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
        """Load MCP server configurations from project and package"""
        import sys
        servers = {}

        # Try to load from current directory .mcp.json files first
        mcp_files = ['.mcp.json', '.mcp-company.json']
        for mcp_file in mcp_files:
            if os.path.exists(mcp_file):
                with open(mcp_file, 'r') as f:
                    config = json.load(f)
                    if 'mcpServers' in config:
                        servers.update(config['mcpServers'])

        # If no servers found, try to load from package installation directory
        if not servers:
            try:
                # Get the package directory
                package_dir = Path(__file__).parent
                package_mcp_file = package_dir / '.mcp.json'

                if package_mcp_file.exists():
                    with open(package_mcp_file, 'r') as f:
                        config = json.load(f)
                        if 'mcpServers' in config:
                            servers.update(config['mcpServers'])
            except Exception:
                # Silently ignore package loading errors
                pass

        # Replace {{SYS_EXECUTABLE}} placeholder with actual Python interpreter
        for server_name, server_config in servers.items():
            if server_config.get('command') == '{{SYS_EXECUTABLE}}':
                server_config['command'] = sys.executable

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
        return """You are Navam, an intelligent financial assistant with access to comprehensive stock market data and analysis tools.

        You have access to MCP tools for:
        - Stock analysis and comparisons
        - Company research and financials
        - Market news and sentiment analysis
        - Portfolio calculations
        - Technical indicators

        Provide accurate, data-driven insights while being helpful and conversational.
        When analyzing stocks or companies, use the available tools to fetch real-time data.
        Always cite the data sources and be transparent about any limitations."""

    def _check_api_status(self) -> Dict[str, Dict[str, Any]]:
        """Check which APIs are configured and active"""
        api_status = {
            "yahoo_finance": {
                "name": "Yahoo Finance",
                "required_key": False,
                "active": True,  # Always active, no key required
                "description": "Stock quotes, history, fundamentals"
            },
            "alpha_vantage": {
                "name": "Alpha Vantage",
                "required_key": True,
                "key_env": "ALPHA_VANTAGE_KEY",
                "active": bool(os.getenv("ALPHA_VANTAGE_KEY")),
                "description": "Company data, news, forex"
            },
            "polygon": {
                "name": "Polygon.io",
                "required_key": True,
                "key_env": "POLYGON_API_KEY",
                "active": bool(os.getenv("POLYGON_API_KEY")),
                "description": "Market data, aggregates"
            },
            "marketaux": {
                "name": "MarketAux",
                "required_key": True,
                "key_env": "MARKETAUX_API_KEY",
                "active": bool(os.getenv("MARKETAUX_API_KEY")),
                "description": "Financial news"
            },
            "newsapi": {
                "name": "NewsAPI",
                "required_key": True,
                "key_env": "NEWSAPI_KEY",
                "active": bool(os.getenv("NEWSAPI_KEY")),
                "description": "General news"
            },
            "finnhub": {
                "name": "Finnhub",
                "required_key": True,
                "key_env": "FINNHUB_API_KEY",
                "active": bool(os.getenv("FINNHUB_API_KEY")),
                "description": "Market data, news"
            },
            "sec": {
                "name": "SEC EDGAR",
                "required_key": False,
                "active": True,  # Always active, no key required
                "description": "Company filings"
            }
        }
        return api_status

    def display_welcome(self):
        """Display welcome message"""
        # Get API status
        api_status = self._check_api_status()
        active_apis = [api for api, info in api_status.items() if info["active"]]
        configured_apis = [api for api, info in api_status.items() if info.get("required_key", False)]

        # Build API status display
        api_status_lines = [
            f"[bold]📡 API Status:[/bold] {len(active_apis)}/{len(api_status)} active"
        ]

        # Show active APIs
        if active_apis:
            api_status_lines.append("[green]✅ Active APIs:[/green]")
            for api_key in active_apis:
                api_info = api_status[api_key]
                api_status_lines.append(f"  • {api_info['name']}: {api_info['description']}")

        # Show missing API keys if any
        missing_apis = [api for api in configured_apis if not api_status[api]["active"]]
        if missing_apis:
            api_status_lines.append("[yellow]⚠️ APIs needing keys:[/yellow]")
            for api_key in missing_apis[:3]:  # Show first 3
                api_info = api_status[api_key]
                api_status_lines.append(f"  • {api_info['name']} ({api_info['key_env']})")
            if len(missing_apis) > 3:
                api_status_lines.append(f"  • ... and {len(missing_apis) - 3} more")

        api_status_text = "\n".join(api_status_lines)

        welcome = Panel.fit(
            "[bold cyan]Navam Enhanced Interactive Chat[/bold cyan]\n"
            "[dim]Powered by ClaudeSDKClient with Advanced Notifications[/dim]\n\n"
            f"{api_status_text}\n\n"
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
            "  [yellow]/api[/yellow]        - Show detailed API status\n"
            "  [yellow]/agents[/yellow]     - List all available AI agents\n"
            "  [yellow]/cache[/yellow]      - Show cache performance statistics\n"
            "  [yellow]/perf[/yellow]       - Show performance metrics\n"
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
  /api      - Show detailed API status and configuration
  /agents   - List available AI agents with descriptions
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
  • AI agents: 18 specialized agents automatically selected for your tasks

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
                "/api - Show detailed API status",
                "/agents - List all available AI agents",
                "/commands - List all slash commands",
                "/status - Show conversation status",
                "/cache - Show cache statistics",
                "/perf - Show performance metrics",
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

        elif command == '/agents':
            # Show all available agents with descriptions
            agents_info = self._load_agents_info()

            if not agents_info:
                self.console.print("[yellow]No agents found in .claude/agents/ folder[/yellow]")
                return True

            agents_text = "[bold]🤖 Available AI Agents[/bold]\n\n"
            agents_text += f"[dim]Total: {len(agents_info)} specialized agents for investment workflows[/dim]\n\n"

            # Group agents by category
            categories = {
                "Strategy & Planning": ["atlas-investment-strategist", "compass-goal-planner", "macro-lens-strategist"],
                "Research & Analysis": ["quill-equity-analyst", "earnings-whisperer", "news-sentry-market-watch", "screen-forge"],
                "Portfolio Management": ["quant-portfolio-optimizer", "risk-shield-manager", "rebalance-bot", "ledger-performance-analyst"],
                "Trading & Execution": ["trader-jane-execution", "compliance-sentinel"],
                "Tax & Treasury": ["tax-scout", "cash-treasury-steward"],
                "Advanced Strategies": ["hedge-smith-options", "factor-scout"],
                "Knowledge Management": ["notionist-librarian"]
            }

            for category, agent_names in categories.items():
                matching_agents = [a for a in agents_info if a['name'] in agent_names]
                if matching_agents:
                    agents_text += f"[bold cyan]{category}:[/bold cyan]\n"
                    for agent in matching_agents:
                        agents_text += f"  🤖 [yellow]{agent['name']}[/yellow]\n"
                        agents_text += f"     {agent['short_description']}\n"
                    agents_text += "\n"

            agents_text += "[dim]💡 Usage Examples:[/dim]\n"
            agents_text += "[dim]  • 'Analyze AAPL stock' → Uses quill-equity-analyst for fundamental analysis[/dim]\n"
            agents_text += "[dim]  • 'Review my portfolio' → Uses ledger-performance-analyst for performance analysis[/dim]\n"
            agents_text += "[dim]  • 'Plan for retirement' → Uses compass-goal-planner for financial planning[/dim]\n"
            agents_text += "[dim]  • 'Find tax loss harvesting opportunities' → Uses tax-scout[/dim]\n\n"
            agents_text += "[dim]Agents are automatically selected based on your query context.[/dim]\n"

            self.console.print(Panel(agents_text, title="AI Agents", border_style="magenta"))

        elif command == '/api':
            # Show detailed API status
            api_status = self._check_api_status()
            active_apis = []
            inactive_apis = []

            for api_key, api_info in api_status.items():
                if api_info["active"]:
                    active_apis.append(api_info)
                elif api_info.get("required_key", False):
                    inactive_apis.append(api_info)

            api_text = "[bold]📡 API Configuration Status[/bold]\n\n"

            # Show active APIs
            api_text += f"[green]✅ Active APIs ({len(active_apis)}):[/green]\n"
            for api_info in active_apis:
                api_text += f"  • {api_info['name']}\n"
                api_text += f"    └─ {api_info['description']}\n"
                if api_info.get("required_key"):
                    api_text += f"    └─ Key: {api_info.get('key_env', 'N/A')} [green]✓[/green]\n"
                else:
                    api_text += f"    └─ No key required [green]✓[/green]\n"

            # Show inactive APIs
            if inactive_apis:
                api_text += f"\n[yellow]⚠️ APIs Needing Configuration ({len(inactive_apis)}):[/yellow]\n"
                for api_info in inactive_apis:
                    api_text += f"  • {api_info['name']}\n"
                    api_text += f"    └─ {api_info['description']}\n"
                    api_text += f"    └─ Set environment variable: [yellow]{api_info.get('key_env', 'N/A')}[/yellow]\n"

                api_text += "\n[dim]💡 To configure APIs:[/dim]\n"
                api_text += "[dim]1. Add API keys to .env file in project root[/dim]\n"
                api_text += "[dim]2. Or export as environment variables:[/dim]\n"
                api_text += "[dim]   export ALPHA_VANTAGE_KEY=your_key_here[/dim]\n"

            # Show summary
            api_text += f"\n[bold]📊 Summary:[/bold]\n"
            api_text += f"  • Total APIs available: {len(api_status)}\n"
            api_text += f"  • Active: {len(active_apis)}\n"
            api_text += f"  • Needs configuration: {len(inactive_apis)}\n"
            api_text += f"  • Coverage: {len(active_apis)}/{len(api_status)} ({int(len(active_apis)/len(api_status)*100)}%)\n"

            self.console.print(Panel(api_text, title="API Status", border_style="cyan"))

        elif command == '/cache':
            # Show cache statistics
            self._show_cache_statistics()

        elif command == '/perf' or command == '/performance':
            # Show performance summary
            self._show_performance_summary()

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

        # Check if this is a stock research command - add optimization instructions
        stock_symbol = None
        if prompt.startswith('/invest:research-stock'):
            # Extract symbol from command
            parts = prompt.split()
            if len(parts) >= 2:
                stock_symbol = parts[1].upper()

                # Add performance optimization instructions
                optimization_note = f"""

**PERFORMANCE OPTIMIZATION INSTRUCTIONS FOR {stock_symbol}:**

CRITICAL: This workflow has session-level caching enabled. To maximize performance and minimize API costs:

1. **Gather Data First, Then Analyze:**
   - Make ALL data-gathering tool calls FIRST (company profile, financials, analyst ratings, stock analysis, news)
   - Use the results from these initial calls for your analysis
   - DO NOT make the same tool call multiple times

2. **Share Context Between Agents:**
   - When launching multiple agents, pass the data you've already gathered as context
   - Example: If you already called get_company_profile for {stock_symbol}, include that data when launching the next agent
   - Agents should AVOID repeating tool calls that have already been made

3. **Minimize Redundancy:**
   - Before calling a tool, check if you or a previous agent already has that data
   - The session cache will automatically eliminate true duplicates, but avoid unnecessary calls entirely

4. **Batch Data Collection:**
   - Gather all required data in a single step before analysis
   - Launch agents with pre-gathered context rather than having each agent fetch the same data

This optimization reduces workflow time from ~9 minutes to ~3 minutes (67% faster).

{prompt}
"""
                prompt = optimization_note

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

                                # Check for progress updates on active operations
                                for op_id in list(self.progress_tracker.active_operations.keys()):
                                    progress_msg = self.progress_tracker.update_operation(op_id)
                                    if progress_msg:
                                        status_lines.append("")
                                        status_lines.append(progress_msg)

                                self.notifications.show_thinking("\n".join(status_lines))

                            # Handle tool usage
                            elif isinstance(block, ToolUseBlock):
                                tool_name = block.name
                                tools_in_use.add(tool_name)

                                # Track performance metrics
                                self.performance_metrics['tool_calls_made'] += 1
                                tool_start_time = time.time()

                                # Store tool start time with tool_use_id for duration tracking
                                if not hasattr(self, '_tool_timings'):
                                    self._tool_timings = {}
                                self._tool_timings[block.id] = {
                                    'tool_name': tool_name,
                                    'start_time': tool_start_time,
                                    'tool_input': block.input
                                }

                                # Show tool usage details
                                tool_input = block.input
                                tool_description = self._get_tool_description(tool_name)

                                # Track tool calls for cache effectiveness analysis
                                # (Skip agent Task tools as they're not cacheable)
                                if tool_name != "Task" and tool_name.startswith("mcp__"):
                                    cache_key = self.session_cache._make_key(tool_name, tool_input)

                                    if cache_key in self.tool_call_tracker:
                                        # This is a duplicate call - could have been cached!
                                        self.tool_call_tracker[cache_key]['count'] += 1
                                        self.performance_metrics['potential_cache_hits'] += 1
                                    else:
                                        # First time seeing this tool call
                                        self.tool_call_tracker[cache_key] = {
                                            'tool_name': tool_name,
                                            'count': 1,
                                            'first_seen': time.time(),
                                            'args': tool_input
                                        }
                                        self.performance_metrics['unique_tool_calls'] += 1

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

                                    # Start progress tracking for this agent
                                    operation_id = f"agent_{agent_type}_{block.id}"
                                    self.progress_tracker.start_operation(operation_id, f"Agent {agent_type}: {task_description}")

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

                                        # Check for progress updates
                                        progress_summary = self.progress_tracker.get_active_operations_summary()
                                        if progress_summary:
                                            status_lines.append("")
                                            status_lines.append(progress_summary)

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
                                # Calculate and log tool execution time
                                if hasattr(self, '_tool_timings') and block.tool_use_id in self._tool_timings:
                                    timing_info = self._tool_timings[block.tool_use_id]
                                    duration = time.time() - timing_info['start_time']
                                    tool_name = timing_info['tool_name']
                                    tool_input = timing_info['tool_input']

                                    # Log timing for Write operations (especially to debug slow reports/ writes)
                                    if tool_name == "Write" and 'file_path' in tool_input:
                                        file_path = tool_input['file_path']
                                        content_size = len(tool_input.get('content', ''))
                                        timing_msg = f"⏱️  Write completed: {file_path} ({content_size:,} chars) - {duration:.2f}s"

                                        # Warn if Write took unusually long
                                        if duration > 5.0:
                                            timing_msg = f"⚠️  SLOW Write: {file_path} ({content_size:,} chars) - {duration:.2f}s"
                                            self.notifications.show_warning(timing_msg)
                                        elif duration > 1.0:
                                            self.notifications.show_status(timing_msg)

                                    # Log timing for other slow operations
                                    elif duration > 10.0:
                                        timing_msg = f"⏱️  {tool_name} completed - {duration:.2f}s"
                                        self.notifications.show_status(timing_msg)

                                    # Clean up timing record
                                    del self._tool_timings[block.tool_use_id]

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

                                        # Complete progress tracking for this agent
                                        operation_id = f"agent_{completed_agent}_{block.tool_use_id}"
                                        completion_msg = self.progress_tracker.complete_operation(operation_id)
                                        if completion_msg:
                                            self.notifications.show_status(completion_msg)

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
            '/help', '/api', '/agents', '/status', '/commands', '/new', '/tools', '/servers',
            '/clear', '/exit', '/quit', '/q', '/cache', '/perf', '/performance'
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

    def _load_agents_info(self) -> List[Dict[str, str]]:
        """Load agent information from .claude/agents/ folder"""
        agents_info = []

        # Try multiple locations for agents folder
        possible_locations = [
            Path(".claude/agents"),  # Local development
            Path(__file__).parent / "agents",  # Package location
            Path.home() / ".navam" / "agents",  # User config
        ]

        for agents_folder in possible_locations:
            if agents_folder.exists():
                for md_file in agents_folder.glob("*.md"):
                    try:
                        content = md_file.read_text()
                        # Extract name and description from YAML frontmatter
                        if content.startswith("---"):
                            # Find the end of frontmatter
                            end_idx = content.find("---", 3)
                            if end_idx > 0:
                                frontmatter = content[3:end_idx]

                                # Parse YAML manually (simple parsing)
                                name = None
                                description = None

                                for line in frontmatter.split('\n'):
                                    if line.startswith('name:'):
                                        name = line.split('name:', 1)[1].strip()
                                    elif line.startswith('description:'):
                                        # Description might span multiple lines or be very long
                                        description_text = line.split('description:', 1)[1].strip()
                                        # Extract first sentence or first example
                                        if 'Use this agent when' in description_text:
                                            # Extract the main "Use this agent when..." part
                                            desc_parts = description_text.split('Examples:')
                                            main_desc = desc_parts[0].strip()
                                            # Truncate if too long
                                            if len(main_desc) > 150:
                                                main_desc = main_desc[:150] + "..."
                                            description = main_desc
                                        else:
                                            description = description_text[:150]

                                if name:
                                    # Use the existing _get_agent_description method for consistency
                                    short_description = self._get_agent_description(name)

                                    agents_info.append({
                                        'name': name,
                                        'short_description': short_description,
                                        'full_description': description or short_description
                                    })
                    except Exception as e:
                        # Skip files that can't be parsed
                        continue

                # If we found agents in this location, don't check other locations
                if agents_info:
                    break

        return sorted(agents_info, key=lambda x: x['name'])

    async def run(self):
        """Run the interactive chat loop with ClaudeSDKClient"""
        self.display_welcome()

        try:
            while True:
                try:
                    # Get user input
                    user_input = await anyio.to_thread.run_sync(
                        self.session.prompt,
                        f"\n[Navam] > "
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
                f"Thank you for using Navam!\n"
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

    async def _pre_tool_use_hook(self, tool_name: str, tool_input: dict) -> dict:
        """
        Pre-execution hook: Check cache before tool execution

        This hook is called by Claude Agent SDK BEFORE executing a tool.
        If we have a cached result, we can skip execution entirely.

        Returns:
            dict with:
                - 'behavior': 'allow' (execute tool) or 'deny' (skip execution)
                - 'result': cached result (if behavior='deny')
        """
        # Only cache MCP tool calls (external API calls)
        if not tool_name.startswith("mcp__"):
            return {"behavior": "allow"}

        # Check if caching is enabled
        if not self.cache_enabled:
            return {"behavior": "allow"}

        # Try to retrieve cached result
        cached = self.session_cache.get(tool_name, tool_input)
        if cached is not None:
            # Cache hit - skip tool execution!
            self.performance_metrics['cache_hits_actual'] += 1
            self.notifications.show_status(f"✅ Cache hit: {tool_name}")
            return {
                "behavior": "deny",  # Skip execution
                "result": cached      # Return cached data
            }

        # Cache miss - allow execution
        self.performance_metrics['cache_misses_actual'] += 1
        return {"behavior": "allow"}

    async def _post_tool_use_hook(self, tool_name: str, tool_input: dict, result: dict):
        """
        Post-execution hook: Store result in cache after tool execution

        This hook is called by Claude Agent SDK AFTER a tool executes successfully.
        We store the result in cache for future use.

        Args:
            tool_name: Name of the tool that was executed
            tool_input: Arguments passed to the tool
            result: Result returned by the tool
        """
        # Only cache MCP tool calls (external API calls)
        if not tool_name.startswith("mcp__"):
            return

        # Check if caching is enabled
        if not self.cache_enabled:
            return

        # Store result in cache
        self.session_cache.set(tool_name, tool_input, result)
        self.notifications.show_status(f"💾 Cached: {tool_name}")

    async def _handle_tool_permission(self, tool_name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle tool permission requests for non-file operations

        Note: File operations (Write, Edit, MultiEdit) are auto-approved by acceptEdits mode.
        This callback should not be called in acceptEdits/bypassPermissions modes.

        Returns:
            Dict with 'behavior' ('allow'|'deny') and optional 'updatedInput' or 'message'
        """
        # Track permission check performance
        permission_start = time.time()
        self.performance_metrics['permission_checks'] += 1

        # DEBUG: Log if permission handler is unexpectedly called for Write operations
        if tool_name in ['Write', 'Edit', 'MultiEdit']:
            file_path = tool_input.get('file_path', 'unknown')
            self.console.print(f"[yellow]⚠️  DEBUG: Permission handler called for {tool_name}: {file_path} (mode: {self.permission_mode})[/yellow]")

        # Defense-in-depth: Auto-approve file operations if in acceptEdits mode
        # (This shouldn't be called in acceptEdits mode, but handle it gracefully if it is)
        if self.permission_mode == 'acceptEdits' and tool_name in ['Write', 'Edit', 'MultiEdit']:
            self.performance_metrics['permission_check_time'] += time.time() - permission_start
            return {"behavior": "allow", "updatedInput": tool_input}

        # Check if this tool is in auto-allow list
        if tool_name in self.default_permissions.get("auto_allow", []):
            self.performance_metrics['permission_check_time'] += time.time() - permission_start
            return {"behavior": "allow", "updatedInput": tool_input}

        # Check if this tool is in auto-deny list
        if tool_name in self.default_permissions.get("auto_deny", []):
            self.performance_metrics['permission_check_time'] += time.time() - permission_start
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
                    self.performance_metrics['permission_check_time'] += time.time() - permission_start
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
            self.performance_metrics['permission_check_time'] += time.time() - permission_start
            if decision == "allow":
                return {"behavior": "allow", "updatedInput": tool_input}
            else:
                return {"behavior": "deny", "message": "Previously denied by user"}

        # Show interactive permission prompt (this will take user interaction time)
        result = await self._show_permission_prompt(tool_name, tool_input, tool_key)
        self.performance_metrics['permission_check_time'] += time.time() - permission_start
        return result

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

    def _show_cache_statistics(self):
        """Display cache performance statistics"""
        stats = self.session_cache.get_stats()
        cached_tools = self.session_cache.get_cached_tools()

        stats_text = "[bold]📊 Cache Performance Analysis[/bold]\n\n"

        # Actual cache performance (from hooks)
        cache_hits = self.performance_metrics.get('cache_hits_actual', 0)
        cache_misses = self.performance_metrics.get('cache_misses_actual', 0)
        total_cached_calls = cache_hits + cache_misses

        if total_cached_calls > 0:
            hit_rate = (cache_hits / total_cached_calls) * 100
            stats_text += f"[cyan]✨ Active Cache Performance (v1.5.0):[/cyan]\n"
            stats_text += f"  • Total MCP tool requests: [yellow]{total_cached_calls}[/yellow]\n"
            stats_text += f"  • Cache hits: [green]{cache_hits}[/green] (saved API calls!)\n"
            stats_text += f"  • Cache misses: [yellow]{cache_misses}[/yellow] (executed)\n"
            stats_text += f"  • Hit rate: [green]{hit_rate:.1f}%[/green]\n"

            if cache_hits > 0:
                stats_text += f"\n  [green]✅ Saved {cache_hits} API calls with hook-based caching![/green]\n"
            else:
                stats_text += f"\n  [yellow]First pass - building cache. Run duplicate queries to see savings.[/yellow]\n"
            stats_text += "\n"

        # Observed tool call patterns (potential optimization)
        total_mcp_calls = self.performance_metrics.get('unique_tool_calls', 0) + self.performance_metrics.get('potential_cache_hits', 0)
        unique_calls = self.performance_metrics.get('unique_tool_calls', 0)
        duplicate_calls = self.performance_metrics.get('potential_cache_hits', 0)

        if total_mcp_calls > 0 and duplicate_calls > 0:
            waste_rate = (duplicate_calls / total_mcp_calls) * 100
            stats_text += f"[cyan]🎯 Pattern Analysis:[/cyan]\n"
            stats_text += f"  • Total observed calls: [yellow]{total_mcp_calls}[/yellow]\n"
            stats_text += f"  • Unique patterns: [green]{unique_calls}[/green]\n"
            stats_text += f"  • Duplicate patterns: [red]{duplicate_calls}[/red] ([red]{waste_rate:.1f}%[/red])\n\n"

            # Show top duplicate tools
            duplicates = [(info['tool_name'], info['count'])
                         for info in self.tool_call_tracker.values()
                         if info['count'] > 1]
            if duplicates:
                duplicates.sort(key=lambda x: x[1], reverse=True)
                stats_text += f"[cyan]🔄 Most Duplicated Tools:[/cyan]\n"
                for tool_name, count in duplicates[:5]:
                    tool_short = tool_name.replace('mcp__', '').replace('__', '.')
                    savings = count - 1
                    stats_text += f"  • {tool_short}: [red]{count} calls[/red] ({savings} duplicates)\n"
                stats_text += "\n"

        # Current cache state
        stats_text += f"[cyan]💾 Cache Infrastructure:[/cyan]\n"
        stats_text += f"  • Status: [green]Active (Hooks Enabled)[/green]\n" if self.cache_enabled else f"  • Status: [red]Disabled[/red]\n"
        stats_text += f"  • Entries: {stats['cache_size']}/{stats['max_size']}\n"
        stats_text += f"  • TTL: 5 minutes\n"
        stats_text += f"  • Strategy: Pre-execution hook + Post-execution storage\n\n"

        # Implementation status
        if total_cached_calls > 0:
            stats_text += "[cyan]📝 Implementation Status:[/cyan]\n"
            stats_text += "  [green]✅ Hook-based caching fully operational (v1.5.0-alpha)[/green]\n"
            stats_text += "  [dim]• Pre-execution hook checks cache and skips tool calls[/dim]\n"
            stats_text += "  [dim]• Post-execution hook stores results for reuse[/dim]\n"
        else:
            stats_text += "[cyan]💡 Tip:[/cyan]\n"
            stats_text += "  Use [yellow]/invest:research-stock[/yellow] to see cache in action\n"

        self.console.print(Panel(stats_text, title="Cache Statistics (v1.5.0)", border_style="cyan"))

    def _track_operation(self, operation_name: str, duration: float = None):
        """Track performance metrics for operations"""
        if not self.performance_metrics.get('workflow_start'):
            self.performance_metrics['workflow_start'] = time.time()

        self.performance_metrics['last_activity'] = time.time()

        operation_info = {
            'name': operation_name,
            'timestamp': time.time(),
            'duration': duration
        }
        self.performance_metrics['operations'].append(operation_info)

    def _show_performance_summary(self):
        """Display performance summary for the current workflow"""
        perf_text = "[bold]⚡ Performance Summary[/bold]\n\n"

        if not self.performance_metrics['workflow_start']:
            perf_text += "[yellow]No workflow activity recorded yet.[/yellow]\n\n"
            perf_text += "[dim]Performance metrics will be tracked once you start using the system.[/dim]\n"
            perf_text += "[dim]Metrics include: workflow duration, tool calls, cache performance, and permission checks.[/dim]\n"
            self.console.print(Panel(perf_text, title="Performance Metrics", border_style="green"))
            return

        total_duration = time.time() - self.performance_metrics['workflow_start']
        operations = self.performance_metrics['operations']

        perf_text += f"[cyan]Workflow Timing:[/cyan]\n"
        perf_text += f"  • Total duration: [yellow]{total_duration:.1f}s[/yellow]\n"
        perf_text += f"  • Operations: {len(operations)}\n"
        perf_text += f"  • Tool calls made: {self.performance_metrics['tool_calls_made']}\n\n"

        # Tool call efficiency analysis
        unique_calls = self.performance_metrics.get('unique_tool_calls', 0)
        duplicate_calls = self.performance_metrics.get('potential_cache_hits', 0)
        total_mcp_calls = unique_calls + duplicate_calls

        if total_mcp_calls > 0:
            efficiency = (unique_calls / total_mcp_calls) * 100 if total_mcp_calls > 0 else 0
            waste = 100 - efficiency

            perf_text += f"[cyan]Tool Call Efficiency:[/cyan]\n"
            perf_text += f"  • MCP tool calls: [yellow]{total_mcp_calls}[/yellow] (unique: {unique_calls}, duplicates: {duplicate_calls})\n"
            perf_text += f"  • Efficiency: [green]{efficiency:.1f}%[/green]"

            if duplicate_calls > 0:
                perf_text += f" ([red]{waste:.1f}% waste[/red])\n"
                perf_text += f"  • Potential savings: [yellow]{duplicate_calls} API calls[/yellow]\n"
            else:
                perf_text += f" [green]✓ No duplicates![/green]\n"
            perf_text += "\n"

        # Show permission check overhead
        if self.performance_metrics['permission_checks'] > 0:
            perf_text += f"[cyan]Permission Checks:[/cyan]\n"
            perf_text += f"  • Total checks: {self.performance_metrics['permission_checks']}\n"
            perf_text += f"  • Time spent: {self.performance_metrics['permission_check_time']:.2f}s\n"
            avg_check_time = self.performance_metrics['permission_check_time'] / self.performance_metrics['permission_checks']
            perf_text += f"  • Average per check: {avg_check_time*1000:.1f}ms\n\n"

        # Show recent operations
        if operations:
            perf_text += f"[cyan]Recent Operations:[/cyan]\n"
            for op in operations[-5:]:  # Show last 5
                name = op['name']
                if op['duration']:
                    perf_text += f"  • {name}: {op['duration']:.1f}s\n"
                else:
                    perf_text += f"  • {name}\n"

        self.console.print(Panel(perf_text, title="Performance Metrics", border_style="green"))

    def _reset_performance_metrics(self):
        """Reset performance tracking for new workflow"""
        self.performance_metrics = {
            'workflow_start': time.time(),
            'last_activity': time.time(),
            'tool_calls_made': 0,
            'operations': [],
            'permission_checks': 0,
            'permission_check_time': 0.0
        }


def main():
    """Main entry point for interactive chat"""
    chat = InteractiveChat()
    anyio.run(chat.run)