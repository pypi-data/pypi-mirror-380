"""
MCP Tools integration and management
"""

import os
import json
import subprocess
from typing import Dict, List, Any
from pathlib import Path

def list_available_tools() -> Dict[str, List[str]]:
    """
    List all available MCP tools organized by category

    Returns:
        Dictionary of tool categories with their respective tools
    """
    tools = {
        "Stock Analyzer": [
            "mcp__stock-analyzer__analyze_stock",
            "mcp__stock-analyzer__compare_stocks",
            "mcp__stock-analyzer__screen_stocks",
            "mcp__stock-analyzer__calculate_portfolio_value",
            "mcp__stock-analyzer__get_moving_averages",
            "mcp__stock-analyzer__find_trending_stocks",
        ],
        "Company Research": [
            "mcp__company-research__get_company_profile",
            "mcp__company-research__get_company_financials",
            "mcp__company-research__get_company_filings",
            "mcp__company-research__get_insider_trading",
            "mcp__company-research__get_analyst_ratings",
            "mcp__company-research__compare_companies",
            "mcp__company-research__search_companies",
        ],
        "News Analyzer": [
            "mcp__news-analyzer__search_news",
            "mcp__news-analyzer__get_trending_topics",
            "mcp__news-analyzer__analyze_sentiment",
            "mcp__news-analyzer__get_market_overview",
            "mcp__news-analyzer__summarize_news",
            "mcp__news-analyzer__get_company_news",
        ],
    }

    return tools

def get_mcp_servers() -> Dict[str, Any]:
    """
    Get configured MCP servers from .mcp.json files

    Returns:
        Dictionary of MCP server configurations
    """
    servers = {}

    # Try multiple locations in order of preference
    possible_locations = [
        '.mcp.json',  # Local development
        Path(__file__).parent / '.mcp.json',  # Package location
        Path.home() / '.navam' / '.mcp.json',  # User config
    ]

    for mcp_file in possible_locations:
        if Path(mcp_file).exists():
            try:
                with open(mcp_file, 'r') as f:
                    config = json.load(f)
                    if 'mcpServers' in config:
                        servers.update(config['mcpServers'])
                        break  # Use first found configuration
            except json.JSONDecodeError as e:
                print(f"Error parsing {mcp_file}: {e}")

    return servers

def test_mcp_connection() -> Dict[str, Dict[str, Any]]:
    """
    Test connections to configured MCP servers

    Returns:
        Dictionary with connection status for each server
    """
    servers = get_mcp_servers()
    results = {}

    for server_name, server_config in servers.items():
        try:
            # Try to test the server connection
            # This is a simplified test - in production you'd want more robust testing
            command = server_config.get('command', '')
            args = server_config.get('args', [])

            if command and args:
                # Test if the server can be launched
                test_cmd = [command] + args + ['--help']
                result = subprocess.run(
                    test_cmd,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=server_config.get('workingDir', '.')
                )

                results[server_name] = {
                    'connected': result.returncode == 0,
                    'tools': _count_server_tools(server_name)
                }
            else:
                results[server_name] = {
                    'connected': False,
                    'error': 'Invalid server configuration'
                }

        except subprocess.TimeoutExpired:
            results[server_name] = {
                'connected': False,
                'error': 'Connection timeout'
            }
        except Exception as e:
            results[server_name] = {
                'connected': False,
                'error': str(e)
            }

    return results

def _count_server_tools(server_name: str) -> int:
    """Count the number of tools available for a given server"""
    tools = list_available_tools()

    # Map server names to tool categories
    server_tool_map = {
        'stock-analyzer': 'Stock Analyzer',
        'company-research': 'Company Research',
        'news-analyzer': 'News Analyzer',
    }

    category = server_tool_map.get(server_name, '')
    return len(tools.get(category, []))

