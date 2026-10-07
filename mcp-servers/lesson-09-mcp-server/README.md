# Lesson 09 MCP server

A tiny, dependency-light MCP-shaped stdio server for learning protocol boundaries. It exposes `word_count` and never needs a network connection.

```bash
python server.py
```

The first line must be a JSON-RPC request. For example:

```json
{"jsonrpc":"2.0","id":1,"method":"tools/list"}
```

For production integrations, use the official MCP SDK and pin its version. This artifact is deliberately transparent, not a replacement SDK.
