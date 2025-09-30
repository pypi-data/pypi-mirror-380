# Company News MCP Server - Evaluation Prompts

Evaluation prompts to test all Company News MCP Server tools, resources, and capabilities.

## Quick Reference
- **6 Tools**: search_news, get_trending_topics, analyze_sentiment, get_market_overview, summarize_news, get_company_news
- **4 Resources**: news search, trending topics, market overview, company news
- **5 Prompts**: News Analysis Report, Daily News Briefing, Competitive Intelligence, Earnings Season Monitor, Crisis Communication Monitor

## 🛠️ Tools Evaluation Prompts

### 1. search_news
```
# Basic News Search
Search for news about "Apple" from the last 7 days and limit to 20 articles.

# Technology News Search
Search for "artificial intelligence" news from the last 3 days with minimum relevance of 0.5.

# Company-Specific Search
Search for news about Tesla (TSLA) with symbol filtering and include full content.

# Multi-Symbol Search
Search for "earnings" news filtering by symbols ["AAPL", "MSFT", "GOOGL"] from last 14 days.

# Market Event Search
Search for "Federal Reserve" news from last 30 days with relevance threshold 0.3.

# Error Test
Try to search for news with invalid parameters (negative days_back or limit > 1000).
```

### 2. get_trending_topics
```
# Daily Trending Topics
Get trending topics for the last 24 hours with limit of 10.

# Weekly Trends
Get trending topics for the last 7 days with limit of 15.

# Monthly Analysis
Get trending topics for the last 30 days and analyze momentum scores.

# Custom Limit
Get trending topics for 24h with limit of 5 to see top trends only.

# Error Test
Try to get trending topics with invalid time period "6h" or "90d".
```

### 3. analyze_sentiment
```
# Company Sentiment Analysis
Analyze sentiment for Apple over the last 7 days.

# Market Event Sentiment
Analyze sentiment for "inflation" over the last 30 days.

# Technology Sentiment
Analyze sentiment for "AI and machine learning" over the last 14 days.

# Symbol-Specific Sentiment
Analyze sentiment for Tesla with symbol filter ["TSLA"] over 7 days.

# Financial Sector Sentiment
Analyze sentiment for "banking sector" over 30 days.

# Error Test
Try sentiment analysis with invalid symbol "INVALID123" or time period "45d".
```

### 4. get_market_overview
```
# Current Market Overview
Get comprehensive market news overview and sentiment.

# Daily Market Check
Get market overview to understand current sentiment and trends.

# Pre-Market Analysis
Get market overview for morning briefing preparation.

# End-of-Day Summary
Get market overview for daily market wrap-up.

# Error Test
Test market overview with no parameters (should work with defaults).
```

### 5. summarize_news
```
# Company News Summary
Summarize news for "Apple" over the last 24 hours analyzing up to 50 articles.

# Sector Summary
Summarize "technology sector" news over 7 days with symbol focus ["AAPL", "MSFT"].

# Market Event Summary
Summarize "earnings season" news over 30 days with maximum 100 articles.

# Crisis Summary
Summarize news about a company crisis over 7 days.

# Industry Summary
Summarize "electric vehicle" industry news over 14 days.

# Error Test
Try to summarize with invalid context or extremely large max_articles (10000).
```

### 6. get_company_news
```
# Apple Company News
Get news for AAPL from the last 7 days with limit of 20.

# Tesla Recent News
Get news for TSLA from the last 3 days with limit of 15.

# Microsoft News
Get news for MSFT from the last 14 days with limit of 25.

# Banking Stock News
Get news for JPM from the last 7 days.

# Tech Giant News
Get news for GOOGL from the last 10 days.

# Error Test
Try to get company news for invalid symbol "BADSTOCK123".
```

## 📊 Resources Test Prompts

### 1. news://search/{query}
```
# Basic Search Resource
Access news search resource for "Apple" and retrieve article data.

# Technology Search
Get search resource for "artificial intelligence" and analyze results.

# Market Search
Access search resource for "Federal Reserve" policy news.

# Company Search
Get search resource for "Tesla earnings" and review coverage.

# Error Test
Try to access search resource with empty query or special characters.
```

### 2. news://trending/{time_period}
```
# Daily Trending Resource
Access trending topics resource for "24h" and show momentum scores.

# Weekly Trends Resource
Get trending resource for "7d" and analyze topic evolution.

# Monthly Trends
Access trending resource for "30d" and identify long-term themes.

# Error Test
Try to access trending resource with invalid period "6h" or "45d".
```

### 3. news://market-overview
```
# Market Overview Resource
Access market overview resource and analyze current sentiment.

# Daily Market Resource
Get market overview resource for comprehensive market intelligence.

# Market Snapshot
Access market overview resource for quick market pulse check.

# Error Test
Test market overview resource access (should always work).
```

