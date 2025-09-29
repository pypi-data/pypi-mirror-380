# Active Backlog

[x] Read artifacts/refer/building-effective-agents.md to understand how to build effective agents. Read .claude/agents/ folder to understand the available agents. Create custom slash commands under .claude/commands/invest/ based on typical retail investor workflows which effectively utilize the agents.

[x] Read artifacts/refer/claude-code-sdk to build a Python package `stockai` managed by uv which will have an interactive chat module running from terminal. The chat will fully utilize capabilities of Claude Code SDK for Python. It will also have access to the MCP tools, agents, and commands defined in this project which will also be bundled as part of the package.

[x] When `uv run stockai chat` command is run and a user prompt is entered the interface waits for few seconds then does not present a response. There should be progressive messages about what Claude Code SDK is doing at the momemnt. There should be a response rendered. Reflect on chat implementation.

[x] When `uv run stockai chat` command is run ensure you are using ClaudeSDKClient instead of query(). Also read the artifacts/refer/claude-code-sdk/ docs to provide more useful notifications to the user when Claude Code SDK is processing a response, like thinking tokens, MCP Server and tools usage, Agents usage, etc. so that user is not waiting on a blank screen before response shows up.

[x] When `uv run stockai chat` command is run, read the docs artifacts/refer/claude-code-sdk/sdk-slash-commands.md to provde capability to easily run custom slash commands defined under .claude/commands/invest/ folder.

[x] When `uv run stockai chat` command is run, just like you show tool execution progress, if agents are being used then show relevant agent usage progress as well.

[x] When `uv run stockai chat` command is run, read artifacts/refer/claude-code-sdk/subagents.md to ensure multi-agent parallel execution is also supported. The progress indication when multi-agents are running should also indicate this to the user.

[x] When `uv run stockai chat` command is run, read artifacts/refer/claude-code-sdk/sdk-permissions.md to enable user to interact with the CLI to provide permissions. Use the same mechanism used by Claude Code to save/read default permissions.

[x] When `uv run stockai chat` command is run, instead of showing progress notifications replacing prior with next one, show progress as a series of well formatted and color coded notifications with newlines, such that user can scroll back and forth to view entire notification history.

[x] Figure out packaging strategy for stockai modules, mcp servers, .claude/commands/invest/ folder commands, .claude/agents/ folder agents, new responses/ folder to write files from stockai chat with permissions enabled, new retrieve/ folder for input files used by the stockai chat, eval/ folder with prompt evaluations for contained MCP servers, and any settings and configuration filts. The package should be ready for publishing to PyPi and installable and functioning independent of containing parent Claude Code folder of src/ folder as it stands. Create a README.md for the package to describe install, run, evaluate, commands, tools, agents, and features. Note that I will continue to develop and test the package using containing parent Claude Code folder with its commands, agents, etc. which I may update from time to time. So if you create a copy of these within package folder for distribution then you should create a slash command in the main Claude Code project to help sync files from parent folder to package folder.

[x] Refer prior backlog item. I don't like the duplication of files this approach required. Rollback changes made for this approach. Instead plan for packaging the root folder as is without duplicating any files.

[x] When `uv run stockai chat` command is run, it is not being able to save files to reports/ folder. Check the permissions so that this is allowed.

[x] When `uv run stockai chat` command is run, if tools are used like Write, TodoWrite, Bash, etc. then also show what files or commands they are working on.

[x] When `uv run stockai chat` command is run, it is not being able to save files. Fix this by improving permissions.

[x] Refactor package and command from `stockai` to `navam`

[x] Revise the project description for `navam` as "Personal AI agents for investing, shopping, health, and learning"

