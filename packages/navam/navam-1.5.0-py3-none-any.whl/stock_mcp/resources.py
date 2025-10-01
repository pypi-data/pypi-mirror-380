"""Dynamic resources for stock data."""

from typing import Dict, Any
from mcp.server.fastmcp import Context

try:
    from .server import mcp
    from .api_clients import StockAPIClient
    from .cache import StockDataCache
except ImportError:
    from server import mcp
    from api_clients import StockAPIClient
    from cache import StockDataCache


@mcp.resource("stock://{symbol}/quote")
async def get_stock_quote(symbol: str, ctx: Context) -> Dict[str, Any]:
    """Get real-time stock quote.

    Args:
        symbol: Stock ticker symbol (e.g., AAPL, MSFT)

    Returns:
        Current stock quote with price, change, volume, etc.
    """
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"quote:{symbol}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    quote = await api_client.get_quote(symbol)
    result = quote.model_dump()
    cache.set(cache_key, result)
    return result


@mcp.resource("stock://{symbol}/history/{period}")
async def get_stock_history(symbol: str, period: str, ctx: Context) -> Dict[str, Any]:
    """Get historical stock data.

    Args:
        symbol: Stock ticker symbol
        period: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)

    Returns:
        Historical price data for the specified period
    """
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"history:{symbol}:{period}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    history = await api_client.get_history(symbol, period)
    result = history.model_dump()
    cache.set(cache_key, result)
    return result


@mcp.resource("stock://{symbol}/fundamentals")
async def get_stock_fundamentals(symbol: str, ctx: Context) -> Dict[str, Any]:
    """Get company fundamental data.

    Args:
        symbol: Stock ticker symbol

    Returns:
        Fundamental metrics like P/E ratio, EPS, dividend yield, etc.
    """
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"fundamentals:{symbol}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    fundamentals = await api_client.get_fundamentals(symbol)
    result = fundamentals.model_dump()
    cache.set(cache_key, result)
    return result


@mcp.resource("stock://{symbol}/indicators")
async def get_technical_indicators(symbol: str, ctx: Context) -> Dict[str, Any]:
    """Get technical analysis indicators.

    Args:
        symbol: Stock ticker symbol

    Returns:
        Technical indicators like RSI, moving averages, MACD, etc.
    """
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = f"indicators:{symbol}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    indicators = await api_client.calculate_indicators(symbol)
    result = indicators.model_dump()
    cache.set(cache_key, result)
    return result


@mcp.resource("market://overview")
async def get_market_overview(ctx: Context) -> Dict[str, Any]:
    """Get market overview with major indices.

    Returns:
        Market indices and their current performance
    """
    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    cache_key = "market:overview"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    overview = await api_client.get_market_overview()
    cache.set(cache_key, overview)
    return overview


@mcp.resource("news://{symbol}/latest")
async def get_stock_news(symbol: str, ctx: Context) -> Dict[str, Any]:
    """Get latest news for a stock.

    Args:
        symbol: Stock ticker symbol

    Returns:
        Recent news articles and sentiment
    """
    return {
        "symbol": symbol,
        "articles": [],
        "note": "News functionality requires additional API integration"
    }