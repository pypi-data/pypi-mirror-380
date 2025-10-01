# Performance Improvement Backlog

## Critical Performance Issues (Production)

### Issue #1: 5+ Minute Report Generation Delay ⚠️ CRITICAL
**Severity**: Critical
**Impact**: Every `/invest:research-stock` request
**Timeline**: Observed in NVDA research execution

**Problem**:
- Report generation takes 5+ minutes (00:10:13 → 00:15:35)
- No user feedback during this time
- Appears to be "hanging"

**Root Cause**:
- Main agent generating massive report in single operation
- Likely hitting token limits, requiring re-processing
- No streaming output

**Solution**:
- [ ] Implement streaming report generation (section by section)
- [ ] Add progress indicators during generation
- [ ] Break report into smaller chunks
- [ ] Consider template-based approach for consistent structure

**Priority**: P0 - Fix immediately
**Estimated effort**: 3 days

---

### Issue #2: Duplicate MCP Tool Calls (70% Waste) ⚠️ HIGH
**Severity**: High
**Impact**: Every multi-agent workflow
**Cost**: 3-4x redundant API calls

**Problem**:
```
Tool                      | Calls | Wasted
-------------------------|-------|--------
get_company_profile      | 4     | 3
get_company_financials   | 3     | 2
get_analyst_ratings      | 3     | 2
analyze_stock            | 3     | 2
```

**Root Cause**:
- No session-level caching
- Each agent makes independent tool calls
- No shared context between agents

**Solution**:
- [x] Create `SessionCache` class (implemented in `cache_manager.py`)
- [ ] Integrate caching into `InteractiveChat`
- [ ] Add cache statistics display
- [ ] Monitor cache hit rate (target: >80%)

**Priority**: P0 - Fix immediately
**Estimated effort**: 2 days

---

### Issue #3: Sequential Tool Execution (Slow)
**Severity**: Medium
**Impact**: Agent execution time
**Delay**: 2-3x slower than necessary

**Problem**:
- Agents make tool calls one at a time
- Not leveraging async/await for parallelism
- Could batch multiple calls

**Root Cause**:
- Claude SDK executes tool calls as they come
- No explicit batching in agent prompts

**Solution**:
- [ ] Update agent system prompts to encourage batching
- [ ] Pre-fetch all data before launching agents
- [ ] Use `asyncio.gather()` for parallel execution

**Priority**: P1 - Important
**Estimated effort**: 3 days

---

### Issue #4: No Progress Indicators
**Severity**: Medium
**Impact**: User experience
**Perception**: System appears frozen

**Problem**:
- 3+ minute gaps with no output
- User can't tell if system is working
- No way to estimate completion time

**Root Cause**:
- No status updates during long operations
- Missing progress tracking

**Solution**:
- [x] Add progress bars for long operations (v1.4.4)
- [x] Stream status updates every 30 seconds (v1.4.4)
- [x] Show "Still working..." messages (v1.4.4)
- [ ] Display estimated time remaining

**Status**: ✅ Mostly Complete (v1.4.4)
**Priority**: P1 - Important
**Estimated effort**: 2 days

---

### Issue #5: Permission System Blocking File Operations ✅ RESOLVED
**Severity**: Critical
**Impact**: Every workflow that writes files
**Timeline**: Observed in v1.4.4, Fixed in v1.4.5

**Problem**:
- File creation operations taking 7+ minutes (00:32:50 → 00:39:31)
- Multiple failed Write attempts requiring fallback methods
- Permission prompts causing retry loops
- Bash heredoc and Python fallbacks still slow

**Evidence from v1.4.4 Execution**:
```
00:32:51 - First Write attempt → fails
00:35:11 - Second Write to /tmp/workspace → fails
00:36:30 - Bash cat heredoc attempt → fails
00:38:44 - Python script attempt (2 min delay!)
00:39:31 - Still attempting file creation
```

**Root Cause**:
1. `can_use_tool` callback was provided even in `acceptEdits` mode
2. This overrode SDK's automatic approval of file operations
3. Permission handler was being called unnecessarily for Write/Edit/MultiEdit

**Solution Implemented** (v1.4.5):
- [x] Fixed callback condition to exclude `acceptEdits` and `bypassPermissions` modes
- [x] Added defense-in-depth fast-path in permission handler
- [x] Added permission performance tracking (checks count, time spent)
- [x] Display permission metrics in `/perf` command
- [x] Created comprehensive test suite (all tests passing)

**Code Changes**:
```python
# Before (v1.4.4) - BUG
can_use_tool=self._handle_tool_permission if self.interactive_permissions else None

# After (v1.4.5) - FIXED
should_use_permission_callback = (
    self.interactive_permissions and
    self.permission_mode not in ['acceptEdits', 'bypassPermissions']
)
can_use_tool=self._handle_tool_permission if should_use_permission_callback else None
```

