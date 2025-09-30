# Company Research MCP Server - Evaluation Prompts

Evaluation prompts to test all Company Research MCP Server tools, resources, and capabilities.

## Quick Reference
- **7 Tools**: get_company_profile, get_company_financials, get_company_filings, get_insider_trading, get_analyst_ratings, compare_companies, search_companies
- **3 Resources**: company profile, financials, SEC filings
- **5 Prompts**: Company Deep Dive, Earnings Analysis, Industry Comparison, Due Diligence, ESG Assessment

## 🛠️ Tools Evaluation Prompts

### 1. get_company_profile
```
# Basic Profile Test
Get the company profile for AAPL including business description, sector, industry, and employee count.

# Financial Services
Get Microsoft's company profile and tell me what sector and industry they're classified in.

# Healthcare Company
Get the profile for Johnson & Johnson (JNJ) and show me their headquarters location.

# Error Test
Try to get company profile for invalid symbol INVALID123.
```

### 2. get_company_financials
```
# Annual Financials
Get Apple's annual financial statements and show me their latest revenue and net income.

# Quarterly Financials
Get Tesla's quarterly financials and compare latest quarter to previous quarter.

# Banking Financials
Get JPMorgan Chase's (JPM) annual financials and analyze their asset quality.

# Period Comparison
Get both annual and quarterly financials for Microsoft and compare trends.

# Error Test
Try to get financials for BADSTOCK with invalid period "monthly".
```

### 3. get_company_filings
```
# Recent Filings
Get the latest SEC filings for Apple (AAPL) and show me the most recent 10-K or 10-Q.

# Specific Filing Type
Get only 10-K filings for Microsoft with limit of 5.

# 8-K Filings
Find recent 8-K filings for Tesla to see material events.

# Large Set
Get 20 recent filings for Amazon (AMZN) of any type.

# Error Test
Try to get filings for symbol INVALID456.
```


### 4. get_insider_trading
```
# Standard Insider Activity
Get 3 months of insider trading activity for Apple and identify major transactions.

# Extended Period
Get 6 months of insider trading for Tesla and analyze executive selling patterns.

# Banking Insider Activity
Get insider trading for JPMorgan Chase over 3 months.

# Custom Period
Get 1 month of recent insider activity for Microsoft.

# Error Test
Try to get insider trading for invalid symbol FAKE123.
```

### 5. get_analyst_ratings
```
# Tech Stock Ratings
Get analyst ratings for Apple and show me the consensus recommendation.

# Growth Stock Analysis
Get analyst ratings for NVIDIA and compare price targets.

# Financial Stock Ratings
Get analyst ratings for Bank of America (BAC) and show buy/sell/hold breakdown.

# Comparison Ready
Get analyst ratings for Google (GOOGL) to prepare for comparison.

# Error Test
Try to get ratings for invalid symbol MISSING789.
```

### 6. compare_companies
```
# Tech Giants Comparison
Compare Apple, Microsoft, and Google across all available metrics.

# Banking Sector
Compare JPMorgan Chase, Bank of America, and Wells Fargo (WFC).

# Auto Industry
Compare Tesla, Ford (F), and General Motors (GM).

# Custom Metrics
Compare AAPL and MSFT focusing on specific metrics: revenue, profit_margin, market_cap.

# Mixed Valid/Invalid
Try to compare AAPL, MSFT, and INVALIDSTOCK (test error handling).
```

### 7. search_companies
```
# Sector Search
Search for "technology" companies and limit results to 10.

# Industry Search
Search for "pharmaceutical" companies and show top 15 results.

# Company Name Search
Search for "bank" and find banking companies.

# Size Filter
Search for companies with filters: minimum market cap, employee count.

# Custom Query
Search for "renewable energy" companies with limit of 5.
```

## 📊 Resources Test Prompts

### 1. company://{symbol}/profile
```
# Basic Profile Resource
Access the company profile resource for AAPL and show business description.

# Multiple Profiles
Get profile resources for MSFT, GOOGL, and AMZN.

# Financial Services
Access profile resource for Goldman Sachs (GS).

# Error Test
Try to access profile resource for invalid symbol BADCOMPANY.
```

### 2. company://{symbol}/financials/{period}
```
# Annual Financial Resource
Access annual financials resource for Apple and show income statement.

# Quarterly Financials
Get quarterly financials resource for Tesla and analyze balance sheet.

# Banking Financials
Access annual financials for JPMorgan Chase and review cash flow.

# Period Variations
Test both "annual" and "quarterly" periods for Microsoft financials.

# Error Test
Try to access financials resource with invalid period "monthly".
```

