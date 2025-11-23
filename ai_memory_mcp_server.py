#!/usr/bin/env python3
"""
AI Memory MCP Server
Allows Claude Desktop to read from AI Memory API
"""
import json
import sys
import requests

# Configuration
API_URL = "http://localhost:5003"
AI_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZlbG9wZXJfaWQiOiJsYXBpbm8td2ViIiwiYWlfbmFtZSI6ImNsYXVkZSIsImV4cCI6MTc2NDAxMzgzMCwiaWF0IjoxNzYzOTI3NDMwLCJ0eXBlIjoiYWlfbWVtb3J5X2FjY2VzcyJ9.rPRPCo7cefTyh2MM2B6lI4FIdnI49a4Y_gcjq2KTnng"

def read_memory(path: str) -> dict:
    """Read memory from API"""
    response = requests.post(
        f"{API_URL}/memory/read",
        headers={"Authorization": f"Bearer {AI_TOKEN}"},
        json={"path": path}
    )
    return response.json()

def handle_request(request: dict) -> dict:
    """Handle MCP request"""
    method = request.get("method")
    params = request.get("params", {})
    
    if method == "tools/list":
        return {
            "tools": [{
                "name": "read_council_memory",
                "description": "Read Council memory files",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path like council-members/claude.md"}
                    },
                    "required": ["path"]
                }
            }]
        }
    
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "read_council_memory":
            result = read_memory(args["path"])
            return {"content": [{"type": "text", "text": result.get("memory", str(result))}]}
    
    return {"error": "Unknown method"}

if __name__ == "__main__":
    for line in sys.stdin:
        try:
            request = json.loads(line)
            response = handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
