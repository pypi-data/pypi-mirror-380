#!/usr/bin/env python
"""Company News MCP Server

An MCP server for comprehensive news analysis and financial media monitoring.
Provides tools for fetching, analyzing, and summarizing news from multiple sources.
"""

import asyncio
import argparse
import json
from contextlib import asynccontextmanager
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
import logging

from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel, Field

# Import with fallback pattern
try:
    from .models import (
        NewsArticle, NewsFeed, NewsAnalysis, NewsQuery, NewsSummary,
        TrendingTopic, NewsAlert, MarketNewsOverview, SentimentType,
        NewsCategory, NewsSource
    )
    from .api_clients import NewsAPIClient
    from .cache import NewsDataCache
except ImportError:
    # Fallback for direct imports when run as script
    from models import (
        NewsArticle, NewsFeed, NewsAnalysis, NewsQuery, NewsSummary,
        TrendingTopic, NewsAlert, MarketNewsOverview, SentimentType,
        NewsCategory, NewsSource
    )
    from api_clients import NewsAPIClient
    from cache import NewsDataCache

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server metadata
SERVER_NAME = "Company News MCP"
SERVER_VERSION = "1.0.0"
SERVER_DESCRIPTION = "Comprehensive news analysis and financial media monitoring"

@asynccontextmanager
async def lifespan(server: FastMCP):
    """Initialize and cleanup server resources"""
    try:
        # Initialize API client and cache
        api_client = await NewsAPIClient.create()
        cache = NewsDataCache()

        logger.info(f"Initializing {SERVER_NAME} v{SERVER_VERSION}")

        # Cleanup expired cache entries on startup
        await cache.cleanup_expired()

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
async def search_news(
    query: str,
    symbols: Optional[List[str]] = None,
    days_back: int = 7,
    limit: int = 20,
    min_relevance: float = 0.0,
    include_content: bool = False,
    ctx: Context = None
) -> NewsFeed:
    """Search for news articles across multiple sources.

    Args:
        query: Search query string
        symbols: Filter by stock symbols (optional)
        days_back: Number of days to search back (default: 7)
        limit: Maximum number of articles to return (default: 20)
        min_relevance: Minimum relevance score (0.0-1.0)
        include_content: Include full article content if available
        ctx: MCP context

    Returns:
        NewsFeed with matching articles and analysis
    """
    await ctx.report_progress(0.1, f"Searching news for: {query}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key(
        "search_news",
        query=query,
        symbols=symbols,
        days_back=days_back,
        limit=limit,
        min_relevance=min_relevance
    )

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached news search for: {query}")
        return NewsFeed(**cached_data)

    try:
        # Build news query
        news_query = NewsQuery(
            query=query,
            symbols=symbols,
            days_back=days_back,
            limit=limit,
            min_relevance=min_relevance,
            include_content=include_content
        )

        await ctx.report_progress(0.5, "Fetching news from sources...")

        # Search news
        news_feed = await api_client.search_news(news_query)

        # Cache results for 15 minutes
        await cache.set(cache_key, news_feed.dict(), ttl=900)

        await ctx.report_progress(1.0, f"Found {news_feed.total_articles} articles")
        return news_feed

    except Exception as e:
        error_msg = f"Error searching news: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def get_trending_topics(
    time_period: str = "24h",
    limit: int = 10,
    ctx: Context = None
) -> List[TrendingTopic]:
    """Get trending news topics and themes.

    Args:
        time_period: Time period for trends ("24h", "7d", "30d")
        limit: Maximum number of topics to return
        ctx: MCP context

    Returns:
        List of trending topics with metadata
    """
    await ctx.report_progress(0.1, f"Analyzing trending topics for {time_period}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key(
        "trending_topics",
        time_period=time_period,
        limit=limit
    )

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached trending topics for {time_period}")
        return [TrendingTopic(**topic) for topic in cached_data]

    try:
        await ctx.report_progress(0.5, "Analyzing news trends...")

        # Get trending topics
        trending_topics = await api_client.get_trending_topics(time_period)

        # Cache results for 30 minutes
        await cache.set(cache_key, [topic.dict() for topic in trending_topics], ttl=1800)

        await ctx.report_progress(1.0, f"Found {len(trending_topics)} trending topics")
        return trending_topics[:limit]

    except Exception as e:
        error_msg = f"Error getting trending topics: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def analyze_sentiment(
    query: str,
    time_period: str = "7d",
    symbols: Optional[List[str]] = None,
    ctx: Context = None
) -> NewsAnalysis:
    """Perform comprehensive sentiment analysis on news.

    Args:
        query: Topic or company to analyze
        time_period: Analysis time period ("1d", "7d", "30d")
        symbols: Focus on specific stock symbols
        ctx: MCP context

    Returns:
        Comprehensive news analysis with sentiment insights
    """
    await ctx.report_progress(0.1, f"Analyzing sentiment for: {query}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key(
        "sentiment_analysis",
        query=query,
        time_period=time_period,
        symbols=symbols
    )

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached sentiment analysis for: {query}")
        return NewsAnalysis(**cached_data)

    try:
        # Determine days back from time period
        days_map = {"1d": 1, "7d": 7, "30d": 30}
        days_back = days_map.get(time_period, 7)

        await ctx.report_progress(0.3, "Gathering news articles...")

        # Get news data
        news_query = NewsQuery(
            query=query,
            symbols=symbols,
            days_back=days_back,
            limit=100  # Get more articles for better analysis
        )

        news_feed = await api_client.search_news(news_query)

        await ctx.report_progress(0.7, "Performing sentiment analysis...")

        # Calculate sentiment distribution
        sentiment_dist = {
            "positive": news_feed.positive_count,
            "negative": news_feed.negative_count,
            "neutral": news_feed.neutral_count
        }

        # Get trending topics for this query
        trending_topics = await api_client.get_trending_topics(time_period)

        # Calculate company mentions
        company_mentions = {}
        symbol_sentiment = {}

        for article in news_feed.articles:
            for company in article.companies:
                company_mentions[company] = company_mentions.get(company, 0) + 1

            for symbol in article.symbols:
                if symbol not in symbol_sentiment:
                    symbol_sentiment[symbol] = []
                symbol_sentiment[symbol].append(article.sentiment_score)

        # Average sentiment by symbol
        for symbol in symbol_sentiment:
            scores = symbol_sentiment[symbol]
            symbol_sentiment[symbol] = sum(scores) / len(scores) if scores else 0.0

        # Create analysis result
        analysis = NewsAnalysis(
            query=query,
            time_period=time_period,
            total_articles=news_feed.total_articles,
            overall_sentiment=news_feed.sentiment_summary,
            sentiment_distribution=sentiment_dist,
            sentiment_trend=[],  # Would need historical data
            trending_topics=trending_topics[:5],
            key_themes=[topic.topic for topic in trending_topics[:10]],
            most_mentioned_companies=[
                {"company": k, "mentions": v}
                for k, v in sorted(company_mentions.items(), key=lambda x: x[1], reverse=True)[:10]
            ],
            symbol_sentiment=symbol_sentiment,
            source_reliability={source: 0.8 for source in news_feed.sources.keys()},
            source_coverage=news_feed.sources,
            market_impact_score=0.5,  # Would need more sophisticated calculation
            urgency_score=0.3,
            summary=f"Analysis of {news_feed.total_articles} articles about {query} shows {news_feed.sentiment_summary.value} sentiment overall.",
            key_developments=[article.title for article in news_feed.articles[:5]],
            risk_factors=[],  # Would extract from negative sentiment articles
            opportunities=[]  # Would extract from positive sentiment articles
        )

        # Cache results for 1 hour
        await cache.set(cache_key, analysis.dict(), ttl=3600)

        await ctx.report_progress(1.0, "Sentiment analysis complete")
        return analysis

    except Exception as e:
        error_msg = f"Error analyzing sentiment: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def get_market_overview(
    ctx: Context = None
) -> MarketNewsOverview:
    """Get comprehensive market news overview and sentiment.

    Args:
        ctx: MCP context

    Returns:
        Market news overview with sentiment and trends
    """
    await ctx.report_progress(0.1, "Gathering market news overview")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key("market_overview")

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info("Using cached market overview")
        return MarketNewsOverview(**cached_data)

    try:
        await ctx.report_progress(0.5, "Analyzing market sentiment...")

        # Get market overview
        market_overview = await api_client.get_market_overview()

        # Cache results for 30 minutes
        await cache.set(cache_key, market_overview.dict(), ttl=1800)

        await ctx.report_progress(1.0, "Market overview complete")
        return market_overview

    except Exception as e:
        error_msg = f"Error getting market overview: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def summarize_news(
    context: str,
    time_period: str = "24h",
    symbols: Optional[List[str]] = None,
    max_articles: int = 50,
    ctx: Context = None
) -> NewsSummary:
    """Generate a concise news summary for a specific context.

    Args:
        context: Context for summary (company name, sector, topic)
        time_period: Time period to summarize ("24h", "7d", "30d")
        symbols: Related stock symbols to focus on
        max_articles: Maximum articles to analyze
        ctx: MCP context

    Returns:
        Summarized news insights and key points
    """
    await ctx.report_progress(0.1, f"Summarizing news for: {context}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key(
        "news_summary",
        context=context,
        time_period=time_period,
        symbols=symbols
    )

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached summary for: {context}")
        return NewsSummary(**cached_data)

    try:
        # Determine days back
        days_map = {"24h": 1, "7d": 7, "30d": 30}
        days_back = days_map.get(time_period, 1)

        await ctx.report_progress(0.3, "Gathering relevant articles...")

        # Get news data
        news_query = NewsQuery(
            query=context,
            symbols=symbols,
            days_back=days_back,
            limit=max_articles
        )

        news_feed = await api_client.search_news(news_query)

        await ctx.report_progress(0.7, "Generating summary...")

        # Calculate average sentiment
        total_sentiment = sum(article.sentiment_score for article in news_feed.articles)
        avg_sentiment = total_sentiment / len(news_feed.articles) if news_feed.articles else 0.0

        # Get top stories by relevance
        top_stories = sorted(news_feed.articles, key=lambda x: x.relevance_score, reverse=True)[:5]

        # Get breaking news (recent high-relevance articles)
        breaking_news = [
            article for article in news_feed.articles
            if article.relevance_score > 0.7 and
               (datetime.now() - datetime.fromisoformat(article.published_date.replace('Z', '+00:00'))).total_seconds() < 86400
        ][:3]

        # Extract key themes
        themes = {}
        for article in news_feed.articles:
            words = article.title.lower().split()
            for word in words:
                if len(word) > 4 and word.isalpha():
                    themes[word] = themes.get(word, 0) + 1

        emerging_themes = [word for word, count in sorted(themes.items(), key=lambda x: x[1], reverse=True)[:5]]

        # Generate key points
        key_points = []
        if news_feed.articles:
            key_points.append(f"Found {news_feed.total_articles} articles about {context}")
            key_points.append(f"Overall sentiment: {news_feed.sentiment_summary.value}")
            if top_stories:
                key_points.append(f"Top story: {top_stories[0].title}")

        # Competitor analysis
        competitor_mentions = {}
        for article in news_feed.articles:
            for company in article.companies:
                if company.lower() != context.lower():
                    competitor_mentions[company] = competitor_mentions.get(company, 0) + 1

        # Risk assessment
        risk_level = "low"
        if avg_sentiment < -0.3:
            risk_level = "high"
        elif avg_sentiment < 0:
            risk_level = "medium"

        summary = NewsSummary(
            context=context,
            time_period=time_period,
            total_articles=news_feed.total_articles,
            sentiment_score=avg_sentiment,
            overall_sentiment=news_feed.sentiment_summary,
            headline_summary=f"{context} news shows {news_feed.sentiment_summary.value} sentiment with {news_feed.total_articles} articles",
            executive_summary=f"Analysis of {context} over {time_period} reveals {news_feed.sentiment_summary.value} sentiment across {news_feed.total_articles} articles. Key themes include {', '.join(emerging_themes[:3])}.",
            key_points=key_points,
            breaking_news=breaking_news,
            top_stories=top_stories,
            emerging_themes=emerging_themes,
            sentiment_trends={},  # Would need historical data
            competitor_mentions=competitor_mentions,
            market_positioning=f"Based on news analysis, {context} appears to be positioned with {news_feed.sentiment_summary.value} market sentiment.",
            risk_level=risk_level,
            risk_factors=[article.title for article in news_feed.articles if article.sentiment == SentimentType.NEGATIVE][:3],
            opportunities=[article.title for article in news_feed.articles if article.sentiment == SentimentType.POSITIVE][:3]
        )

        # Cache results for 1 hour
        await cache.set(cache_key, summary.dict(), ttl=3600)

        await ctx.report_progress(1.0, "News summary complete")
        return summary

    except Exception as e:
        error_msg = f"Error summarizing news: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

