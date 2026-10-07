"""Offline production-shaped MCP entry point for lesson 18."""
import json
import sys


def response(request):
    request_id = request.get("id")
    if request.get("method") == "tools/list":
        result = {"tools": [{"name": "health", "description": "Return agent health."}]}
    elif request.get("method") == "tools/call" and request.get("params", {}).get("name") == "health":
        result = {"content": [{"type": "text", "text": "ok"}], "isError": False}
    else:
        result = {"content": [{"type": "text", "text": "unsupported request"}], "isError": True}
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(response(json.loads(line))), flush=True)