def get_tool_description(tool_name: str) -> str:
    """
    Get description for a specific tool

    Args:
        tool_name: Full tool name (e.g., "mcp__stock-analyzer__analyze_stock")

    Returns:
        Tool description
    """
    descriptions = {
        # Stock Analyzer
        "mcp__stock-analyzer__analyze_stock": "Perform comprehensive stock analysis",
        "mcp__stock-analyzer__compare_stocks": "Compare multiple stocks side by side",
        "mcp__stock-analyzer__screen_stocks": "Screen stocks based on criteria",
        "mcp__stock-analyzer__calculate_portfolio_value": "Calculate portfolio value and analysis",
        "mcp__stock-analyzer__get_moving_averages": "Calculate moving averages for specific periods",
        "mcp__stock-analyzer__find_trending_stocks": "Find stocks with strong trends",

        # Company Research
        "mcp__company-research__get_company_profile": "Get detailed company profile",
        "mcp__company-research__get_company_financials": "Get company financial statements",
        "mcp__company-research__get_company_filings": "Get recent SEC filings",
        "mcp__company-research__get_insider_trading": "Get insider trading activity",
        "mcp__company-research__get_analyst_ratings": "Get analyst ratings and price targets",
        "mcp__company-research__compare_companies": "Compare multiple companies",
        "mcp__company-research__search_companies": "Search for companies by criteria",

        # News Analyzer
        "mcp__news-analyzer__search_news": "Search for news articles",
        "mcp__news-analyzer__get_trending_topics": "Get trending news topics",
        "mcp__news-analyzer__analyze_sentiment": "Perform sentiment analysis on news",
        "mcp__news-analyzer__get_market_overview": "Get market news overview",
        "mcp__news-analyzer__summarize_news": "Generate news summary",
        "mcp__news-analyzer__get_company_news": "Get company-specific news",
    }

    return descriptions.get(tool_name, "No description available")

def create_custom_tool(tool_function, tool_name: str, description: str):
    """
    Create a custom tool that can be used with Claude Code SDK

    Args:
        tool_function: The function to wrap as a tool
        tool_name: Name for the tool
        description: Tool description

    Returns:
        Wrapped tool function
    """
    # This would integrate with Claude Code SDK's custom tool API
    # Implementation depends on the exact SDK interface
    pass

def load_agent_commands() -> List[Dict[str, Any]]:
    """
    Load custom agent commands from multiple possible locations

    Returns:
        List of available agent commands
    """
    commands = []

    # Try multiple locations in order of preference
    possible_locations = [
        Path('.claude/commands/invest'),  # Local development
        Path(__file__).parent / 'commands' / 'invest',  # Package location
        Path.home() / '.navam' / 'commands' / 'invest',  # User config
    ]

    for commands_dir in possible_locations:
        if commands_dir.exists():
            # Look for both .yaml and .md files
            for pattern in ['*.yaml', '*.yml', '*.md']:
                for command_file in commands_dir.glob(pattern):
                    try:
                        if command_file.suffix in ['.yaml', '.yml']:
                            import yaml
                            with open(command_file, 'r') as f:
                                command_config = yaml.safe_load(f)
                        else:  # .md files
                            with open(command_file, 'r') as f:
                                command_config = {
                                    'title': command_file.stem.replace('-', ' ').title(),
                                    'description': f.read()
                                }

                        commands.append({
                            'name': command_file.stem,
                            'config': command_config
                        })
                    except Exception as e:
                        print(f"Error loading command {command_file}: {e}")

            if commands:  # If we found commands, stop looking in other locations
                break

    return commands

def execute_agent_command(command_name: str, **kwargs) -> Any:
    """
    Execute a custom agent command

    Args:
        command_name: Name of the command to execute
        **kwargs: Arguments to pass to the command

    Returns:
        Command execution result
    """
    commands = load_agent_commands()

    for command in commands:
        if command['name'] == command_name:
            # Execute the command based on its configuration
            # This would integrate with the agent system
            pass

    raise ValueError(f"Command '{command_name}' not found")