@mcp.tool()
async def get_company_news(
    symbol: str,
    days_back: int = 7,
    limit: int = 20,
    ctx: Context = None
) -> NewsFeed:
    """Get news specifically for a company by stock symbol.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL", "MSFT")
        days_back: Number of days to search back
        limit: Maximum number of articles
        ctx: MCP context

    Returns:
        NewsFeed with company-specific news
    """
    await ctx.report_progress(0.1, f"Fetching news for {symbol}")

    api_client = ctx.request_context.lifespan_context["api_client"]
    cache = ctx.request_context.lifespan_context["cache"]

    # Create cache key
    cache_key = cache.create_cache_key(
        "company_news",
        symbol=symbol,
        days_back=days_back,
        limit=limit
    )

    # Check cache first
    cached_data = await cache.get(cache_key)
    if cached_data:
        await ctx.info(f"Using cached news for {symbol}")
        return NewsFeed(**cached_data)

    try:
        # Build news query
        news_query = NewsQuery(
            query=f"{symbol} stock company",
            symbols=[symbol],
            days_back=days_back,
            limit=limit,
            min_relevance=0.3  # Higher relevance threshold for company-specific news
        )

        await ctx.report_progress(0.5, f"Searching news for {symbol}...")

        # Search news
        news_feed = await api_client.search_news(news_query)

        # Cache results for 30 minutes
        await cache.set(cache_key, news_feed.dict(), ttl=1800)

        await ctx.report_progress(1.0, f"Found {news_feed.total_articles} articles for {symbol}")
        return news_feed

    except Exception as e:
        error_msg = f"Error fetching company news for {symbol}: {str(e)}"
        await ctx.error(error_msg)
        raise RuntimeError(error_msg)

