# Installation Guide

## Prerequisites

### 1. Install Python 3.12+

```bash
# Check Python version
python --version  # Should be 3.12 or higher
```

### 2. Install uv (Fast Python Package Manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Install Gemini CLI

```bash
npm install -g @google/gemini-cli

# Configure Gemini (one-time setup)
gemini config
```

## Installation Methods

### Method 1: From Source (Recommended for Development)

```bash
# Clone the repository
git clone <repository-url>
cd gemini-cli-mcp-tool

# Install dependencies
uv sync

# Test installation
uv run gemini-mcp
```

### Method 2: System-Wide Installation

```bash
cd gemini-cli-mcp-tool
uv pip install .

# Test installation
gemini-mcp
```

## Configuration in AI Tools

### Claude Code CLI

#### Option A: Using `claude add mcp` (Easiest)

```bash
cd /path/to/gemini-cli-mcp-tool
claude add mcp gemini-mcp \
  --command "uv" \
  --arg "run" \
  --arg "--directory" \
  --arg "$PWD" \
  --arg "gemini-mcp"
```

#### Option B: Manual Configuration

Edit `~/.config/claude-code/mcp_settings.json`:

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/gemini-cli-mcp-tool",
        "gemini-mcp"
      ]
    }
  }
}
```

### Cursor

Edit `~/.cursor/mcp_settings.json`:

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/gemini-cli-mcp-tool",
        "gemini-mcp"
      ]
    }
  }
}
```

### Claude Desktop

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/gemini-cli-mcp-tool",
        "gemini-mcp"
      ]
    }
  }
}
```

## Verify Installation

### 1. Test Server Startup

```bash
cd /path/to/gemini-cli-mcp-tool
uv run gemini-mcp
```

**Expected**: ASCII art banner showing "FastMCP 2.0" and "Gemini MCP Server"

Press `Ctrl+C` to stop.

### 2. Test in Claude Code

Restart Claude Code, then try:

```
Use gemini_query tool to ask: "What is 2+2?"
```

**Expected**: Response from Gemini with the answer.

### 3. Test Tools Available

In Claude Code:

```
What tools do you have access to?
```

You should see:
- `gemini_query`
- `gemini_context_query`
- `gemini_analyze_codebase`
- `gemini_code_review`

## Environment Configuration (Optional)

Create `.env` file in project root:

```bash
cp .env.example .env
# Edit .env with your preferences
```

Available settings:
- `GEMINI_MCP_DEFAULT_MODEL` - Default model (default: gemini-2.5-pro)
- `GEMINI_MCP_DEFAULT_TIMEOUT` - Timeout in seconds (default: 120)
- `GEMINI_MCP_LOG_LEVEL` - Logging level (default: INFO)

## Troubleshooting

### "gemini command not found"

```bash
npm install -g @google/gemini-cli
which gemini  # Should show path
```

### "uv command not found"

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Restart terminal
```

### Server Not Starting

```bash
# Check dependencies
cd gemini-cli-mcp-tool
uv sync

# Check for errors
uv run gemini-mcp
```

### Tools Not Appearing in Claude Code

1. Verify configuration file path
2. Restart Claude Code completely
3. Check logs in Claude Code console

## Uninstallation

```bash
# Remove from Claude Code
claude remove mcp gemini-mcp

# Delete project directory
rm -rf /path/to/gemini-cli-mcp-tool
```

## Next Steps

See [QUICKSTART.md](QUICKSTART.md) for usage examples.
