You are providing ongoing monitoring and alerts for portfolio holdings to stay informed of material developments and performance changes. Execute this continuous monitoring workflow:

**WORKFLOW: Portfolio Holdings Monitoring & Alert System**

1. **Real-Time News Monitoring (News Sentry)**
   - Use news-sentry-market-watch agent for continuous news monitoring of all holdings
   - Filter for material events: earnings surprises, analyst actions, regulatory changes, management changes
   - Generate prioritized alerts with actionability ratings (IMMEDIATE/MONITOR/BACKGROUND)
   - Track unusual volume patterns and market anomalies for holdings

2. **Earnings & Guidance Tracking (Earnings Whisperer)**
   - Use earnings-whisperer agent to monitor upcoming earnings for all holdings
   - Analyze earnings surprises and guidance changes
   - Track post-earnings price movements and analyst reaction
   - Identify potential post-earnings drift opportunities or risks

3. **Performance Attribution (Ledger Performance Analyst)**
   - Use ledger-performance-analyst agent for ongoing performance tracking
   - Monitor individual position performance vs sector and market benchmarks
   - Track contribution to overall portfolio returns (positive/negative contributors)
   - Identify performance outliers requiring investigation

4. **Factor Exposure Drift (Factor Scout)**
   - Use factor-scout agent to monitor factor exposure changes over time
   - Track style drift in individual holdings (value→growth transitions, etc.)
   - Alert on significant factor exposure changes that affect portfolio positioning
   - Monitor correlation breakdown between holdings

5. **Risk Alert System (Risk Shield)**
   - Use risk-shield-manager agent for continuous risk monitoring
   - Track position size changes due to price movements
   - Monitor sector concentration drift and correlation changes
   - Alert on VAR threshold breaches or emerging risk concentrations

6. **Thesis Validation (Quill Equity Analyst)**
   - Use quill-equity-analyst agent for periodic thesis updates on major holdings
   - Re-evaluate investment cases based on new developments
   - Update fair value estimates and recommendation changes
   - Flag positions requiring detailed review or potential exit

**Output Format:**
- Daily Dashboard: Holdings performance, news alerts, upcoming events
- Weekly Summary: Performance attribution, significant developments, action items
- Alert System: Real-time notifications for material events requiring attention
- Monthly Review: Thesis updates, position reviews, portfolio health metrics
- Watchlist Maintenance: Add/remove monitoring criteria based on portfolio changes

Maintain continuous situational awareness of portfolio holdings to enable proactive decision-making and rapid response to material developments affecting investment positions.
Save your response in reports/ folder as a well formatted markdown file with appropriate name and timestamp.