# Claude Agent SDK Overview

**Formerly**: Claude Code SDK
**Status**: Renamed and enhanced (2025)
**Purpose**: Build production-ready AI agents across any domain

---

## What is Claude Agent SDK?

The Claude Agent SDK (formerly Claude Code SDK) provides comprehensive building blocks for creating sophisticated AI agents. While it started as a coding assistant SDK, it has evolved to support agents across all domains:

### Supported Agent Types

**🤖 Business Agents**
- Legal contract reviewers
- Finance analysis assistants
- Customer support agents
- Content creation tools
- HR and recruiting assistants

**💻 Specialized Coding Agents**
- SRE diagnostic tools
- Security review bots
- Oncall engineering assistants
- Code review agents
- DevOps automation

**🎯 Custom Domain Agents**
- Investment research analysts
- Medical diagnostics assistants
- Educational tutors
- Research assistants
- Any specialized domain

---

## Core Features

### 1. 🧠 Context Management
- **Automatic context compaction**: Prevents running out of context
- **Smart summarization**: Maintains conversation continuity
- **Session persistence**: Resume workflows across restarts

### 2. 🔧 Comprehensive Tool Ecosystem

**Built-in Tools:**
- File operations (Read, Write, Edit, Glob, Grep)
- Code execution (Bash, Python)
- Web search and fetching
- MCP (Model Context Protocol) extensibility

**Custom Tools:**
- Define domain-specific tools
- Type-safe with Zod schemas
- Async/await support
- Error handling

### 3. 🎯 Advanced Agent Capabilities

**Subagents:**
- Parallel execution (3-4x faster workflows)
- Specialized contexts (prevent information overload)
- Task-specific tool access
- Independent system prompts

**Sessions:**
- Persistent conversation memory
- Resume/fork workflows
- Session branching for exploration
- Cross-session learning

### 4. 🔐 Fine-Grained Permissions

**Four Permission Modes:**
- `default`: Standard permission checks
- `plan`: Read-only tool usage (not yet supported)
- `acceptEdits`: Auto-approve file edits
- `bypassPermissions`: Allow all (use cautiously)

**Permission Flow:**
1. PreToolUse Hook
2. Ask Rules (settings.json)
3. Deny Rules (settings.json)
4. Permission Mode Check
5. Allow Rules (settings.json)
6. canUseTool Callback
7. PostToolUse Hook

### 5. 📊 Built-in Monitoring

**Cost Tracking:**
- Token usage per message
- Cache hit rates
- Total cost in USD
- Step-by-step breakdown

**Todo Tracking:**
- Automatic task decomposition
- Real-time progress updates
- Status transitions (pending → in_progress → completed)

### 6. 🔌 Extensibility

**MCP Integration:**
- stdio servers (external processes)
- HTTP/SSE servers (remote services)
- SDK MCP servers (in-process)
- Custom resources and tools

**Hooks System:**
- Pre/post tool execution
- Request/response interceptors
- Error handlers
- Custom logging

---

## SDK Options

### Python SDK
```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

options = ClaudeAgentOptions(
    system_prompt="You are an expert investment analyst",
    allowed_tools=['Read', 'mcp__stock-analyzer__*'],
    permission_mode="acceptEdits",
    agents={
        'fundamental-analyst': {
            'description': 'Analyze company fundamentals',
            'tools': ['mcp__company-research__*']
        }
    }
)

client = ClaudeSDKClient(options=options)
```

### TypeScript/JavaScript SDK
```typescript
import { query, ClaudeAgentOptions } from '@anthropic-ai/claude-agent-sdk';

const options: ClaudeAgentOptions = {
  systemPrompt: 'You are an expert investment analyst',
  allowedTools: ['Read', 'mcp__stock-analyzer__*'],
  permissionMode: 'acceptEdits'
};

const result = await query({
  prompt: 'Analyze AAPL stock',
  options
});
```

---

## Authentication Methods

### 1. Claude API Key
```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'your-key-here'

client = ClaudeSDKClient()
```

### 2. Amazon Bedrock
```python
options = ClaudeAgentOptions(
    provider='bedrock',
    region='us-west-2'
)
```

