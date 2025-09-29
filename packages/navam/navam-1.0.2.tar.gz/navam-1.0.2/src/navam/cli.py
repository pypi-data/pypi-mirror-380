"""
Command-line interface for Navam - Personal AI Agents
"""

import click
import anyio
import sys
from pathlib import Path
from typing import Optional, List
from .chat import InteractiveChat
from .tools import list_available_tools, test_mcp_connection
from claude_code_sdk import query, ClaudeCodeOptions
from rich.console import Console

console = Console()

@click.group()
@click.version_option(version='1.0.0', prog_name='navam')
def cli():
    """Navam - Personal AI agents for investing, shopping, health, and learning"""
    pass

@cli.command()
@click.option('--history-file', type=click.Path(), help='Path to chat history file')
@click.option('--mcp-server', multiple=True, help='Specific MCP servers to load')
@click.option('--tools', multiple=True, help='Specific tools to allow')
@click.option('--permission-mode', type=click.Choice(['default', 'acceptEdits', 'bypassPermissions']),
              default='acceptEdits', help='Permission mode for tool usage')
@click.option('--no-interactive-permissions', is_flag=True,
              help='Disable interactive permission prompts')
@click.option('--test-mode', is_flag=True, help='Run in test mode without Claude Code SDK')
def chat(history_file: Optional[str], mcp_server: List[str], tools: List[str],
         permission_mode: str, no_interactive_permissions: bool, test_mode: bool):
    """Start interactive chat session"""
    try:
        if test_mode:
            from .simple_chat import SimpleChat
            chat_instance = SimpleChat(history_file=history_file)
            chat_instance.run()
        else:
            chat_instance = InteractiveChat(
                history_file=history_file,
                mcp_servers=list(mcp_server) if mcp_server else None,
                allowed_tools=list(tools) if tools else None,
                permission_mode=permission_mode,
                interactive_permissions=not no_interactive_permissions
            )
            anyio.run(chat_instance.run)
    except KeyboardInterrupt:
        console.print("\n[yellow]Chat session terminated[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        console.print("[yellow]Try running with --test-mode flag to test the interface[/yellow]")
        sys.exit(1)

@cli.command()
@click.argument('prompt')
@click.option('--tools', multiple=True, help='Specific tools to allow')
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
def query_command(prompt: str, tools: List[str], output_json: bool):
    """Send a single query to Claude"""
    async def run_query():
        options = ClaudeCodeOptions(
            allowed_tools=list(tools) if tools else None,
            permission_mode="default"
        )

        response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, str):
                response += message

        if output_json:
            import json
            console.print_json(json.dumps({"response": response}))
        else:
            console.print(response)

    try:
        anyio.run(run_query)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('symbol')
def analyze(symbol: str):
    """Quick stock analysis for a given symbol"""
    async def run_analysis():
        prompt = f"Provide a comprehensive analysis of {symbol} stock including current price, key metrics, recent news, and technical indicators."

        options = ClaudeCodeOptions(
            allowed_tools=[
                "mcp__stock-analyzer__analyze_stock",
                "mcp__company-research__get_company_profile",
                "mcp__news-analyzer__get_company_news"
            ],
            permission_mode="default"
        )

        console.print(f"[cyan]Analyzing {symbol}...[/cyan]\n")

        response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, str):
                response += message

        console.print(response)

    try:
        anyio.run(run_analysis)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('symbols', nargs=-1, required=True)
def compare(symbols: tuple):
    """Compare multiple stocks"""
    if len(symbols) < 2:
        console.print("[red]Please provide at least 2 symbols to compare[/red]")
        sys.exit(1)

    async def run_comparison():
        symbols_str = ", ".join(symbols)
        prompt = f"Compare these stocks: {symbols_str}. Include price performance, key metrics, and relative strengths/weaknesses."

        options = ClaudeCodeOptions(
            allowed_tools=[
                "mcp__stock-analyzer__compare_stocks",
                "mcp__company-research__compare_companies"
            ],
            permission_mode="default"
        )

        console.print(f"[cyan]Comparing {symbols_str}...[/cyan]\n")

        response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, str):
                response += message

        console.print(response)

    try:
        anyio.run(run_comparison)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
def list_tools():
    """List all available MCP tools"""
    tools = list_available_tools()
    console.print("[bold cyan]Available MCP Tools:[/bold cyan]\n")

    for category, tool_list in tools.items():
        console.print(f"[bold yellow]{category}:[/bold yellow]")
        for tool in tool_list:
            console.print(f"  • {tool}")
        console.print()

@cli.command()
def test_connection():
    """Test MCP server connections"""
    console.print("[cyan]Testing MCP server connections...[/cyan]\n")

    results = test_mcp_connection()

    for server, status in results.items():
        if status['connected']:
            console.print(f"✅ [green]{server}[/green]: Connected")
            if 'tools' in status:
                console.print(f"   Tools available: {status['tools']}")
        else:
            console.print(f"❌ [red]{server}[/red]: Failed")
            if 'error' in status:
                console.print(f"   Error: {status['error']}")

@cli.command()
@click.option('--sector', help='Filter by sector')
@click.option('--min-price', type=float, help='Minimum stock price')
@click.option('--max-price', type=float, help='Maximum stock price')
@click.option('--limit', type=int, default=10, help='Number of results')
def screen(sector: Optional[str], min_price: Optional[float],
          max_price: Optional[float], limit: int):
    """Screen stocks based on criteria"""
    async def run_screening():
        criteria = []
        if sector:
            criteria.append(f"sector: {sector}")
        if min_price:
            criteria.append(f"minimum price: ${min_price}")
        if max_price:
            criteria.append(f"maximum price: ${max_price}")

        criteria_str = ", ".join(criteria) if criteria else "all stocks"
        prompt = f"Screen stocks with these criteria: {criteria_str}. Return top {limit} results."

        options = ClaudeCodeOptions(
            allowed_tools=["mcp__stock-analyzer__screen_stocks"],
            permission_mode="default"
        )

        console.print(f"[cyan]Screening stocks: {criteria_str}...[/cyan]\n")

        response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, str):
                response += message

        console.print(response)

    try:
        anyio.run(run_screening)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('topic')
@click.option('--days', type=int, default=7, help='Number of days back')
def news(topic: str, days: int):
    """Get news and sentiment analysis for a topic or symbol"""
    async def run_news_analysis():
        prompt = f"Analyze news and sentiment for {topic} over the past {days} days. Include trending topics and key developments."

        options = ClaudeCodeOptions(
            allowed_tools=[
                "mcp__news-analyzer__search_news",
                "mcp__news-analyzer__analyze_sentiment",
                "mcp__news-analyzer__get_trending_topics"
            ],
            permission_mode="default"
        )

        console.print(f"[cyan]Analyzing news for {topic}...[/cyan]\n")

        response = ""
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, str):
                response += message

        console.print(response)

    try:
        anyio.run(run_news_analysis)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

def main():
    """Main entry point for CLI"""
    cli()

if __name__ == "__main__":
    main()