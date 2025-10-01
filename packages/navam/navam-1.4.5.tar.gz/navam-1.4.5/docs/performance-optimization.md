# Navam Performance Optimization Plan

## Executive Summary

Analysis of production usage revealed significant performance bottlenecks in the `/invest:research-stock` workflow:
- **5+ minute delays** during report generation
- **Duplicate MCP tool calls** across agents (3-4x redundancy)
- **Sequential execution** instead of parallel batching
- **No user feedback** during long operations

## Performance Metrics from Real Execution

### Timeline Analysis: NVDA Research Request

| Phase | Duration | Operations | Issue |
|-------|----------|------------|-------|
| Initial tool calls | 4 seconds | 10+ MCP calls | ✅ Good |
| Agent processing | 3 minutes | Agent analysis | ⚠️ Slow |
| Report generation | **5+ minutes** | File write | ❌ Critical |
| **Total** | **~9 minutes** | Full workflow | ❌ Too slow |

### Tool Call Redundancy

| Tool | Called By | Times | Wasted Calls |
|------|-----------|-------|--------------|
| `get_company_profile` | 3 agents | 4x | 3 duplicate |
| `get_company_financials` | 3 agents | 3x | 2 duplicate |
| `get_analyst_ratings` | 2 agents | 3x | 2 duplicate |
| `analyze_stock` | 2 agents | 3x | 2 duplicate |

**Total waste**: ~10 duplicate API calls per research request

## Root Causes

### 1. No Session-Level Caching
Each agent makes independent tool calls without checking if data already exists in session.

**Example**: All 3 agents call `get_company_profile("NVDA")` separately.

### 2. Sequential Tool Execution
Agents make tool calls one at a time instead of batching.

**Current**:
```python
result1 = await get_company_profile("NVDA")  # Wait
result2 = await get_financials("NVDA")       # Wait
result3 = await get_analyst_ratings("NVDA")  # Wait
```

**Optimal**:
```python
results = await asyncio.gather(
    get_company_profile("NVDA"),
    get_financials("NVDA"),
    get_analyst_ratings("NVDA")
)
```

### 3. Report Generation Bottleneck
The main agent generates a massive report (likely 10k+ tokens) in a single operation with no streaming feedback.

### 4. No Progress Indicators
User sees no feedback during 5+ minute report generation, creating poor UX.

## Proposed Solutions

### Priority 1: Session-Level Tool Result Caching

**Implementation**: Add caching layer in `InteractiveChat` class

```python
class InteractiveChat:
    def __init__(self):
        self.tool_cache = {}  # Session-level cache
        self.cache_ttl = 300  # 5 minutes

    async def _cached_tool_call(self, tool_name: str, args: dict) -> dict:
        """Execute tool with caching"""
        cache_key = f"{tool_name}:{json.dumps(args, sort_keys=True)}"

        # Check cache
        if cache_key in self.tool_cache:
            cached = self.tool_cache[cache_key]
            if time.time() - cached['timestamp'] < self.cache_ttl:
                return cached['result']

        # Execute and cache
        result = await self._execute_tool(tool_name, args)
        self.tool_cache[cache_key] = {
            'result': result,
            'timestamp': time.time()
        }
        return result
```

**Expected Impact**:
- Reduce duplicate calls by 70%
- Save 2-3 minutes per research request
- Lower API costs

### Priority 2: Streaming Report Generation

**Implementation**: Update report generation to stream sections

```python
async def generate_report(self, data: dict):
    """Generate report with streaming updates"""

    # Stream executive summary first
    yield "## Executive Summary\n"
    summary = await generate_summary(data)
    yield summary

    # Stream fundamental analysis
    yield "\n## Fundamental Analysis\n"
    fundamentals = await generate_fundamentals(data)
    yield fundamentals

    # Continue streaming sections...
```

**Expected Impact**:
- User sees progress immediately
- No perception of "hanging"
- Can interrupt if needed

### Priority 3: Agent Context Sharing

**Implementation**: Pass shared context to agents

```python
# In chat.py
agent_context = {
    'symbol': 'NVDA',
    'available_data': {
        'company_profile': {...},  # Already fetched
        'financials': {...},       # Already fetched
        'analyst_ratings': {...}   # Already fetched
    }
}

# Agent prompt includes:
"""
Available data in context:
- Company profile: {json.dumps(context['available_data']['company_profile'])}
- Use this data instead of calling tools again
"""
```

**Expected Impact**:
- Eliminate 90% of duplicate calls
- Agents can reference pre-fetched data
- Faster agent execution

### Priority 4: Parallel Agent Execution with Data Gathering

