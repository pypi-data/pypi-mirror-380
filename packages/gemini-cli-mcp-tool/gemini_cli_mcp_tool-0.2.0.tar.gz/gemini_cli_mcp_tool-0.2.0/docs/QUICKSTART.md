# Gemini MCP Quick Start Guide

## 5-Minute Setup

### Step 1: Prerequisites

```bash
# Install Gemini CLI
npm install -g @google/gemini-cli

# Configure Gemini (one-time setup)
gemini config
```

### Step 2: Install Gemini MCP

```bash
cd /path/to/your/projects
git clone <repository-url>
cd gemini-cli-mcp-tool
uv sync
```

### Step 3: Test the Server

```bash
# Run server directly
uv run gemini-mcp

# Server should start and wait for MCP connections
# Press Ctrl+C to stop
```

### Step 4: Add to Claude Code

```bash
# Option A: Using claude add mcp (easiest)
claude add mcp gemini-mcp \
  --command "uv" \
  --arg "run" \
  --arg "--directory" \
  --arg "$PWD" \
  --arg "gemini-mcp"

# Option B: Manual configuration
# Edit ~/.config/claude-code/mcp_settings.json:
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/gemini-cli-mcp-tool", "gemini-mcp"]
    }
  }
}
```

### Step 5: Try It Out

In Claude Code, ask:

```
Use the gemini_query tool to ask: "What is the capital of France?"
```

## Usage Tips

### Basic Query
```
Ask Gemini: "Explain async/await in Python"
```

### Large Context
```
Use gemini_context_query with this context: [paste large file]
Question: "Summarize the main functions"
```

### Codebase Analysis
```
Analyze this repo: https://github.com/user/repo
Question: "Find all TODO comments"
```

## Troubleshooting

### "gemini command not found"
```bash
npm install -g @google/gemini-cli
which gemini
```

### Server not connecting
1. Check absolute path in MCP config
2. Test: `uv run gemini-mcp`
3. Check Claude Code logs

### Need help?
Open an issue on the project repository
