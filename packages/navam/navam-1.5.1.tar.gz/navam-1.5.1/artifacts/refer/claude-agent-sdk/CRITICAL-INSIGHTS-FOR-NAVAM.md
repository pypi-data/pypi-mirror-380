# Critical Insights: Claude Agent SDK for Navam Performance

**Analysis Date**: 2025-01-10
**Current Version**: Navam 1.4.8
**SDK Version**: Claude Agent SDK (formerly Claude Code SDK)

---

## 🚨 Critical Discovery: Tool Execution Hooks Enable Caching!

### The Problem We Faced

In v1.4.8, we implemented cache tracking but couldn't actually intercept tool execution because:
- Claude SDK handles tool execution internally via `client.query()`
- We receive results through streaming messages (ToolUseBlock/ToolResultBlock)
- No way to inject cached results before actual execution

**Result**: We can measure duplicates but not prevent them.

### The Solution: Pre/Post Tool Hooks! 🎉

The Agent SDK provides **hooks** that run before and after tool execution:

```python
async def pre_tool_use_hook(tool_name: str, tool_input: dict) -> dict:
    """
    Called BEFORE tool execution.
    Can deny execution and provide cached result!
    """
    # Check cache
    cached_result = session_cache.get(tool_name, tool_input)

    if cached_result is not None:
        # ✅ RETURN CACHED RESULT, SKIP ACTUAL EXECUTION!
        return {
            "behavior": "deny",  # Don't execute tool
            "message": "Using cached result",
            "result": cached_result  # Provide cached data
        }

    # Cache miss - allow execution
    return {"behavior": "allow"}


async def post_tool_use_hook(tool_name: str, tool_input: dict, result: dict):
    """
    Called AFTER tool execution.
    Perfect place to cache results!
    """
    if tool_name.startswith("mcp__"):
        session_cache.set(tool_name, tool_input, result)


# Configure client with hooks
options = ClaudeAgentOptions(
    hooks={
        'pre_tool_use': pre_tool_use_hook,
        'post_tool_use': post_tool_use_hook
    }
)

client = ClaudeSDKClient(options=options)
```

### Impact on Issue #2 (Duplicate MCP Tool Calls)

**Current State (v1.4.8)**:
- ✅ Can detect duplicates
- ✅ Can measure waste
- ❌ Cannot prevent duplicates

**With Hooks (v1.5.0)**:
- ✅ Can detect duplicates
- ✅ Can measure waste
- ✅ **CAN PREVENT DUPLICATES!**
- ✅ Cache hit → Skip execution → Return cached result
- ✅ 70% reduction in API calls (based on tracking data)

**Implementation Effort**: 1-2 days (hooks integration)

---

## 🚀 Critical Discovery: Subagents Enable 3-4x Speed Improvement!

### The Problem: Sequential Agent Execution

Current `/invest:research-stock` workflow:
```
Main Agent
  ↓
Launch Agent 1: Fundamental Analysis (60s)
  ↓ (waits)
Launch Agent 2: Technical Analysis (60s)
  ↓ (waits)
Launch Agent 3: News Sentiment (60s)
  ↓
Generate Report (300s)
  ↓
Total: 480s (8 minutes)
```

### The Solution: Parallel Subagents

With Agent SDK subagents:
```
Main Agent
  ├→ Subagent 1: Fundamental (60s) ┐
  ├→ Subagent 2: Technical (60s)   ├─ Run in PARALLEL
  └→ Subagent 3: News (60s)        ┘
      ↓ (all complete together)
  Generate Report (180s - faster with streaming!)
      ↓
Total: 240s (4 minutes) - 50% faster!
```

### Implementation