### 3. Google Vertex AI
```python
options = ClaudeAgentOptions(
    provider='vertex',
    project_id='your-project'
)
```

---

## Key Differentiators

### vs Other Agent Frameworks

**✅ File System Integration**
- Leverages Claude Code's proven filesystem config
- Project-level (`.claude/`) and user-level (`~/.claude/`) settings
- Version-controlled agent configurations

**✅ Production-Ready**
- Built-in error handling
- Automatic context management
- Robust permission system
- Cost and performance monitoring

**✅ MCP Native**
- First-class Model Context Protocol support
- Easy extensibility with MCP servers
- Standard protocol for tool integration

**✅ Advanced Features**
- Subagents for parallel execution
- Session management and forking
- Todo tracking and progress monitoring
- Comprehensive hooks system

---

## Use Case Examples

### Investment Research Agent (Navam)
```python
options = ClaudeAgentOptions(
    system_prompt="You are an expert investment analyst",
    agents={
        'fundamental-analyst': {
            'description': 'Analyze company fundamentals',
            'tools': ['mcp__company-research__*'],
            'model': 'sonnet'
        },
        'technical-analyst': {
            'description': 'Analyze price patterns',
            'tools': ['mcp__stock-analyzer__*'],
            'model': 'sonnet'
        },
        'news-analyst': {
            'description': 'Analyze news sentiment',
            'tools': ['mcp__news-analyzer__*'],
            'model': 'haiku'  # Faster, cheaper
        }
    }
)

# All three analysts run in parallel! 🚀
client = ClaudeSDKClient(options=options)
await client.query('/invest:research-stock AAPL')
```

### Code Review Agent
```python
options = ClaudeAgentOptions(
    system_prompt="You are a senior software engineer focused on security",
    agents={
        'security-reviewer': {
            'description': 'Review for security vulnerabilities',
            'tools': ['Read', 'Grep', 'Glob'],
            'model': 'sonnet'
        },
        'style-reviewer': {
            'description': 'Check code style and best practices',
            'tools': ['Read', 'Grep'],
            'model': 'haiku'
        }
    }
)
```

### Customer Support Agent
```python
options = ClaudeAgentOptions(
    system_prompt="You are a helpful customer support agent",
    agents={
        'ticket-classifier': {
            'description': 'Classify and route support tickets',
            'tools': ['mcp__crm__*'],
            'model': 'haiku'
        },
        'issue-resolver': {
            'description': 'Resolve common customer issues',
            'tools': ['mcp__kb__*', 'mcp__crm__*'],
            'model': 'sonnet'
        }
    }
)
```

---

## Architecture Patterns

### Single Agent (Simple)
```
User Query → Main Agent → Tools → Response
```

**Use when:**
- Simple, linear workflows
- Single domain of expertise
- Low latency requirements

### Multi-Agent (Recommended)
```
User Query → Main Agent
              ├→ Subagent 1 (parallel) → Tools → Results
              ├→ Subagent 2 (parallel) → Tools → Results
              └→ Subagent 3 (parallel) → Tools → Results
              ↓
           Aggregation → Final Response
```

**Use when:**
- Complex, multi-step workflows
- Multiple domains of expertise
- Performance is critical
- Context needs to be separated

### Hierarchical Agents
```
User Query → Orchestrator Agent
              ├→ Domain Agent 1
              │   ├→ Specialist 1a
              │   └→ Specialist 1b
              └→ Domain Agent 2
                  ├→ Specialist 2a
                  └→ Specialist 2b
```

**Use when:**
- Very complex workflows
- Need for specialized sub-specialists
- Deep domain hierarchies

---

## Performance Characteristics

### Streaming vs Single Mode

**Streaming (Recommended):**
- Real-time feedback
- Progressive results
- Interruption support
- Rich interactions

**Single Mode:**
- Simpler implementation
- Good for stateless environments (lambdas)
- One-shot responses

### Parallel Execution with Subagents

**Without Subagents (Sequential):**
```
Agent 1 (60s) → Agent 2 (60s) → Agent 3 (60s) = 180s total
```