# ============================================================================
# RESOURCES - Dynamic resources for news data
# ============================================================================

@mcp.resource("news://search/{query}")
async def news_search_resource(query: str, ctx: Context) -> str:
    """Resource for news search results"""
    try:
        api_client = ctx.request_context.lifespan_context["api_client"]

        news_query = NewsQuery(query=query, limit=10)
        news_feed = await api_client.search_news(news_query)

        return news_feed.json()
    except Exception as e:
        error_response = {
            "error": f"Failed to fetch news for query '{query}': {str(e)}",
            "query": query,
            "articles": [],
            "total_articles": 0
        }
        return json.dumps(error_response, indent=2)

@mcp.resource("news://trending/{time_period}")
async def trending_topics_resource(time_period: str, ctx: Context) -> str:
    """Resource for trending topics"""
    try:
        api_client = ctx.request_context.lifespan_context["api_client"]

        trending_topics = await api_client.get_trending_topics(time_period)

        return json.dumps([topic.dict() for topic in trending_topics], indent=2)
    except Exception as e:
        error_response = {
            "error": f"Failed to fetch trending topics for period '{time_period}': {str(e)}",
            "time_period": time_period,
            "topics": []
        }
        return json.dumps(error_response, indent=2)

@mcp.resource("news://market-overview")
async def market_overview_resource(ctx: Context) -> str:
    """Resource for market news overview"""
    try:
        api_client = ctx.request_context.lifespan_context["api_client"]

        market_overview = await api_client.get_market_overview()

        return market_overview.json()
    except Exception as e:
        error_response = {
            "error": f"Failed to fetch market overview: {str(e)}",
            "market_date": datetime.now().strftime('%Y-%m-%d'),
            "market_sentiment": "unknown"
        }
        return json.dumps(error_response, indent=2)

