# Claude Code SDK → Claude Agent SDK Migration Guide

**Status**: Claude Code SDK is being renamed to Claude Agent SDK
**Timeline**: Active migration recommended
**Impact**: Breaking changes require code updates

---

## Overview

The Claude Code SDK has been renamed to **Claude Agent SDK** to reflect its expanded scope beyond coding tasks. The SDK now supports business agents, specialized coding agents, and custom agents across various domains.

### Why the Rename?

The SDK evolved from a coding-focused tool to a comprehensive agent-building framework supporting:
- 🤖 Business agents (legal, finance, customer support)
- 💻 Specialized coding agents (SRE, security, oncall)
- 🎯 Custom agents across any domain
- 🔧 Advanced capabilities (sessions, hooks, subagents)

---

## Migration Steps

### Python Migration

#### 1. Uninstall Old Package
```bash
pip uninstall claude-code-sdk
```

#### 2. Install New Package
```bash
pip install claude-agent-sdk
```

#### 3. Update Imports
```python
# BEFORE (Old)
from claude_code_sdk import (
    ClaudeSDKClient,
    ClaudeCodeOptions,
    query,
    tool
)

# AFTER (New)
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,  # ⚠️ Name changed
    query,
    tool
)
```

#### 4. Update Type Names
```python
# BEFORE
options = ClaudeCodeOptions(
    system_prompt="...",
    allowed_tools=[...]
)

# AFTER
options = ClaudeAgentOptions(  # ⚠️ Renamed
    system_prompt="...",
    allowed_tools=[...]
)
```

### TypeScript/JavaScript Migration

#### 1. Uninstall Old Package
```bash
npm uninstall @anthropic-ai/claude-code
```

#### 2. Install New Package
```bash
npm install @anthropic-ai/claude-agent-sdk
```

#### 3. Update Imports
```typescript
// BEFORE
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// AFTER
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
```

---

## Breaking Changes

### 1. ⚠️ System Prompt No Longer Default

**Impact**: HIGH - Affects all implementations

**Before**: SDK automatically included Claude Code's system prompt
**After**: Must explicitly request or provide custom system prompt

```python
# OLD (implicit Claude Code prompt)
client = ClaudeSDKClient()

# NEW (must specify)
from claude_agent_sdk import ClaudeAgentOptions

# Option 1: Use Claude Code preset
options = ClaudeAgentOptions(
    system_prompt="preset:claude-code"  # Explicitly request Claude Code prompt
)

# Option 2: Provide custom prompt
options = ClaudeAgentOptions(
    system_prompt="You are a specialized investment analyst..."
)

# Option 3: Append to default
options = ClaudeAgentOptions(
    system_prompt="Additional instructions...",
    append_system_prompt=True  # Appends to base prompt
)

client = ClaudeSDKClient(options=options)
```

### 2. ⚠️ Settings Sources Not Auto-Loaded

**Impact**: MEDIUM - Affects projects using CLAUDE.md or settings.json

**Before**: SDK automatically loaded filesystem settings (CLAUDE.md, .mcp.json)
**After**: Must explicitly configure setting sources

```python
# OLD (automatic)
client = ClaudeSDKClient()

# NEW (explicit configuration required)
from claude_agent_sdk import SettingSource

options = ClaudeAgentOptions(
    setting_sources=[
        SettingSource.USER,      # ~/.claude/
        SettingSource.PROJECT,   # .claude/
        SettingSource.WORKSPACE  # workspace settings
    ]
)

client = ClaudeSDKClient(options=options)
```

### 3. ⚠️ Package Name Changes

**Impact**: LOW - Only affects imports

- Python: `claude_code_sdk` → `claude_agent_sdk`
- TypeScript: `@anthropic-ai/claude-code` → `@anthropic-ai/claude-agent-sdk`
- Type: `ClaudeCodeOptions` → `ClaudeAgentOptions`

---

## Feature Additions in Agent SDK

### New Capabilities Not Available in Code SDK

