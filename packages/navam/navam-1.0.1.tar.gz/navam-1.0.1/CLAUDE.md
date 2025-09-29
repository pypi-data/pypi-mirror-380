# Project: Stock AI MCP Server

This project focuses on building high-quality MCP (Model Context Protocol) servers in Python for stock market data analysis and financial APIs.

## Project Overview

Building MCP servers to:
- Connect to open finance APIs for stock data
- Expose finance API schemas as resources
- Provide tools for read-only search queries
- Include prompts for common stock analysis tasks

## Development Environment

### Python Setup
- Use Python 3.11+ for MCP server development
- Recommended: Use `uv` for dependency management: `uv init && uv add "mcp[cli]"`
- Alternative: `pip install "mcp[cli]"` for pip-based projects
- Virtual environment: `python -m venv venv`
- Activate: `source venv/bin/activate`

### MCP SDK Installation
```bash
# With uv (recommended)
uv add "mcp[cli]"

# With pip
pip install "mcp[cli]"
```

### FastMCP Framework
- Use FastMCP for high-level server implementation
- Leverage decorators for tools, resources, and prompts
- Implement proper async/await patterns for all I/O operations
- Use Context objects for logging, progress reporting, and LLM interactions
- Support structured output with Pydantic models and TypedDict

## Core Commands

### Build & Development
- `pip install -e .` - Install package in development mode
- `python -m pytest tests/` - Run test suite
- `python -m black .` - Format code
- `python -m mypy .` - Type check

### MCP Server Commands
- `uv run mcp dev server.py` - Launch MCP Inspector for testing
- `uv run mcp install server.py` - Install in Claude Desktop
- `uv run server.py stdio` - Run server with stdio transport
- `uv run server.py streamable-http --host 0.0.0.0 --port 8080` - HTTP transport
- `uv run mcp list` - List installed servers
- `uv run mcp inspect <server>` - Inspect server capabilities

## Code Style Guidelines

### Python Standards
- Use type hints for all function signatures
- Follow PEP 8 conventions
- Use dataclasses for data structures
- Implement proper async/await patterns
- Use logging instead of print statements

### MCP Server Conventions
- All tools should be read-only for safety (no side effects)
- Resources are for data exposure (like GET endpoints)
- Tools are for actions/computation (like POST endpoints)
- Prompts are reusable interaction templates
- Use structured output for rich data types
- Implement proper rate limiting and caching
- Handle API errors with informative messages
- Support pagination for large datasets

### Documentation
- Document all MCP resources with clear descriptions
- Include example usage for each tool
- Provide sample prompts for common tasks
- Keep API documentation up-to-date

## Project Structure

```
stockai-e1/
├── src/
│   └── stock_mcp/
│       ├── __init__.py
│       ├── server.py          # FastMCP server with lifespan management
│       ├── resources.py       # Dynamic resources for stock data
│       ├── tools.py          # Stock analysis tools
│       ├── prompts.py        # Analysis prompt templates
│       ├── models.py         # Pydantic models for structured output
│       ├── api_clients.py   # Finance API client implementations
│       └── cache.py         # Caching layer for API responses
├── tests/
│   ├── test_tools.py
│   ├── test_resources.py
│   └── test_integration.py
├── requirements.txt
├── pyproject.toml
├── .mcp.json              # MCP server configuration
└── README.md
```

## Finance API Integration

### Supported APIs
- Alpha Vantage (free tier available)
- Yahoo Finance (yfinance library)
- IEX Cloud (if API key provided)
- Polygon.io (if API key provided)

### Data Types
- Stock quotes (real-time and historical)
- Company fundamentals
- Technical indicators
- Market news and sentiment
- Options data

## Testing Strategy

- Unit tests for all tool functions
- Integration tests for API connections
- Mock external API calls in tests
- Test error handling and edge cases
- Verify rate limiting works correctly

## Security & Best Practices

### API Keys
- Store API keys in .env file
- NEVER commit .env to git
- Use environment variables for secrets
- Implement key rotation support

### Rate Limiting
- Respect API rate limits
- Implement exponential backoff
- Cache frequently requested data
- Queue requests when necessary

## Workflow Guidelines

1. **Before implementing features:**
   - Review MCP documentation in artifacts/refer/mcp/
   - Check existing implementations for patterns
   - Design resource schemas first
   - Plan error handling strategy

2. **During development:**
   - Write tests alongside implementation
   - Use type hints consistently
   - Add proper logging
   - Document as you code

3. **After implementation:**
   - Run full test suite
   - Verify type checking passes
   - Test with actual API calls
   - Update documentation

## MCP Implementation Patterns

### FastMCP Server Initialization
```python
from mcp.server.fastmcp import FastMCP
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(server: FastMCP):
    # Initialize API clients, caches, etc.
    api_client = await FinanceAPIClient.create()
    yield {"api_client": api_client}
    # Cleanup
    await api_client.close()

mcp = FastMCP(
    "Stock Analysis MCP",
    version="1.0.0",
    lifespan=lifespan
)
```