### 3. company://{symbol}/filings
```
# Recent Filings Resource
Access SEC filings resource for Apple and list recent 10-K and 10-Q forms.

# Tech Company Filings
Get filings resource for NVIDIA and identify material events.

# Banking Filings
Access filings resource for Bank of America and review regulatory submissions.

# Error Test
Try to access filings resource for symbol DOESNOTEXIST.
```

## 📝 Prompts Test Cases

### 1. Company Deep Dive Prompt
```
# Tech Company Analysis
Use Company Deep Dive prompt for Apple (AAPL) to get comprehensive analysis.

# Growth Company Focus
Apply Company Deep Dive prompt to Tesla (TSLA) for complete evaluation.

# Financial Services
Use Company Deep Dive prompt for JPMorgan Chase (JPM).

# Healthcare Company
Apply Company Deep Dive prompt to Johnson & Johnson (JNJ).
```

### 2. Earnings Analysis Prompt
```
# Latest Earnings
Use Earnings Analysis prompt for Apple with "latest" quarter.

# Specific Quarter
Apply Earnings Analysis prompt for Tesla with "Q3 2024" quarter.

# Year-over-year
Use Earnings Analysis prompt for Microsoft with current quarter focus.

# Banking Earnings
Apply Earnings Analysis prompt to Bank of America for latest results.
```

### 3. Industry Comparison Prompt
```
# Tech Giants
Use Industry Comparison prompt with ["AAPL", "MSFT", "GOOGL"].

# Banking Sector
Apply Industry Comparison with ["JPM", "BAC", "WFC"].

# Auto Industry
Use Industry Comparison prompt for ["TSLA", "F", "GM"].

# Pharma Companies
Apply Industry Comparison with ["JNJ", "PFE", "MRK"].
```

### 4. Due Diligence Prompt
```
# Investment Due Diligence
Use Due Diligence prompt for Apple (AAPL) for investment analysis.

# Acquisition Target
Apply Due Diligence prompt for smaller tech company evaluation.

# Risk Assessment
Use Due Diligence prompt for Tesla (TSLA) focusing on risk factors.

# Value Investment
Apply Due Diligence prompt to Warren Buffett holding like Coca-Cola (KO).
```

### 5. ESG Assessment Prompt
```
# Tech Company ESG
Use ESG Assessment prompt for Apple's sustainability initiatives.

# Energy Company ESG
Apply ESG Assessment prompt for ExxonMobil (XOM) environmental impact.

# Financial Services ESG
Use ESG Assessment prompt for Goldman Sachs governance practices.

# Consumer Goods ESG
Apply ESG Assessment prompt to Procter & Gamble (PG).
```

## 🧪 Edge Cases & Error Testing

### Invalid Input Tests
```
# Bad Symbols
Get company profile for "INVALID123" and verify error handling.

# Mixed Valid/Invalid
Compare companies: ["AAPL", "MSFT", "BADSTOCK123"].

# Empty Inputs
Try company profile with empty string symbol.

# Special Characters
Test profile with symbols like "AAPL@" or "MSFT#".

# Case Sensitivity
Test with lowercase symbols like "aapl" vs "AAPL".
```

### Parameter Edge Cases
```
# Invalid Periods
Get financials with period "monthly" (should be annual/quarterly).

# Extreme Limits
Search companies with limit of 1000.

# Zero Limits
Get filings with limit of 0.

# Negative Values
Get insider trading with months = -5.

# Very Large Values
Get insider trading with months = 120.
```

### Data Availability Tests
```
# Delisted Company
Try to get profile for recently delisted company.

# New IPO
Get financials for very recent IPO (may have limited data).

# Foreign Companies
Test with ADR symbols like "TSM" or "ASML".

# ETFs vs Companies
Test company tools with ETF symbols like "SPY" or "QQQ".
```

### Performance Tests
```
# Multiple Company Comparison
Compare 10+ companies: ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "JNJ", "PG", "KO"].

# Large Search Results
Search for "technology" with limit of 50.

# Concurrent Requests
Get company profiles for multiple companies simultaneously.

# Data-heavy Request
Get both annual and quarterly financials for 5 companies.
```

## 📈 Complete Test Scenarios

### Scenario 1: Investment Research Workflow
```
# Comprehensive Company Analysis
1. Get company profile for Apple (AAPL)
2. Get annual and quarterly financials for AAPL
3. Get recent analyst ratings for AAPL
4. Get insider trading for AAPL
5. Use Company Deep Dive prompt for complete analysis
```