```python
# Define specialized subagents
options = ClaudeAgentOptions(
    system_prompt="You are an investment research orchestrator",
    agents={
        'fundamental-analyst': {
            'description': 'Analyze company financials and fundamentals',
            'prompt': """Analyze:
                - Balance sheet strength
                - Income statement trends
                - Cash flow quality
                - Key financial ratios
                Provide data-driven insights with confidence levels.""",
            'tools': [
                'mcp__company-research__get_company_profile',
                'mcp__company-research__get_company_financials',
                'mcp__company-research__get_analyst_ratings'
            ],
            'model': 'sonnet'
        },
        'technical-analyst': {
            'description': 'Analyze price patterns and technical indicators',
            'prompt': """Analyze:
                - Price trends and momentum
                - Volume patterns
                - Technical indicators (RSI, MACD, etc)
                - Support/resistance levels
                Focus on actionable signals.""",
            'tools': [
                'mcp__stock-analyzer__analyze_stock',
                'mcp__stock-analyzer__get_moving_averages'
            ],
            'model': 'sonnet'
        },
        'news-analyst': {
            'description': 'Analyze recent news and market sentiment',
            'prompt': """Analyze:
                - Recent company news (7 days)
                - Market sentiment
                - Key events and catalysts
                - Risk factors
                Provide sentiment summary and key takeaways.""",
            'tools': [
                'mcp__news-analyzer__get_company_news',
                'mcp__news-analyzer__analyze_sentiment'
            ],
            'model': 'haiku'  # Faster, cheaper for news summaries
        }
    }
)

# Main agent orchestrates subagents
client = ClaudeSDKClient(options=options)

# Subagents run in parallel automatically!
response = await client.query("Research AAPL stock comprehensively")
```

### Benefits Beyond Speed

**1. Context Separation**
- Each subagent has focused context
- No information overload
- More accurate, focused analysis

**2. Tool Specialization**
- Each agent only accesses relevant tools
- Better security (principle of least privilege)
- Clearer audit trail

**3. Model Optimization**
- Use Sonnet for complex analysis
- Use Haiku for simple tasks (3x cheaper, 2x faster)
- Optimize cost vs quality per task

**4. Error Isolation**
- If one subagent fails, others continue
- Graceful degradation
- Better error handling

### Impact on Performance Issues

**Issue #1: 5+ Minute Report Generation**
- Current: Main agent generates entire report (300s)
- With subagents: Each generates section in parallel (60s)
- With streaming: Display sections as completed
- **Result**: 5x faster, progressive display

**Issue #3: Sequential Tool Execution**
- Current: Tools executed one at a time
- With subagents: Multiple tools in parallel across agents
- **Result**: 3-4x throughput improvement

---

## 💰 Critical Discovery: Built-in Cost Tracking

### Current Problem (Issue #8)

We track tool calls but don't know:
- Actual API costs
- Cache savings in dollars
- ROI of optimizations

### Solution: Native Cost Tracking

```python
class CostTracker:
    def __init__(self):
        self.seen_message_ids = set()
        self.total_cost = 0.0
        self.steps = []

    async def track_messages(self, client):
        async for message in client.receive_messages():
            if isinstance(message, AssistantMessage):
                usage = message.usage

                # Deduplicate by message ID
                if message.id in self.seen_message_ids:
                    continue
                self.seen_message_ids.add(message.id)

                if usage:
                    step_cost = {
                        'input_tokens': usage.input_tokens,
                        'output_tokens': usage.output_tokens,
                        'cache_creation': usage.cache_creation_input_tokens,
                        'cache_hits': usage.cache_read_input_tokens,
                        'cost_usd': usage.total_cost_usd
                    }

                    self.steps.append(step_cost)
                    self.total_cost += usage.total_cost_usd

        return {
            'total_cost': self.total_cost,
            'steps': self.steps,
            'cache_savings': self._calculate_cache_savings()
        }

    def _calculate_cache_savings(self):
        """Calculate $ saved by caching"""
        total_cache_hits = sum(s['cache_hits'] for s in self.steps)
        # Claude API: $3/M input tokens, cache reads are 90% cheaper
        cache_cost = (total_cache_hits / 1_000_000) * 0.30  # $0.30/M cached tokens
        full_cost = (total_cache_hits / 1_000_000) * 3.00   # $3/M if not cached
        return full_cost - cache_cost
```