### 4. news://company/{symbol}
```
# Apple Company Resource
Access company news resource for AAPL and review recent coverage.

# Tesla Company Resource
Get company news resource for TSLA and analyze article quality.

# Microsoft Resource
Access company news resource for MSFT and check data completeness.

# Banking Company Resource
Get company news resource for JPM and review financial coverage.

# Error Test
Try to access company resource for invalid symbol "FAKE123".
```

## 📝 Prompts Test Cases

### 1. News Analysis Report Prompt
```
# Technology Company Analysis
Use News Analysis Report prompt for Apple with 7-day time period.

# Market Event Analysis
Apply News Analysis Report prompt to "Federal Reserve policy" for 30 days.

# Sector Analysis
Use News Analysis Report prompt for "electric vehicle sector" over 14 days.

# Crisis Analysis
Apply News Analysis Report prompt to recent corporate crisis for 7 days.
```

### 2. Daily News Briefing Prompt
```
# Technology Focus Briefing
Use Daily News Briefing prompt focusing on ["AI", "Apple", "Microsoft"].

# Financial Markets Briefing
Apply Daily News Briefing with focus areas ["Fed policy", "inflation", "banking"].

# Tech Earnings Briefing
Use Daily News Briefing for ["earnings", "technology", "guidance"].

# Market Volatility Briefing
Apply Daily News Briefing focusing on ["market volatility", "recession", "inflation"].
```

### 3. Competitive Intelligence Prompt
```
# Tech Giants Intelligence
Use Competitive Intelligence prompt for Apple vs ["Microsoft", "Google", "Amazon"].

# Auto Industry Intelligence
Apply Competitive Intelligence for Tesla vs ["Ford", "GM", "Rivian"].

# Banking Sector Intelligence
Use Competitive Intelligence for JPMorgan vs ["Bank of America", "Wells Fargo"].

# Streaming Competition
Apply Competitive Intelligence for Netflix vs ["Disney", "Amazon Prime", "Apple TV"].
```

### 4. Earnings Season Monitor Prompt
```
# Apple Earnings Monitor
Use Earnings Season Monitor prompt for AAPL during earnings period.

# Tesla Earnings Tracking
Apply Earnings Season Monitor prompt for TSLA around earnings date.

# Microsoft Earnings Analysis
Use Earnings Season Monitor prompt for MSFT quarterly results.

# Banking Earnings Review
Apply Earnings Season Monitor prompt for JPM earnings coverage.
```

### 5. Crisis Communication Monitor Prompt
```
# Corporate Crisis Monitor
Use Crisis Communication Monitor prompt for company facing reputation issues.

# Product Recall Monitor
Apply Crisis Communication Monitor for product safety crisis.

# Data Breach Monitor
Use Crisis Communication Monitor for cybersecurity incident.

# Regulatory Crisis Monitor
Apply Crisis Communication Monitor for regulatory investigation.
```

## 🧪 Edge Cases & Error Testing

### Invalid Input Tests
```
# Bad Query Strings
Search for news with empty string "" or special characters "@@##".

# Invalid Symbols
Get company news for "INVALID123" and verify error handling.

# Mixed Valid/Invalid
Search news with symbols ["AAPL", "BADSTOCK", "MSFT"] and test behavior.

# Extreme Values
Search news with days_back = 0 or limit = 0.

# Negative Parameters
Try sentiment analysis with days_back = -5 or limit = -10.
```

### Parameter Edge Cases
```
# Invalid Time Periods
Get trending topics with period "6h" or "90d" (not supported).

# Extreme Limits
Search news with limit of 10000 (test system limits).

# Zero Values
Summarize news with max_articles = 0.

# Very Large Time Ranges
Analyze sentiment with time_period "365d" (if supported).

# Special Characters in Queries
Search for news with query "Apple & Microsoft | Google".
```

### Data Availability Tests
```
# Very Recent Events
Search for news from last 1 hour (test real-time capabilities).

# Obscure Companies
Get company news for small-cap or international symbols.

# Non-Market Hours
Test news availability during weekends or holidays.

# International Markets
Search for news about foreign companies or markets.
```

### Performance Tests
```
# Large Result Sets
Search for "technology" with limit of 500 and measure response time.

# Complex Sentiment Analysis
Analyze sentiment for broad query "market volatility" over 30 days.

# Multiple Concurrent Requests
Get trending topics and market overview simultaneously.

# Resource-Heavy Summary
Summarize news analyzing 1000 articles for comprehensive topic.
```

## 📈 Complete Test Scenarios

### Scenario 1: Daily Market Intelligence Workflow
```
# Morning Market Brief
1. Get market overview for current sentiment
2. Get trending topics for last 24h
3. Search for "earnings" news from yesterday
4. Summarize key market developments
5. Use Daily News Briefing prompt for comprehensive brief
```

