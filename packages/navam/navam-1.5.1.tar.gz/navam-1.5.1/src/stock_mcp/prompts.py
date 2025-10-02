"""Analysis prompt templates for common stock analysis tasks."""

try:
    from .server import mcp
except ImportError:
    from server import mcp


@mcp.prompt("Stock Research")
def research_stock(symbol: str, timeframe: str = "1y") -> str:
    """Generate a comprehensive research prompt for a stock.

    Args:
        symbol: Stock ticker symbol to research
        timeframe: Analysis timeframe (default: 1y)
    """
    return f"""Analyze {symbol.upper()} stock over the {timeframe} timeframe. Please provide:

1. **Current Performance**:
   - Current price and daily change
   - Trading volume vs average
   - 52-week high/low analysis

2. **Technical Analysis**:
   - Key technical indicators (RSI, moving averages, MACD)
   - Support and resistance levels
   - Chart pattern identification
   - Trend analysis and momentum

3. **Fundamental Analysis**:
   - P/E ratio and valuation metrics
   - Financial health indicators
   - Revenue and earnings trends
   - Debt levels and liquidity

4. **Market Context**:
   - Sector performance comparison
   - Market cap and competitive position
   - Recent news impact

5. **Investment Recommendation**:
   - Buy/Hold/Sell recommendation with rationale
   - Price targets and risk factors
   - Suitable investment timeframe

Use the available MCP tools to gather comprehensive data for this analysis.
"""


@mcp.prompt("Portfolio Review")
def review_portfolio(risk_tolerance: str = "moderate") -> str:
    """Generate a portfolio review prompt.

    Args:
        risk_tolerance: Investment risk tolerance (conservative, moderate, aggressive)
    """
    return f"""Conduct a comprehensive portfolio review with {risk_tolerance} risk tolerance:

1. **Portfolio Overview**:
   - Total portfolio value and performance
   - Asset allocation breakdown
   - Diversification analysis

2. **Individual Holdings**:
   - Performance of each position
   - Position sizing appropriateness
   - Risk contribution of each holding

3. **Risk Assessment**:
   - Overall portfolio risk level
   - Concentration risk analysis
   - Correlation between holdings
   - Volatility metrics

4. **Performance Analysis**:
   - Returns vs benchmarks
   - Risk-adjusted returns
   - Winning vs losing positions

5. **Recommendations**:
   - Rebalancing suggestions
   - Position size adjustments
   - New investment opportunities
   - Risk mitigation strategies

Please analyze the portfolio holdings and provide actionable insights.
"""


@mcp.prompt("Market Analysis")
def analyze_market(focus: str = "overall") -> str:
    """Generate a market analysis prompt.

    Args:
        focus: Market focus area (overall, sector, trend)
    """
    return f"""Provide a comprehensive market analysis focusing on {focus} conditions:

1. **Market Overview**:
   - Major indices performance (S&P 500, NASDAQ, Dow Jones)
   - Market sentiment indicators
   - VIX and volatility analysis

2. **Sector Analysis**:
   - Top performing sectors
   - Lagging sectors and reasons
   - Sector rotation patterns

3. **Economic Indicators**:
   - Key economic data impact
   - Interest rate environment
   - Inflation trends

4. **Market Trends**:
   - Trending stocks and themes
   - Technical market levels
   - Volume and breadth indicators

5. **Investment Implications**:
   - Current market opportunities
   - Risk factors to watch
   - Strategic positioning suggestions

Use market overview resources and trending stock tools for comprehensive analysis.
"""


@mcp.prompt("Earnings Analysis")
def analyze_earnings(symbol: str, quarters: int = 4) -> str:
    """Generate an earnings analysis prompt.

    Args:
        symbol: Stock ticker symbol
        quarters: Number of quarters to analyze
    """
    return f"""Conduct an earnings analysis for {symbol.upper()} covering the last {quarters} quarters:

1. **Earnings Trends**:
   - Revenue growth patterns
   - EPS progression
   - Profit margin trends

2. **Key Metrics**:
   - P/E ratio evolution
   - Return on equity (ROE)
   - Debt-to-equity changes

3. **Guidance Analysis**:
   - Management guidance vs actual results
   - Forward-looking statements
   - Market reaction to earnings

4. **Competitive Position**:
   - Performance vs industry peers
   - Market share trends
   - Competitive advantages

5. **Investment Thesis**:
   - Earnings quality assessment
   - Future growth prospects
   - Valuation implications

Focus on fundamental data and compare with industry standards.
"""


@mcp.prompt("Risk Assessment")
def assess_risk(investment_type: str = "stock") -> str:
    """Generate a risk assessment prompt.

    Args:
        investment_type: Type of investment to assess (stock, portfolio, sector)
    """
    return f"""Perform a comprehensive risk assessment for this {investment_type} investment:

1. **Market Risk**:
   - Beta and volatility analysis
   - Correlation with market indices
   - Sensitivity to market movements

2. **Fundamental Risk**:
   - Financial health indicators
   - Debt levels and liquidity risk
   - Business model sustainability

3. **Technical Risk**:
   - Support/resistance levels
   - Technical breakdown risks
   - Momentum indicators

4. **External Risk Factors**:
   - Sector-specific risks
   - Economic sensitivity
   - Regulatory risks

5. **Risk Mitigation**:
   - Diversification opportunities
   - Hedging strategies
   - Position sizing recommendations
   - Stop-loss considerations

Provide a risk score and specific mitigation strategies.
"""


@mcp.prompt("Sector Comparison")
def compare_sectors(sectors: str = "technology,finance,healthcare") -> str:
    """Generate a sector comparison prompt.

    Args:
        sectors: Comma-separated list of sectors to compare
    """
    sector_list = sectors.split(',')
    sector_names = ', '.join(sector_list)

    return f"""Compare the following sectors: {sector_names}

1. **Performance Comparison**:
   - YTD returns for each sector
   - Historical performance patterns
   - Volatility comparison

2. **Valuation Analysis**:
   - Average P/E ratios
   - Price-to-book ratios
   - Growth vs value characteristics

3. **Economic Sensitivity**:
   - Interest rate sensitivity
   - Economic cycle positioning
   - Inflation impact

4. **Growth Prospects**:
   - Future growth expectations
   - Innovation and disruption factors
   - Market expansion opportunities

5. **Investment Recommendations**:
   - Current sector attractiveness ranking
   - Top stock picks in each sector
   - Allocation suggestions

Use sector screening tools to analyze representative stocks from each sector.
"""


@mcp.prompt("Technical Setup")
def find_technical_setups(pattern_type: str = "breakout") -> str:
    """Generate a technical analysis setup prompt.

    Args:
        pattern_type: Type of technical pattern (breakout, reversal, momentum)
    """
    return f"""Identify stocks with {pattern_type} technical setups:

1. **Pattern Identification**:
   - Chart pattern recognition
   - Key technical levels
   - Volume confirmation

2. **Technical Indicators**:
   - RSI levels and divergences
   - Moving average alignments
   - MACD signals

3. **Entry/Exit Strategy**:
   - Optimal entry points
   - Stop-loss levels
   - Profit targets

4. **Risk/Reward Analysis**:
   - Setup probability assessment
   - Risk-reward ratios
   - Position sizing recommendations

5. **Market Context**:
   - Overall market conditions
   - Sector strength alignment
   - Volume and momentum factors

Use trending stocks and technical indicator tools to identify the best setups.
"""