**With Subagents (Parallel):**
```
Agent 1 (60s) }
Agent 2 (60s) } → Parallel = 60s total
Agent 3 (60s) }
```

**Performance Improvement**: 3x faster (or more with many agents)

---

## Best Practices

### 1. System Prompt Design
```python
# ❌ Bad: Vague and generic
system_prompt = "You are helpful"

# ✅ Good: Specific and actionable
system_prompt = """You are an expert investment analyst specializing in:
- Fundamental analysis using financial statements
- Technical analysis of price patterns
- News sentiment analysis

Follow these guidelines:
1. Always cite sources
2. Provide confidence levels
3. Consider risk factors
4. Use data-driven reasoning
"""
```

### 2. Tool Access Control
```python
# ❌ Bad: Allow all tools
allowed_tools = ['*']

# ✅ Good: Principle of least privilege
allowed_tools = [
    'Read',  # Safe read access
    'mcp__stock-analyzer__*',  # Domain-specific
    'mcp__company-research__get_company_profile'  # Specific tool
]
```

### 3. Subagent Design
```python
# ❌ Bad: One agent doing everything
agents = {
    'do-everything': {
        'description': 'Does all tasks',
        'tools': ['*']  # Too broad
    }
}

# ✅ Good: Specialized, focused agents
agents = {
    'fundamental-analyst': {
        'description': 'Analyze company fundamentals ONLY',
        'tools': ['mcp__company-research__*'],
        'prompt': 'Focus on balance sheet, income statement, cash flow'
    },
    'technical-analyst': {
        'description': 'Analyze price patterns ONLY',
        'tools': ['mcp__stock-analyzer__*'],
        'prompt': 'Focus on trends, indicators, volume patterns'
    }
}
```

### 4. Error Handling
```python
try:
    async for message in client.receive_messages():
        if isinstance(message, ErrorMessage):
            # Handle gracefully
            log_error(message)
            notify_user(message)
        elif isinstance(message, ToolResultBlock):
            if message.is_error:
                # Tool failed, decide recovery strategy
                handle_tool_failure(message)
except Exception as e:
    # Catch SDK-level errors
    handle_sdk_error(e)
```

### 5. Cost Management
```python
# Track costs in real-time
total_cost = 0.0
for message in client.receive_messages():
    if isinstance(message, AssistantMessage) and message.usage:
        step_cost = message.usage.total_cost_usd
        total_cost += step_cost

        # Alert if exceeding budget
        if total_cost > MAX_COST:
            await client.interrupt()
            raise CostLimitExceeded(f"Exceeded ${MAX_COST}")
```

---

## Common Patterns

### Pattern 1: Research Agent
```python
# Gather data → Analyze → Synthesize → Report
```

### Pattern 2: Code Review Agent
```python
# Scan files → Check patterns → Report issues → Suggest fixes
```

### Pattern 3: Interactive Assistant
```python
# Listen → Understand context → Execute tools → Provide feedback → Loop
```

### Pattern 4: Batch Processing
```python
# Load tasks → Process in parallel with subagents → Aggregate results
```

---

## Migration from Claude Code SDK

See [MIGRATION-GUIDE.md](./MIGRATION-GUIDE.md) for comprehensive migration instructions.

**Quick Checklist:**
- [ ] Update package: `pip install claude-agent-sdk`
- [ ] Update imports: `claude_code_sdk` → `claude_agent_sdk`
- [ ] Rename: `ClaudeCodeOptions` → `ClaudeAgentOptions`
- [ ] Add explicit system prompt
- [ ] Configure setting sources

---

## Resources

- [Migration Guide](./MIGRATION-GUIDE.md)
- [Python API Reference](./sdk-python.md)
- [Streaming vs Single Mode](./streaming-vs-single-mode.md)
- [Permissions System](./sdk-permissions.md)
- [Subagents Guide](./subagents.md)
- [Cost Tracking](./sdk-cost-tracking.md)
- [MCP Integration](./sdk-mcp.md)

---

*Last Updated: 2025-01-10*
*Version: 2.0 (Agent SDK)*