#### 1. 🎯 Subagents (Multi-Agent Orchestration)
```python
options = ClaudeAgentOptions(
    agents={
        'code-reviewer': {
            'description': 'Expert code review specialist',
            'prompt': 'Analyze for security and best practices',
            'tools': ['Read', 'Grep', 'Glob'],
            'model': 'sonnet'
        },
        'documentation-writer': {
            'description': 'Technical documentation expert',
            'prompt': 'Create clear, comprehensive docs',
            'tools': ['Read', 'Write'],
            'model': 'haiku'
        }
    }
)
```

**Benefits**:
- Parallel execution (massive speed improvements)
- Specialized contexts (prevent information overload)
- Task-specific tool access

#### 2. 📊 Cost Tracking
```python
# Track API costs at message level
for message in client.receive_messages():
    if isinstance(message, AssistantMessage):
        usage = message.usage
        if usage:
            print(f"Input tokens: {usage.input_tokens}")
            print(f"Output tokens: {usage.output_tokens}")
            print(f"Cache hits: {usage.cache_read_input_tokens}")
            print(f"Total cost: ${usage.total_cost_usd}")
```

#### 3. 🎯 Todo Tracking
```python
# SDK automatically creates and manages todos
# Track progress through message stream
for message in client.receive_messages():
    if message.subtype == 'todo_update':
        print(f"Todo: {message.content}")
        print(f"Status: {message.status}")  # pending, in_progress, completed
```

#### 4. 🔧 Advanced Hooks
```python
async def pre_tool_use(tool_name: str, tool_input: dict):
    """Called before any tool execution"""
    print(f"About to execute: {tool_name}")
    # Can modify input or deny execution
    return {"behavior": "allow", "updatedInput": tool_input}

async def post_tool_use(tool_name: str, result: dict):
    """Called after tool execution"""
    print(f"Tool {tool_name} completed")
    # Can log, monitor, or modify result

options = ClaudeAgentOptions(
    hooks={
        'pre_tool_use': pre_tool_use,
        'post_tool_use': post_tool_use
    }
)
```

#### 5. 🔐 Enhanced Permissions
```python
# Four permission modes
options = ClaudeAgentOptions(
    permission_mode="default"          # Standard checks
    # permission_mode="plan"           # Read-only (not yet supported)
    # permission_mode="acceptEdits"    # Auto-approve file edits
    # permission_mode="bypassPermissions"  # Allow all (dangerous!)
)

# Permission flow:
# 1. PreToolUse Hook
# 2. Ask Rules (settings.json)
# 3. Deny Rules (settings.json)
# 4. Permission Mode Check
# 5. Allow Rules (settings.json)
# 6. canUseTool Callback
# 7. PostToolUse Hook
```

#### 6. 🧠 Session Management
```python
# Capture session ID
session_id = None
for message in client.receive_messages():
    if isinstance(message, SystemMessage) and message.subtype == 'init':
        session_id = message.session_id

# Resume later
new_client = ClaudeSDKClient(options=ClaudeAgentOptions(
    resume=session_id,
    fork_session=False  # True to branch, False to continue
))
```

---

## Navam Project Migration Checklist

### Immediate Actions Required

- [x] ✅ Update imports in `src/navam/chat.py`
- [x] ✅ Rename `ClaudeCodeOptions` → `ClaudeAgentOptions`
- [ ] ⚠️ Add explicit system prompt configuration
- [ ] ⚠️ Configure setting sources for CLAUDE.md and .mcp.json
- [ ] Update requirements.txt / pyproject.toml dependencies

### Optional Enhancements to Consider

#### High Priority (Performance Improvements)