**Testing**:
- ✅ Test 1: acceptEdits mode doesn't use callback
- ✅ Test 2: default mode uses callback when interactive=True
- ✅ Test 3: bypassPermissions doesn't use callback
- ✅ Test 4: interactive=False disables callback

**Impact**:
- **Fixed**: 7+ minute regression eliminated
- File operations now instant in acceptEdits mode
- Workflow performance restored to expected ~3 minutes
- All v1.4.3 and v1.4.4 improvements now working as intended

**Status**: ✅ Resolved in v1.4.5
**Released**: 2025-10-01

---

### Issue #6: /perf and /cache Commands Not Displaying Output ✅ RESOLVED
**Severity**: High
**Impact**: Performance monitoring and debugging
**Timeline**: Observed in v1.4.5 production, Fixed in v1.4.6

**Problem**:
- `/perf` command executes but shows no output (Duration: 17ms)
- `/cache` command executes but shows no output (Duration: 13ms)
- Both commands connect to Claude but don't display metrics panels
- Users cannot see cache hit rates or performance statistics

**Evidence from v1.4.5 Execution**:
```
[Navam] > /perf
You (Turn 4): /perf
✅ Claude SDK Client connected (Turn 4)
🎯 Query completed (Turn 4)
⏱️  Duration: 17ms
[No output displayed]

[Navam] > /cache
You (Turn 5): /cache
✅ Claude SDK Client connected (Turn 5)
🎯 Query completed (Turn 5)
⏱️  Duration: 13ms
[No output displayed]
```

**Root Cause**:
Commands `/cache` and `/perf` were NOT in the `builtin_commands` set in `_is_builtin_command()` method:
```python
# Line 1287-1292 in chat.py (v1.4.5) - THE BUG
builtin_commands = {
    '/help', '/api', '/agents', '/status', '/commands', '/new', '/tools', '/servers',
    '/clear', '/exit', '/quit', '/q'
    # Missing: '/cache', '/perf', '/performance'
}
```

This caused the commands to fall through to `process_query()` and be sent to Claude API instead of being handled locally.

**Solution Implemented** (v1.4.6):
- [x] Added `/cache`, `/perf`, and `/performance` to builtin_commands set
- [x] Fixed early return in `_show_performance_summary()` to show informative message
- [x] Added commands to `/commands` list for discoverability
- [x] Tested command detection (all tests passing)

**Code Changes**:
```python
# After (v1.4.6) - FIXED
builtin_commands = {
    '/help', '/api', '/agents', '/status', '/commands', '/new', '/tools', '/servers',
    '/clear', '/exit', '/quit', '/q', '/cache', '/perf', '/performance'
}
```

Also improved `_show_performance_summary()`:
```python
# Before (v1.4.5) - Silent failure
if not self.performance_metrics['workflow_start']:
    return  # Returns with no output

# After (v1.4.6) - Friendly message
if not self.performance_metrics['workflow_start']:
    perf_text += "[yellow]No workflow activity recorded yet.[/yellow]\n\n"
    perf_text += "[dim]Performance metrics will be tracked once you start using the system.[/dim]\n"
    self.console.print(Panel(perf_text, title="Performance Metrics", border_style="green"))
    return
```

**Testing**:
```bash
✅ PASS: /cache -> builtin=True
✅ PASS: /perf -> builtin=True
✅ PASS: /performance -> builtin=True
✅ PASS: /help -> builtin=True
✅ PASS: /agents -> builtin=True
✅ PASS: /unknown -> builtin=False
```

**Impact**:
- `/cache` and `/perf` commands now display metrics properly
- Users can monitor cache hit rates and performance statistics
- Better debugging and performance optimization experience
- Commands appear in `/commands` list for easy discovery

**Status**: ✅ Resolved in v1.4.6
**Released**: 2025-10-01

**Priority**: P1 - High (affects debugging and monitoring)
**Estimated effort**: 1 day (actual: completed same day)

---

### Issue #7: File Write Operations Still Slow (2m 45s) 🔍 INVESTIGATING
**Severity**: Medium
**Impact**: Report generation workflows
**Timeline**: Observed in v1.4.5 production, Investigating in v1.4.7

**Problem**:
- Write to `/tmp/` directory: instant (00:59:10) ✅
- Write to `reports/` directory: 2m 45s delay (00:59:13 → 01:01:58) ❌
- Inconsistent behavior between different paths
- Still significant delay despite v1.4.5 permission fix

**Evidence from v1.4.5 Execution**:
```
00:59:10 - Write to /tmp/amazon_investment_report.md - instant ✅
00:59:13 - Check pwd command - instant ✅
01:01:58 - Write to reports/AMZN_Investment_Research_2025-10-01.md - 2m 45s delay ❌
```

**Investigation Results** (v1.4.7):

