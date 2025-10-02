# Reference Documentation Index

This folder contains reference materials for the Navam project, organized by topic.

---

## 📚 Documentation Structure

### Claude Agent SDK (Primary AI Framework)
**Location**: `claude-agent-sdk/`

**Start Here**:
- [`overview.md`](claude-agent-sdk/overview.md) - Complete SDK capabilities and features
- [`MIGRATION-GUIDE.md`](claude-agent-sdk/MIGRATION-GUIDE.md) - Migrate from Claude Code SDK
- [`CRITICAL-INSIGHTS-FOR-NAVAM.md`](claude-agent-sdk/CRITICAL-INSIGHTS-FOR-NAVAM.md) - Performance optimization opportunities

**Key Topics**:
- Subagents (parallel execution)
- Hooks system (pre/post tool execution)
- Cost tracking
- Permissions
- Session management
- Custom tools
- MCP integration

### Model Context Protocol (MCP)
**Location**: `mcp/`

- MCP server development
- Python SDK reference
- Tool and resource patterns

### Best Practices & Patterns
**Files in root**:
- [`claude-code-best-practices.md`](claude-code-best-practices.md) - General AI agent best practices
- [`building-effective-agents.md`](building-effective-agents.md) - Agent design patterns
- [`agents.md`](agents.md) - Agent configurations

### Next.js (If needed for future web interface)
**Location**: `nextjs/`

---

## 🎯 Quick Navigation

### For Migration Tasks
1. Start: [`claude-agent-sdk/MIGRATION-GUIDE.md`](claude-agent-sdk/MIGRATION-GUIDE.md)
2. Reference: [`claude-agent-sdk/overview.md`](claude-agent-sdk/overview.md)
3. Implementation: [`claude-agent-sdk/CRITICAL-INSIGHTS-FOR-NAVAM.md`](claude-agent-sdk/CRITICAL-INSIGHTS-FOR-NAVAM.md)

### For Performance Optimization
1. Analysis: [`claude-agent-sdk/CRITICAL-INSIGHTS-FOR-NAVAM.md`](claude-agent-sdk/CRITICAL-INSIGHTS-FOR-NAVAM.md)
2. Implementation Plan: `../backlog/COMPREHENSIVE-AGENT-SDK-MIGRATION-AND-PERFORMANCE-PLAN.md`

### For MCP Server Development
1. Python SDK: [`mcp/Python-SDK-README.md`](mcp/Python-SDK-README.md)
2. Full Spec: [`mcp/llms-full.txt`](mcp/llms-full.txt)

### For Agent Design
1. Best Practices: [`claude-code-best-practices.md`](claude-code-best-practices.md)
2. Design Patterns: [`building-effective-agents.md`](building-effective-agents.md)

---

## 📝 Important Notes

### Claude Code SDK → Claude Agent SDK
- **Old SDK** (claude-code-sdk) is being deprecated
- **New SDK** (claude-agent-sdk) is the current version
- All new development should use Agent SDK
- See migration guide for breaking changes

### Documentation Organization
- **claude-agent-sdk/** - Most up-to-date AI framework docs
- **mcp/** - MCP server development (still current)
- Root files - General patterns and best practices

---

## 🔄 Keeping Documentation Updated

When adding new reference docs:
1. Place in appropriate subfolder
2. Update this README with link
3. Update `CLAUDE.md` if it affects project instructions
4. Cross-reference with related docs

---

*Last Updated: 2025-01-10*
*Maintainer: Development Team*
