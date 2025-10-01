# Testing Guide

## Manual Testing

### 1. Test Server Startup

```bash
cd /path/to/gemini-cli-mcp-tool
uv run gemini-mcp
```

**Expected Output:**
```
╭────────────────────────────────────────────────────────────────────────────╮
│                              FastMCP  2.0                                  │
│             🖥️  Server name:     Gemini MCP Server                          │
│             📦 Transport:       STDIO                                      │
╰────────────────────────────────────────────────────────────────────────────╯
```

Server will wait for MCP connections. Press `Ctrl+C` to stop.

### 2. Configure in Claude Code

```bash
claude add mcp gemini-mcp \
  --command "uv" \
  --arg "run" \
  --arg "--directory" \
  --arg "$PWD" \
  --arg "gemini-mcp"
```

### 3. Test in Claude Code

Restart Claude Code, then try these prompts:

#### Test 1: Basic Query
```
Use the gemini_query tool to ask: "What is 2+2?"
```

**Expected**: Response from Gemini with "4"

#### Test 2: Context Query
```
Use gemini_context_query with this context:
"Python is a high-level programming language."
Question: "What programming paradigm does Python support?"
```

**Expected**: Response explaining Python's multi-paradigm nature

#### Test 3: Codebase Analysis
```
Use gemini_analyze_codebase to analyze some codebase content.
Provide the codebase_content parameter with file contents.
Question: "Summarize the project structure"
```

**Expected**: Analysis of the provided codebase content

## Automated Testing

### Run All Tests

```bash
uv run pytest
```

### Run with Coverage

```bash
uv run pytest --cov=gemini_mcp --cov-report=html
open htmlcov/index.html
```

### Run Specific Tests

```bash
# Unit tests only
uv run pytest tests/unit -v

# Integration tests only
uv run pytest tests/integration -v

# Specific test file
uv run pytest tests/unit/test_config.py -v
```

### Run with Benchmarks

```bash
uv run pytest --benchmark-only
```

## Integration Testing

### Test with MCP Inspector

```bash
# Install MCP Inspector
npm install -g @modelcontextprotocol/inspector

# Run inspector
mcp-inspector uv run --directory /path/to/gemini-cli-mcp-tool gemini-mcp
```

### Test Gemini CLI Directly

```bash
# Ensure Gemini CLI works
gemini "What is the capital of France?"
```

**Expected**: Response with "Paris"

## Troubleshooting Tests

### Server Won't Start

1. Check Python version: `python --version` (need 3.12+)
2. Check uv: `uv --version`
3. Check dependencies: `uv sync`
4. Check for syntax errors: `uv run ruff check`

### Gemini CLI Not Found

```bash
npm install -g @google/gemini-cli
which gemini
```

### Tests Failing

```bash
# Clean and rebuild
rm -rf .venv
uv sync

# Run with verbose output
uv run pytest -vv
```

## Performance Testing

### Benchmark Tool Execution

```bash
uv run pytest tests/unit --benchmark-only --benchmark-autosave
```

### Load Testing

Create `tests/load_test.py`:

```python
import asyncio
from gemini_mcp.services import GeminiClient
from gemini_mcp.config import get_settings

async def load_test():
    settings = get_settings()
    client = GeminiClient(settings)
    
    # Run 10 concurrent queries
    tasks = [
        client.query(prompt=f"Query {i}")
        for i in range(10)
    ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Completed {len(results)} queries")

asyncio.run(load_test())
```

## CI/CD Testing

### GitHub Actions (example)

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: astral-sh/setup-uv@v1
      - run: uv sync
      - run: uv run pytest
      - run: uv run ruff check
      - run: uv run pyright
```

## Test Coverage Goals

- **Unit Tests**: >80% coverage
- **Integration Tests**: Critical paths covered
- **E2E Tests**: Manual verification in Claude Code

## Known Issues

None at this time. If you encounter issues:

1. Check [TROUBLESHOOTING](README.md#troubleshooting) section
2. Open an issue: https://github.com/giovanimoutinho/gemini-cli-mcp-tool/issues
