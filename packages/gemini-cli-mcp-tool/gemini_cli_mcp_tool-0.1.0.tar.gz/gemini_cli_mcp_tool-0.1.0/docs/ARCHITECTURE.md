# Architecture Documentation

## System Design

### Core Principles

1. **SOLID Principles**
   - Single Responsibility: Each component has one clear purpose
   - Open/Closed: Extensible via middleware and tool patterns
   - Liskov Substitution: Middleware can be swapped
   - Interface Segregation: Minimal interfaces
   - Dependency Inversion: Dependencies injected, not instantiated

2. **DRY (Don't Repeat Yourself)**
   - Centralized configuration management
   - Reusable error handling patterns
   - Shared subprocess execution logic

3. **Async-First**
   - Non-blocking I/O operations
   - Concurrent execution support
   - Timeout management

## Component Architecture

```
┌─────────────────────────────────────────┐
│         FastMCP Server                  │
├─────────────────────────────────────────┤
│  Middleware Layer                       │
│  ├── LoggingMiddleware                  │
│  └── GeminiErrorMiddleware              │
├─────────────────────────────────────────┤
│  Tools Layer                            │
│  ├── gemini_query                       │
│  ├── gemini_context_query               │
│  └── gemini_analyze_codebase            │
├─────────────────────────────────────────┤
│  Service Layer                          │
│  └── GeminiClient                       │
│      └── Async subprocess execution     │
├─────────────────────────────────────────┤
│  Configuration Layer                    │
│  └── Pydantic Settings                  │
└─────────────────────────────────────────┘
```

## Data Flow

### Request Flow
```
MCP Client → FastMCP → Middleware → Tool → Service → Gemini CLI
```

### Response Flow
```
Gemini CLI → GeminiResponse → Tool Result → Middleware → FastMCP → MCP Client
```

## Error Handling Strategy

### Layers
1. **Service Layer**: Catch subprocess errors, transform to GeminiError
2. **Tool Layer**: Catch GeminiError, transform to ToolError
3. **Middleware Layer**: Log all errors, track statistics
4. **FastMCP Layer**: Transform to MCP error responses

### Error Types
- `GeminiError`: Gemini CLI failures
- `ToolError`: MCP tool errors (sent to client)
- `TimeoutError`: Operation timeouts

## Security Considerations

1. **Input Validation**: Pydantic Field validators
2. **Subprocess Safety**: Proper shell escaping
3. **Error Masking**: Production mode hides internal details
4. **Timeout Protection**: All operations have timeouts
5. **Sandbox Support**: Optional sandboxed execution

## Performance Optimizations

1. **Async Subprocess**: Non-blocking CLI execution
2. **Settings Cache**: LRU cached configuration
3. **Structured Logging**: Efficient JSON logging
4. **Timeout Management**: Configurable per operation

## Testing Strategy

### Test Pyramid
```
     /\
    /  \    E2E (Manual)
   /────\   Integration Tests
  /──────\  Unit Tests (Automated)
 /────────\
```

### Coverage Goals
- Unit Tests: >80% coverage
- Integration Tests: Critical paths
- E2E Tests: Full workflow validation

## Monitoring & Observability

### Structured Logging
- Request/response logging
- Error tracking with counts
- Performance metrics

### Key Metrics
- Request duration
- Error rates by type
- Tool usage statistics

## Deployment

### Requirements
- Python 3.12+
- Gemini CLI configured
- uv (recommended) or pip

### Configuration
- Environment variables
- .env file support
- Runtime overrides

## Extension Points

### Adding New Tools
```python
@mcp.tool
async def my_new_tool(param: str, ctx: Context) -> dict:
    settings = get_settings()
    client = GeminiClient(settings)
    return await client.query(prompt=param)
```

### Adding Middleware
```python
class MyMiddleware(Middleware):
    async def on_message(self, context, call_next):
        # Pre-processing
        response = await call_next(context)
        # Post-processing
        return response

mcp.add_middleware(MyMiddleware())
```

## Future Enhancements

1. **Streaming Support**: Real-time response streaming
2. **Caching Layer**: Response caching for repeated queries
3. **Rate Limiting**: Client-level rate limiting
4. **Metrics Dashboard**: Prometheus/Grafana integration
5. **Multi-Model Support**: Support other CLI tools

## Technical Debt

None identified at this time. Architecture follows best practices and is production-ready.