### Integration with /perf Command

```python
# Enhanced performance summary
def _show_performance_summary(self):
    perf_text = "[bold]⚡ Performance Summary[/bold]\n\n"

    # ... existing metrics ...

    # Add cost tracking
    if hasattr(self, 'cost_tracker'):
        costs = self.cost_tracker.get_summary()

        perf_text += f"[cyan]💰 Cost Analysis:[/cyan]\n"
        perf_text += f"  • Total cost: [yellow]${costs['total_cost']:.4f}[/yellow]\n"
        perf_text += f"  • Input tokens: {costs['total_input_tokens']:,}\n"
        perf_text += f"  • Output tokens: {costs['total_output_tokens']:,}\n"
        perf_text += f"  • Cache hits: [green]{costs['cache_hits']:,}[/green]\n"
        perf_text += f"  • Cache savings: [green]${costs['cache_savings']:.4f}[/green]\n\n"

        # Cost per agent (if using subagents)
        if costs['agent_costs']:
            perf_text += f"[cyan]Cost by Agent:[/cyan]\n"
            for agent, cost in costs['agent_costs'].items():
                perf_text += f"  • {agent}: ${cost:.4f}\n"
```

---

## 📊 Critical Discovery: Native Todo Tracking

### Current Implementation (Custom)

We manually track todos in chat.py with TodoWrite tool.

### SDK Native Implementation

The Agent SDK automatically creates and tracks todos:

```python
# SDK automatically detects complex tasks and creates todos
# No need to manually call TodoWrite!

async for message in client.receive_messages():
    if message.subtype == 'todo_update':
        todo = {
            'content': message.content,
            'status': message.status,  # pending, in_progress, completed
            'activeForm': message.active_form
        }

        # Display in UI
        update_todo_display(todo)
```

**Benefits**:
- Automatic todo detection (no manual tracking)
- Consistent across all agents
- Less code to maintain
- Better integration with SDK features

**Migration Path**:
- Keep current TodoWrite for backwards compatibility
- Gradually migrate to SDK native todos
- Remove custom implementation in v2.0

---

## 🎯 Implementation Priority Matrix

### High Priority (Week 1)

| Feature | Impact | Effort | ROI |
|---------|--------|--------|-----|
| Pre/Post Tool Hooks (Caching) | 70% API call reduction | 1-2 days | **VERY HIGH** |
| Subagents (Parallel) | 3-4x speed improvement | 2-3 days | **VERY HIGH** |
| Cost Tracking | Visibility & optimization | 1 day | **HIGH** |

### Medium Priority (Week 2)

| Feature | Impact | Effort | ROI |
|---------|--------|--------|-----|
| Streaming Report Generation | Better UX, perceived speed | 2-3 days | **MEDIUM** |
| Session Management | Resume workflows | 1-2 days | **MEDIUM** |
| Model Optimization | 30% cost reduction | 1 day | **MEDIUM** |

### Low Priority (Week 3+)

| Feature | Impact | Effort | ROI |
|---------|--------|--------|-----|
| Native Todo Migration | Code simplification | 2 days | **LOW** |
| Session Forking | Advanced feature | 1 day | **LOW** |
| Advanced Permissions | Enhanced security | 1 day | **LOW** |

---

## 📋 Concrete Implementation Plan

### Phase 1: Hook-Based Caching (v1.5.0)

**Goal**: Eliminate 70% of duplicate API calls

**Implementation**:
```python
# 1. Update chat.py - Add hook methods
class InteractiveChat:
    async def _pre_tool_use_hook(self, tool_name: str, tool_input: dict) -> dict:
        """Check cache before tool execution"""
        if not tool_name.startswith("mcp__"):
            return {"behavior": "allow"}

        cached = self.session_cache.get(tool_name, tool_input)
        if cached is not None:
            self.performance_metrics['cache_hits'] += 1
            return {
                "behavior": "deny",
                "message": f"Cache hit for {tool_name}",
                "result": cached
            }

        return {"behavior": "allow"}

    async def _post_tool_use_hook(self, tool_name: str, tool_input: dict, result: dict):
        """Cache result after execution"""
        if tool_name.startswith("mcp__"):
            self.session_cache.set(tool_name, tool_input, result)

    def __init__(self, ...):
        # ... existing init ...

        self.claude_options = ClaudeAgentOptions(
            # ... existing options ...
            hooks={
                'pre_tool_use': self._pre_tool_use_hook,
                'post_tool_use': self._post_tool_use_hook
            }
        )
```