### Scenario 2: Sector Analysis
```
# Banking Sector Deep Dive
1. Search for "banking" companies, limit 10
2. Compare top 3 banks: JPM, BAC, WFC
3. Use Industry Comparison prompt for banking sector
4. Get analyst ratings for each bank
5. Use ESG Assessment for banking sector sustainability
```

### Scenario 3: Due Diligence Process
```
# M&A Target Evaluation
1. Get company profile for target company
2. Get 3 years of annual financials
3. Get recent SEC filings (10-K, 10-Q, 8-K)
4. Get insider trading patterns over 6 months
5. Use Due Diligence prompt for comprehensive review
```

### Scenario 4: Earnings Season Preparation
```
# Quarterly Earnings Analysis
1. Get company profile
2. Get quarterly financials for trend analysis
3. Get analyst ratings and expectations
4. Use Earnings Analysis prompt for latest quarter
5. Compare with industry peers
```

### Scenario 5: ESG Investment Screening
```
# Sustainable Investment Research
1. Search for companies in clean energy sector
2. Get company profiles for ESG-focused companies
3. Use ESG Assessment prompt for each candidate
4. Compare ESG scores across industry
```

### Scenario 6: Combined Stock & Company Analysis
```
# Integrated Financial Analysis (using both MCPs)
1. Use Stock MCP: Analyze AAPL stock price and technical indicators
2. Use Company MCP: Get AAPL company profile and financials
3. Use Stock MCP: Get moving averages and trend analysis
4. Use Company MCP: Get analyst ratings
5. Use both: Compare stock performance vs company fundamentals
6. Combined recommendation: Technical + fundamental analysis
```

## ✅ Quick Validation Checklist

### Essential Tests
- [ ] Basic company profile: Get Apple profile
- [ ] Financial data: Get AAPL annual financials
- [ ] SEC filings: Get recent Tesla filings
- [ ] Insider activity: Get AAPL insider trading
- [ ] Analyst consensus: Get NVDA analyst ratings
- [ ] Company comparison: Compare AAPL vs MSFT vs GOOGL
- [ ] Company search: Find "technology" companies
- [ ] Resource access: Get AAPL profile and financials resources
- [ ] Prompt generation: Company Deep Dive for any symbol
- [ ] Error handling: Test with "INVALID123"

### Performance Expectations
- Company profile retrieval: < 5 seconds
- Financial data fetch: < 8 seconds
- SEC filings lookup: < 10 seconds
- Multi-company comparison: < 15 seconds
- Search functionality: < 12 seconds

### Critical Features
- [ ] All tools return structured company data
- [ ] Progress reporting visible during data fetching
- [ ] Invalid symbols handled gracefully
- [ ] Financial data includes key metrics (revenue, profit, ratios)
- [ ] SEC filings are recent and accessible
- [ ] Insider trading shows transaction details
- [ ] Analyst ratings include consensus and targets
- [ ] Company comparisons highlight key differences
- [ ] Search returns relevant companies with key metrics
- [ ] Resources provide JSON-formatted data
- [ ] Prompts generate comprehensive analysis templates

### Data Quality Checks
- [ ] Company profiles include complete business descriptions
- [ ] Financial statements have proper accounting periods
- [ ] SEC filings are officially filed documents
- [ ] Insider transactions include proper disclosure
- [ ] Analyst ratings are from recognized firms
- [ ] Comparison metrics are consistently formatted
- [ ] Search results match query criteria

---

**🎯 QUICK START: Run these 5 prompts to validate core functionality:**

1. `Get company profile for AAPL including business description and key metrics`
2. `Get Apple's annual financials and show revenue and profit trends`
3. `Compare AAPL, MSFT, and GOOGL across key business metrics`
4. `Get recent analyst ratings for Tesla and show consensus recommendation`
5. `Search for "technology" companies and show top 10 results with market caps`

**🔗 COMBINED MCP TESTING: Validate integration with Stock MCP:**

6. `Analyze AAPL stock price (Stock MCP) and get company profile (Company MCP)`
7. `Compare TSLA technical indicators (Stock) with company financials (Company)`
8. `Get NVDA moving averages (Stock) and analyst ratings (Company)`
9. `Screen tech stocks by price (Stock) and get company profiles (Company)`
10. `Portfolio analysis (Stock) combined with company due diligence (Company)`