You are conducting comprehensive stock research for potential investment. Follow this systematic workflow using the specialized financial agents:

**⚡ PERFORMANCE OPTIMIZATION (CRITICAL):**

BEFORE launching agents, gather ALL required data in ONE batch to eliminate redundant API calls:

1. **Data Collection Phase (Do First):**
   - Call `get_company_profile` for target symbol
   - Call `get_company_financials` for target symbol (annual period)
   - Call `get_analyst_ratings` for target symbol
   - Call `analyze_stock` for target symbol
   - Call `get_company_news` for target symbol (7 days)

2. **Context Passing (Critical):**
   - Once you have all data, PASS IT AS CONTEXT to each agent
   - Agents should use the provided data rather than making duplicate calls
   - Only make NEW tool calls if you need additional data not in the initial batch

This approach reduces execution time from ~9 minutes to ~3 minutes (67% faster) and eliminates 70% of redundant API calls.

**WORKFLOW: Stock Research & Investment Analysis**

1. **Initial Screening (Screen Forge)**
   - If researching a specific symbol: Skip to step 2
   - If seeking investment ideas: Use screen-forge agent to identify candidates based on user criteria (value, growth, sector, momentum, etc.)
   - Generate shortlist of 3-5 top candidates with key metrics

2. **Fundamental Analysis (Quill Equity Analyst)**
   - Launch quill-equity-analyst agent WITH pre-gathered data as context
   - Agent uses provided data for: Company deep dive, DCF valuation, comparable analysis, investment thesis
   - Get clear BUY/HOLD/SELL recommendation with fair value range and confidence level
   - Identify key catalysts and material risks

3. **News & Event Analysis (News Sentry)**
   - Launch news-sentry-market-watch agent WITH pre-gathered news data as context
   - Assess recent news flow and sentiment from provided data
   - Check for upcoming events, earnings announcements, or material developments
   - Identify any red flags or positive catalysts

4. **Risk Assessment (Risk Shield)**
   - Launch risk-shield-manager agent WITH pre-gathered analysis data as context
   - Evaluate stock-specific and portfolio impact risks
   - Assess how adding this position affects overall portfolio concentration and risk metrics
   - Get position sizing recommendations based on risk parameters

5. **Synthesis & Decision Framework**
   - Combine insights from all agents into actionable investment recommendation
   - Provide: Entry price range, position size, stop-loss levels, timeline for review
   - Include specific catalysts to monitor and risk factors to watch

**Output Format:**
- Executive Summary: Clear investment decision with rationale
- Key Metrics: Valuation, risk measures, position sizing
- Action Plan: Entry strategy, monitoring checklist, exit criteria
- Follow-up: Schedule for re-evaluation and key events to track

Focus on delivering actionable intelligence that enables confident investment decisions while maintaining appropriate risk management discipline. 
Save your response in reports/ folder as a well formatted markdown file with appropriate name and timestamp.