# 🤖 Navam - Personal AI Agents for Life

[![PyPI](https://img.shields.io/pypi/v/navam.svg)](https://pypi.org/project/navam/)
[![Python 3.11+](https://img.shields.io/pypi/pyversions/navam.svg)](https://www.python.org/downloads/)
[![Downloads](https://img.shields.io/pypi/dm/navam.svg)](https://pypi.org/project/navam/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![Grade A-](https://img.shields.io/badge/Stock%20MCP-Grade%20A--90%25-brightgreen.svg)]()
[![Grade C+](https://img.shields.io/badge/Company%20MCP-Grade%20C%2B%2075%25-orange.svg)]()
[![Grade B](https://img.shields.io/badge/News%20MCP-Grade%20B%2080%25-green.svg)]()

> **Personal AI agents for investing, shopping, health, and learning - starting with comprehensive financial intelligence.**

Navam provides personal AI agents to assist with key areas of your life. Currently focused on investing with a complete financial analysis ecosystem featuring an interactive AI chat interface, 19 specialized investment agents, 3 MCP servers, and custom investment workflows. Future versions will expand to shopping, health, and learning domains.

## 📋 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Quick Start Guide](#-quick-start-guide)
- [📊 Available Capabilities](#-available-capabilities)
- [🔧 Claude Desktop Integration](#-claude-desktop-integration)
- [💡 Example Use Cases](#-example-use-cases)
- [🏗️ Architecture](#-architecture)
- [🧪 Development & Testing](#-development--testing)
- [🔒 Security & Compliance](#-security--compliance)
- [📊 Performance & Quality](#-performance--quality)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🆘 Support](#-support)

## 🚀 Features

### 💬 Interactive AI Chat Interface
- **Conversational Analysis** - Natural language interaction with Claude Code SDK
- **19 Specialized AI Agents** - Each focused on specific aspects of financial analysis
- **Custom Investment Commands** - Pre-built workflows for common investment tasks
- **Multi-Agent Parallel Execution** - Run multiple analyses simultaneously
- **Rich Progress Indicators** - Real-time status updates during analysis
- **Persistent Permissions System** - Secure handling of sensitive operations

### 📊 Stock Analysis MCP Server (Powered by FastMCP)
- **Real-time Market Data** - Live quotes, volume, and price movements
- **Technical Analysis** - RSI, MACD, moving averages, and trend indicators
- **Historical Data** - Customizable time periods and data granularity
- **Portfolio Management** - Value tracking, returns calculation, and allocation analysis
- **Stock Screening** - Filter by sector, price range, volume, and fundamentals
- **Market Overview** - Major indices and market-wide performance metrics

### 🏢 Company Research MCP Server (Powered by FastMCP)
- **Company Profiles** - Comprehensive business information and metrics
- **Financial Statements** - Income statements, balance sheets, cash flow analysis
- **SEC Filings** - Access to 10-K, 10-Q, 8-K, and other regulatory documents
- **Analyst Coverage** - Ratings, price targets, and consensus recommendations
- **Insider Trading** - Executive transactions and ownership changes
- **Peer Comparisons** - Industry benchmarking and competitive analysis

### 📰 News Analysis MCP Server (Powered by FastMCP)
- **News Search** - Multi-source financial news aggregation and filtering
- **Sentiment Analysis** - AI-powered sentiment scoring and trend analysis
- **Market Overview** - Real-time market sentiment and breaking news
- **Trending Topics** - Identification of market themes and momentum
- **Company News** - Symbol-specific news feeds with relevance scoring
- **News Summarization** - Automated insights and key developments extraction

## 🛠️ Quick Start

### Prerequisites
- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) (recommended) or pip for package management

### Installation

**Option 1: Install from PyPI (Recommended)**
```bash
pip install navam
```

This includes all MCP servers, FastMCP framework, and the interactive chat interface.

**Option 2: Install with Development Tools**
```bash
# Install with development tools (pytest, black, mypy, etc.)
pip install navam[dev]

# Install everything (currently same as [dev])
pip install navam[all]
```

**Option 3: Local Development/Testing**
```bash
# Clone the repository
git clone https://github.com/manavsehgal/navam.git
cd navam

# Install with uv (recommended for development)
uv sync

# Or install in editable mode with pip
pip install -e .
```

> **Note**: When developing with `uv`, use `uv run navam` to execute commands. When installed via pip in an activated virtual environment, you can use `navam` directly.

### Local Testing & Development

**Quick Test Installation:**
```bash
# Test if package installs correctly
uv pip install -e .

# Verify command is available (use uv run for development)
uv run navam --help

# Test basic functionality
uv run navam test-connection
```

**Building the Package:**
```bash
# Install build tools
uv add build twine

# Build distribution packages
uv run python -m build

# Check build output
ls dist/
# Should show: navam-1.0.0-py3-none-any.whl and navam-1.0.0.tar.gz
```

**Testing Package Installation:**
```bash
# Create a clean test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from local build
pip install dist/navam-1.0.0-py3-none-any.whl

# Test the installation
navam --help
navam test-connection

# Cleanup
deactivate
rm -rf test_env
```

### Environment Setup

Create a `.env` file for API keys:

```bash
# Required for chat interface
ANTHROPIC_API_KEY=your_anthropic_key

# Optional API keys for additional data sources
ALPHA_VANTAGE_API_KEY=your_key_here
IEX_CLOUD_API_KEY=your_key_here
POLYGON_API_KEY=your_key_here
MARKETAUX_API_KEY=your_key_here
NEWSAPI_KEY=your_key_here
FINNHUB_API_KEY=your_key_here
```

## 🚀 Quick Start Guide

### 1. Basic Installation & Setup

```bash
# Install StockAI
pip install navam

# Set up your environment
export ANTHROPIC_API_KEY="your_anthropic_key_here"

# Test the installation
navam --help
navam test-connection
```

### 2. Using the Interactive Chat

Start the interactive AI chat interface:

```bash
# Interactive chat with AI agents and investment commands
navam chat

# Or with uv (for development)
uv run navam chat
```

### 3. Try These Examples

**Investment Commands in Chat:**
```bash
# In the chat interface:
/invest:research-stock NVDA
/invest:review-portfolio
/invest:screen-opportunities
/invest:plan-goals
/invest:monitor-holdings
/invest:optimize-taxes
/invest:execute-rebalance
```

**CLI Commands:**
```bash
# Analyze a single stock
navam analyze AAPL

# Compare multiple stocks
navam compare AAPL MSFT GOOGL

# Screen for opportunities
navam screen --sector technology --min-price 100

# Get latest news
navam news "Federal Reserve"
```

## 📖 API Usage

### Python API

```python
from navam import StockAnalyzer, CompanyResearch, NewsAnalyzer

# Initialize analyzers
stock = StockAnalyzer()
company = CompanyResearch()
news = NewsAnalyzer()

# Analyze a stock
analysis = await stock.analyze_stock("AAPL")
print(f"Stock: {analysis.symbol}, Price: ${analysis.price}")

# Get company profile
profile = await company.get_company_profile("AAPL")
print(f"Company: {profile.name}, Sector: {profile.sector}")

# Search news
news_feed = await news.search_news("Apple earnings", days_back=7)
for article in news_feed.articles:
    print(f"Title: {article.title}")
    print(f"Sentiment: {article.sentiment}")
```

### MCP Integration

```python
# Use with Claude Desktop or other MCP clients
# Add to your .mcp.json configuration:
{
  "mcpServers": {
    "navam": {
      "command": "navam",
      "args": ["mcp-server", "--transport", "stdio"]
    }
  }
}
```

### Running the MCP Servers

**Stock Analysis Server:**
```bash
# For Claude Desktop (stdio transport)
uv run python -m src.stock_mcp.server stdio

# For web/HTTP clients
uv run python -m src.stock_mcp.server streamable-http --port 8080
```

**Company Research Server:**
```bash
# For Claude Desktop (stdio transport)
uv run python -m src.company_mcp.server stdio

# For web/HTTP clients
uv run python -m src.company_mcp.server streamable-http --port 8080
```

**News Analysis Server:**
```bash
# For Claude Desktop (stdio transport)
uv run python -m src.news_mcp.server stdio

# For web/HTTP clients
uv run python -m src.news_mcp.server streamable-http --port 8080
```

### Testing with MCP Inspector

```bash
# Test Stock Analysis Server
uv run mcp dev src/stock_mcp/server.py

# Test Company Research Server
uv run mcp dev src/company_mcp/server.py

# Test News Analysis Server
uv run mcp dev src/news_mcp/server.py
```

## 🔧 Claude Desktop Integration

Add all three servers to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "stock-analyzer": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.stock_mcp.server", "stdio"],
      "workingDir": "/absolute/path/to/navam-e1"
    },
    "company-research": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.company_mcp.server", "stdio"],
      "workingDir": "/absolute/path/to/navam-e1"
    },
    "news-analyzer": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.news_mcp.server", "stdio"],
      "workingDir": "/absolute/path/to/navam-e1"
    }
  }
}
```

**💡 Pro Tip:** Use absolute paths for `workingDir` to ensure reliable server startup.

## 📚 Available Capabilities

### Stock Analysis Tools
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `analyze_stock` | Comprehensive stock analysis with technical and fundamental data | Analyze AAPL with current metrics |
| `compare_stocks` | Side-by-side comparison of multiple stocks | Compare AAPL vs MSFT vs GOOGL |
| `screen_stocks` | Filter stocks by criteria (sector, price, volume) | Find tech stocks under $200 |
| `calculate_portfolio_value` | Portfolio analysis with returns and allocation | Calculate portfolio with holdings |
| `get_moving_averages` | Technical indicators for trend analysis | Get 20/50/200 day MAs for TSLA |
| `find_trending_stocks` | Identify stocks with strong momentum | Find top trending stocks |

### Company Research Tools
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `get_company_profile` | Detailed company information and metrics | Get Apple's business profile |
| `get_company_financials` | Financial statements and key ratios | Analyze Microsoft's quarterly results |
| `get_company_filings` | SEC documents and regulatory filings | Review Tesla's latest 10-K filing |
| `get_analyst_ratings` | Professional analyst coverage | Check analyst sentiment on NVDA |
| `get_insider_trading` | Executive and insider transactions | Track insider activity at Meta |
| `compare_companies` | Multi-company competitive analysis | Compare Big Tech companies |

### News Analysis Tools
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `search_news` | Multi-source news search with filtering | Search for Apple news from last 7 days |
| `get_trending_topics` | Identify trending market themes | Get top trending topics for 24h |
| `analyze_sentiment` | AI-powered sentiment analysis | Analyze Tesla sentiment over 7 days |
| `get_market_overview` | Current market sentiment snapshot | Get today's market overview |
| `summarize_news` | Automated news summarization | Summarize Fed policy news |
| `get_company_news` | Symbol-specific news feeds | Get AAPL company news |

### Dynamic Resources
- **Stock Resources**: `stock://{symbol}/quote`, `stock://{symbol}/history/{period}`
- **Company Resources**: `company://{symbol}/profile`, `company://{symbol}/financials`
- **News Resources**: `news://search/{query}`, `news://trending/{time_period}`, `news://company/{symbol}`
- **Market Resources**: `market://overview`, `market://indices`

### Analysis Prompts
- **Stock Research** - Comprehensive equity analysis framework
- **Portfolio Review** - Holdings evaluation and optimization
- **Market Analysis** - Sector and market trend assessment
- **Earnings Analysis** - Financial results evaluation
- **Risk Assessment** - Downside and volatility analysis
- **Technical Setup** - Chart pattern and indicator analysis
- **News Analysis** - Multi-source news research and sentiment
- **Crisis Monitor** - Real-time crisis communication tracking

## 💡 Example Use Cases

### Portfolio Analysis
```
Analyze my portfolio performance:
- AAPL: 100 shares at $150 cost basis
- MSFT: 50 shares at $300 cost basis
- GOOGL: 25 shares at $2800 cost basis
```

### Company Research
```
Research Apple (AAPL) for investment:
- Get company profile and business overview
- Analyze latest financial statements
- Review analyst ratings and price targets
- Check recent news and insider activity
```

### Technical Analysis
```
Perform technical analysis on Tesla (TSLA):
- Calculate RSI, MACD, and moving averages
- Identify trend direction and momentum
- Assess support and resistance levels
```

### Market Screening
```
Find investment opportunities:
- Technology stocks under $200
- Companies with P/E ratio below 25
- Strong trading volume (>1M shares/day)
- Positive analyst sentiment
```

### News & Sentiment Analysis
```
Monitor market developments:
- Search for Federal Reserve policy news
- Analyze Tesla sentiment over past week
- Get trending topics for market themes
- Track Apple-specific news with sentiment
```

## 🏗️ Architecture

### Project Structure
```
navam-e1/
├── src/
│   ├── stock_mcp/              # Stock Analysis MCP Server (Grade A-)
│   │   ├── server.py           # FastMCP server implementation
│   │   ├── models.py           # Pydantic data models
│   │   ├── api_clients.py      # Finance API integrations
│   │   ├── cache.py            # Response caching layer
│   │   ├── resources.py        # Dynamic MCP resources
│   │   └── prompts.py          # Analysis prompt templates
│   ├── company_mcp/            # Company Research MCP Server (Grade C+)
│   │   ├── server.py           # FastMCP server implementation
│   │   ├── models.py           # Company data models
│   │   ├── api_clients.py      # Company data APIs
│   │   └── cache.py            # Caching implementation
│   └── news_mcp/               # News Analysis MCP Server (Grade B)
│       ├── server.py           # FastMCP server implementation
│       ├── models.py           # News data models
│       ├── api_clients.py      # News API integrations
│       └── cache.py            # News caching layer
├── tests/                      # Comprehensive test suite
├── eval/                       # MCP server evaluation frameworks
├── artifacts/                  # Documentation and references
├── .mcp.json                   # MCP server configuration
└── pyproject.toml             # Python project configuration
```

### Data Sources
- **Yahoo Finance** (primary) - Free, comprehensive market data
- **Alpha Vantage** (optional) - Enhanced technical indicators and news
- **IEX Cloud** (optional) - Real-time quotes and fundamentals
- **Polygon.io** (optional) - Professional-grade market data
- **MarketAux** (optional) - Financial news aggregation
- **NewsAPI** (optional) - Global news coverage
- **Finnhub** (optional) - Real-time financial news
- **SEC EDGAR** - Official company filings and documents

## 🧪 Development & Testing

### Quick Functionality Tests

**Test Chat Interface:**
```bash
# Start interactive chat (requires ANTHROPIC_API_KEY)
uv run navam chat

# Test specific commands in chat:
# /invest:research-stock AAPL
# /commands
# /help
```

**Test CLI Commands:**
```bash
# Test stock analysis
uv run navam analyze AAPL

# Test stock comparison
uv run navam compare AAPL MSFT GOOGL

# Test news analysis
uv run navam news Tesla

# Test stock screening
uv run navam screen --sector technology --min-price 100 --max-price 300

# List available MCP tools
uv run navam list-tools

# Test MCP server connections
uv run navam test-connection
```

**Test MCP Servers Individually:**
```bash
# Test stock MCP server
echo '{"symbol": "AAPL"}' | uv run python -m src.stock_mcp.server stdio

# Test company MCP server
echo '{"symbol": "AAPL"}' | uv run python -m src.company_mcp.server stdio

# Test news MCP server
echo '{"query": "Apple"}' | uv run python -m src.news_mcp.server stdio
```

### Development Testing

**Running Tests:**
```bash
# Run all tests (when test suite exists)
uv run python -m pytest tests/

# Run with coverage
uv run python -m pytest tests/ --cov=src

# Run specific test file
uv run python -m pytest tests/test_stock_tools.py -v
```

**Code Quality:**
```bash
# Format code
uv run python -m black .

# Type checking
uv run python -m mypy .

# Linting
uv run python -m ruff check .
```

**MCP Server Development:**
```bash
# Launch development inspector
uv run mcp dev src/stock_mcp/server.py
uv run mcp dev src/company_mcp/server.py
uv run mcp dev src/news_mcp/server.py

# Install servers locally for testing
uv run mcp install src/stock_mcp/server.py
uv run mcp install src/company_mcp/server.py
uv run mcp install src/news_mcp/server.py

# List installed MCP servers
uv run mcp list
```

## 🔒 Security & Compliance

- **Read-only Operations** - No trading or account modification capabilities
- **API Key Security** - Environment variable storage with .env support
- **Rate Limiting** - Respectful API usage with intelligent caching
- **Data Privacy** - No personal financial data storage or transmission
- **Regulatory Compliance** - Adheres to finance API terms of service

## 📊 Performance & Quality

### Server Performance
| Server | Grade | Response Time | Data Quality | Production Ready |
|--------|-------|---------------|--------------|------------------|
| Stock MCP | **A- (90%)** | 2-4 seconds | Excellent | ✅ Yes |
| Company MCP | **C+ (75%)** | 2-4 seconds | Good | ✅ Yes |
| News MCP | **B (80%)** | <2 seconds | Very Good | ✅ Yes |

### Technical Metrics
- **Response Times** - 2-4 seconds for most analysis requests
- **Data Freshness** - Real-time quotes with intelligent caching
- **Reliability** - Robust error handling and fallback mechanisms
- **Scalability** - Async/await patterns for concurrent operations

## 🤝 Contributing

We welcome contributions to StockAI! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/manavsehgal/navam.git
cd navam

# Install in development mode with all dependencies
pip install -e .[dev,all]

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Format and lint code
black .
ruff check .
mypy .
```

### Development Guidelines

- **Code Style**: We use `black` for formatting and `ruff` for linting
- **Type Hints**: All functions must include type hints
- **Testing**: Write tests for new features using `pytest`
- **Documentation**: Update README and docstrings for new features
- **Commits**: Use conventional commit messages

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests and documentation
4. Run the test suite: `pytest`
5. Submit a pull request with a clear description

### Reporting Issues

Please use [GitHub Issues](https://github.com/manavsehgal/navam/issues) to report bugs or request features. Include:

- Python version and operating system
- Error messages and stack traces
- Steps to reproduce the issue
- Expected vs actual behavior

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📈 What's New

### Version 1.0.0
- ✨ **Interactive AI Chat Interface** with 19 specialized financial agents
- 🏗️ **Three Production-Ready MCP Servers** for stock, company, and news analysis
- 📊 **Comprehensive CLI Tools** for terminal-based analysis
- 🔄 **Real-time Data Integration** with multiple financial APIs
- 🎯 **Custom Investment Commands** for common workflows
- 🛡️ **Enterprise-Grade Security** with read-only operations
- 📚 **Extensive Documentation** and examples

[View full changelog →](https://github.com/manavsehgal/navam/blob/main/CHANGELOG.md)

## 🆘 Support & Community

### Getting Help

- 📖 **Documentation**: Check the `artifacts/` directory for comprehensive guides
- 🐛 **Bug Reports**: Report issues via [GitHub Issues](https://github.com/manavsehgal/navam/issues)
- 💬 **Discussions**: Join conversations in [GitHub Discussions](https://github.com/manavsehgal/navam/discussions)
- 📧 **Contact**: Reach out to [manav@sehgal.ai](mailto:manav@sehgal.ai)

### Resources

- 🌐 **Homepage**: [https://navam.readthedocs.io](https://navam.readthedocs.io)
- 📦 **PyPI Package**: [https://pypi.org/project/navam/](https://pypi.org/project/navam/)
- 📋 **GitHub Repository**: [https://github.com/manavsehgal/navam](https://github.com/manavsehgal/navam)

## ⭐ Acknowledgments

StockAI stands on the shoulders of amazing open-source projects:

- 🔗 **[MCP](https://modelcontextprotocol.io/)** - Model Context Protocol framework
- ⚡ **[FastMCP](https://github.com/modelcontextprotocol/python-sdk)** - High-performance MCP framework
- 🤖 **[Claude Code SDK](https://claude.com/claude-code)** - AI agent framework
- 📊 **Data Providers**: Yahoo Finance, Alpha Vantage, IEX Cloud, Polygon.io, and others

Special thanks to the financial data providers who make this analysis possible while maintaining free tiers for developers.

---

<div align="center">

### 🚀 Ready to supercharge your financial analysis?

**Install StockAI and start making data-driven investment decisions today!**

```bash
pip install navam
```

[![Star on GitHub](https://img.shields.io/github/stars/manavsehgal/navam?style=social)](https://github.com/manavsehgal/navam)
[![Follow on Twitter](https://img.shields.io/twitter/follow/manavsehgal?style=social)](https://twitter.com/manavsehgal)

*Built with ❤️ for the financial community*

</div>