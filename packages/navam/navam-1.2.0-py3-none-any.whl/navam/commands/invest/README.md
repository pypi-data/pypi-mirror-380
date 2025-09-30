# Investment Workflow Commands

This folder contains specialized slash commands designed for retail investors using Claude Code's powerful financial agent ecosystem. Each command orchestrates multiple AI agents to deliver institutional-quality investment analysis and portfolio management.

## Available Commands

### 📊 `/invest:research-stock` - Stock Research & Analysis
**Purpose**: Comprehensive fundamental analysis of individual stocks for investment decisions

**When to Use**:
- Evaluating a specific stock for potential investment
- Comparing multiple investment opportunities
- Updating analysis on existing holdings
- Due diligence before major position changes

**Workflow**: Screen Forge → Quill Equity Analyst → News Sentry → Risk Shield Manager

**Example Usage**:
```
/invest:research-stock
```
Then provide: "Analyze Tesla (TSLA) as a potential investment for my growth portfolio"

**Expected Output**: Investment thesis with BUY/HOLD/SELL recommendation, fair value range, key catalysts, risk assessment, and position sizing guidance

---

### 🎯 `/invest:plan-goals` - Financial Goal Planning
**Purpose**: Create comprehensive financial plans aligned with specific life goals and time horizons

**When to Use**:
- Starting investment journey or major life changes
- Multiple competing financial goals (retirement, house, education)
- Need for formal Investment Policy Statement (IPS)
- Risk tolerance assessment and strategic allocation guidance

**Workflow**: Compass Goal Planner → Atlas Investment Strategist → Risk Shield Manager

**Example Usage**:
```
/invest:plan-goals
```
Then provide: "I'm 35, want to retire at 60, have $50K saved, can invest $2K monthly. Also need $100K for house down payment in 5 years."

**Expected Output**: Detailed financial plan with goal prioritization, asset allocation targets, IPS document, and implementation roadmap

---

### 🔍 `/invest:review-portfolio` - Portfolio Health Check
**Purpose**: Comprehensive evaluation of portfolio performance, risk, and optimization opportunities

**When to Use**:
- Quarterly or annual portfolio reviews
- Performance evaluation and attribution analysis
- Risk assessment and limit monitoring
- Identifying rebalancing needs and optimization opportunities

**Workflow**: Ledger Performance Analyst → Risk Shield Manager → Factor Scout → Quill Equity Analyst → Rebalance Bot → News Sentry

**Example Usage**:
```
/invest:review-portfolio
```
Then provide portfolio holdings, target allocations, and performance benchmarks

**Expected Output**: Portfolio scorecard, performance attribution, risk dashboard, factor analysis, and prioritized action items

---

### 🔎 `/invest:screen-opportunities` - Investment Opportunity Discovery
**Purpose**: Systematic market screening to identify new investment opportunities based on specific criteria

**When to Use**:
- Weekly investment idea generation
- Sector rotation or thematic investing
- Finding undervalued or momentum stocks
- Building watchlists for future consideration

**Workflow**: Screen Forge → Quill Equity Analyst → News Sentry → Risk Shield Manager

**Example Usage**:
```
/invest:screen-opportunities
```
Then provide criteria: "Find undervalued dividend growth stocks in the consumer staples sector with 10+ year dividend growth history"

**Expected Output**: Ranked opportunity list with investment cases, entry strategies, and portfolio fit analysis

---

### ⚖️ `/invest:execute-rebalance` - Portfolio Rebalancing & Trade Execution
**Purpose**: Systematic portfolio rebalancing with optimal execution and tax efficiency

**When to Use**:
- Significant portfolio drift from targets (>5% allocation variance)
- Quarterly or semi-annual rebalancing schedule
- Major cash inflows/outflows requiring deployment
- Strategic allocation changes

**Workflow**: Rebalance Bot → Risk Shield Manager → Tax Scout → Trader Jane → Cash Treasury Steward → Compliance Sentinel

