"""Standalone copy of the lesson 09 stdio server."""
import json
import sys


def handle(request):
    method, request_id = request.get("method"), request.get("id")
    if method == "initialize":
        result = {"protocolVersion": "2024-11-05", "serverInfo": {"name": "lesson-09", "version": "0.1.0"}, "capabilities": {"tools": {}}}
    elif method == "tools/list":
        result = {"tools": [{"name": "word_count", "description": "Count whitespace-separated words."}]}
    elif method == "tools/call":
        params = request.get("params", {})
        if params.get("name") != "word_count":
            return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32602, "message": "unknown tool"}}
        result = {"content": [{"type": "text", "text": str(len(params.get("arguments", {}).get("text", "").split()))}], "isError": False}
    else:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "method not found"}}
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle(json.loads(line))), flush=True)