**Current Workflow**:
```
Main Agent → Launch Agent 1 → Wait → Launch Agent 2 → Wait → Launch Agent 3 → Wait → Synthesize
```

**Optimized Workflow**:
```
Main Agent → Gather ALL data first (parallel) → Launch all 3 agents with data → Synthesize
```

**Implementation**:
```python
async def research_stock_optimized(self, symbol: str):
    # Phase 1: Parallel data gathering (60 seconds)
    data = await self._gather_all_data(symbol)

    # Phase 2: Parallel agent execution with data (90 seconds)
    agent_results = await asyncio.gather(
        self._run_agent('quill-equity-analyst', data),
        self._run_agent('news-sentry-market-watch', data),
        self._run_agent('risk-shield-manager', data)
    )

    # Phase 3: Synthesize and stream report (60 seconds)
    await self._stream_report(symbol, data, agent_results)
```

**Expected Impact**:
- Reduce total time from 9 minutes to ~3 minutes
- Better resource utilization
- Cleaner architecture

### Priority 5: Progress Indicators

**Implementation**: Add status updates during long operations

```python
async def show_progress(self, operation: str, current: int, total: int):
    """Display progress for long operations"""
    percentage = (current / total) * 100

    self.console.print(
        f"[cyan]⏳ {operation}[/cyan] "
        f"[yellow]{current}/{total}[/yellow] "
        f"[green]({percentage:.1f}%)[/green]"
    )
```

**Expected Impact**:
- Better UX during long operations
- User knows system is working
- Can estimate time remaining

## Implementation Roadmap

### Phase 1: Quick Wins (1-2 days)
- [ ] Add session-level caching for MCP tools
- [ ] Add progress indicators for long operations
- [ ] Add timeout warnings (>2 minutes)

### Phase 2: Architecture Improvements (3-5 days)
- [ ] Implement streaming report generation
- [ ] Refactor workflow to gather data first
- [ ] Add shared context for agents

### Phase 3: Advanced Optimization (1 week)
- [ ] Implement Redis caching for cross-session persistence
- [ ] Add response compression for large payloads
- [ ] Implement request deduplication at protocol level

## Success Metrics

### Target Performance

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Total workflow time | 9 min | 3 min | 67% faster |
| Duplicate API calls | 10 | 1 | 90% reduction |
| Time to first output | 3 min | 10 sec | 95% faster |
| User feedback frequency | None | Every 30s | ∞ improvement |

### Monitoring

```python
# Add performance tracking
class PerformanceMonitor:
    def track_workflow(self, workflow_name: str):
        return {
            'start_time': time.time(),
            'tool_calls': [],
            'cache_hits': 0,
            'cache_misses': 0
        }

    def report(self):
        print(f"""
        Performance Report:
        - Total time: {self.duration}s
        - Tool calls: {len(self.tool_calls)}
        - Cache hit rate: {self.cache_hits / (self.cache_hits + self.cache_misses) * 100}%
        - Average tool latency: {self.avg_latency}s
        """)
```

## Testing Plan

### Test Cases

1. **Cache Effectiveness**
   ```python
   # Test that second agent doesn't re-fetch data
   assert cache_hit_rate > 80%
   ```

2. **Streaming Works**
   ```python
   # Test that user sees output within 10 seconds
   assert time_to_first_output < 10
   ```

3. **Total Performance**
   ```python
   # Test that full workflow completes in <4 minutes
   assert total_workflow_time < 240
   ```

## Alternative Approaches Considered

### 1. Pre-compute Common Queries
Cache results for popular stocks (AAPL, NVDA, TSLA, etc.)

**Pros**: Instant results for common requests
**Cons**: Staleness issues, complex invalidation

### 2. Use Claude's Native Caching
Let Claude SDK handle caching of tool results

**Pros**: No custom code needed
**Cons**: Not exposed in current SDK, less control

### 3. Background Processing
Start analysis in background, notify when complete

**Pros**: Non-blocking user experience
**Cons**: Complex state management, notification system needed

## Conclusion

The current performance bottleneck is solvable through systematic improvements:

1. **Session caching** eliminates redundant API calls
2. **Streaming output** improves perceived performance
3. **Parallel execution** reduces total time
4. **Progress indicators** enhance user experience

**Estimated implementation effort**: 2 weeks
**Expected improvement**: 67% faster (9min → 3min)
**ROI**: High - affects every research request

## Next Steps

1. Implement Priority 1 (Session caching) - **Start immediately**
2. Add performance monitoring to measure improvements
3. Roll out Priority 2-5 incrementally
4. Monitor metrics and iterate

---

*Last updated: 2025-10-01*
*Status: Planning phase*
