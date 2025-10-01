#!/usr/bin/env python
"""Company Research MCP Server

An MCP server for comprehensive company research and analysis.
Provides tools for accessing company fundamentals, financials, filings, and profiles.
"""

import asyncio
import argparse
from contextlib import asynccontextmanager
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
import logging

from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import with fallback pattern
try:
    from .models import (
        CompanyProfile, CompanyFinancials, CompanyFilings,
        CompanyInsiders, CompanyRatings,
        IndustryComparison, CompanyOverview
    )
    from .api_clients import CompanyAPIClient
    from .cache import CompanyDataCache
except ImportError:
    # Fallback for direct imports when run as script
    from models import (
        CompanyProfile, CompanyFinancials, CompanyFilings,
        CompanyInsiders, CompanyRatings,
        IndustryComparison, CompanyOverview
    )
    from api_clients import CompanyAPIClient
    from cache import CompanyDataCache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server metadata
SERVER_NAME = "Company Research MCP"
SERVER_VERSION = "1.0.0"
SERVER_DESCRIPTION = "Comprehensive company research and analysis tools"

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Initialize and cleanup server resources"""
    try:
        # Initialize API client and cache
        api_client = await CompanyAPIClient.create()
        cache = CompanyDataCache()

        logger.info(f"Initializing {SERVER_NAME} v{SERVER_VERSION}")

        # Yield resources to be available in context
        yield {
            "api_client": api_client,
            "cache": cache
        }

        # Cleanup
        logger.info(f"Shutting down {SERVER_NAME}")
        await api_client.close()

    except Exception as e:
        logger.error(f"Error in lifespan: {e}")
        raise

# Initialize MCP server
mcp = FastMCP(
    name=SERVER_NAME,
    lifespan=lifespan
)

# ============================================================================
# TOOLS - All defined directly in server.py to avoid circular imports
# ============================================================================

@mcp.tool()
async def get_company_profile(
    symbol: str,
    ctx: Context
) -> CompanyProfile:
    """Get detailed company profile including description, sector, industry, employees, etc.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL", "MSFT")
        ctx: MCP context

    Returns:
        Comprehensive company profile information
    """
    # Validate symbol format
    if not symbol or not symbol.strip():
        error_msg = "Invalid symbol: Symbol cannot be empty"
        await ctx.error(error_msg)
        raise ValueError(error_msg)

    symbol = symbol.upper().strip()
    if len(symbol) > 10 or not symbol.isalpha():
        error_msg = f"Invalid symbol format: {symbol}. Symbols should be 1-10 letters only."
        await ctx.error(error_msg)
        raise ValueError(error_msg)

    await ctx.report_progress(0.1, f"Fetching profile for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Check cache first
    cached_data = await cache.get(f"profile_{symbol}")
    if cached_data:
        await ctx.info(f"Using cached profile for {symbol}")
        return CompanyProfile(**cached_data)

    # Check rate limit
    if not await cache.check_rate_limit('profile', symbol):
        await ctx.warning(f"Rate limit reached for profile requests. Using any available cached data.")
        # Try to return stale cache if available
        cached_data = await cache.get(f"profile_{symbol}")
        if cached_data:
            return CompanyProfile(**cached_data)
        raise RuntimeError(f"Rate limit exceeded for {symbol}. Please try again later.")

    try:
        profile = await api_client.get_company_profile(symbol)

        # Validate profile data
        if profile.name == f"{symbol} (Data Unavailable)":
            error_msg = f"Symbol {symbol} not found or data unavailable"
            await ctx.error(error_msg)
            raise ValueError(error_msg)

        # Use appropriate TTL from cache configuration
        ttl = cache.get_ttl_for_type('profile')
        await cache.set(f"profile_{symbol}", profile.dict(), ttl=ttl)
        await ctx.report_progress(1.0, "Profile fetched successfully")
        return profile
    except ValueError:
        raise  # Re-raise validation errors
    except Exception as e:
        error_msg = f"Error fetching profile for {symbol}: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def get_company_financials(
    symbol: str,
    period: str = "annual",
    ctx: Context = None
) -> CompanyFinancials:
    """Get company financial statements (income statement, balance sheet, cash flow).

    Args:
        symbol: Stock ticker symbol
        period: "annual" or "quarterly"
        ctx: MCP context

    Returns:
        Company financial statements
    """
    await ctx.report_progress(0.1, f"Fetching financials for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"financials_{symbol}_{period}"
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached financials for {symbol}")
        return CompanyFinancials(**cached_data)

    # Check rate limit
    if not await cache.check_rate_limit('financials', symbol):
        await ctx.warning(f"Rate limit reached for financials requests. Using any available cached data.")
        if cached_data:
            return CompanyFinancials(**cached_data)
        raise RuntimeError(f"Rate limit exceeded for {symbol}. Please try again later.")

    try:
        financials = await api_client.get_financials(symbol, period)
        ttl = cache.get_ttl_for_type('financials')
        await cache.set(cache_key, financials.dict(), ttl=ttl)
        await ctx.report_progress(1.0, "Financials fetched successfully")
        return financials
    except Exception as e:
        await ctx.error(f"Error fetching financials: {str(e)}")
        raise

@mcp.tool()
async def get_company_filings(
    symbol: str,
    filing_type: Optional[str] = None,
    limit: int = 10,
    ctx: Context = None
) -> CompanyFilings:
    """Get recent SEC filings for a company.

    Args:
        symbol: Stock ticker symbol
        filing_type: Specific filing type (e.g., "10-K", "10-Q", "8-K")
        limit: Number of filings to return
        ctx: MCP context

    Returns:
        Recent company SEC filings
    """
    await ctx.report_progress(0.1, f"Fetching SEC filings for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]

    try:
        filings = await api_client.get_sec_filings(symbol, filing_type, limit)
        await ctx.report_progress(1.0, "Filings fetched successfully")
        return filings
    except Exception as e:
        await ctx.error(f"Error fetching filings: {str(e)}")
        raise


@mcp.tool()
async def get_insider_trading(
    symbol: str,
    months: int = 3,
    ctx: Context = None
) -> CompanyInsiders:
    """Get insider trading activity for a company.

    Args:
        symbol: Stock ticker symbol
        months: Number of months of insider activity (default 3)
        ctx: MCP context

    Returns:
        Recent insider trading transactions
    """
    await ctx.report_progress(0.1, f"Fetching insider trading for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]

    try:
        insiders = await api_client.get_insider_trading(symbol, months)
        await ctx.report_progress(1.0, "Insider data fetched successfully")
        return insiders
    except Exception as e:
        await ctx.error(f"Error fetching insider data: {str(e)}")
        raise

@mcp.tool()
async def get_analyst_ratings(
    symbol: str,
    ctx: Context = None
) -> CompanyRatings:
    """Get analyst ratings and price targets for a company.

    Args:
        symbol: Stock ticker symbol
        ctx: MCP context

    Returns:
        Analyst ratings and consensus recommendations
    """
    await ctx.report_progress(0.1, f"Fetching analyst ratings for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"ratings_{symbol}"
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached ratings for {symbol}")
        return CompanyRatings(**cached_data)

    # Check rate limit
    if not await cache.check_rate_limit('ratings', symbol):
        await ctx.warning(f"Rate limit reached for ratings requests. Using any available cached data.")
        if cached_data:
            return CompanyRatings(**cached_data)
        raise RuntimeError(f"Rate limit exceeded for {symbol}. Please try again later.")

    try:
        ratings = await api_client.get_analyst_ratings(symbol)
        ttl = cache.get_ttl_for_type('ratings')
        await cache.set(cache_key, ratings.dict(), ttl=ttl)
        await ctx.report_progress(1.0, "Ratings fetched successfully")
        return ratings
    except Exception as e:
        await ctx.error(f"Error fetching ratings: {str(e)}")
        raise

@mcp.tool()
async def compare_companies(
    symbols: List[str],
    metrics: Optional[List[str]] = None,
    ctx: Context = None
) -> IndustryComparison:
    """Compare multiple companies across key metrics.

    Args:
        symbols: List of stock ticker symbols to compare
        metrics: Specific metrics to compare (default: all available)
        ctx: MCP context

    Returns:
        Comparative analysis of specified companies
    """
    await ctx.report_progress(0.1, f"Comparing companies: {', '.join(symbols)}")

    api_client = ctx.request_context.lifespan_context["api_client"]

    try:
        comparison = await api_client.compare_companies(symbols, metrics)
        await ctx.report_progress(1.0, "Comparison completed successfully")
        return comparison
    except Exception as e:
        await ctx.error(f"Error comparing companies: {str(e)}")
        raise

@mcp.tool()
async def search_companies(
    query: str,
    filters: Optional[Dict[str, Any]] = None,
    limit: int = 20,
    ctx: Context = None
) -> List[CompanyOverview]:
    """Search for companies by name, sector, industry, or other criteria.

    Args:
        query: Search query (company name, sector, industry, etc.)
        filters: Additional filters (market_cap, employees, revenue, etc.)
        limit: Maximum number of results
        ctx: MCP context

    Returns:
        List of companies matching search criteria
    """
    await ctx.report_progress(0.1, f"Searching companies: {query}")

    api_client = ctx.request_context.lifespan_context["api_client"]

    try:
        companies = await api_client.search_companies(query, filters, limit)
        await ctx.report_progress(1.0, f"Found {len(companies)} companies")
        return companies
    except Exception as e:
        await ctx.error(f"Error searching companies: {str(e)}")
        raise

# ============================================================================
# RESOURCES - Dynamic resources for company data
# ============================================================================

@mcp.resource("company://{symbol}/profile")
async def company_profile_resource(symbol: str, ctx: Context) -> str:
    """Resource for company profile data"""
    api_client = ctx.request_context.lifespan_context["api_client"]
    profile = await api_client.get_company_profile(symbol)
    return profile.json()

@mcp.resource("company://{symbol}/financials/{period}")
async def company_financials_resource(symbol: str, period: str, ctx: Context) -> str:
    """Resource for company financial statements"""
    api_client = ctx.request_context.lifespan_context["api_client"]
    financials = await api_client.get_financials(symbol, period)
    return financials.json()

@mcp.resource("company://{symbol}/filings")
async def company_filings_resource(symbol: str, ctx: Context) -> str:
    """Resource for SEC filings"""
    api_client = ctx.request_context.lifespan_context["api_client"]
    filings = await api_client.get_sec_filings(symbol, None, 10)
    return filings.json()

# ============================================================================
# PROMPTS - Templates for common company research tasks
# ============================================================================

@mcp.prompt(title="Company Deep Dive")
def company_deep_dive(symbol: str) -> str:
    return f"""Perform a comprehensive analysis of {symbol}:
    1. Company profile and business model
    2. Financial health (revenue, profit, cash flow trends)
    3. Recent SEC filings and material changes
    4. Insider trading patterns
    5. Analyst consensus and price targets
    6. Recent news and sentiment
    7. Competitive position in industry
    8. Key risks and opportunities"""

@mcp.prompt(title="Earnings Analysis")
def earnings_analysis(symbol: str, quarter: str = "latest") -> str:
    return f"""Analyze {symbol}'s {quarter} earnings:
    1. Revenue and earnings vs expectations
    2. Year-over-year and sequential growth
    3. Margin trends and profitability
    4. Segment performance breakdown
    5. Guidance updates and management commentary
    6. Cash flow and balance sheet changes
    7. Key metrics and KPIs"""

@mcp.prompt(title="Industry Comparison")
def industry_comparison(symbols: List[str]) -> str:
    companies = ", ".join(symbols)
    return f"""Compare these companies: {companies}
    1. Market capitalization and valuation multiples
    2. Revenue growth rates and profitability
    3. Market share and competitive positioning
    4. Financial strength and leverage
    5. Operating efficiency metrics
    6. Innovation and R&D investment
    7. Management effectiveness"""

@mcp.prompt(title="Due Diligence")
def due_diligence(symbol: str) -> str:
    return f"""Conduct due diligence on {symbol}:
    1. Business model and revenue streams
    2. Management team and board composition
    3. Financial statement analysis (3-5 years)
    4. Legal and regulatory issues
    5. Insider ownership and trading
    6. Related party transactions
    7. Audit opinions and accounting changes
    8. Risk factors from latest 10-K"""

@mcp.prompt(title="ESG Assessment")
def esg_assessment(symbol: str) -> str:
    return f"""Evaluate {symbol}'s ESG performance:
    1. Environmental impact and sustainability initiatives
    2. Social responsibility and employee relations
    3. Corporate governance structure
    4. Board diversity and independence
    5. Executive compensation alignment
    6. Regulatory compliance history
    7. Community engagement and philanthropy"""

# ============================================================================
# MAIN - Entry point with transport handling
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=SERVER_DESCRIPTION)
    parser.add_argument(
        "transport",
        nargs="?",
        default="stdio",
        choices=["stdio", "streamable-http"],
        help="Transport mechanism (default: stdio)"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host for HTTP transport"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8081,
        help="Port for HTTP transport"
    )

    args = parser.parse_args()

    if args.transport == "streamable-http":
        import uvicorn
        from mcp.server.http import MCPHTTPServer

        http_server = MCPHTTPServer(mcp, cors=True)
        uvicorn.run(
            http_server.app,
            host=args.host,
            port=args.port,
            log_level="info"
        )
    else:
        # Default to stdio transport
        mcp.run(transport="stdio")