### Adding Dynamic Resources
```python
@mcp.resource("stock://{symbol}/quote")
async def get_stock_quote(symbol: str, ctx: Context) -> dict:
    """Get real-time stock quote."""
    api = ctx.request_context.lifespan_context["api_client"]
    return await api.get_quote(symbol)
```

### Creating Tools with Structured Output
```python
from pydantic import BaseModel, Field

class StockAnalysis(BaseModel):
    symbol: str
    price: float = Field(description="Current price")
    volume: int = Field(description="Trading volume")
    indicators: dict[str, float]

@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    """Perform comprehensive stock analysis."""
    await ctx.report_progress(0.5, "Fetching data...")
    # Implementation
    return StockAnalysis(...)
```

### Creating Analysis Prompts
```python
@mcp.prompt(title="Stock Research")
def research_stock(symbol: str, timeframe: str = "1y") -> str:
    return f"""Analyze {symbol} over {timeframe}:
    1. Price performance and trends
    2. Key technical indicators
    3. Recent news sentiment
    4. Trading volume patterns
    """

## MCP Best Practices

### Transport Mechanisms
- **stdio**: Default for Claude Desktop integration
- **Streamable HTTP**: For web-based clients (configure CORS)
- **SSE**: For server-sent events support

### Context Object Usage
```python
@mcp.tool()
async def complex_analysis(symbol: str, ctx: Context) -> dict:
    # Logging
    await ctx.info(f"Starting analysis for {symbol}")
    await ctx.debug("Fetching market data")

    # Progress reporting
    await ctx.report_progress(0.3, "Analyzing trends...")

    # Error handling
    await ctx.error("API rate limit reached")

    # LLM interaction (if supported)
    result = await ctx.sample(
        messages=[{"role": "user", "content": "Summarize trends"}]
    )
```

### Testing MCP Servers
```python
# Unit test example
import pytest
from mcp.server.fastmcp import FastMCP

@pytest.fixture
async def mcp_server():
    server = FastMCP("Test Server")
    # Add test tools/resources
    return server

async def test_stock_tool(mcp_server):
    result = await mcp_server.call_tool(
        "analyze_stock",
        {"symbol": "AAPL"}
    )
    assert result["symbol"] == "AAPL"
```

### Claude Desktop Integration
1. Create `.mcp.json` in project root:
```json
{
  "mcpServers": {
    "stock-analyzer": {
      "command": "uv",
      "args": ["run", "src/stock_mcp/server.py", "stdio"],
      "env": {
        "ALPHA_VANTAGE_KEY": "${ALPHA_VANTAGE_KEY}"
      }
    }
  }
}
```

2. Install: `uv run mcp install src/stock_mcp/server.py`

### Important Notes
- All tools must be read-only (no trading execution)
- Use structured output for complex data types
- Implement pagination for large result sets
- Cache API responses to minimize rate limit issues
- Support both US and international markets
- Handle missing/invalid data gracefully
- Follow finance API terms of service strictly

## Common MCP Patterns for Finance

### Resource Patterns
- `stock://{symbol}/quote` - Real-time quotes
- `stock://{symbol}/history/{period}` - Historical data
- `stock://{symbol}/fundamentals` - Company financials
- `market://indices` - Market indices
- `news://{symbol}/latest` - Company news

### Tool Categories
- **Data Retrieval**: get_quote, get_history, get_fundamentals
- **Analysis**: calculate_indicators, analyze_trends, compare_stocks
- **Screening**: find_stocks, filter_by_criteria, rank_by_metric
- **Reporting**: generate_summary, create_chart_data

### Prompt Templates
- Stock research and analysis
- Portfolio evaluation
- Market trend identification
- Risk assessment
- Earnings analysis

## Error Handling

```python
from mcp.server.errors import McpError

@mcp.tool()
async def get_data(symbol: str, ctx: Context) -> dict:
    try:
        return await fetch_stock_data(symbol)
    except RateLimitError:
        await ctx.error("Rate limit reached, using cached data")
        return await get_cached_data(symbol)
    except InvalidSymbolError:
        raise McpError(f"Invalid symbol: {symbol}")
```

## Critical MCP Server Implementation Learnings

### Key Fixes for Working MCP Servers

Based on debugging and fixing the Stock AI MCP Server, these are **critical patterns and fixes** needed for MCP servers to work correctly:

#### 1. Import Structure and Circular Dependencies

**CRITICAL FIX**: Use try/except fallback imports to handle both module and direct execution:

```python
# ❌ WRONG - Causes circular imports
from .api_clients import StockAPIClient
from .models import StockAnalysis

# ✅ CORRECT - Fallback import pattern
try:
    from .api_clients import StockAPIClient
    from .models import (
        StockQuote, StockHistory, StockAnalysis, MarketOverview,
        PortfolioAnalysis, TechnicalIndicators, StockFundamentals
    )
except ImportError:
    # Fallback for direct imports when run as script
    from api_clients import StockAPIClient
    from models import (
        StockQuote, StockHistory, StockAnalysis, MarketOverview,
        PortfolioAnalysis, TechnicalIndicators, StockFundamentals
    )
```