@mcp.resource("news://company/{symbol}")
async def company_news_resource(symbol: str, ctx: Context) -> str:
    """Resource for company-specific news"""
    try:
        api_client = ctx.request_context.lifespan_context["api_client"]

        news_query = NewsQuery(
            query=f"{symbol} company",
            symbols=[symbol],
            limit=15
        )
        news_feed = await api_client.search_news(news_query)

        return news_feed.json()
    except Exception as e:
        error_response = {
            "error": f"Failed to fetch news for company '{symbol}': {str(e)}",
            "symbol": symbol,
            "articles": [],
            "total_articles": 0
        }
        return json.dumps(error_response, indent=2)

# ============================================================================
# PROMPTS - Templates for common news analysis tasks
# ============================================================================

@mcp.prompt(title="News Analysis Report")
def news_analysis_report(topic: str, time_period: str = "7d") -> str:
    return f"""Perform comprehensive news analysis for {topic}:

1. **Executive Summary**
   - Overall news sentiment and key themes
   - Major developments and breaking stories
   - Market impact assessment

2. **Sentiment Analysis**
   - Positive, negative, and neutral coverage breakdown
   - Sentiment trends over {time_period}
   - Key drivers of sentiment

3. **Key Developments**
   - Most significant news stories
   - Breaking news and announcements
   - Industry impact and implications

4. **Market Intelligence**
   - Competitor mentions and positioning
   - Industry trends and themes
   - Regulatory or policy impacts

5. **Risk Assessment**
   - Potential risks identified in coverage
   - Negative sentiment drivers
   - Reputation management considerations

6. **Opportunities**
   - Positive developments and opportunities
   - Strategic implications
   - Market positioning insights

7. **Media Coverage Analysis**
   - Source diversity and reliability
   - Coverage volume and frequency
   - Geographic and demographic reach

Please provide data-driven insights based on recent news coverage."""