**Testing**:
- Run `/invest:research-stock AAPL` twice
- Second run should show 70%+ cache hits
- Verify in `/cache` command

**Expected Results**:
- 70% reduction in MCP tool calls
- 2x faster for repeated queries
- Visible cache hits in logs

---

### Phase 2: Parallel Subagents (v1.5.1)

**Goal**: 3-4x speed improvement for research workflows

**Implementation**:
```python
# 1. Create subagent configurations
# File: src/navam/agent_configs.py

INVESTMENT_RESEARCH_AGENTS = {
    'fundamental-analyst': {
        'description': 'Analyzes company financials, fundamentals, and analyst ratings',
        'prompt': """You are a fundamental analyst. Analyze:
            1. Financial statements (balance sheet, income, cash flow)
            2. Key ratios (P/E, ROE, debt/equity, margins)
            3. Analyst ratings and price targets
            4. Company profile and business model

            Provide:
            - Data-driven insights
            - Confidence levels (high/medium/low)
            - Key risks and opportunities
            - Comparable company context""",
        'tools': [
            'mcp__company-research__get_company_profile',
            'mcp__company-research__get_company_financials',
            'mcp__company-research__get_analyst_ratings',
            'mcp__company-research__compare_companies'
        ],
        'model': 'sonnet'  # High quality for financial analysis
    },

    'technical-analyst': {
        'description': 'Analyzes price patterns, trends, and technical indicators',
        'prompt': """You are a technical analyst. Analyze:
            1. Price trends and momentum
            2. Volume patterns and liquidity
            3. Technical indicators (RSI, MACD, moving averages)
            4. Support/resistance levels

            Provide:
            - Chart pattern identification
            - Trend strength assessment
            - Entry/exit signals
            - Risk/reward ratios""",
        'tools': [
            'mcp__stock-analyzer__analyze_stock',
            'mcp__stock-analyzer__get_moving_averages',
            'mcp__stock-analyzer__find_trending_stocks'
        ],
        'model': 'sonnet'  # High quality for pattern recognition
    },

    'news-analyst': {
        'description': 'Analyzes recent news, sentiment, and market events',
        'prompt': """You are a news analyst. Analyze:
            1. Recent company news (last 7 days)
            2. Market sentiment (positive/negative/neutral)
            3. Key events and catalysts
            4. Industry trends

            Provide:
            - Sentiment summary
            - Key takeaways
            - Potential market movers
            - Risk factors""",
        'tools': [
            'mcp__news-analyzer__get_company_news',
            'mcp__news-analyzer__analyze_sentiment',
            'mcp__news-analyzer__get_trending_topics'
        ],
        'model': 'haiku'  # Fast and cheap for news summaries
    }
}

# 2. Update chat.py to use subagents for investment commands
async def _load_investment_command_with_agents(self, command: str):
    """Load investment command with parallel subagent execution"""

    # Load base prompt
    prompt_content = await self._load_investment_command_prompt(command)

    # Add subagent orchestration
    if command.startswith('/invest:research-stock'):
        # Use parallel subagents for comprehensive research
        options = ClaudeAgentOptions(
            system_prompt=prompt_content,
            agents=INVESTMENT_RESEARCH_AGENTS,
            hooks={
                'pre_tool_use': self._pre_tool_use_hook,
                'post_tool_use': self._post_tool_use_hook
            }
        )

        return options
```

**Testing**:
- Benchmark `/invest:research-stock AAPL` before and after
- Measure: Total time, time to first result, cache hits
- Verify all three subagents run in parallel