1. **Python File I/O Test** - ✅ NOT the bottleneck
   ```python
   Test 1: Write to /tmp - 0.0004s ✅
   Test 2: Write to reports/ - 0.0001s ✅
   Test 3: Large file (1.4MB) to reports/ - 0.0005s ✅
   ```
   Conclusion: Python file operations are instant for both /tmp and reports/ directories.

2. **Added Detailed Timing Instrumentation** (chat.py):
   - Store tool start time with tool_use_id for accurate duration tracking
   - Log completion time for all Write operations
   - Warn if Write takes > 5 seconds
   - Show status if Write takes > 1 second
   - DEBUG logging if permission handler unexpectedly called for Write

3. **Permission Mode Verification**:
   - Default permission_mode: `acceptEdits` (cli.py:28)
   - Should auto-approve Write/Edit/MultiEdit operations
   - Permission callback should NOT be provided in acceptEdits mode (v1.4.5 fix)

**Root Cause Hypothesis** (Updated):
The delay is NOT in Python file I/O. The bottleneck must be in:
1. **Claude Code SDK Write tool execution** - Something in the SDK pipeline
2. **Network latency** - If SDK is making network calls during Write
3. **File path resolution** - SDK may be doing slow path operations
4. **Tool result processing** - Delay in receiving/processing ToolResultBlock

**Next Steps**:
- [ ] Run production workflow with new timing logs enabled
- [ ] Capture exact timing: tool start → tool result received
- [ ] Check if DEBUG warning appears (permission handler called)
- [ ] Profile Claude Code SDK Write tool internals
- [ ] Check if SDK is making network calls for file operations

**Changes Made** (v1.4.7-dev):
```python
# chat.py - Track tool execution timing
self._tool_timings[block.id] = {
    'tool_name': tool_name,
    'start_time': tool_start_time,
    'tool_input': block.input
}

# chat.py - Log Write timing on completion
if tool_name == "Write" and 'file_path' in tool_input:
    duration = time.time() - timing_info['start_time']
    if duration > 5.0:
        self.notifications.show_warning(f"⚠️  SLOW Write: {file_path} - {duration:.2f}s")
```

**Priority**: P1 - Medium-High (still impacts UX)
**Estimated effort**: 1-2 days (investigation ongoing)
**Target Release**: v1.4.7

---

### Issue #8: Cache Effectiveness Unknown (No Visibility) ⚠️ MEDIUM
**Severity**: Medium
**Impact**: Cannot verify cache is working as designed
**Timeline**: Observed in v1.4.5 production AMZN research

