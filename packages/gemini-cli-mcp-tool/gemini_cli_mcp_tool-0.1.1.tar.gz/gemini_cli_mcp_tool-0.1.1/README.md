# Gemini CLI MCP Server

> 🚀 Token-efficient AI operations using Gemini's massive 1M token context window

A production-grade [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that wraps the [Gemini CLI](https://github.com/google-gemini/gemini-cli), enabling AI tools like Claude Code, Cursor, and Claude Desktop to leverage Gemini's large context window and free tier for cost-effective operations.

## ✨ Features

- **🎯 Large Context Window**: Leverage Gemini's 1M token context for analyzing entire codebases
- **💰 Token Efficient**: Use Gemini's free tier (1,000 requests/day) to save on API costs
- **🔧 Four Powerful Tools**:
  - `gemini_query`: Direct queries to Gemini models
  - `gemini_context_query`: Queries with large context support
  - `gemini_analyze_codebase`: Full repository/codebase analysis
  - `gemini_code_review`: Adversarial code review with critic capabilities
- **🏗️ Senior Staff Engineering**: Built following SOLID principles and best practices
- **⚡ Async-First**: Non-blocking async subprocess execution
- **📊 Observability**: Structured logging with comprehensive error handling
- **🧪 Production-Ready**: Type-safe, fully tested, and battle-hardened

## 🚀 Quick Start

### Prerequisites

Install the Gemini CLI and authenticate:

```bash
npm install -g @google/gemini-cli
gemini config  # Follow authentication prompts
```

### Installation

**One-line setup for Claude Code:**

```bash
claude mcp add gemini-mcp -- uvx --from gemini-cli-mcp-tool gemini-mcp
```

That's it! Restart Claude Code and you're ready to use all four Gemini tools.

### Alternative Setup Methods

<details>
<summary>Manual configuration for Claude Code</summary>

Add to `~/.config/claude-code/mcp_settings.json`:

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uvx",
      "args": ["--from", "gemini-cli-mcp-tool", "gemini-mcp"]
    }
  }
}
```
</details>

<details>
<summary>Cursor setup</summary>

Add to `~/.cursor/mcp_settings.json`:

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uvx",
      "args": ["--from", "gemini-cli-mcp-tool", "gemini-mcp"]
    }
  }
}
```
</details>

<details>
<summary>Claude Desktop setup</summary>

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "uvx",
      "args": ["--from", "gemini-cli-mcp-tool", "gemini-mcp"]
    }
  }
}
```
</details>

## 📚 Documentation

- **[Quick Start Guide](docs/QUICKSTART.md)** - Get started in 5 minutes
- **[Installation Guide](docs/INSTALL.md)** - Complete setup instructions
- **[Architecture](docs/ARCHITECTURE.md)** - Technical design details
- **[Testing Guide](docs/TESTING.md)** - Development workflow

## 🛠️ Tools Reference

### `gemini_query`

Direct queries to Gemini models for general-purpose AI assistance.

**Parameters:**
- `prompt` (string, required): The question or instruction
- `model` (string, optional): Model to use (default: gemini-2.5-pro)
- `timeout` (float, optional): Timeout in seconds (default: 120, max: 600)
- `sandbox` (bool, optional): Enable sandbox mode for code execution

**Returns:** `{response: string, model: string, success: bool}`

**Example:**
```
Use gemini_query to explain: "How does async/await work in Python?"
```

### `gemini_context_query`

Optimized for large context queries (up to 1M tokens) - perfect for analyzing entire documents or codebases.

**Parameters:**
- `prompt` (string, required): The main question
- `context` (string, required): Large context content
- `model` (string, optional): Model to use
- `timeout` (float, optional): Timeout in seconds (default: 240)

**Returns:** `{response: string, model: string, success: bool, context_size: int}`

**Example:**
```
Use gemini_context_query with context from [large document] to answer: "What are the main themes?"
```

### `gemini_analyze_codebase`

Comprehensive repository/codebase analysis using Gemini's large context window.

**Parameters:**
- `prompt` (string, required): Analysis question
- `codebase_content` (string, required): The codebase content to analyze
- `model` (string, optional): Model to use

**Returns:** `{analysis: string, model: string, success: bool}`

**Example:**
```
Use gemini_analyze_codebase to review security of [codebase content]
```

### `gemini_code_review`

Adversarial code review tool with critic capabilities. Identifies logic errors, security issues, performance problems, and more.

**Parameters:**
- `code` (string, required): The code to review
- `context` (string, optional): Additional context about the code
- `review_focus` (string, optional): Specific areas to focus on (e.g., "security", "performance")
- `model` (string, optional): Model to use

**Returns:** `{review: string, model: string, success: bool}`

**Example:**
```
Use gemini_code_review to review [code] focusing on "security and logic errors"
```

## ⚙️ Configuration

Optional `.env` file configuration:

```bash
# Gemini CLI Configuration
GEMINI_MCP_GEMINI_CLI_PATH=gemini
GEMINI_MCP_DEFAULT_MODEL=gemini-2.5-pro

# Execution Settings
GEMINI_MCP_DEFAULT_TIMEOUT=120.0
GEMINI_MCP_MAX_CONTEXT_TOKENS=1000000

# Server Settings
GEMINI_MCP_SERVER_NAME="Gemini MCP Server"
GEMINI_MCP_MASK_ERROR_DETAILS=true
GEMINI_MCP_LOG_LEVEL=INFO

# Feature Flags
GEMINI_MCP_ENABLE_SANDBOX=false
GEMINI_MCP_ENABLE_YOLO_MODE=false
```

See [`.env.example`](.env.example) for full configuration options.


## 💻 Development

### Setup Development Environment

```bash
git clone https://github.com/mgiovani/gemini-cli-mcp-tool.git
cd gemini-cli-mcp-tool
uv sync
```

### Testing

```bash
# Run all tests
uv run pytest

# With coverage
uv run pytest --cov=gemini_mcp --cov-report=html

# Integration tests only
uv run pytest tests/integration/ -v
```

### Code Quality

```bash
# Lint and format
uv run ruff check
uv run ruff format

# Type checking
uv run pyright
```

## 🔧 Troubleshooting

### "gemini command not found"

```bash
npm install -g @google/gemini-cli
which gemini  # Should show path
```

### MCP Server Not Connecting

1. Check the absolute path in your MCP configuration
2. Ensure `uv` is in your PATH: `which uv`
3. Test the server manually: `uv run gemini-mcp`
4. Check logs in your AI tool's console

### Gemini CLI Authentication Issues

```bash
# Re-authenticate
gemini config

# Or check settings
cat ~/.gemini/settings.json
```

### Timeout Errors

Increase timeout via environment variable:
```bash
export GEMINI_MCP_DEFAULT_TIMEOUT=300
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 and use `ruff` for linting
- Add type hints to all functions
- Write tests for new features
- Update documentation as needed

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 🙏 Acknowledgments

- [FastMCP](https://gofastmcp.com) - Pythonic MCP framework
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Official Gemini CLI
- [Model Context Protocol](https://modelcontextprotocol.io) - MCP specification

## 💬 Support

- 🐛 [Report Bug](https://github.com/mgiovani/gemini-cli-mcp-tool/issues)
- 💡 [Request Feature](https://github.com/mgiovani/gemini-cli-mcp-tool/issues)
- 📧 [Contact](mailto:e@giovani.dev)