**Expected Results**:
- 3-4x faster execution (8min → 2-3min)
- Progressive results (see fundamental analysis first)
- Higher cache hit rates (agents don't duplicate each other)

---

### Phase 3: Cost Tracking & Optimization (v1.5.2)

**Goal**: Visibility into costs and 30% cost reduction

**Implementation**:
```python
# 1. Add CostTracker class
class CostTracker:
    # ... (implementation from above) ...

# 2. Integrate into InteractiveChat
class InteractiveChat:
    def __init__(self, ...):
        # ... existing init ...
        self.cost_tracker = CostTracker()

    async def process_query(self, prompt: str):
        # ... existing code ...

        # Track costs during message processing
        await self.cost_tracker.track_messages(self.client)

    def _show_performance_summary(self):
        # ... existing code ...

        # Add cost section
        costs = self.cost_tracker.get_summary()
        perf_text += f"[cyan]💰 Cost Analysis:[/cyan]\n"
        perf_text += f"  • Total: ${costs['total_cost']:.4f}\n"
        perf_text += f"  • Cache savings: ${costs['cache_savings']:.4f}\n"

        # Show cost by agent
        for agent, cost in costs['agent_costs'].items():
            perf_text += f"  • {agent}: ${cost:.4f}\n"
```

**Testing**:
- Run workflows and check `/perf` for cost data
- Verify cache savings calculation
- Compare costs with and without caching

**Expected Results**:
- Full cost visibility
- Measure cache ROI in dollars
- Identify expensive operations for optimization

---

## 🎯 Success Metrics

### Phase 1: Caching (v1.5.0)
- [ ] Cache hit rate >70% on repeated queries
- [ ] `/cache` shows actual cache hits (not just potential)
- [ ] 50% reduction in API response time for repeated queries

### Phase 2: Subagents (v1.5.1)
- [ ] Research workflow <3 minutes (from 8 minutes)
- [ ] Three subagents verified running in parallel
- [ ] Progressive results visible to user

### Phase 3: Cost Tracking (v1.5.2)
- [ ] Cost displayed in `/perf` command
- [ ] Cache savings measured in USD
- [ ] 30% cost reduction from caching + model optimization

---

## 🚧 Migration Risks & Mitigation

### Risk 1: Breaking Changes in Agent SDK

**Probability**: MEDIUM
**Impact**: HIGH

**Mitigation**:
- Pin to specific Agent SDK version
- Comprehensive test suite before migration
- Gradual rollout (alpha → beta → production)
- Rollback plan documented

### Risk 2: Hook Performance Overhead

**Probability**: LOW
**Impact**: MEDIUM

**Mitigation**:
- Benchmark hook overhead (<5ms expected)
- Optimize cache lookup (O(1) hash-based)
- Monitor performance metrics
- A/B test with and without hooks

### Risk 3: Subagent Context Confusion

**Probability**: MEDIUM
**Impact**: MEDIUM

**Mitigation**:
- Clear, focused agent prompts
- Strict tool access controls
- Test with diverse queries
- Monitor agent output quality

### Risk 4: Cost Tracking Accuracy

**Probability**: LOW
**Impact**: LOW

**Mitigation**:
- Message ID deduplication
- Cross-check with Claude API dashboard
- Unit tests for cost calculations
- Regular reconciliation

---

## 📚 Additional Resources

- [Agent SDK Migration Guide](./MIGRATION-GUIDE.md)
- [Agent SDK Overview](./overview.md)
- [Subagents Documentation](./subagents.md)
- [Cost Tracking Guide](./sdk-cost-tracking.md)
- [Performance Improvements Backlog](../../backlog/performance-improvements.md)

---

*This document provides actionable insights for implementing Agent SDK features to solve Navam's performance challenges. All recommendations are based on actual SDK capabilities and measured performance data.*

*Last Updated: 2025-01-10*
*Next Review: After Phase 1 implementation (v1.5.0)*
