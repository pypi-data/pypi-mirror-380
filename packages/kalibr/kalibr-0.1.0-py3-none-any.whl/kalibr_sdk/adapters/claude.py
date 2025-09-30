"""Claude MCP adapter"""
import json
import os

class ClaudeAdapter:
    @staticmethod
    def generate_config(actions, base_url):
        """Generate MCP config for Claude Desktop"""
        
        # Generate the Node.js MCP server
        server_code = ClaudeAdapter._generate_server_code(actions, base_url)
        
        # Save server file
        os.makedirs("kalibr_generated/claude", exist_ok=True)
        with open("kalibr_generated/claude/mcp_server.js", "w") as f:
            f.write(server_code)
        
        # Generate config for Claude Desktop
        config = {
            "mcpServers": {
                "kalibr": {
                    "command": "node",
                    "args": ["kalibr_generated/claude/mcp_server.js"]
                }
            }
        }
        
        with open("kalibr_generated/claude/claude_config.json", "w") as f:
            json.dump(config, f, indent=2)
        
        return config
    
    @staticmethod
    def _generate_server_code(actions, base_url):
        """Generate Node.js MCP server code"""
        tools_json = json.dumps([{
            "name": action.name,
            "description": action.description,
            "parameters": action.params or {}
        } for action in actions])
        
        return f"""
// Auto-generated Claude MCP Server
const {{ Server }} = require('@modelcontextprotocol/sdk/server/index.js');
const {{ StdioServerTransport }} = require('@modelcontextprotocol/sdk/server/stdio.js');
const fetch = require('node-fetch');

const PROXY_URL = '{base_url}';

const server = new Server({{
  name: 'kalibr-mcp',
  version: '1.0.0',
}}, {{ capabilities: {{ tools: {{}} }} }});

// Register tools
const tools = {tools_json};

tools.forEach(tool => {{
  server.setRequestHandler(`tools/\${{tool.name}}`, async (request) => {{
    const response = await fetch(`\${{PROXY_URL}}/proxy/\${{tool.name}}`, {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify(request.params)
    }});
    return await response.json();
  }});
}});

// Start server
const transport = new StdioServerTransport();
server.connect(transport);
"""
