# Development Guide

## Package Synchronization

When developing the `navam` package, certain files need to be synchronized from development locations to the package structure for proper bundling and deployment.

### Sync Package Script

The `scripts/sync_package.py` script automates the synchronization process that ensures production deployments work correctly.

#### Usage

```bash
# Option 1: Run the standalone script
python scripts/sync_package.py

# Option 2: Run from the navam package (for development)
uv run python -m navam.sync

# Option 3: Use with uv directly
uv run python scripts/sync_package.py
```

#### What It Does

1. **Investment Commands**: Copies all `.md` files from `.claude/commands/invest/` to `src/navam/commands/invest/`
2. **MCP Configuration**: Converts development MCP config to production format
   - Changes `uv run python -m src.stock_mcp.server stdio` → `python -m stock_mcp.server stdio`
   - Removes development-specific settings like `workingDir`
3. **Validation**: Verifies package structure and configuration is ready for building

#### When to Run

Run the sync script whenever:
- Investment commands are added/updated in `.claude/commands/invest/`
- MCP server configurations change in `.mcp.json`
- Before building/releasing a new package version
- After making changes that affect bundled package components

#### Example Output

```
🔄 Syncing package files...

✅ Copied 8 investment commands:
   - README.md
   - execute-rebalance.md
   - monitor-holdings.md
   - optimize-taxes.md
   - plan-goals.md
   - research-stock.md
   - review-portfolio.md
   - screen-opportunities.md

✅ Updated MCP configuration for production:
   - stock-analyzer: python -m stock_mcp.server stdio
   - company-research: python -m company_mcp.server stdio
   - news-analyzer: python -m news_mcp.server stdio

✅ Package structure verified:
   - Investment commands: 8 files
   - MCP configuration: present
   - Package config: present

✅ Package data configuration is correct

✅ Package sync completed successfully!
📦 Ready to build package with: uv run python -m build
```

### File Structure

#### Source Files (Development)
- `.claude/commands/invest/` - Investment command documentation
- `.mcp.json` - Development MCP server configuration

#### Target Files (Package)
- `src/navam/commands/invest/` - Bundled investment commands
- `src/navam/.mcp.json` - Production MCP configuration

#### Related Files
- `scripts/sync_package.py` - Standalone sync script
- `src/navam/sync.py` - Package version of sync script
- `src/navam/tools.py` - Discovery logic for commands and MCP servers
- `pyproject.toml` - Package data configuration for bundling

### Why This Is Needed

The sync process fixes the production deployment issue where:
- `pip install navam` would show "No MCP servers loaded"
- Investment commands weren't found ("No investment commands found")
- MCP tools were visible but servers wouldn't start

By ensuring files are properly bundled and configured for production, the package works correctly in any environment.

## Building and Testing

After running the sync script:

```bash
# Build the package
uv run python -m build

# Test in a clean environment
python -m venv test_env
source test_env/bin/activate
pip install dist/navam-*.whl

# Verify functionality
python -c "
import navam.tools
print('MCP Servers:', list(navam.tools.get_mcp_servers().keys()))
print('Investment Commands:', len(navam.tools.load_agent_commands()))
"
```

Expected output:
```
MCP Servers: ['stock-analyzer', 'company-research', 'news-analyzer']
Investment Commands: 8
```