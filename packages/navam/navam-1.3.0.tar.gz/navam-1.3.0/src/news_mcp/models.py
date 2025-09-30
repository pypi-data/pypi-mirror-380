"""Pydantic models for news data structures"""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class SentimentType(str, Enum):
    """News sentiment categories"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    BULLISH = "bullish"
    BEARISH = "bearish"

class NewsCategory(str, Enum):
    """News category types"""
    EARNINGS = "earnings"
    MERGER = "merger"
    ACQUISITION = "acquisition"
    PRODUCT = "product"
    REGULATORY = "regulatory"
    LEADERSHIP = "leadership"
    FINANCIAL = "financial"
    TECHNOLOGY = "technology"
    MARKET = "market"
    GENERAL = "general"

class NewsSource(str, Enum):
    """Supported news sources"""
    MARKETAUX = "marketaux"
    NEWSAPI = "newsapi"
    FINNHUB = "finnhub"
    YAHOO_FINANCE = "yahoo_finance"
    ALPHA_VANTAGE = "alpha_vantage"
    SEC = "sec"
    REDDIT = "reddit"

class NewsArticle(BaseModel):
    """Individual news article"""
    title: str = Field(description="Article headline")
    summary: str = Field(description="Article summary or excerpt")
    content: Optional[str] = Field(default="", description="Full article content if available")
    url: str = Field(description="Article URL")
    source: str = Field(description="News source name")
    source_type: NewsSource = Field(description="Source API type")
    author: Optional[str] = Field(default="", description="Article author")
    published_date: str = Field(description="Publication timestamp")
    image_url: Optional[str] = Field(default="", description="Featured image URL")

    # Analysis fields
    sentiment: SentimentType = Field(description="Article sentiment")
    sentiment_score: float = Field(description="Sentiment confidence score (-1 to 1)")
    relevance_score: float = Field(description="Relevance to query (0 to 1)")
    category: NewsCategory = Field(description="News category")

    # Financial context
    symbols: List[str] = Field(default_factory=list, description="Related stock symbols")
    companies: List[str] = Field(default_factory=list, description="Mentioned companies")
    sectors: List[str] = Field(default_factory=list, description="Related sectors")

    # Engagement metrics
    view_count: Optional[int] = Field(default=0, description="Article views")
    share_count: Optional[int] = Field(default=0, description="Social shares")
    comment_count: Optional[int] = Field(default=0, description="Comments count")

class NewsFeed(BaseModel):
    """Collection of news articles with metadata"""
    query: str = Field(description="Search query used")
    articles: List[NewsArticle] = Field(description="List of news articles")
    total_articles: int = Field(description="Total articles found")
    page: int = Field(default=1, description="Current page number")
    per_page: int = Field(default=20, description="Articles per page")

    # Time range
    from_date: Optional[str] = Field(description="Start date for articles")
    to_date: Optional[str] = Field(description="End date for articles")

    # Analysis aggregates
    sentiment_summary: SentimentType = Field(description="Overall sentiment")
    positive_count: int = Field(description="Positive articles count")
    negative_count: int = Field(description="Negative articles count")
    neutral_count: int = Field(description="Neutral articles count")

    # Source breakdown
    sources: Dict[str, int] = Field(default_factory=dict, description="Articles by source")
    categories: Dict[str, int] = Field(default_factory=dict, description="Articles by category")

    # Performance metrics
    fetch_time_ms: int = Field(description="Time taken to fetch news")
    last_updated: str = Field(description="Last update timestamp")

class TrendingTopic(BaseModel):
    """Trending news topic"""
    topic: str = Field(description="Topic name or keyword")
    article_count: int = Field(description="Number of articles")
    sentiment: SentimentType = Field(description="Overall sentiment")
    sentiment_score: float = Field(description="Average sentiment score")
    trend_score: float = Field(description="Trending momentum (0-1)")
    related_symbols: List[str] = Field(default_factory=list, description="Related stock symbols")
    sample_headlines: List[str] = Field(description="Sample article headlines")

class NewsAnalysis(BaseModel):
    """Comprehensive news analysis and insights"""
    query: str = Field(description="Analysis query")
    time_period: str = Field(description="Analysis time period")
    total_articles: int = Field(description="Total articles analyzed")

    # Sentiment analysis
    overall_sentiment: SentimentType = Field(description="Overall sentiment")
    sentiment_distribution: Dict[str, int] = Field(description="Sentiment breakdown")
    sentiment_trend: List[Dict[str, Any]] = Field(description="Sentiment over time")

    # Topic analysis
    trending_topics: List[TrendingTopic] = Field(description="Trending topics")
    key_themes: List[str] = Field(description="Key themes identified")

    # Company/Symbol analysis
    most_mentioned_companies: List[Dict[str, Any]] = Field(description="Top mentioned companies")
    symbol_sentiment: Dict[str, float] = Field(description="Sentiment by symbol")

    # Source analysis
    source_reliability: Dict[str, float] = Field(description="Source reliability scores")
    source_coverage: Dict[str, int] = Field(description="Coverage by source")

    # Impact assessment
    market_impact_score: float = Field(description="Potential market impact (0-1)")
    urgency_score: float = Field(description="News urgency level (0-1)")

    # Key insights
    summary: str = Field(description="Executive summary")
    key_developments: List[str] = Field(description="Key developments")
    risk_factors: List[str] = Field(description="Identified risks")
    opportunities: List[str] = Field(description="Identified opportunities")

class NewsQuery(BaseModel):
    """News search and filter parameters"""
    query: str = Field(description="Search query string")
    symbols: Optional[List[str]] = Field(default=None, description="Filter by stock symbols")
    companies: Optional[List[str]] = Field(default=None, description="Filter by company names")
    sectors: Optional[List[str]] = Field(default=None, description="Filter by sectors")
    categories: Optional[List[NewsCategory]] = Field(default=None, description="Filter by categories")
    sources: Optional[List[NewsSource]] = Field(default=None, description="Filter by sources")

    # Time filters
    from_date: Optional[str] = Field(default=None, description="Start date (YYYY-MM-DD)")
    to_date: Optional[str] = Field(default=None, description="End date (YYYY-MM-DD)")
    days_back: Optional[int] = Field(default=7, description="Days back from today")

    # Sentiment filters
    min_sentiment: Optional[float] = Field(default=None, description="Minimum sentiment score")
    max_sentiment: Optional[float] = Field(default=None, description="Maximum sentiment score")

    # Result controls
    limit: int = Field(default=20, description="Maximum results to return")
    page: int = Field(default=1, description="Page number for pagination")
    sort_by: str = Field(default="date", description="Sort field")
    sort_order: str = Field(default="desc", description="Sort order (asc/desc)")

    # Content filters
    min_relevance: float = Field(default=0.0, description="Minimum relevance score")
    include_content: bool = Field(default=False, description="Include full article content")
    language: str = Field(default="en", description="Article language")

class NewsSummary(BaseModel):
    """Summarized news insights for a specific context"""
    context: str = Field(description="Summary context (company, sector, etc.)")
    time_period: str = Field(description="Time period covered")

    # Article metrics
    total_articles: int = Field(description="Total articles analyzed")
    sentiment_score: float = Field(description="Average sentiment score")
    overall_sentiment: SentimentType = Field(description="Overall sentiment")

    # Key insights
    headline_summary: str = Field(description="One-line headline summary")
    executive_summary: str = Field(description="Executive summary paragraph")
    key_points: List[str] = Field(description="Key bullet points")

    # Recent developments
    breaking_news: List[NewsArticle] = Field(description="Recent breaking news")
    top_stories: List[NewsArticle] = Field(description="Top stories by relevance")

    # Trends and patterns
    emerging_themes: List[str] = Field(description="Emerging themes")
    sentiment_trends: Dict[str, float] = Field(description="Sentiment trends over time")

    # Competitive intelligence
    competitor_mentions: Dict[str, int] = Field(description="Competitor mentions")
    market_positioning: str = Field(description="Market positioning insights")

    # Risk assessment
    risk_level: str = Field(description="Overall risk level (low/medium/high)")
    risk_factors: List[str] = Field(description="Key risk factors")
    opportunities: List[str] = Field(description="Identified opportunities")

class NewsAlert(BaseModel):
    """News alert configuration and trigger"""
    alert_id: str = Field(description="Unique alert identifier")
    query: NewsQuery = Field(description="Alert query parameters")
    trigger_conditions: Dict[str, Any] = Field(description="Alert trigger conditions")

    # Alert settings
    frequency: str = Field(description="Alert frequency (realtime/hourly/daily)")
    enabled: bool = Field(default=True, description="Alert enabled status")

    # Notification settings
    notify_on_sentiment: List[SentimentType] = Field(description="Sentiment types to alert on")
    min_relevance_threshold: float = Field(description="Minimum relevance to trigger")
    max_alerts_per_day: int = Field(default=10, description="Maximum alerts per day")

    # Metadata
    created_date: str = Field(description="Alert creation date")
    last_triggered: Optional[str] = Field(description="Last trigger timestamp")
    trigger_count: int = Field(default=0, description="Total times triggered")

class MarketNewsOverview(BaseModel):
    """Overall market news overview"""
    market_date: str = Field(description="Market date")

    # Market sentiment
    market_sentiment: SentimentType = Field(description="Overall market sentiment")
    sentiment_score: float = Field(description="Market sentiment score")
    sentiment_change: float = Field(description="Sentiment change from previous period")

    # News volume
    total_articles: int = Field(description="Total market news articles")
    volume_change: float = Field(description="Volume change percentage")

    # Sector breakdown
    sector_sentiment: Dict[str, float] = Field(description="Sentiment by sector")
    sector_volume: Dict[str, int] = Field(description="News volume by sector")

    # Top movers
    most_mentioned_stocks: List[Dict[str, Any]] = Field(description="Most mentioned stocks")
    biggest_sentiment_changes: List[Dict[str, Any]] = Field(description="Biggest sentiment shifts")

    # Key themes
    trending_topics: List[TrendingTopic] = Field(description="Market trending topics")
    breaking_news: List[NewsArticle] = Field(description="Latest breaking news")

    # Economic indicators
    economic_themes: List[str] = Field(description="Economic themes in news")
    policy_mentions: List[str] = Field(description="Policy-related mentions")

    # Summary
    market_summary: str = Field(description="Market news summary")
    key_developments: List[str] = Field(description="Key market developments")