@mcp.prompt(title="Daily News Briefing")
def daily_news_briefing(focus_areas: List[str]) -> str:
    focus_list = ", ".join(focus_areas)
    return f"""Create a daily news briefing focusing on: {focus_list}

**EXECUTIVE SUMMARY**
- Top 3 stories of the day
- Overall market sentiment
- Key themes and trends

**BREAKING NEWS**
- Latest developments (last 24 hours)
- Impact assessment
- Immediate implications

**MARKET MOVERS**
- Companies in the news
- Significant announcements
- Stock-moving events

**SECTOR HIGHLIGHTS**
- Industry-specific developments
- Regulatory updates
- Competitive dynamics

**TRENDING TOPICS**
- Emerging themes
- Social media buzz
- Analyst commentary

**RISK ALERTS**
- Potential negative developments
- Regulatory concerns
- Market volatility factors

**OPPORTUNITIES**
- Positive developments
- Growth indicators
- Strategic insights

Please provide concise, actionable insights for decision-making."""

@mcp.prompt(title="Competitive Intelligence")
def competitive_intelligence(company: str, competitors: List[str]) -> str:
    competitor_list = ", ".join(competitors)
    return f"""Analyze competitive landscape for {company} vs {competitor_list}:

1. **News Coverage Comparison**
   - Volume of coverage for each company
   - Sentiment comparison across competitors
   - Share of voice analysis

2. **Strategic Developments**
   - Product launches and innovations
   - Market expansion activities
   - Partnership and acquisition news

3. **Financial Performance News**
   - Earnings and revenue coverage
   - Investor sentiment
   - Analyst recommendations

4. **Leadership and Management**
   - Executive changes and appointments
   - Strategic communications
   - Thought leadership presence

5. **Market Positioning**
   - Brand perception in media
   - Industry leadership indicators
   - Innovation and differentiation

6. **Crisis and Risk Management**
   - Negative news handling
   - Reputation management
   - Risk exposure comparison

7. **Opportunities and Threats**
   - Market opportunities each company is pursuing
   - Competitive threats and challenges
   - Strategic advantages and weaknesses

Provide actionable competitive intelligence insights."""

@mcp.prompt(title="Earnings Season Monitor")
def earnings_season_monitor(symbol: str) -> str:
    return f"""Monitor earnings-related news for {symbol}:

**PRE-EARNINGS ANALYSIS**
- Analyst expectations and predictions
- Management guidance and outlook
- Market sentiment leading up to earnings

**EARNINGS ANNOUNCEMENT COVERAGE**
- Actual vs expected results
- Management commentary highlights
- Investor and analyst reactions

**POST-EARNINGS IMPACT**
- Stock price movement and volume
- Analyst rating changes
- Forward-looking guidance updates

**COMPETITIVE CONTEXT**
- Peer company comparisons
- Industry performance benchmarks
- Sector-wide trends and implications

**MEDIA SENTIMENT TRACKING**
- Positive vs negative coverage
- Key themes in earnings coverage
- Long-term outlook implications

**STRATEGIC INSIGHTS**
- Business strategy updates
- Market expansion plans
- Investment priorities and capital allocation

Provide comprehensive earnings season intelligence."""

@mcp.prompt(title="Crisis Communication Monitor")
def crisis_communication_monitor(entity: str) -> str:
    return f"""Monitor crisis-related news and communications for {entity}:

**SITUATION ASSESSMENT**
- Nature and scope of the crisis
- Timeline of developments
- Stakeholders affected

**MEDIA COVERAGE ANALYSIS**
- Volume and tone of coverage
- Key media outlets and journalists
- Narrative trends and framing

**COMMUNICATION RESPONSE**
- Official statements and responses
- Leadership communication strategy
- Transparency and accountability measures

**STAKEHOLDER REACTIONS**
- Investor sentiment and market impact
- Customer and public reactions
- Regulatory or government responses

**REPUTATION IMPACT**
- Brand sentiment tracking
- Trust and credibility indicators
- Long-term reputation implications

**COMPETITIVE IMPLICATIONS**
- Competitor positioning and responses
- Market share and advantage shifts
- Industry-wide impacts

**RECOVERY INDICATORS**
- Positive sentiment signals
- Resolution and remediation efforts
- Stakeholder confidence restoration

Provide real-time crisis intelligence and strategic recommendations."""

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
        default=8082,
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