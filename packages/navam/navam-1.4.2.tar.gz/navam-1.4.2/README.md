# 🤖 Navam - Personal AI Agents Platform

<div align="center">

[![PyPI Version](https://img.shields.io/pypi/v/navam?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/navam/)
[![Python](https://img.shields.io/pypi/pyversions/navam?logo=python&logoColor=white)](https://pypi.org/project/navam/)
[![Downloads](https://img.shields.io/pypi/dm/navam?color=green&logo=python)](https://pypi.org/project/navam/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-brightgreen?logo=anthropic)](https://modelcontextprotocol.io/)

**Personal AI agents for investing, shopping, health, and learning**

[🚀 Quick Start](#-quick-start) •
[📖 Documentation](#-features) •
[💬 Chat Interface](#-interactive-chat) •
[🔧 Integration](#-integrations) •
[🤝 Contributing](#-contributing)

</div>

---

## 🎯 What is Navam?

Navam is a **comprehensive AI agents platform** that brings specialized artificial intelligence to key areas of your life. Starting with **financial intelligence**, Navam provides:

- 🤖 **Interactive AI Chat Interface** powered by Claude Code SDK
- 📊 **18 Specialized Financial Agents** for investment research and analysis
- ⚡ **3 High-Performance MCP Servers** for real-time data
- 🎯 **Custom Investment Workflows** with slash commands
- 🔌 **Claude Desktop Integration** for seamless experience
- 💬 **Advanced Chat Features** - Real-time thinking tokens, tool tracking, multi-agent coordination

> **Currently focused on investing** with plans to expand into shopping, health, and learning domains.

## ✨ Features

### 💬 Interactive Chat
- **Natural Language Financial Analysis** - Ask questions, get intelligent insights
- **Real-time Progress Indicators** - See thinking tokens, tool execution, and agent activity
- **Multi-Agent Coordination** - Multiple AI agents working in parallel with progress tracking
- **Persistent Chat History** - Context-aware conversations with turn tracking
- **Custom Slash Commands** - Pre-built investment workflows
- **Built-in Commands** - `/agents`, `/api`, `/tools`, `/help`, and more

### 📊 Financial Intelligence
- **Live Market Data** - Real-time quotes, volume, price movements
- **Technical Analysis** - RSI, MACD, moving averages, trend indicators
- **Company Research** - Fundamentals, SEC filings, analyst ratings
- **News & Sentiment** - Multi-source aggregation with AI sentiment analysis
- **Portfolio Management** - Value tracking, allocation analysis, performance metrics

### 🤖 AI Agents
- **18 Specialized Financial Agents** - Expert AI for every investment scenario
- **Strategy & Planning** - Atlas (investment strategy), Compass (goal planning), Macro Lens (market analysis)
- **Research & Analysis** - Quill (equity research), Earnings Whisperer, News Sentry, Screen Forge
- **Portfolio Management** - Ledger (performance), Quant Optimizer, Risk Shield, Rebalance Bot
- **Trading & Execution** - Trader Jane, Compliance Sentinel
- **Tax & Treasury** - Tax Scout, Cash Treasury Steward
- **Advanced Strategies** - Hedge Smith (options), Factor Scout
- **Knowledge Management** - Notionist Librarian

Use `/agents` command in chat to see all agents with detailed descriptions!

### 🔧 Integration Ready
- **Claude Desktop Compatible** - Works seamlessly with Claude Desktop
- **MCP Protocol** - Industry-standard Model Context Protocol
- **API-First Design** - Easy integration with other tools
- **Standalone or Integrated** - Use independently or with Claude Desktop

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install navam

# Verify installation
navam --version
```

### Setup

```bash
# Required: Set your Anthropic API key
export ANTHROPIC_API_KEY="your_anthropic_api_key"

# Optional: Add API keys for enhanced data (see Configuration section)
export ALPHA_VANTAGE_KEY="your_alpha_vantage_key"
```

### Start Chatting

```bash
# Launch interactive AI chat
navam chat

# Once in chat, try these commands:
/agents      # See all 18 specialized AI agents
/api         # Check which APIs are active
/help        # Get complete command reference

# Or use direct CLI commands
navam analyze AAPL
navam compare AAPL MSFT GOOGL
navam news "Federal Reserve"
```

**First time using Navam?** Start with `navam chat` and type `/help` to see all features!

## 💡 Usage Examples

### Interactive Chat Commands
```bash
# Launch interactive chat
navam chat

# Built-in commands (use within chat):
/agents      # List all 18 specialized AI agents
/api         # Show API status and configuration
/help        # Show all available commands
/tools       # List available MCP tools
/commands    # List all slash commands

# Investment workflow commands:
/invest:research-stock NVDA
/invest:review-portfolio
/invest:screen-opportunities
/invest:plan-goals
/invest:optimize-taxes
```

### CLI Commands
```bash
# Stock analysis
navam analyze AAPL

# Multi-stock comparison
navam compare AAPL MSFT GOOGL

# Market screening
navam screen --sector technology --min-price 100

# News analysis
navam news "Tesla earnings"

# Check API status
navam chat
# Then use: /api
```

### Python API
```python
from navam import StockAnalyzer, CompanyResearch

# Analyze stocks programmatically
stock = StockAnalyzer()
analysis = await stock.analyze_stock("AAPL")
print(f"Price: ${analysis.price}")

# Research companies
company = CompanyResearch()
profile = await company.get_company_profile("AAPL")
print(f"Sector: {profile.sector}")
```

## ⚙️ Configuration

### API Key Setup

Navam uses a **tiered API approach** - basic functionality works with free APIs, premium features unlock with paid keys:

#### Required
```bash
export ANTHROPIC_API_KEY="your_anthropic_key"  # For AI chat functionality
```

#### Optional (Enhanced Features)
```bash
# Financial data enhancement
export ALPHA_VANTAGE_KEY="your_key"     # Company data, technical indicators
export POLYGON_API_KEY="your_key"       # Professional market data
export MARKETAUX_API_KEY="your_key"     # Financial news aggregation
export NEWSAPI_KEY="your_key"           # Global news coverage
export FINNHUB_API_KEY="your_key"       # Real-time financial news
```

#### Configuration Methods

**Method 1: Environment Variables** (Production)
```bash
echo 'export ANTHROPIC_API_KEY="your_key"' >> ~/.bashrc
source ~/.bashrc
```

**Method 2: .env File** (Development)
```bash
# Create .env file in project directory
echo "ANTHROPIC_API_KEY=your_key" > .env
echo "ALPHA_VANTAGE_KEY=your_key" >> .env
```

**Method 3: Session Variables** (Temporary)
```bash
export ANTHROPIC_API_KEY="your_key"
navam chat
```

### Check Configuration Status
```bash
navam chat

# Inside chat, use these commands:
/api         # Shows detailed API status - which are active, which need keys
/agents      # List all 18 specialized AI agents available
/tools       # Show all available MCP tools
/help        # Complete command reference
```

## 🔌 Integrations

### Claude Desktop Integration

Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "navam-stock": {
      "command": "python",
      "args": ["-m", "stock_mcp.server", "stdio"],
      "env": {
        "ALPHA_VANTAGE_KEY": "your_key"
      }
    },
    "navam-company": {
      "command": "python",
      "args": ["-m", "company_mcp.server", "stdio"]
    },
    "navam-news": {
      "command": "python",
      "args": ["-m", "news_mcp.server", "stdio"]
    }
  }
}
```

### Standalone MCP Servers

```bash
# Run individual MCP servers
python -m stock_mcp.server stdio
python -m company_mcp.server streamable-http --port 8080
python -m news_mcp.server stdio
```

## 🏗️ Architecture

### Component Overview
```
📦 Navam Platform
├── 💬 Interactive Chat (navam chat)
│   ├── Real-time thinking token display
│   ├── Live tool execution tracking
│   ├── Multi-agent parallel execution monitoring
│   └── Built-in commands (/agents, /api, /tools, /help)
├── 📊 Stock Analysis MCP Server (Grade A- 90%)
├── 🏢 Company Research MCP Server (Grade C+ 75%)
├── 📰 News Analysis MCP Server (Grade B 80%)
├── 🤖 18 Specialized AI Agents
│   ├── Strategy & Planning (3 agents)
│   ├── Research & Analysis (4 agents)
│   ├── Portfolio Management (4 agents)
│   ├── Trading & Execution (2 agents)
│   ├── Tax & Treasury (2 agents)
│   ├── Advanced Strategies (2 agents)
│   └── Knowledge Management (1 agent)
├── ⚡ Custom Investment Commands
└── 🔧 Claude Desktop Integration
```

### Data Sources
| Source | Type | Features |
|--------|------|----------|
| **Yahoo Finance** | Free | Stock quotes, company data, news |
| **SEC EDGAR** | Free | Official company filings |
| **Alpha Vantage** | Premium | Technical indicators, fundamentals |
| **Polygon.io** | Premium | Real-time professional data |
| **MarketAux** | Premium | Curated financial news |
| **NewsAPI** | Premium | Global news coverage |
| **Finnhub** | Premium | Real-time market news |

## 📊 Performance

| MCP Server | Grade | Response Time | Production Ready |
|------------|-------|---------------|------------------|
| Stock Analysis | **A- (90%)** | 2-4s | ✅ |
| Company Research | **C+ (75%)** | 2-4s | ✅ |
| News Analysis | **B (80%)** | <2s | ✅ |

- **Async/Await Architecture** - Concurrent operations
- **Intelligent Caching** - Minimizes API calls
- **Graceful Degradation** - Works with or without premium APIs
- **Rate Limiting** - Respects API quotas

## 🧪 Development

### Local Development
```bash
# Clone repository
git clone https://github.com/navam-ai/navam.git
cd navam

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Code formatting
black .
ruff check .
mypy .
```

### Testing MCP Servers
```bash
# Test with MCP inspector
mcp dev stock_mcp/server.py
mcp dev company_mcp/server.py
mcp dev news_mcp/server.py

# Test individual servers
echo '{"symbol": "AAPL"}' | python -m stock_mcp.server stdio
```

## 💡 Chat Command Reference

When you run `navam chat`, you have access to powerful built-in commands:

| Command | Description |
|---------|-------------|
| `/agents` | List all 18 specialized AI agents with descriptions and categories |
| `/api` | Show detailed API status - which are active, which need configuration |
| `/help` | Display complete help with all features and commands |
| `/commands` | List all available slash commands (built-in + investment workflows) |
| `/tools` | Show all MCP tools available for financial analysis |
| `/servers` | Display loaded MCP servers status |
| `/status` | Show conversation metrics (turns, tools used, agents invoked) |
| `/new` | Start a fresh conversation (clear context) |
| `/clear` | Clear the screen |
| `/exit` | Exit the chat interface |

**Investment Workflow Commands:**
- `/invest:research-stock [SYMBOL]` - Deep dive stock research
- `/invest:review-portfolio` - Portfolio analysis and recommendations
- `/invest:screen-opportunities` - Find investment opportunities
- `/invest:plan-goals` - Financial goal planning
- `/invest:optimize-taxes` - Tax optimization strategies

## 🔒 Security & Compliance

- ✅ **Read-Only Operations** - No trading or account modifications
- ✅ **API Key Security** - Environment variable storage
- ✅ **Rate Limiting** - Respectful API usage
- ✅ **No Data Storage** - No personal financial data stored
- ✅ **Open Source** - Full transparency

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Quick Contribution Setup
```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/navam.git
cd navam

# Development setup
pip install -e .[dev]
pre-commit install

# Make changes, test, and submit PR
pytest
black .
git commit -m "feat: your contribution"
```

### Ways to Contribute
- 🐛 **Bug Reports** - [GitHub Issues](https://github.com/navam-ai/navam/issues)
- ✨ **Feature Requests** - [GitHub Discussions](https://github.com/navam-ai/navam/discussions)
- 📖 **Documentation** - Improve guides and examples
- 🔧 **Code** - New features, bug fixes, optimizations
- 🧪 **Testing** - Add test coverage, performance testing

## 📈 What's New

### Version 1.4.1 (Latest)
- 🐛 **Bug Fix** - Fixed `/agents` command not finding agents in installed package
- 📦 **Package Fix** - All 18 agent files now properly included in PyPI distribution

### Version 1.4.0
- 🤖 **New `/agents` Command** - List all 18 specialized AI agents with descriptions
- 📊 **Enhanced Chat Interface** - Real-time thinking tokens and tool execution tracking
- ⚡ **Multi-Agent Monitoring** - See parallel agent execution in real-time
- 🔧 **Improved Notifications** - Scrollable notification history with timestamps
- 💬 **Better UX** - Context-aware conversations with turn tracking

### Version 1.2.0
- ✨ **Enhanced API Status Monitoring** - Real-time API health dashboard (`/api` command)
- 🔧 **Improved Configuration** - Comprehensive API key documentation
- 📊 **Better Error Handling** - Graceful fallbacks when APIs unavailable
- 🚀 **Performance Optimizations** - Faster response times

### Version 1.1.3
- 🤖 **18 Specialized Financial Agents** - Expert AI for every investment need
- 💬 **Interactive Chat Interface** - Natural language financial analysis
- 📊 **Production MCP Servers** - High-performance data integration
- ⚡ **Custom Investment Commands** - Pre-built workflows
- 🔐 **Enterprise Security** - Read-only, secure operations

## 🆘 Support

### Getting Help
- 📖 **Documentation** - Comprehensive guides in `/docs`
- 💬 **Discord Community** - [Join our Discord](https://discord.gg/navam)
- 🐛 **Bug Reports** - [GitHub Issues](https://github.com/navam-ai/navam/issues)
- 💡 **Feature Requests** - [GitHub Discussions](https://github.com/navam-ai/navam/discussions)

### Resources
- 🌐 **Website** - [navam.ai](https://navam.ai)
- 📦 **PyPI** - [pypi.org/project/navam](https://pypi.org/project/navam/)
- 📚 **Documentation** - [docs.navam.ai](https://docs.navam.ai)
- 💼 **GitHub** - [github.com/navam-ai/navam](https://github.com/navam-ai/navam)

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

## ⭐ Acknowledgments

Built with amazing open-source technologies:

- 🧠 **[Anthropic Claude](https://claude.ai)** - AI foundation
- ⚡ **[MCP Protocol](https://modelcontextprotocol.io/)** - Agent communication
- 🚀 **[FastMCP](https://github.com/modelcontextprotocol/python-sdk)** - High-performance framework
- 📊 **[Yahoo Finance](https://finance.yahoo.com/)** - Financial data
- 🔧 **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal interfaces

---

<div align="center">

### 🚀 Ready to supercharge your financial intelligence?

**Start your journey with AI-powered investing today!**

```bash
pip install navam && navam chat
```

[![⭐ Star on GitHub](https://img.shields.io/github/stars/navam-ai/navam?style=social)](https://github.com/navam-ai/navam)
[![🐦 Follow on Twitter](https://img.shields.io/twitter/follow/navam_ai?style=social)](https://twitter.com/navam_ai)

*Built with ❤️ for the global financial community*

</div>