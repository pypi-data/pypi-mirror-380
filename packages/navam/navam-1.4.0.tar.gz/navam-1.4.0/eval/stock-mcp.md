# Stock MCP Server - Evaluation Prompts

Evaluation prompts to test all Stock AI MCP Server tools, resources, and capabilities.

## Quick Reference
- **7 Tools**: analyze_stock, compare_stocks, screen_stocks, calculate_portfolio_value, get_moving_averages, get_historical_price, find_trending_stocks
- **6 Resources**: stock quotes, history, fundamentals, indicators, market overview, news
- **7 Prompts**: Stock Research, Portfolio Review, Market Analysis, Earnings Analysis, Risk Assessment, Sector Comparison, Technical Setup

## 🛠️ Tools Evaluation Prompts

### 1. analyze_stock
```
# Basic Test
Analyze AAPL stock and show me the current price, RSI, moving averages, P/E ratio, and your buy/sell recommendation.

# Growth Stock
Analyze NVDA and tell me if it's overbought based on technical indicators.

# Value Stock
Analyze BRK-B and evaluate its fundamental metrics.

# Error Test
Try to analyze stock symbol INVALID123.
```

### 2. compare_stocks
```
# Tech Comparison
Compare AAPL, MSFT, and GOOGL. Which has the best performance today and which has the highest P/E ratio?

# Banking Sector
Compare JPM, BAC, and WFC. Show me their market caps and identify the best performer.

# Mixed Test
Compare AAPL, MSFT, and BADSTOCK123 (test error handling).
```

### 3. screen_stocks
```
# Tech Screen
Screen technology stocks with minimum price of $100. Show me the top 3.

# Healthcare Screen
Find healthcare stocks under $200 per share.

# Finance Screen
Screen finance stocks between $50-$300 price range.
```

### 4. calculate_portfolio_value
```
# Tech Portfolio Test
Calculate my portfolio value: 100 AAPL at $150 cost basis, 50 MSFT at $200 cost basis.

# Diversified Test
Value my portfolio: 100 AAPL ($150), 75 JPM ($120), 200 XOM ($60).

# Single Position
Calculate value of 500 TSLA shares bought at $180.
```

### 5. get_moving_averages
```
# Standard Averages
Get 20, 50, and 200-day moving averages for AAPL.

# Short-term Analysis
Calculate 5, 10, 20-day moving averages for TSLA.

# Custom Periods
Get moving averages for SPY using periods: 9, 21, 50, 100.
```

### 6. get_historical_price
```
# Recent Date
What was AAPL's price on 2025-01-15?

# Specific Date
Get TSLA's closing price on 2024-12-20.

# Weekend Test
What was MSFT's price on 2024-12-28 (Saturday)?
```

### 7. find_trending_stocks
```
# Uptrend Search
Find the top 5 uptrending stocks right now.

# Downtrend Search
Find 3 stocks in strong downtrends.

# Custom Limit
Find trending stocks but limit results to 8.
```

## 📊 Resources Test Prompts

### 1. stock://{symbol}/quote
```
# Basic Quote
Get me the current quote for AAPL including price, volume, and market cap.

# Multiple Quotes
Show me quotes for TSLA, NVDA, and SPY.

# Invalid Test
Try to get a quote for stock symbol INVALID.
```

### 2. stock://{symbol}/history/{period}
```
# Recent History
Get AAPL's price history for the last 1 month.

# Extended History
Show me TSLA's price history over the past 1 year.

# Short Period
Get NVDA's history for the last 5 days.
```

### 3. stock://{symbol}/fundamentals
```
# Tech Fundamentals
Get fundamental data for AAPL including P/E ratio, EPS, and debt levels.

# Banking Fundamentals
Show me JPM's fundamental metrics.

# Growth vs Value
Compare fundamentals between NVDA (growth) and JNJ (value).
```

### 4. stock://{symbol}/indicators
```
# Technical Indicators
Get technical indicators for TSLA including RSI, MACD, and moving averages.

# Market Indicators
Show me technical indicators for SPY.

# Volatile Stock
Get indicators for a high-volatility stock like AMC.
```

### 5. market://overview
```
# Market Status
Show me the current market overview with major indices performance.

# Index Performance
What are the Dow Jones, S&P 500, and NASDAQ doing today?
```

### 6. news://{symbol}/latest
```
# Stock News
Get the latest news for AAPL.

# Market News
Show me recent news for SPY.
```

## 📝 Prompts Test Cases

### 1. Stock Research Prompt
```
# Basic Research
Use the Stock Research prompt to analyze AAPL over a 1-year timeframe.

# Growth Stock Focus
Research NVDA using the Stock Research prompt with a 6-month timeframe.

# Value Stock Analysis
Use Stock Research prompt for BRK-B with 2-year timeframe.
```

### 2. Portfolio Review Prompt
```
# Conservative Review
Use Portfolio Review prompt with "conservative" risk tolerance.

# Aggressive Strategy
Apply Portfolio Review prompt with "aggressive" risk tolerance.

# Balanced Approach
Use Portfolio Review with default "moderate" risk tolerance.
```

### 3. Market Analysis Prompt
```
# Overall Market
Use Market Analysis prompt focusing on "overall" market conditions.

# Sector Focus
Apply Market Analysis with "sector" focus.

# Trend Analysis
Use Market Analysis prompt with "trend" focus.
```

### 4. Earnings Analysis Prompt
```
# Standard Earnings
Use Earnings Analysis prompt for AAPL covering 4 quarters.

# Extended Period
Apply Earnings Analysis for TSLA over 8 quarters.

# Recent Focus
Use Earnings Analysis for MSFT covering 2 quarters.
```

