# Navam Package

Navam is an interactive command-line tool that integrates Claude Code SDK with MCP (Model Context Protocol) tools to provide comprehensive stock market analysis capabilities.

## Features

- **Interactive Chat**: Full-featured chat interface powered by Claude Code SDK
- **MCP Tools Integration**: Access to stock analysis, company research, and news analysis tools
- **Command-Line Interface**: Quick commands for common analysis tasks
- **Agent Support**: Integration with custom investment workflow agents
- **Real-time Data**: Access to live market data through MCP servers

## Installation

The package is managed by `uv` and can be installed in development mode:

```bash
uv sync
```

## Usage

### Interactive Chat

Start an interactive chat session:

```bash
navam chat
```

Chat Commands:
- `/help` - Show available commands
- `/tools` - List available MCP tools
- `/servers` - Show loaded MCP servers
- `/clear` - Clear the screen
- `/exit` - Exit the chat

### Quick Commands

#### Analyze a Stock
```bash
navam analyze AAPL
```

#### Compare Stocks
```bash
navam compare MSFT GOOGL AMZN
```

#### Screen Stocks
```bash
navam screen --sector technology --min-price 100 --max-price 500
```

#### Get News and Sentiment
```bash
navam news TSLA --days 7
```

#### Send Single Query
```bash
navam query "What are the top trending tech stocks today?"
```

### Testing Tools

#### List Available Tools
```bash
navam list-tools
```

#### Test MCP Connections
```bash
navam test-connection
```

## MCP Tools Available

### Stock Analyzer
- `analyze_stock` - Comprehensive stock analysis
- `compare_stocks` - Compare multiple stocks
- `screen_stocks` - Screen by criteria
- `calculate_portfolio_value` - Portfolio analysis
- `get_moving_averages` - Technical indicators
- `find_trending_stocks` - Trending stock discovery

### Company Research
- `get_company_profile` - Company information
- `get_company_financials` - Financial statements
- `get_company_filings` - SEC filings
- `get_insider_trading` - Insider activity
- `get_analyst_ratings` - Analyst recommendations
- `compare_companies` - Company comparisons
- `search_companies` - Company search

### News Analyzer
- `search_news` - News search
- `get_trending_topics` - Trending topics
- `analyze_sentiment` - Sentiment analysis
- `get_market_overview` - Market overview
- `summarize_news` - News summaries
- `get_company_news` - Company-specific news

## Architecture

The package consists of:

1. **chat.py**: Interactive chat interface using Claude Code SDK
2. **cli.py**: Command-line interface using Click
3. **tools.py**: MCP tools integration and management
4. **__main__.py**: Package entry point for module execution

## Configuration

MCP servers are configured via `.mcp.json` files in the project root. The package automatically loads these configurations to access the available tools.

## Development

Run the package in development mode:

```bash
# As a module
uv run python -m navam

# Using the CLI
uv run navam --help

# Interactive Python
uv run python
>>> import navam
>>> navam.__version__
'1.0.0'
```

## Requirements

- Python 3.11+
- Claude Code SDK
- MCP CLI tools
- Configured MCP servers for stock, company, and news data