1. **Implement Subagents** (Issue #2 solution)
   - Current: Sequential agent execution
   - With subagents: Parallel execution
   - **Expected impact**: 3-4x faster workflows

   ```python
   # For /invest:research-stock command
   options = ClaudeAgentOptions(
       agents={
           'fundamental-analyst': {
               'description': 'Analyze company fundamentals',
               'tools': ['mcp__company-research__*'],
               'model': 'sonnet'
           },
           'technical-analyst': {
               'description': 'Analyze price and volume patterns',
               'tools': ['mcp__stock-analyzer__*'],
               'model': 'sonnet'
           },
           'news-analyst': {
               'description': 'Analyze recent news sentiment',
               'tools': ['mcp__news-analyzer__*'],
               'model': 'haiku'  # Faster for news summarization
           }
       }
   )
   # All three analysts run in parallel! 🚀
   ```

2. **Add Cost Tracking** (Issue #6 enhancement)
   - Track API usage per session
   - Display costs in `/perf` command
   - Monitor cache effectiveness impact on costs

3. **Implement Pre/Post Tool Hooks** (Issue #2 solution)
   - Pre-tool hook: Check cache before execution
   - Post-tool hook: Cache results after execution
   - **This enables client-side caching!**

   ```python
   async def pre_tool_use_hook(tool_name: str, tool_input: dict):
       # Check cache
       cached = session_cache.get(tool_name, tool_input)
       if cached is not None:
           # Return cached result, skip actual tool execution
           return {
               "behavior": "deny",
               "message": "Using cached result",
               "result": cached
           }
       return {"behavior": "allow"}

   async def post_tool_use_hook(tool_name: str, tool_input: dict, result: dict):
       # Cache result for future use
       if tool_name.startswith("mcp__"):
           session_cache.set(tool_name, tool_input, result)
   ```

#### Medium Priority

4. **Enhanced Todo Tracking**
   - Already partially implemented
   - SDK now provides native todo support
   - Can remove custom implementation and use SDK's

5. **Session Persistence**
   - Save session IDs to resume workflows
   - Implement session history browser
   - Allow users to fork sessions for "what-if" analysis

#### Low Priority

6. **Model Selection Per Agent**
   - Use Sonnet for complex analysis
   - Use Haiku for simple tasks (faster, cheaper)
   - Optimize cost vs performance

---

## Migration Timeline Recommendation

### Phase 1: Critical Updates (Day 1)
- [ ] Update package dependencies
- [ ] Fix import statements
- [ ] Add explicit system prompt
- [ ] Configure setting sources
- [ ] Test existing functionality

### Phase 2: Performance Enhancements (Week 1)
- [ ] Implement pre/post tool hooks for caching
- [ ] Add subagents for parallel execution
- [ ] Integrate cost tracking

### Phase 3: Advanced Features (Week 2-3)
- [ ] Session management UI
- [ ] Enhanced permissions
- [ ] Model optimization per agent
- [ ] Todo tracking integration

---

## Testing Strategy

### 1. Smoke Tests
```bash
# Test basic functionality
python -m pytest tests/test_agent_sdk_migration.py

# Test MCP integration
python -m pytest tests/test_mcp_integration.py
```

### 2. Integration Tests
```bash
# Test full workflow
navam /invest:research-stock AAPL

# Verify /cache command shows metrics
navam /cache

# Check /perf for cost tracking
navam /perf
```

### 3. Performance Tests
```bash
# Before migration baseline
# After migration comparison
# Subagents parallel execution benchmark
```

---

## Rollback Plan

If migration issues arise:

```bash
# Quick rollback
pip uninstall claude-agent-sdk
pip install claude-code-sdk==<previous-version>

# Revert code changes
git revert <migration-commit>
```

---

## Resources

- [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)
- [Python API Reference](https://docs.claude.com/en/api/agent-sdk/python)
- [Subagents Documentation](https://docs.claude.com/en/api/agent-sdk/subagents)
- [Cost Tracking Guide](https://docs.claude.com/en/api/agent-sdk/cost-tracking)
- [Permissions System](https://docs.claude.com/en/api/agent-sdk/permissions)

---

## Questions or Issues?

- Check updated documentation in `artifacts/refer/claude-agent-sdk/`
- Review code examples in tests/
- Consult performance improvements backlog for optimization opportunities

---

*Last Updated: 2025-01-10*
*Version: 1.0*
*Status: Active Migration*
