"""API clients for news data from multiple sources"""

import os
import asyncio
import aiohttp
import logging
from typing import List, Optional, Dict, Any, Union
from datetime import datetime, timedelta
import json
from urllib.parse import quote
import yfinance as yf
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import models with fallback
try:
    from .models import (
        NewsArticle, NewsFeed, NewsAnalysis, NewsQuery, NewsSummary,
        TrendingTopic, NewsAlert, MarketNewsOverview, SentimentType,
        NewsCategory, NewsSource
    )
except ImportError:
    from models import (
        NewsArticle, NewsFeed, NewsAnalysis, NewsQuery, NewsSummary,
        TrendingTopic, NewsAlert, MarketNewsOverview, SentimentType,
        NewsCategory, NewsSource
    )

logger = logging.getLogger(__name__)

class NewsAPIClient:
    """Unified client for fetching news from multiple sources"""

    def __init__(self):
        # API keys from environment
        self.marketaux_key = os.getenv("MARKETAUX_API_KEY", "")
        self.newsapi_key = os.getenv("NEWSAPI_KEY", "")
        self.finnhub_key = os.getenv("FINNHUB_API_KEY", "")
        self.alpha_vantage_key = os.getenv("ALPHA_VANTAGE_KEY", "")

        # API endpoints
        self.marketaux_base = "https://api.marketaux.com/v1"
        self.newsapi_base = "https://newsapi.org/v2"
        self.finnhub_base = "https://finnhub.io/api/v1"
        self.alpha_vantage_base = "https://www.alphavantage.co/query"

        self.session: Optional[aiohttp.ClientSession] = None

    @classmethod
    async def create(cls) -> "NewsAPIClient":
        """Create and initialize the API client"""
        client = cls()
        client.session = aiohttp.ClientSession(
            headers={
                "User-Agent": "NewsAnalysisMCP/1.0 (news-research@example.com)"
            },
            timeout=aiohttp.ClientTimeout(total=30)
        )
        return client

    async def close(self):
        """Close the HTTP session"""
        if self.session:
            await self.session.close()

    async def search_news(self, query: NewsQuery) -> NewsFeed:
        """Search for news across multiple sources"""
        start_time = datetime.now()
        all_articles = []
        sources_used = {}
        errors = []

        # Build search parameters
        search_query = query.query
        from_date = query.from_date or (datetime.now() - timedelta(days=query.days_back)).strftime('%Y-%m-%d')
        to_date = query.to_date or datetime.now().strftime('%Y-%m-%d')

        # Try Alpha Vantage news first (we have a working key)
        if self.alpha_vantage_key and (not query.sources or NewsSource.ALPHA_VANTAGE in query.sources):
            try:
                av_articles = await self._fetch_alpha_vantage_news(search_query, query.symbols)
                all_articles.extend(av_articles)
                sources_used["alpha_vantage"] = len(av_articles)
                logger.info(f"Alpha Vantage returned {len(av_articles)} articles")
            except Exception as e:
                errors.append(f"Alpha Vantage failed: {e}")
                logger.debug(f"Alpha Vantage failed: {e}")

        # Always try Yahoo Finance (no key required)
        if not query.sources or NewsSource.YAHOO_FINANCE in query.sources:
            try:
                yahoo_articles = await self._fetch_yahoo_news(search_query, query.symbols)
                all_articles.extend(yahoo_articles)
                sources_used["yahoo_finance"] = len(yahoo_articles)
                logger.info(f"Yahoo Finance returned {len(yahoo_articles)} articles")
            except Exception as e:
                errors.append(f"Yahoo Finance failed: {e}")
                logger.debug(f"Yahoo Finance failed: {e}")

        # Try MarketAux if key is configured
        if self.marketaux_key and self.marketaux_key != "your_marketaux_api_key_here" and (not query.sources or NewsSource.MARKETAUX in query.sources):
            try:
                marketaux_articles = await self._fetch_marketaux_news(search_query, from_date, to_date, query.limit)
                all_articles.extend(marketaux_articles)
                sources_used["marketaux"] = len(marketaux_articles)
                logger.info(f"MarketAux returned {len(marketaux_articles)} articles")
            except Exception as e:
                errors.append(f"MarketAux failed: {e}")
                logger.debug(f"MarketAux failed: {e}")

        # Try NewsAPI if key is configured
        if self.newsapi_key and self.newsapi_key != "your_newsapi_key_here" and (not query.sources or NewsSource.NEWSAPI in query.sources):
            try:
                newsapi_articles = await self._fetch_newsapi_news(search_query, from_date, to_date, query.limit)
                all_articles.extend(newsapi_articles)
                sources_used["newsapi"] = len(newsapi_articles)
                logger.info(f"NewsAPI returned {len(newsapi_articles)} articles")
            except Exception as e:
                errors.append(f"NewsAPI failed: {e}")
                logger.debug(f"NewsAPI failed: {e}")

        # Try Finnhub if key is configured
        if self.finnhub_key and self.finnhub_key != "your_finnhub_api_key_here" and (not query.sources or NewsSource.FINNHUB in query.sources):
            try:
                finnhub_articles = await self._fetch_finnhub_news(search_query, from_date, to_date, query.limit)
                all_articles.extend(finnhub_articles)
                sources_used["finnhub"] = len(finnhub_articles)
                logger.info(f"Finnhub returned {len(finnhub_articles)} articles")
            except Exception as e:
                errors.append(f"Finnhub failed: {e}")
                logger.debug(f"Finnhub failed: {e}")

        # Log errors if no articles found
        if not all_articles and errors:
            logger.warning(f"All news sources failed: {'; '.join(errors)}")

        # If still no articles, provide helpful error message instead of mock data
        if not all_articles:
            raise Exception(f"No news articles found. Sources tried: {list(sources_used.keys()) if sources_used else 'none'}. Configure API keys in .env file for better coverage.")

        # Apply filters and deduplication
        filtered_articles = self._filter_and_deduplicate(all_articles, query)

        # Calculate sentiment aggregates
        sentiment_counts = self._calculate_sentiment_counts(filtered_articles)
        overall_sentiment = self._determine_overall_sentiment(sentiment_counts)

        # Calculate categories breakdown
        categories = {}
        for article in filtered_articles:
            cat = article.category.value
            categories[cat] = categories.get(cat, 0) + 1

        fetch_time = int((datetime.now() - start_time).total_seconds() * 1000)

        return NewsFeed(
            query=query.query,
            articles=filtered_articles[:query.limit],
            total_articles=len(filtered_articles),
            page=query.page,
            per_page=query.limit,
            from_date=from_date,
            to_date=to_date,
            sentiment_summary=overall_sentiment,
            positive_count=sentiment_counts.get("positive", 0),
            negative_count=sentiment_counts.get("negative", 0),
            neutral_count=sentiment_counts.get("neutral", 0),
            sources=sources_used,
            categories=categories,
            fetch_time_ms=fetch_time,
            last_updated=datetime.now().isoformat()
        )

    async def _fetch_marketaux_news(self, query: str, from_date: str, to_date: str, limit: int) -> List[NewsArticle]:
        """Fetch news from MarketAux API"""
        url = f"{self.marketaux_base}/news/all"
        params = {
            'api_token': self.marketaux_key,
            'search': query,
            'published_after': from_date,
            'published_before': to_date,
            'language': 'en',
            'limit': min(limit, 100)
        }

        async with self.session.get(url, params=params) as response:
            if response.status != 200:
                raise Exception(f"MarketAux API error: {response.status}")

            data = await response.json()
            articles = []

            for item in data.get('data', []):
                # Extract sentiment from entities
                sentiment = SentimentType.NEUTRAL
                sentiment_score = 0.0
                symbols = []
                companies = []

                for entity in item.get('entities', []):
                    if 'symbol' in entity:
                        symbols.append(entity['symbol'])
                    if 'name' in entity:
                        companies.append(entity['name'])
                    if 'sentiment_score' in entity:
                        score = entity['sentiment_score']
                        if score > 0.1:
                            sentiment = SentimentType.POSITIVE
                            sentiment_score = score
                        elif score < -0.1:
                            sentiment = SentimentType.NEGATIVE
                            sentiment_score = score

                # Determine category from title and description
                category = self._categorize_article(item.get('title', ''), item.get('description', ''))

                articles.append(NewsArticle(
                    title=item.get('title', ''),
                    summary=item.get('description', ''),
                    url=item.get('url', ''),
                    source=item.get('source', 'Unknown'),
                    source_type=NewsSource.MARKETAUX,
                    published_date=item.get('published_at', ''),
                    sentiment=sentiment,
                    sentiment_score=sentiment_score,
                    relevance_score=0.8,  # MarketAux is generally high quality
                    category=category,
                    symbols=symbols,
                    companies=companies,
                    image_url=item.get('image_url', '')
                ))

            return articles

    async def _fetch_newsapi_news(self, query: str, from_date: str, to_date: str, limit: int) -> List[NewsArticle]:
        """Fetch news from NewsAPI"""
        url = f"{self.newsapi_base}/everything"
        params = {
            'apiKey': self.newsapi_key,
            'q': f'{query} AND (business OR finance OR technology)',
            'from': from_date,
            'to': to_date,
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': min(limit, 100)
        }

        async with self.session.get(url, params=params) as response:
            if response.status != 200:
                raise Exception(f"NewsAPI error: {response.status}")

            data = await response.json()
            articles = []

            for item in data.get('articles', []):
                # Simple sentiment analysis based on title and description
                title = item.get('title', '')
                description = item.get('description', '')
                sentiment, sentiment_score = self._analyze_sentiment(title, description)

                # Determine category
                category = self._categorize_article(title, description)

                # Extract potential symbols/companies from text
                symbols, companies = self._extract_entities(title + ' ' + description)

                articles.append(NewsArticle(
                    title=title,
                    summary=description,
                    content=item.get('content', ''),
                    url=item.get('url', ''),
                    source=item.get('source', {}).get('name', 'NewsAPI'),
                    source_type=NewsSource.NEWSAPI,
                    author=item.get('author', ''),
                    published_date=item.get('publishedAt', ''),
                    image_url=item.get('urlToImage', ''),
                    sentiment=sentiment,
                    sentiment_score=sentiment_score,
                    relevance_score=0.6,  # General news, moderate relevance
                    category=category,
                    symbols=symbols,
                    companies=companies
                ))

            return articles

    async def _fetch_finnhub_news(self, query: str, from_date: str, to_date: str, limit: int) -> List[NewsArticle]:
        """Fetch news from Finnhub API"""
        # Convert symbols if query contains them
        symbols = self._extract_symbols_from_query(query)
        articles = []

        if symbols:
            # Fetch company-specific news
            for symbol in symbols[:3]:  # Limit to avoid rate limits
                url = f"{self.finnhub_base}/company-news"
                params = {
                    'symbol': symbol,
                    'from': from_date,
                    'to': to_date,
                    'token': self.finnhub_key
                }

                try:
                    async with self.session.get(url, params=params) as response:
                        if response.status == 200:
                            data = await response.json()

                            for item in data[:limit//len(symbols)]:
                                sentiment, sentiment_score = self._analyze_sentiment(
                                    item.get('headline', ''),
                                    item.get('summary', '')
                                )

                                category = self._categorize_article(
                                    item.get('headline', ''),
                                    item.get('summary', '')
                                )

                                articles.append(NewsArticle(
                                    title=item.get('headline', ''),
                                    summary=item.get('summary', ''),
                                    url=item.get('url', ''),
                                    source=item.get('source', 'Finnhub'),
                                    source_type=NewsSource.FINNHUB,
                                    published_date=datetime.fromtimestamp(
                                        item.get('datetime', 0)
                                    ).isoformat() if item.get('datetime') else '',
                                    image_url=item.get('image', ''),
                                    sentiment=sentiment,
                                    sentiment_score=sentiment_score,
                                    relevance_score=0.9,  # Company-specific news is highly relevant
                                    category=category,
                                    symbols=[symbol],
                                    companies=[]
                                ))
                except Exception as e:
                    logger.debug(f"Finnhub symbol {symbol} failed: {e}")

        return articles

    async def _fetch_alpha_vantage_news(self, query: str, symbols: Optional[List[str]] = None) -> List[NewsArticle]:
        """Fetch news from Alpha Vantage API"""
        articles = []

        # Alpha Vantage news endpoint
        url = f"{self.alpha_vantage_base}"
        params = {
            'function': 'NEWS_SENTIMENT',
            'apikey': self.alpha_vantage_key,
            'limit': 50
        }

        # Add specific symbols if provided
        if symbols and len(symbols) > 0:
            params['tickers'] = ','.join(symbols[:5])  # Limit to 5 symbols
        else:
            # Use broad market keywords for general queries
            params['topics'] = 'technology,financial_markets'

        try:
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()

                    # Alpha Vantage returns news in 'feed' array
                    for item in data.get('feed', [])[:20]:  # Limit results
                        # Extract sentiment
                        sentiment_data = item.get('overall_sentiment_score', 0.0)
                        sentiment_score = float(sentiment_data)

                        if sentiment_score > 0.1:
                            sentiment = SentimentType.POSITIVE
                        elif sentiment_score < -0.1:
                            sentiment = SentimentType.NEGATIVE
                        else:
                            sentiment = SentimentType.NEUTRAL

                        # Extract symbols from ticker sentiments
                        symbols_list = []
                        ticker_sentiment = item.get('ticker_sentiment', [])
                        for ticker in ticker_sentiment:
                            symbols_list.append(ticker.get('ticker', ''))

                        # Determine category
                        title = item.get('title', '')
                        summary = item.get('summary', '')
                        category = self._categorize_article(title, summary)

                        articles.append(NewsArticle(
                            title=title,
                            summary=summary,
                            url=item.get('url', ''),
                            source=item.get('source', 'Alpha Vantage'),
                            source_type=NewsSource.ALPHA_VANTAGE,
                            author=', '.join(item.get('authors', [])),
                            published_date=item.get('time_published', ''),
                            image_url=item.get('banner_image', ''),
                            sentiment=sentiment,
                            sentiment_score=sentiment_score,
                            relevance_score=0.8,  # Alpha Vantage provides quality financial news
                            category=category,
                            symbols=symbols_list,
                            companies=[]
                        ))

                else:
                    logger.debug(f"Alpha Vantage API returned status {response.status}")

        except Exception as e:
            logger.debug(f"Alpha Vantage news fetch failed: {e}")

        return articles

    async def _fetch_yahoo_news(self, query: str, symbols: Optional[List[str]] = None) -> List[NewsArticle]:
        """Fetch news from Yahoo Finance as fallback"""
        articles = []

        # If symbols provided, get news for those symbols
        if symbols:
            for symbol in symbols[:3]:  # Limit to avoid issues
                try:
                    ticker = yf.Ticker(symbol)
                    news = ticker.news

                    if news:
                        for item in news[:5]:  # Limit per symbol
                            # Extract from new nested structure
                            content = item.get('content', {})
                            title = content.get('title', '')
                            summary = content.get('summary', '')

                            # Extract URL from nested structure
                            url = ''
                            if 'clickThroughUrl' in content:
                                url = content['clickThroughUrl'].get('url', '')
                            elif 'canonicalUrl' in content:
                                url = content['canonicalUrl'].get('url', '')

                            # Extract provider/source
                            provider = content.get('provider', {})
                            source_name = provider.get('displayName', 'Yahoo Finance')

                            # Extract published date
                            pub_date = content.get('pubDate', '')

                            # Extract thumbnail
                            thumbnail = content.get('thumbnail', {})
                            image_url = thumbnail.get('originalUrl', '')

                            sentiment, sentiment_score = self._analyze_sentiment(
                                title, summary
                            )

                            articles.append(NewsArticle(
                                title=title,
                                summary=summary,
                                url=url,
                                source=source_name,
                                source_type=NewsSource.YAHOO_FINANCE,
                                published_date=pub_date,
                                sentiment=sentiment,
                                sentiment_score=sentiment_score,
                                relevance_score=0.7,
                                category=NewsCategory.FINANCIAL,
                                symbols=[symbol],
                                companies=[],
                                image_url=image_url
                            ))
                except Exception as e:
                    logger.debug(f"Yahoo Finance symbol {symbol} failed: {e}")
        else:
            # For general queries without symbols, Yahoo Finance doesn't provide news search
            # This is expected - we rely on other sources for general news
            logger.debug(f"Yahoo Finance: No symbols provided for query '{query}', skipping general news search")

        return articles

    def _analyze_sentiment(self, title: str, description: str) -> tuple[SentimentType, float]:
        """Simple sentiment analysis based on keywords"""
        text = (title + ' ' + description).lower()

        positive_words = [
            'surge', 'gain', 'rise', 'up', 'beat', 'exceed', 'positive', 'growth',
            'bullish', 'rally', 'strong', 'good', 'great', 'excellent', 'success',
            'profit', 'revenue', 'earnings', 'breakthrough', 'milestone'
        ]

        negative_words = [
            'fall', 'drop', 'down', 'miss', 'loss', 'decline', 'negative', 'cut',
            'bearish', 'weak', 'poor', 'bad', 'concern', 'worry', 'risk',
            'debt', 'deficit', 'lawsuit', 'investigation', 'scandal'
        ]

        pos_count = sum(1 for word in positive_words if word in text)
        neg_count = sum(1 for word in negative_words if word in text)

        if pos_count > neg_count:
            score = min(0.8, (pos_count - neg_count) * 0.2)
            return SentimentType.POSITIVE, score
        elif neg_count > pos_count:
            score = max(-0.8, (pos_count - neg_count) * 0.2)
            return SentimentType.NEGATIVE, score
        else:
            return SentimentType.NEUTRAL, 0.0

    def _categorize_article(self, title: str, description: str) -> NewsCategory:
        """Categorize article based on content"""
        text = (title + ' ' + description).lower()

        if any(word in text for word in ['earnings', 'revenue', 'profit', 'eps', 'quarterly']):
            return NewsCategory.EARNINGS
        elif any(word in text for word in ['merger', 'acquire', 'acquisition', 'buyout']):
            return NewsCategory.MERGER
        elif any(word in text for word in ['product', 'launch', 'release', 'innovation']):
            return NewsCategory.PRODUCT
        elif any(word in text for word in ['regulation', 'regulatory', 'sec', 'fda', 'policy']):
            return NewsCategory.REGULATORY
        elif any(word in text for word in ['ceo', 'cfo', 'executive', 'management', 'leadership']):
            return NewsCategory.LEADERSHIP
        elif any(word in text for word in ['technology', 'ai', 'software', 'digital', 'tech']):
            return NewsCategory.TECHNOLOGY
        elif any(word in text for word in ['market', 'trading', 'stock', 'share', 'index']):
            return NewsCategory.MARKET
        elif any(word in text for word in ['financial', 'finance', 'bank', 'credit', 'loan']):
            return NewsCategory.FINANCIAL
        else:
            return NewsCategory.GENERAL

    def _extract_entities(self, text: str) -> tuple[List[str], List[str]]:
        """Extract potential stock symbols and company names from text"""
        # Simple pattern matching for symbols (2-5 uppercase letters)
        import re

        # Find potential stock symbols
        symbol_pattern = r'\b[A-Z]{2,5}\b'
        potential_symbols = re.findall(symbol_pattern, text)

        # Filter out common words that aren't symbols
        common_words = {'THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HAD', 'HER', 'WAS', 'ONE', 'OUR', 'OUT', 'DAY', 'GET', 'HAS', 'HIM', 'HOW', 'ITS', 'MAY', 'NEW', 'NOW', 'OLD', 'SEE', 'TWO', 'WHO', 'BOY', 'DID', 'ITS', 'LET', 'PUT', 'SAY', 'SHE', 'TOO', 'USE'}
        symbols = [s for s in potential_symbols if s not in common_words]

        # Simple company name extraction (words ending with Inc, Corp, Ltd, etc.)
        company_pattern = r'\b[A-Z][a-zA-Z\s]+(?:Inc|Corp|Corporation|Ltd|Limited|LLC|Co)\b'
        companies = re.findall(company_pattern, text)

        return symbols[:5], companies[:5]  # Limit results

    def _extract_symbols_from_query(self, query: str) -> List[str]:
        """Extract stock symbols from query string"""
        symbols, _ = self._extract_entities(query)
        return symbols

    def _filter_and_deduplicate(self, articles: List[NewsArticle], query: NewsQuery) -> List[NewsArticle]:
        """Filter and deduplicate articles based on query parameters"""
        filtered = []
        seen_urls = set()
        seen_titles = set()

        for article in articles:
            # Skip duplicates by URL
            if article.url in seen_urls:
                continue

            # Skip duplicates by similar titles (first 50 chars)
            title_key = article.title.lower()[:50]
            if title_key in seen_titles:
                continue

            # Apply filters
            if query.min_relevance and article.relevance_score < query.min_relevance:
                continue

            if query.min_sentiment and article.sentiment_score < query.min_sentiment:
                continue

            if query.max_sentiment and article.sentiment_score > query.max_sentiment:
                continue

            # Apply symbol filter
            if query.symbols:
                if not any(symbol in article.symbols for symbol in query.symbols):
                    continue

            # Apply category filter
            if query.categories:
                if article.category not in query.categories:
                    continue

            filtered.append(article)
            seen_urls.add(article.url)
            seen_titles.add(title_key)

        # Sort by relevance and date
        if query.sort_by == "relevance":
            filtered.sort(key=lambda x: x.relevance_score, reverse=(query.sort_order == "desc"))
        else:  # sort by date
            filtered.sort(key=lambda x: x.published_date, reverse=(query.sort_order == "desc"))

        return filtered

    def _calculate_sentiment_counts(self, articles: List[NewsArticle]) -> Dict[str, int]:
        """Calculate sentiment distribution"""
        counts = {"positive": 0, "negative": 0, "neutral": 0, "bullish": 0, "bearish": 0}

        for article in articles:
            counts[article.sentiment.value] = counts.get(article.sentiment.value, 0) + 1

        return counts

    def _determine_overall_sentiment(self, sentiment_counts: Dict[str, int]) -> SentimentType:
        """Determine overall sentiment from counts"""
        total = sum(sentiment_counts.values())
        if total == 0:
            return SentimentType.NEUTRAL

        positive_ratio = (sentiment_counts.get("positive", 0) + sentiment_counts.get("bullish", 0)) / total
        negative_ratio = (sentiment_counts.get("negative", 0) + sentiment_counts.get("bearish", 0)) / total

        if positive_ratio > 0.6:
            return SentimentType.POSITIVE
        elif negative_ratio > 0.6:
            return SentimentType.NEGATIVE
        elif positive_ratio > negative_ratio * 1.5:
            return SentimentType.POSITIVE
        elif negative_ratio > positive_ratio * 1.5:
            return SentimentType.NEGATIVE
        else:
            return SentimentType.NEUTRAL

    async def get_trending_topics(self, time_period: str = "24h") -> List[TrendingTopic]:
        """Get trending news topics"""
        # Validate time period
        valid_periods = ["24h", "7d", "30d"]
        if time_period not in valid_periods:
            raise ValueError(f"Invalid time period '{time_period}'. Must be one of: {valid_periods}")

        # Map time periods to days
        days_map = {"24h": 1, "7d": 7, "30d": 30}
        days_back = days_map[time_period]

        query = NewsQuery(
            query="trending finance business technology",
            days_back=days_back,
            limit=50
        )

        try:
            news_feed = await self.search_news(query)
        except Exception as e:
            logger.error(f"Failed to fetch news for trending topics: {e}")
            return []  # Return empty list rather than crashing

        # Simple topic extraction from titles
        topic_counts = {}
        for article in news_feed.articles:
            words = article.title.lower().split()
            for word in words:
                if len(word) > 4 and word.isalpha():  # Skip short words and numbers
                    topic_counts[word] = topic_counts.get(word, 0) + 1

        # Convert to trending topics
        trending = []
        for topic, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            if count >= 2:  # Minimum threshold
                # Get sample headlines for this topic
                sample_headlines = [
                    article.title for article in news_feed.articles
                    if topic in article.title.lower()
                ][:3]

                trending.append(TrendingTopic(
                    topic=topic.title(),
                    article_count=count,
                    sentiment=SentimentType.NEUTRAL,  # Would need more sophisticated analysis
                    sentiment_score=0.0,
                    trend_score=min(1.0, count / 10.0),
                    sample_headlines=sample_headlines
                ))

        return trending

    async def get_market_overview(self) -> MarketNewsOverview:
        """Get overall market news overview"""
        query = NewsQuery(
            query="market economy finance stocks",
            days_back=1,
            limit=100
        )

        news_feed = await self.search_news(query)

        # Calculate metrics
        sentiment_counts = self._calculate_sentiment_counts(news_feed.articles)
        overall_sentiment = self._determine_overall_sentiment(sentiment_counts)

        # Get trending topics
        trending = await self.get_trending_topics("24h")

        # Mock sector data (would need real sector classification)
        sector_sentiment = {
            "Technology": 0.2,
            "Finance": -0.1,
            "Healthcare": 0.1,
            "Energy": -0.3,
            "Consumer": 0.0
        }

        return MarketNewsOverview(
            market_date=datetime.now().strftime('%Y-%m-%d'),
            market_sentiment=overall_sentiment,
            sentiment_score=sum(a.sentiment_score for a in news_feed.articles) / len(news_feed.articles) if news_feed.articles else 0.0,
            sentiment_change=0.0,  # Would need historical comparison
            total_articles=news_feed.total_articles,
            volume_change=0.0,  # Would need historical comparison
            sector_sentiment=sector_sentiment,
            sector_volume={"Technology": 25, "Finance": 30, "Healthcare": 15, "Energy": 10, "Consumer": 20},
            most_mentioned_stocks=[],  # Would extract from articles
            biggest_sentiment_changes=[],  # Would need historical data
            trending_topics=trending,
            breaking_news=news_feed.articles[:5],
            economic_themes=["inflation", "interest rates", "GDP"],
            policy_mentions=["Federal Reserve", "SEC", "regulation"],
            market_summary="Mixed sentiment in today's market news with technology leading gains.",
            key_developments=["Fed policy decisions", "Earnings season continues", "Tech sector updates"]
        )