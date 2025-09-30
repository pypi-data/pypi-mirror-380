#!/usr/bin/env python3
"""
Sync Package Files Script

Synchronizes development files to package structure for proper bundling.
This script implements the sync-package command functionality.
"""

import json
import shutil
from pathlib import Path


def sync_investment_commands():
    """Copy investment commands from .claude/commands/invest/ to src/navam/commands/invest/"""
    source_dir = Path('.claude/commands/invest')
    target_dir = Path('src/navam/commands/invest')

    if not source_dir.exists():
        print(f"❌ Source directory not found: {source_dir}")
        return False

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy all files from source to target
    copied_files = []
    for file_path in source_dir.glob('*'):
        if file_path.is_file():
            target_file = target_dir / file_path.name
            shutil.copy2(file_path, target_file)
            copied_files.append(file_path.name)

    print(f"✅ Copied {len(copied_files)} investment commands:")
    for file_name in sorted(copied_files):
        print(f"   - {file_name}")

    return True


def sync_mcp_configuration():
    """Copy and update MCP configuration for production deployment"""
    source_file = Path('.mcp.json')
    target_file = Path('src/navam/.mcp.json')

    if not source_file.exists():
        print(f"❌ Source MCP config not found: {source_file}")
        return False

    # Read source configuration
    with open(source_file, 'r') as f:
        config = json.load(f)

    # Update server configuration for production deployment
    if 'mcpServers' in config:
        for server_name, server_config in config['mcpServers'].items():
            # Convert complex development config to simple production config
            if 'args' in server_config and isinstance(server_config['args'], list):
                # Find the module name in args (after -m flag)
                module_name = None
                for i, arg in enumerate(server_config['args']):
                    if arg == '-m' and i + 1 < len(server_config['args']):
                        module_name = server_config['args'][i + 1]
                        break

                if module_name and module_name.startswith('src.'):
                    # Convert src.stock_mcp.server to stock_mcp.server
                    production_module = module_name.replace('src.', '')

                    # Set robust production configuration using sys.executable placeholder
                    # This will be replaced at runtime with the actual Python interpreter
                    server_config['command'] = '{{SYS_EXECUTABLE}}'
                    server_config['args'] = ['-m', production_module, 'stdio']

                    # Remove development-specific settings
                    if 'workingDir' in server_config:
                        del server_config['workingDir']

    # Write updated configuration to target
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(target_file, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"✅ Updated MCP configuration for production:")
    if 'mcpServers' in config:
        for server_name, server_config in config['mcpServers'].items():
            args_str = ' '.join(server_config.get('args', []))
            print(f"   - {server_name}: {server_config.get('command', 'python')} {args_str}")

    return True


def verify_package_structure():
    """Verify that package structure is correct for bundling"""
    required_paths = [
        'src/navam/commands/invest',
        'src/navam/.mcp.json',
        'pyproject.toml'
    ]

    missing_paths = []
    for path_str in required_paths:
        path = Path(path_str)
        if not path.exists():
            missing_paths.append(path_str)

    if missing_paths:
        print(f"❌ Missing required paths:")
        for path in missing_paths:
            print(f"   - {path}")
        return False

    # Check investment commands
    invest_dir = Path('src/navam/commands/invest')
    invest_files = list(invest_dir.glob('*.md'))
    print(f"✅ Package structure verified:")
    print(f"   - Investment commands: {len(invest_files)} files")
    print(f"   - MCP configuration: present")
    print(f"   - Package config: present")

    return True


def check_pyproject_configuration():
    """Verify pyproject.toml has correct package data configuration"""
    pyproject_file = Path('pyproject.toml')

    if not pyproject_file.exists():
        print("❌ pyproject.toml not found")
        return False

    content = pyproject_file.read_text()

    # Check for required package data configuration
    required_configs = [
        '"commands/invest/*.md"',
        '".mcp.json"'
    ]

    missing_configs = []
    for config in required_configs:
        if config not in content:
            missing_configs.append(config)

    if missing_configs:
        print(f"❌ Missing package data configuration in pyproject.toml:")
        for config in missing_configs:
            print(f"   - {config}")
        return False

    print("✅ Package data configuration is correct")
    return True


def main():
    """Main sync function"""
    print("🔄 Syncing package files...")
    print()

    success = True

    # Sync investment commands
    if not sync_investment_commands():
        success = False

    print()

    # Sync MCP configuration
    if not sync_mcp_configuration():
        success = False

    print()

    # Verify package structure
    if not verify_package_structure():
        success = False

    print()

    # Check pyproject configuration
    if not check_pyproject_configuration():
        success = False

    print()

    if success:
        print("✅ Package sync completed successfully!")
        print("📦 Ready to build package with: uv run python -m build")
    else:
        print("❌ Package sync failed - please check errors above")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())