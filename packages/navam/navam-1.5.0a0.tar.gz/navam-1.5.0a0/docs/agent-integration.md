# Agent Integration with Claude Code SDK

## Overview

Navam includes 18 specialized AI agents that are automatically recognized by the Claude Code SDK when installed via PyPI. This document explains how the integration works.

## How It Works

### Agent Recognition by Claude Code SDK

The Claude Code SDK automatically detects subagents from:
- **Project-level**: `.claude/agents/*.md` (in the current directory)
- **User-level**: `~/.claude/agents/*.md` (in user's home directory)

### Navam's Implementation

Navam ensures agents are available regardless of installation method through a multi-tier approach:

#### 1. Development Environment
When running from the git repository, agents are available in `.claude/agents/`:
```
navam/
├── .claude/
│   └── agents/
│       ├── atlas-investment-strategist.md
│       ├── quill-equity-analyst.md
│       └── ... (18 agents total)
```

#### 2. PyPI Installation
When installed via `pip install navam`, agents are packaged in `site-packages/navam/agents/`:
```
site-packages/
└── navam/
    ├── agents/
    │   ├── atlas-investment-strategist.md
    │   ├── quill-equity-analyst.md
    │   └── ... (18 agents total)
    └── chat.py
```

On first run, Navam automatically copies agents to `~/.claude/agents/` so the Claude Code SDK can find them.

### Code Implementation

The key implementation is in `src/navam/chat.py`:

```python
def _get_agent_directories(self) -> List[Path]:
    """
    Get directories containing .claude/agents/ to be added to Claude Code SDK's accessible paths.
    """
    agent_dirs = []

    # Check for local development .claude/agents
    if Path(".claude/agents").exists():
        agent_dirs.append(Path.cwd())

    # Check for package installation
    package_agents_dir = Path(__file__).parent / "agents"
    if package_agents_dir.exists():
        self._ensure_user_agents_dir(package_agents_dir)

    # Check for user-level agents
    user_claude_agents = Path.home() / ".claude" / "agents"
    if user_claude_agents.exists():
        agent_dirs.append(Path.home())

    return agent_dirs

def _ensure_user_agents_dir(self, package_agents_dir: Path):
    """
    Ensure agents from package are available in ~/.claude/agents/
    """
    user_agents_dir = Path.home() / ".claude" / "agents"
    user_agents_dir.mkdir(parents=True, exist_ok=True)

    # Copy agent files if not already present
    for agent_file in package_agents_dir.glob("*.md"):
        dest_file = user_agents_dir / agent_file.name
        if not dest_file.exists():
            shutil.copy2(agent_file, dest_file)
```

The directories are then passed to `ClaudeCodeOptions`:

```python
self.claude_options = ClaudeCodeOptions(
    # ... other options
    add_dirs=agent_dirs,  # Enable SDK to find agents
)
```

## Available Agents

Navam includes 18 specialized financial agents organized by category:

### Strategy & Planning (3 agents)
- `atlas-investment-strategist` - Portfolio strategy & asset allocation
- `compass-goal-planner` - Financial planning & goal mapping
- `macro-lens-strategist` - Market analysis & sector allocation

### Research & Analysis (4 agents)
- `quill-equity-analyst` - Company research & valuation
- `earnings-whisperer` - Earnings analysis & guidance
- `news-sentry-market-watch` - Real-time signal detection
- `screen-forge` - Stock screening & candidate identification

### Portfolio Management (4 agents)
- `quant-portfolio-optimizer` - Risk/return optimization
- `risk-shield-manager` - Portfolio risk monitoring
- `rebalance-bot` - Portfolio rebalancing
- `ledger-performance-analyst` - Performance & attribution

### Trading & Execution (2 agents)
- `trader-jane-execution` - Order routing & TCA
- `compliance-sentinel` - Regulatory compliance

### Tax & Treasury (2 agents)
- `tax-scout` - Tax-loss harvesting & optimization
- `cash-treasury-steward` - Treasury & liquidity management

### Advanced Strategies (2 agents)
- `hedge-smith-options` - Hedging & protection strategies
- `factor-scout` - Factor exposure analysis

### Knowledge Management (1 agent)
- `notionist-librarian` - Research organization

## Verification

To verify agents are properly configured:

```bash
navam chat
# Then use:
/agents  # List all available agents
```

Or check the agent files directly:

```bash
ls -la ~/.claude/agents/
```

## Technical Details

### Package Data Configuration

Agents are included in the package distribution via `pyproject.toml`:

```toml
[tool.setuptools.package-data]
"navam" = [
    "agents/*.md",
    # ...
]
```

### Agent File Format

Each agent follows the Claude Code SDK format with YAML frontmatter:

```markdown
---
name: agent-name
description: When to use this agent...
model: sonnet
color: blue
---

You are [Agent Name], a specialized AI assistant for...

**Core Competencies:**
- ...

**Approach:**
1. ...
```

## Benefits

1. **Automatic Discovery**: Agents work immediately after installation
2. **User Customization**: Users can modify agents in `~/.claude/agents/`
3. **Version Control**: Package updates can include new/updated agents
4. **Separation of Concerns**: Development agents in `.claude/`, user agents in `~/.claude/`
5. **Cross-platform**: Works on macOS, Linux, and Windows

## Troubleshooting

### Agents Not Appearing

If agents don't appear in chat:

1. Check if `~/.claude/agents/` exists:
   ```bash
   ls ~/.claude/agents/
   ```

2. Verify 18 agent files are present:
   ```bash
   ls ~/.claude/agents/*.md | wc -l
   # Should output: 18
   ```

3. Run `navam chat` again - first run copies agents automatically

### Updating Agents

To update agents from package:

```bash
# Remove existing user agents
rm -rf ~/.claude/agents/

# Run navam chat - will recreate from package
navam chat
```

## Future Enhancements

Potential improvements:
- Agent versioning and update checking
- User-specific agent customization without losing updates
- Agent marketplace for community contributions
- Performance metrics for agent usage
