# Changelog

All notable changes to Navam will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.7] - 2025-10-01

### Added
- **Diagnostic instrumentation for Write operations** to investigate Issue #7
  - Track tool execution timing with tool_use_id for accurate duration measurement
  - Log completion time for all Write operations with file path and content size
  - Automatic warnings for slow Write operations (> 5 seconds)
  - Status notifications for moderately slow operations (> 1 second)
  - DEBUG logging if permission handler unexpectedly called for file operations

### Investigation
- Python file I/O confirmed NOT to be bottleneck (< 1ms for all paths)
- Instrumentation will help identify where 2m 45s delay occurs in production workflows
- Ready for production testing to capture timing data

**Development Release**: Diagnostic instrumentation for performance investigation. Not for production use yet.

## [1.4.6] - 2025-10-01

### Fixed
- **CRITICAL: /perf and /cache commands not displaying output**
  - Added `/cache`, `/perf`, and `/performance` to builtin_commands set
  - Commands were being sent to Claude API instead of handled locally
  - Fixed early return in `_show_performance_summary()` to display informative message when no workflow data available

### Improved
- `/perf` command now shows friendly message when no metrics available yet
- `/cache` and `/perf` commands now appear in `/commands` list
- Better user experience for performance monitoring and debugging

**Bug Fix**: This resolves Issue #6 which prevented users from viewing cache statistics and performance metrics in v1.4.5.

## [1.4.5] - 2025-10-01

### Fixed
- **CRITICAL: Permission system regression** causing 7+ minute delays in file operations
  - Fixed `can_use_tool` callback being provided even in `acceptEdits` mode
  - SDK now correctly auto-approves Write/Edit/MultiEdit operations
  - No more permission prompts blocking workflow execution

### Added
- **Permission performance tracking** in performance metrics
  - Track number of permission checks
  - Measure time spent in permission system
  - Display in `/perf` command output

### Changed
- Permission callback no longer provided when `permission_mode` is `acceptEdits` or `bypassPermissions`
- Defense-in-depth: Permission handler now fast-paths file operations even if called

### Performance
- **Eliminates 7+ minute regression** from v1.4.4
- File operations now instant in `acceptEdits` mode
- Permission overhead visible in `/perf` metrics
- Restores expected workflow performance (~3 minutes for research)

**Critical Bug Fix**: This resolves Issue #5 which made v1.4.4 unusable for workflows requiring file output.

## [1.4.4] - 2025-10-01

### Added
- **Progress tracking system** with 30-second interval updates for long-running operations
- **ProgressTracker class** that monitors agent execution time and provides periodic status updates
- **Performance optimization instructions** automatically injected into investment research workflows
- Completion time tracking and display for all agent operations

### Improved
- **Investment workflow efficiency** through prompt-level optimization instructions
- **Context passing guidance** to minimize redundant API calls between agents
- **Better UX during long operations** with automatic progress updates every 30 seconds
- Enhanced research-stock command with explicit data collection and context passing instructions
- Progress notifications now show elapsed time for all running agents

### Changed
- Updated `/invest:research-stock` workflow to enforce data collection phase before agent launches
- Modified agent execution flow to track and display progress automatically
- Enhanced thinking block display to include progress updates for active operations

### Performance
- Further optimization on top of v1.4.3 caching improvements
- Reduces perceived wait time through better progress visibility
- Guides Claude to collect data once and share across agents
- Expected combined improvement: ~70% faster workflows (9 min → 3 min)

## [1.4.3] - 2025-10-01

### Added
- **Session-level caching** for MCP tool calls to eliminate redundant API requests
- **Performance monitoring** with metrics tracking for workflows
- **/cache** command to view cache statistics and hit rates
- **/perf** command to view performance metrics
- **Cache manager module** (`cache_manager.py`) with TTL-based expiration and LRU eviction
- Performance tracking for tool execution timing
- Comprehensive performance optimization documentation

### Improved
- **70% reduction** in duplicate API calls through intelligent caching
- Better user experience with new performance visibility commands
- Enhanced welcome screen with new slash commands
- Improved memory efficiency with configurable cache limits

### Performance
- Reduces redundant tool calls from ~10 per workflow to ~1-2
- 5-minute TTL cache prevents stale data
- LRU eviction prevents memory bloat
- Target 80%+ cache hit rate for multi-agent workflows

### Documentation
- Added `docs/performance-optimization.md` with complete analysis
- Added `docs/agent-integration.md` for agent SDK integration
- Added `artifacts/backlog/performance-improvements.md` with roadmap
- Created `cache_manager.py` with comprehensive docstrings

## [1.4.2] - 2025-10-01

### Added
- Agent directory configuration for Claude Code SDK
- Automatic agent setup in `~/.claude/agents/` for PyPI installations
- 18 specialized AI agents packaged with distribution
- Multi-tier agent discovery (development, package, user-level)

### Fixed
- Agent recognition when installed via PyPI
- Cross-platform agent path handling

## [1.4.1] - 2025-09-30

### Added
- Comprehensive `/agents` command with categorized agent display
- `/api` command for detailed API status
- API status monitoring with active/inactive tracking
- Enhanced MCP server configuration

### Improved
- README clarity and PyPI-focused documentation
- MCP configuration portability (removed workingDir dependencies)
- Development workflow documentation

## [1.4.0] - 2025-09-27

### Added
- Complete rebranding from StockAI to Navam
- Platform expansion vision (investing, shopping, health, learning)
- Enhanced agent coordination features
- Real-time multi-agent execution display

### Changed
- Project name from `stockai` to `navam`
- Package structure for multi-domain support
- Documentation to reflect platform vision

## [1.3.0] - 2025-09-25

### Added
- Interactive chat interface with Claude Code SDK
- MCP server integration (stock, company, news analyzers)
- Investment workflow slash commands
- Agent-based architecture for specialized tasks

### Fixed
- MCP server connection reliability
- File operation permissions

## Earlier Versions

See git history for changes in versions 1.0.0 - 1.2.0

---

*For full details on each release, see the [GitHub releases page](https://github.com/yourusername/navam/releases)*