#### 2. Tool Registration Strategy

**CRITICAL FIX**: Define tools directly in server.py instead of importing from separate modules:

```python
# ❌ WRONG - Causes circular imports and loading issues
from . import tools  # tools.py tries to import mcp from server.py

# ✅ CORRECT - Define tools directly in server.py
@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    """Tool implementation here"""
    api_client = ctx.request_context.lifespan_context["api_client"]
    # ... implementation
```

**Why**: Tools need access to the `mcp` instance and resources from lifespan context. Importing creates circular dependencies.

#### 3. MCP Configuration (.mcp.json)

**CRITICAL FIX**: Proper command structure and working directory:

```json
{
  "mcpServers": {
    "stock-analyzer": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.stock_mcp.server", "stdio"],
      "workingDir": "/full/absolute/path/to/project"
    }
  }
}
```

**Key Points**:
- Use `uv run python -m` for proper module execution
- Use dot notation for module path: `src.stock_mcp.server`
- Always specify absolute `workingDir`
- Remove environment variables unless actually needed

#### 4. Server Entry Point and Transport Handling

**CRITICAL FIX**: Add proper CLI argument parsing and transport selection:

```python
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Stock MCP Server")
    parser.add_argument(
        "transport",
        nargs="?",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="Transport mechanism"
    )
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP transport")
    parser.add_argument("--port", type=int, default=8080, help="Port for HTTP transport")

    args = parser.parse_args()

    mcp.run(transport=args.transport)
```

#### 5. Resource and Prompt Loading

**CRITICAL FIX**: Safe import of resources and prompts with fallback handling:

```python
# Import resources and prompts with error handling
try:
    from . import resources
    from . import prompts
except ImportError:
    # Fallback for direct imports
    try:
        import resources
        import prompts
    except ImportError:
        pass  # Continue without resources/prompts if they have issues
```

#### 6. Lifespan Context Access Pattern

**CRITICAL**: Always access lifespan context through the full path:

```python
@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    # ✅ CORRECT - Full context path
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Use api_client and cache...
```

#### 7. Module Structure Best Practices

**File Organization**:
```
src/stock_mcp/
├── __init__.py          # Empty or minimal imports
├── server.py            # Main server with all tools defined here
├── models.py            # Pydantic models only
├── api_clients.py       # API client classes only
├── cache.py             # Cache implementation only
├── resources.py         # Resources that import from server
└── prompts.py           # Prompts that import from server
```

**Critical Rule**: Only `server.py` should instantiate the FastMCP object. All other files either define data classes/models or import the mcp instance from server.

#### 8. Common Import Error Patterns to Avoid

**❌ Don't do this**:
```python
# In tools.py
from server import mcp  # Circular import

# In server.py
from tools import *     # Circular import
```

**✅ Do this instead**:
```python
# All in server.py
mcp = FastMCP(name="Server")

@mcp.tool()
def my_tool():
    pass

# Optional: Import at end with error handling
try:
    from . import resources  # Only if resources don't create circular deps
except ImportError:
    pass
```

#### 9. Testing MCP Servers

**CRITICAL**: Test server loading with proper module path:

```bash
# Test server can load without errors
uv run python -m src.stock_mcp.server --help

# Test stdio transport works
echo '{}' | uv run python -m src.stock_mcp.server stdio

# Test MCP inspector
uv run mcp dev src/stock_mcp/server.py
```

#### 10. Debugging MCP Issues

**Common Issues and Solutions**:

| Issue | Symptom | Fix |
|-------|---------|-----|
| Circular imports | ImportError during loading | Use try/except fallback imports |
| Module not found | "No module named..." | Check .mcp.json args and workingDir |
| Transport errors | Server doesn't respond | Add proper CLI argument handling |
| Context errors | "KeyError" in lifespan context | Use full context path |
| Tool registration fails | Tools not appearing | Define tools in server.py directly |

### MCP Development Workflow

1. **Start Simple**: Create server.py with basic FastMCP and one tool
2. **Test Early**: Use `mcp dev` to test before adding complexity
3. **Add Incrementally**: Add one tool at a time, testing each
4. **Handle Imports**: Add try/except patterns as you modularize
5. **Configuration Last**: Set up .mcp.json after server works standalone

This pattern ensures MCP servers work reliably with Claude Desktop and avoid common import/configuration issues.

## References

- MCP Python SDK: artifacts/refer/mcp/Python-SDK-README.md
- MCP Ecosystem: artifacts/refer/mcp/llms-full.txt
- Claude Code Best Practices: artifacts/refer/claude-code-best-practices.md
- Active Backlog: artifacts/backlog/active.md
- MCP Specification: https://spec.modelcontextprotocol.io
- FastMCP Examples: https://github.com/modelcontextprotocol/python-sdk