**Example Usage**:
```
/invest:execute-rebalance
```
Then provide current holdings, target allocations, and any constraints

**Expected Output**: Specific trade orders, execution plan, tax impact analysis, and cost estimates

---

### 👁️ `/invest:monitor-holdings` - Ongoing Portfolio Monitoring
**Purpose**: Continuous monitoring and alerts for material developments affecting portfolio holdings

**When to Use**:
- Daily/weekly portfolio monitoring routine
- Staying informed of earnings and news for holdings
- Tracking performance attribution and factor drift
- Early warning system for position issues

**Workflow**: News Sentry → Earnings Whisperer → Ledger Performance Analyst → Factor Scout → Risk Shield Manager → Quill Equity Analyst

**Example Usage**:
```
/invest:monitor-holdings
```
Then provide list of holdings to monitor

**Expected Output**: Daily dashboard, weekly summary, real-time alerts, and thesis updates

---

### 💰 `/invest:optimize-taxes` - Tax Optimization & Year-End Planning
**Purpose**: Minimize tax liability through strategic tax-loss harvesting and portfolio optimization

**When to Use**:
- Year-end tax planning (October-December)
- After realizing significant gains
- Portfolio restructuring for tax efficiency
- Coordinating tax strategy with rebalancing

**Workflow**: Tax Scout → Risk Shield Manager → Rebalance Bot → Trader Jane → Cash Treasury Steward → Quill Equity Analyst

**Example Usage**:
```
/invest:optimize-taxes
```
Then provide taxable account holdings, realized gains/losses, and tax situation

**Expected Output**: Tax-loss harvesting plan, reinvestment strategy, trade execution plan, and estimated tax savings

---

## Command Usage Best Practices

### Getting Started
1. **Begin with Goal Planning**: Use `/invest:plan-goals` to establish strategic framework
2. **Set Up Monitoring**: Use `/invest:monitor-holdings` for ongoing awareness
3. **Regular Reviews**: Schedule `/invest:review-portfolio` quarterly
4. **Opportunity Pipeline**: Use `/invest:screen-opportunities` weekly for new ideas

### Integration Workflow
- Commands work together as an integrated system
- Results from one command often inform others
- Maintain consistency across all investment decisions
- Update analysis regularly as market conditions change

### Agent Collaboration
Each command leverages multiple specialized agents:
- **Screen Forge**: Systematic opportunity identification
- **Quill Equity Analyst**: Fundamental analysis and thesis development
- **Compass Goal Planner**: Goal-based planning and risk profiling
- **Atlas Investment Strategist**: Strategic asset allocation
- **Risk Shield Manager**: Portfolio risk management
- **Ledger Performance Analyst**: Performance analysis and attribution
- **Factor Scout**: Style and factor analysis
- **News Sentry**: Real-time news and event monitoring
- **Earnings Whisperer**: Earnings analysis and guidance tracking
- **Tax Scout**: Tax optimization and planning
- **Rebalance Bot**: Portfolio rebalancing and drift management
- **Trader Jane**: Trade execution and cost optimization
- **Cash Treasury Steward**: Cash management and optimization
- **Compliance Sentinel**: Regulatory compliance and audit trails

### Tips for Effective Use
- **Be Specific**: Provide detailed context and constraints for better results
- **Follow Workflows**: Trust the multi-agent process for comprehensive analysis
- **Document Decisions**: Keep records of analysis and decision rationale
- **Review Regularly**: Update analysis as new information becomes available
- **Integrate Results**: Use outputs from one command to inform others

### Support and Feedback
These commands represent best practices from institutional investment management adapted for retail investors. They provide systematic, disciplined approaches to common investment workflows while leveraging the full power of Claude Code's financial agent ecosystem.

For questions or suggestions about these workflows, refer to the individual command files for detailed implementation guidance.