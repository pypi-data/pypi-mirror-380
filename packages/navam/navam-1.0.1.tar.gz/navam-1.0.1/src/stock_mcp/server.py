#!/usr/bin/env python3
"""Stock MCP Server - Main server implementation using FastMCP."""

import os
import sys
from contextlib import asynccontextmanager
from typing import Dict, Any, List, Optional

from mcp.server.fastmcp import FastMCP, Context
from dotenv import load_dotenv

try:
    from .api_clients import StockAPIClient
    from .models import (
        StockQuote, StockHistory, StockAnalysis, MarketOverview,
        PortfolioAnalysis, TechnicalIndicators, StockFundamentals
    )
    from .cache import StockDataCache
except ImportError:
    # Fallback for direct imports
    from api_clients import StockAPIClient
    from models import (
        StockQuote, StockHistory, StockAnalysis, MarketOverview,
        PortfolioAnalysis, TechnicalIndicators, StockFundamentals
    )
    from cache import StockDataCache

load_dotenv()

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Initialize and cleanup server resources."""
    api_client = StockAPIClient()
    cache = StockDataCache()

    yield {
        "api_client": api_client,
        "cache": cache
    }

    await cache.cleanup()

mcp = FastMCP(
    name="Stock Analysis MCP",
    lifespan=lifespan
)


# ===== TOOLS REGISTRATION =====
# Define tools directly here to avoid circular imports

@mcp.tool()
async def analyze_stock(symbol: str, ctx: Context) -> StockAnalysis:
    """Perform comprehensive stock analysis.

    Args:
        symbol: Stock ticker symbol (e.g., AAPL, MSFT)

    Returns:
        Complete analysis including quote, indicators, and fundamentals
    """
    api_client = ctx.request_context.lifespan_context["api_client"]

    await ctx.report_progress(0.1, f"Starting analysis for {symbol}")

    await ctx.report_progress(0.3, "Fetching current quote...")
    quote = await api_client.get_quote(symbol)

    await ctx.report_progress(0.5, "Calculating technical indicators...")
    indicators = await api_client.calculate_indicators(symbol)

    await ctx.report_progress(0.7, "Getting fundamental data...")
    fundamentals = await api_client.get_fundamentals(symbol)

    await ctx.report_progress(0.9, "Generating recommendation...")

    recommendation = "Hold"
    sentiment = "Neutral"

    if indicators.rsi:
        if indicators.rsi < 30:
            sentiment = "Oversold"
            recommendation = "Buy"
        elif indicators.rsi > 70:
            sentiment = "Overbought"
            recommendation = "Sell"

    await ctx.report_progress(1.0, "Analysis complete!")

    return StockAnalysis(
        symbol=symbol,
        quote=quote,
        indicators=indicators,
        fundamentals=fundamentals,
        recommendation=recommendation,
        sentiment=sentiment
    )


@mcp.tool()
async def compare_stocks(symbols: List[str], ctx: Context) -> Dict[str, Any]:
    """Compare multiple stocks side by side.

    Args:
        symbols: List of stock ticker symbols to compare

    Returns:
        Comparison data for all provided stocks
    """
    api_client = ctx.request_context.lifespan_context["api_client"]

    await ctx.info(f"Comparing {len(symbols)} stocks: {', '.join(symbols)}")

    comparisons = {}

    for i, symbol in enumerate(symbols):
        await ctx.report_progress((i + 1) / len(symbols), f"Analyzing {symbol}...")

        try:
            quote = await api_client.get_quote(symbol)
            indicators = await api_client.calculate_indicators(symbol)
            fundamentals = await api_client.get_fundamentals(symbol)

            comparisons[symbol] = {
                "price": quote.price,
                "change_percent": quote.change_percent,
                "volume": quote.volume,
                "market_cap": quote.market_cap,
                "pe_ratio": fundamentals.pe_ratio,
                "rsi": indicators.rsi,
                "sma_50": indicators.sma_50
            }
        except Exception as e:
            await ctx.error(f"Failed to analyze {symbol}: {str(e)}")
            comparisons[symbol] = {"error": str(e)}

    return {
        "symbols": symbols,
        "comparisons": comparisons,
        "best_performer": max(
            comparisons.keys(),
            key=lambda x: comparisons[x].get("change_percent", -999)
        ) if comparisons else None
    }


@mcp.tool()
async def screen_stocks(
    ctx: Context,
    sector: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_volume: Optional[int] = None
) -> List[Dict[str, Any]]:
    """Screen stocks based on criteria.

    Args:
        sector: Sector to filter by (technology, finance, healthcare, energy, consumer)
        min_price: Minimum stock price
        max_price: Maximum stock price
        min_volume: Minimum trading volume

    Returns:
        List of stocks matching the criteria
    """
    api_client = ctx.request_context.lifespan_context["api_client"]

    await ctx.info(f"Screening stocks with criteria - sector: {sector}, price range: {min_price}-{max_price}")

    results = await api_client.search_stocks("", sector=sector)

    filtered_results = []
    for stock in results:
        meets_criteria = True

        if min_price and stock["price"] < min_price:
            meets_criteria = False
        if max_price and stock["price"] > max_price:
            meets_criteria = False

        if meets_criteria:
            filtered_results.append(stock)

    await ctx.info(f"Found {len(filtered_results)} stocks matching criteria")
    return filtered_results


@mcp.tool()
async def calculate_portfolio_value(
    holdings: List[Dict[str, Any]],
    ctx: Context
) -> PortfolioAnalysis:
    """Calculate portfolio value and analysis.

    Args:
        holdings: List of holdings with symbol and quantity
                 Example: [{"symbol": "AAPL", "quantity": 100, "cost_basis": 150.00}]

    Returns:
        Portfolio analysis with total value, returns, and allocation
    """
    api_client = ctx.request_context.lifespan_context["api_client"]

    await ctx.info(f"Calculating portfolio value for {len(holdings)} holdings")

    total_value = 0.0
    total_cost = 0.0
    analyzed_holdings = []

    for i, holding in enumerate(holdings):
        symbol = holding["symbol"]
        quantity = holding["quantity"]
        cost_basis = holding.get("cost_basis", 0)

        await ctx.report_progress((i + 1) / len(holdings), f"Analyzing {symbol}...")

        try:
            quote = await api_client.get_quote(symbol)
            current_value = quote.price * quantity
            position_cost = cost_basis * quantity
            position_return = current_value - position_cost

            total_value += current_value
            total_cost += position_cost

            analyzed_holdings.append({
                "symbol": symbol,
                "quantity": quantity,
                "current_price": quote.price,
                "current_value": current_value,
                "cost_basis": cost_basis,
                "position_return": position_return,
                "return_percent": (position_return / position_cost * 100) if position_cost > 0 else 0,
                "allocation_percent": 0  # Will calculate after total is known
            })
        except Exception as e:
            await ctx.error(f"Failed to analyze {symbol}: {str(e)}")

    for holding in analyzed_holdings:
        holding["allocation_percent"] = (holding["current_value"] / total_value * 100) if total_value > 0 else 0

    total_return = total_value - total_cost
    return_percentage = (total_return / total_cost * 100) if total_cost > 0 else 0

    allocation = {holding["symbol"]: holding["allocation_percent"] for holding in analyzed_holdings}

    risk_metrics = {
        "largest_position": max(analyzed_holdings, key=lambda x: x["allocation_percent"])["symbol"] if analyzed_holdings else None,
        "concentration_risk": max([h["allocation_percent"] for h in analyzed_holdings]) if analyzed_holdings else 0
    }

    return PortfolioAnalysis(
        total_value=total_value,
        total_return=total_return,
        return_percentage=return_percentage,
        holdings=analyzed_holdings,
        allocation=allocation,
        risk_metrics=risk_metrics
    )


@mcp.tool()
async def get_moving_averages(symbol: str, periods: List[int], ctx: Context) -> Dict[str, float]:
    """Calculate moving averages for specific periods.

    Args:
        symbol: Stock ticker symbol
        periods: List of periods to calculate (e.g., [20, 50, 200])

    Returns:
        Dictionary of moving averages for each period
    """
    api_client = ctx.request_context.lifespan_context["api_client"]

    await ctx.info(f"Calculating moving averages for {symbol}")

    history = await api_client.get_history(symbol, "1y")

    moving_averages = {}
    if history.data:
        prices = [float(day["close"]) for day in history.data]

        for period in periods:
            if len(prices) >= period:
                ma = sum(prices[-period:]) / period
                moving_averages[f"sma_{period}"] = ma
            else:
                moving_averages[f"sma_{period}"] = None

    return moving_averages


@mcp.tool()
async def find_trending_stocks(ctx: Context, direction: str = "up", limit: int = 10) -> List[Dict[str, Any]]:
    """Find stocks with strong trends.

    Args:
        direction: Trend direction ('up' or 'down')
        limit: Maximum number of results to return

    Returns:
        List of trending stocks with trend indicators
    """
    await ctx.info(f"Finding {direction} trending stocks")

    # This would typically connect to a screener API
    # For now, return a sample structure
    sample_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

    api_client = ctx.request_context.lifespan_context["api_client"]
    trending = []

    for symbol in sample_stocks[:limit]:
        try:
            quote = await api_client.get_quote(symbol)
            indicators = await api_client.calculate_indicators(symbol)

            trend_strength = 0
            if indicators.rsi and indicators.sma_20 and indicators.sma_50:
                if direction == "up":
                    if quote.price > indicators.sma_20 > indicators.sma_50:
                        trend_strength = abs(quote.change_percent)
                elif direction == "down":
                    if quote.price < indicators.sma_20 < indicators.sma_50:
                        trend_strength = abs(quote.change_percent)

            trending.append({
                "symbol": symbol,
                "price": quote.price,
                "change_percent": quote.change_percent,
                "trend_strength": trend_strength,
                "rsi": indicators.rsi
            })
        except:
            pass

    trending.sort(key=lambda x: x["trend_strength"], reverse=True)
    return trending


# Import resources and prompts (if they don't have circular dependencies)
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