### Scenario 2: Company Research Pipeline
```
# Deep Company Analysis
1. Get company news for AAPL from last 7 days
2. Analyze sentiment for Apple over same period
3. Search for "Apple earnings" or "Apple product" news
4. Use News Analysis Report prompt for comprehensive review
5. Compare with competitor intelligence
```

### Scenario 3: Crisis Management Response
```
# Crisis Monitoring Workflow
1. Search for news about company crisis
2. Analyze sentiment to gauge severity
3. Get trending topics to see if crisis is trending
4. Use Crisis Communication Monitor prompt
5. Summarize crisis developments and impacts
```

### Scenario 4: Earnings Season Coverage
```
# Comprehensive Earnings Analysis
1. Search for earnings news with relevant symbols
2. Get company-specific news for each symbol
3. Analyze sentiment around earnings announcements
4. Use Earnings Season Monitor prompt
5. Summarize earnings season performance
```

### Scenario 5: Competitive Intelligence Gathering
```
# Competitor Analysis Process
1. Search news for each competitor company
2. Analyze sentiment for competitive landscape
3. Get trending topics related to industry
4. Use Competitive Intelligence prompt
5. Summarize competitive positioning insights
```

### Scenario 6: Combined Company Research + News Analysis
```
# Integrated Analysis (using both MCPs)
1. Use Company MCP: Get company profile and financials for AAPL
2. Use News MCP: Get recent news and sentiment for Apple
3. Use Company MCP: Get analyst ratings and insider trading
4. Use News MCP: Analyze news sentiment around earnings
5. Combined: Fundamental analysis vs news sentiment correlation
6. Integrated recommendation: Financial health + media perception
```

## ✅ Quick Validation Checklist

### Essential Tests
- [ ] Basic news search: Search for "Apple" news from last 7 days
- [ ] Trending topics: Get trending topics for 24h
- [ ] Sentiment analysis: Analyze sentiment for Tesla over 7 days
- [ ] Market overview: Get current market news overview
- [ ] News summary: Summarize "technology" news over 24h
- [ ] Company news: Get AAPL company-specific news
- [ ] Resource access: Get news search and trending resources
- [ ] Prompt generation: News Analysis Report for any topic
- [ ] Error handling: Test with "INVALID123" symbol
- [ ] Performance: All tools respond within 10 seconds

### Performance Expectations
- News search: < 8 seconds
- Trending topics: < 5 seconds
- Sentiment analysis: < 12 seconds
- Market overview: < 6 seconds
- News summary: < 15 seconds
- Company news: < 8 seconds

### Critical Features
- [ ] All tools return structured news data with sentiment scores
- [ ] Progress reporting visible during data fetching
- [ ] Invalid inputs handled gracefully with error messages
- [ ] News articles include titles, sources, dates, and sentiment
- [ ] Trending topics show momentum and related symbols
- [ ] Sentiment analysis provides distribution and insights
- [ ] Market overview covers current themes and sentiment
- [ ] News summaries are concise and actionable
- [ ] Company news is relevant and symbol-specific
- [ ] Resources provide JSON-formatted data
- [ ] Prompts generate comprehensive analysis templates

### Data Quality Checks
- [ ] News articles have valid URLs and publication dates
- [ ] Sentiment scores are within expected range (-1 to 1)
- [ ] Trending topics include relevant financial context
- [ ] Market overview reflects current market conditions
- [ ] News summaries capture key themes accurately
- [ ] Company news is properly filtered by symbol
- [ ] Sources are diverse and reputable
- [ ] Articles are recent and relevant to queries

---

**🎯 QUICK START: Run these 5 prompts to validate core functionality:**

1. `Search for news about "Apple" from the last 7 days and show sentiment`
2. `Get trending topics for the last 24 hours and identify market themes`
3. `Analyze sentiment for Tesla over the last 7 days and show distribution`
4. `Get current market overview and summarize key developments`
5. `Summarize news about "Federal Reserve" from last 30 days with key insights`

**🔗 COMBINED MCP TESTING: Validate integration with Company Research MCP:**

6. `Get AAPL company profile (Company MCP) and recent news sentiment (News MCP)`
7. `Compare Tesla financials (Company) with recent news coverage (News)`
8. `Get Microsoft analyst ratings (Company) and earnings news sentiment (News)`
9. `Search technology companies (Company) and analyze sector news trends (News)`
10. `Company due diligence (Company) combined with crisis monitoring (News)`

**🚨 EDGE CASE VALIDATION: Test error handling and limits:**

11. `Search news with invalid symbol "INVALID123" and verify error handling`
12. `Get trending topics with invalid time period "6h" and check response`
13. `Analyze sentiment with extreme parameters (days_back: -5, limit: 0)`
14. `Test performance with large result sets (limit: 500 articles)`
15. `Validate resource access with malformed URIs and special characters`