### 5. Risk Assessment Prompt
```
# Individual Stock
Use Risk Assessment prompt for "stock" investment type.

# Portfolio Level
Apply Risk Assessment for "portfolio" investment type.

# Sector Analysis
Use Risk Assessment prompt for "sector" investment type.
```

### 6. Sector Comparison Prompt
```
# Tech vs Finance
Use Sector Comparison prompt for "technology,finance" sectors.

# Healthcare vs Energy
Compare "healthcare,energy" using Sector Comparison prompt.

# Multi-sector
Use Sector Comparison for "technology,finance,healthcare" sectors.
```

### 7. Technical Setup Prompt
```
# Breakout Patterns
Use Technical Setup prompt for "breakout" pattern type.

# Reversal Signals
Apply Technical Setup prompt for "reversal" patterns.

# Momentum Plays
Use Technical Setup prompt for "momentum" patterns.
```

## 🧪 Edge Cases & Error Testing

### Invalid Input Tests
```
# Bad Symbols
Analyze stock "INVALID123" and see error handling.

# Mixed Valid/Invalid
Compare AAPL, MSFT, and BADSTOCK123.

# Empty Inputs
Try analyzing an empty string symbol.

# Special Characters
Test with symbols like "AAPL@" or "MSFT#".
```

### Date & Period Tests
```
# Weekend Date
Get AAPL's price on 2024-12-28 (Saturday).

# Future Date
What was MSFT's price on 2025-12-31?

# Invalid Period
Get TSLA's history for "invalid_period".

# Very Old Date
Get price for AAPL on 1990-01-01.
```

### Portfolio Edge Cases
```
# Zero Quantity
Calculate portfolio with 0 shares of AAPL at $150 cost basis.

# Negative Values
Portfolio: -100 AAPL shares at $150 cost basis.

# Missing Cost Basis
Portfolio: 100 AAPL shares with no cost basis specified.

# Extreme Numbers
Portfolio: 1,000,000 AAPL shares at $0.01 cost basis.
```

### Performance Tests
```
# Multiple Stocks
Compare 15 stocks at once: AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM, JNJ, PG, KO, WMT, V, MA, DIS.

# Concurrent Analysis
Analyze AAPL, TSLA, and NVDA simultaneously.

# Large Portfolio
Calculate portfolio with 20+ positions.

# Data-heavy Request
Get 5-year history for 5 different stocks.
```

## 📈 Complete Test Scenarios

### Scenario 1: Day Trading Setup
```
# Quick Analysis Chain
1. Analyze TSLA for current price and RSI
2. Get 5, 10, 20-day moving averages for TSLA
3. Find trending stocks in "up" direction, limit 5
4. Use Technical Setup prompt for "momentum" patterns
```

### Scenario 2: Long-term Investment Research
```
# Deep Fundamental Analysis
1. Use Stock Research prompt for AAPL, 2-year timeframe
2. Get AAPL fundamentals (P/E, EPS, debt ratios)
3. Compare AAPL, MSFT, GOOGL fundamentals and performance
4. Use Risk Assessment prompt for "stock" type
```

### Scenario 3: Portfolio Management
```
# Portfolio Evaluation & Rebalancing
1. Calculate portfolio: 100 AAPL ($150), 50 MSFT ($200), 75 NVDA ($100)
2. Use Portfolio Review prompt, "moderate" risk tolerance
3. Screen technology stocks, minimum $100 price
4. Compare current holdings: AAPL, MSFT, NVDA
```

### Scenario 4: Market Analysis
```
# Market Timing & Sector Rotation
1. Get market overview (indices performance)
2. Use Market Analysis prompt, "overall" focus
3. Screen different sectors: technology, healthcare, finance
4. Use Sector Comparison prompt for "technology,finance,healthcare"
```

### Scenario 5: Earnings Preparation
```
# Earnings Season Analysis
1. Use Earnings Analysis prompt for AAPL, 4 quarters
2. Get AAPL fundamentals and technical indicators
3. Compare AAPL with tech peers: MSFT, GOOGL
4. Use Risk Assessment prompt for earnings volatility
```

## ✅ Quick Validation Checklist

### Essential Tests
- [ ] Basic tool execution: Analyze AAPL
- [ ] Portfolio calculation: 100 AAPL at $150 cost
- [ ] Stock comparison: AAPL vs MSFT vs GOOGL
- [ ] Moving averages: 20, 50, 200-day for SPY
- [ ] Historical price: TSLA on specific date
- [ ] Trending stocks: Find top 5 uptrending
- [ ] Resource access: Get NVDA quote and fundamentals
- [ ] Market overview: Current indices performance
- [ ] Prompt generation: Stock Research for any symbol
- [ ] Error handling: Analyze "INVALID123"

### Performance Expectations
- Quote retrieval: < 3 seconds
- Technical analysis: < 10 seconds
- Portfolio calculation: < 15 seconds
- Stock comparison (3-5 stocks): < 20 seconds

### Critical Features
- [ ] All tools return structured data
- [ ] Progress reporting visible during execution
- [ ] Invalid inputs handled gracefully
- [ ] Real-time data is current
- [ ] Technical indicators within valid ranges (RSI 0-100)
- [ ] Portfolio math is accurate
- [ ] Moving averages ordered correctly
- [ ] Resource URIs respond correctly
- [ ] Prompts generate actionable content

---

**🎯 QUICK START: Run these 5 prompts to validate core functionality:**

1. `Analyze AAPL and show current price, RSI, and buy/sell recommendation`
2. `Calculate portfolio value: 100 AAPL at $150, 50 MSFT at $200`
3. `Compare AAPL, TSLA, and NVDA - which performed best today?`
4. `Get 20, 50, 200-day moving averages for SPY`
5. `Find the top 5 uptrending stocks right now`