**Problem**:
- Multiple duplicate tool calls observed in logs
- Cannot verify if cache is catching duplicates
- `/cache` command not working (Issue #6)
- No cache hit rate visibility
- Cannot measure actual performance improvement

**Evidence from v1.4.5 Execution**:
```
Tool calls observed:
- mcp__stock-analyzer__analyze_stock (AMZN) - appeared 3 times
- mcp__company-research__get_company_profile (AMZN) - appeared 4 times
- mcp__company-research__get_analyst_ratings (AMZN) - appeared 4 times
- mcp__news-analyzer__get_company_news (AMZN) - appeared 3 times
```

**Questions**:
1. Are these actual API calls or cache hits?
2. Is session cache working correctly?
3. What is actual cache hit rate?
4. How many duplicate calls were prevented?

**Dependencies**:
- Requires Issue #6 fix (get `/cache` command working)
- Need to verify cache is enabled and functioning
- May need additional logging in cache_manager.py

**Solution**:
- [ ] Fix `/cache` command (Issue #6)
- [ ] Add cache hit/miss logging in tool execution
- [ ] Verify SessionCache is properly integrated
- [ ] Test cache with known duplicate calls
- [ ] Add cache statistics to session completion summary

**Priority**: P2 - Medium (affects verification, not functionality)
**Estimated effort**: Dependent on Issue #6
**Target Release**: v1.4.6

---

## Proposed Architecture Changes

### Current Flow (9 minutes total)
```
User Request
  ↓
Launch Agent 1 (60s)
  → Tool Call 1 (10s)
  → Tool Call 2 (10s)
  → Tool Call 3 (10s)
  ↓
Launch Agent 2 (90s)
  → Tool Call 1 (duplicate! 10s)
  → Tool Call 2 (duplicate! 10s)
  → Tool Call 3 (10s)
  ↓
Launch Agent 3 (60s)
  → Tool Call 1 (duplicate! 10s)
  → Tool Call 2 (10s)
  ↓
Generate Report (300s!) ⚠️
  ↓
Done (540s total)
```

### Optimized Flow (3 minutes target)
```
User Request
  ↓
Gather ALL Data (parallel, 30s)
  → fetch_profile()     ┐
  → fetch_financials()  ├─ asyncio.gather()
  → fetch_ratings()     ┘
  ↓
Launch Agents (parallel, with data, 60s)
  → Agent 1 (uses cached data) ┐
  → Agent 2 (uses cached data) ├─ asyncio.gather()
  → Agent 3 (uses cached data) ┘
  ↓
Stream Report (section by section, 60s)
  → Executive Summary (10s)
  → Fundamentals (15s)
  → News Analysis (15s)
  → Risk Assessment (10s)
  → Synthesis (10s)
  ↓
Done (150s total - 72% faster!)
```

---

## Implementation Plan

### Phase 1: Emergency Fixes (Week 1)
**Goal**: Get to <5 minute total time

- [ ] Day 1-2: Implement session caching
  - Integrate `SessionCache` into `InteractiveChat`
  - Add cache statistics display
  - Test cache hit rate

- [ ] Day 3-4: Add progress indicators
  - Status updates every 30s
  - Progress bars for long operations
  - "Still working..." messages

- [ ] Day 5: Deploy and monitor
  - Release v1.4.3 with fixes
  - Monitor performance metrics
  - Gather user feedback

### Phase 2: Architecture Improvements (Week 2)
**Goal**: Get to <3 minute total time

- [ ] Day 1-2: Pre-fetch data pattern
  - Gather all data before agent launch
  - Pass data to agents as context
  - Eliminate duplicate calls

- [ ] Day 3-4: Streaming report generation
  - Break report into sections
  - Stream each section as completed
  - Add progress for each section

- [ ] Day 5: Performance testing
  - Benchmark against Phase 1
  - Verify <3 minute target
  - Load testing

### Phase 3: Polish & Monitoring (Week 3)
**Goal**: Production-ready monitoring

- [ ] Add performance monitoring dashboard
- [ ] Alert on slow requests (>4 minutes)
- [ ] Cache hit rate tracking
- [ ] Cost optimization analysis

---

## Success Criteria

### Performance Targets

| Metric | Current | Phase 1 Target | Phase 2 Target |
|--------|---------|----------------|----------------|
| Total time | 9 min | 5 min | 3 min |
| Cache hit rate | 0% | 50% | 80% |
| Time to first output | 3 min | 30 sec | 10 sec |
| Duplicate calls | 10 | 5 | 1 |

### User Experience

- [ ] No gaps >1 minute without feedback
- [ ] Clear progress indicators
- [ ] Estimated time remaining shown
- [ ] Cache statistics visible (optional)

### Cost Optimization

- [ ] 70% reduction in API calls
- [ ] Lower OpenAI/Claude API costs
- [ ] Faster time-to-value

---

## Monitoring & Alerts

### Key Metrics to Track

```python
# Add to InteractiveChat
class PerformanceMetrics:
    workflow_duration: float
    tool_calls_made: int
    cache_hits: int
    cache_misses: int
    time_to_first_output: float
    report_generation_time: float
```

### Alert Conditions

- Workflow takes >5 minutes → Send alert
- Cache hit rate <50% → Investigate
- Time to first output >2 minutes → Warning
- Any single operation >3 minutes → Log

---

## Testing Strategy

### Unit Tests

```python
def test_session_cache_hit():
    cache = SessionCache()
    cache.set('tool1', {'arg': 'val'}, 'result')
    assert cache.get('tool1', {'arg': 'val'}) == 'result'

def test_cache_expiration():
    cache = SessionCache(ttl_seconds=1)
    cache.set('tool1', {}, 'result')
    time.sleep(2)
    assert cache.get('tool1', {}) is None
```

### Integration Tests

```python
async def test_research_workflow_performance():
    start = time.time()
    result = await chat.research_stock('NVDA')
    duration = time.time() - start

    assert duration < 180  # 3 minutes
    assert result['cache_hit_rate'] > 0.8
```

### Load Tests

- Run 10 concurrent research requests
- Verify cache sharing works correctly
- Ensure no race conditions
- Monitor memory usage

---

## Documentation Updates

- [ ] Update README with performance benchmarks
- [ ] Document caching behavior
- [ ] Add performance tuning guide
- [ ] Create troubleshooting section

---

## Future Optimizations (Backlog)

### Cross-Session Caching (v1.5.0)
- Redis-based cache for popular stocks
- Pre-compute for top 50 stocks
- Update cache on market close

### Response Compression (v1.5.0)
- Compress large MCP responses
- Delta encoding for similar requests
- Reduce network transfer time

### Smart Prefetching (v1.6.0)
- Predict likely follow-up queries
- Prefetch in background
- Ready before user asks

### Parallel Agent Execution (v1.6.0)
- Launch all agents simultaneously
- Share data via message passing
- Aggregate results in real-time

---

*Last updated: 2025-10-01*
*Status: Planning → Implementation (Phase 1)*
*Owner: Development Team*
