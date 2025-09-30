"""Main Kalibr SDK"""
import json
import os
from typing import Optional, Dict
from .schemas.action import Action
from .adapters.gpt import GPTAdapter

class Kalibr:
    def __init__(self, api_url: str, api_key: Optional[str] = None):
        """Initialize Kalibr with your API"""
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.actions = []
    
    def add_action(self, name: str, endpoint: str, method: str = "GET", 
                   params: Optional[Dict] = None, description: str = ""):
        """Add an action that AI platforms can call"""
        action = Action(name, endpoint, method, params, description)
        self.actions.append(action)
        return self
    
    def generate_configs(self, proxy_url: str = "http://localhost:8000"):
        """Generate configs for all platforms"""
        # Create output directory
        os.makedirs("kalibr_generated", exist_ok=True)
        
        # Generate GPT config
        gpt_config = GPTAdapter.generate_config(self.actions, proxy_url)
        
        # Save to file
        with open("kalibr_generated/gpt_config.json", "w") as f:
            json.dump(gpt_config, f, indent=2)
        
        print("✅ Generated configs:")
        print(f"   GPT: kalibr_generated/gpt_config.json")
        print(f"\n📋 Next steps:")
        print(f"   1. Start proxy: python3 universal_proxy.py")
        print(f"   2. Start ngrok: ngrok http 8000")
        print(f"   3. Copy config to ChatGPT Actions")
        
        return gpt_config

    def generate_claude_config(self, proxy_url: str = "http://localhost:8000"):
        """Generate Claude MCP configuration"""
        from .adapters.claude import ClaudeAdapter
        
        claude_config = ClaudeAdapter.generate_config(self.actions, proxy_url)
        print("✅ Generated Claude MCP server:")
        print("   1. Install: cd kalibr_generated/claude && npm install @modelcontextprotocol/sdk")
        print("   2. Add to Claude Desktop settings")
        return claude_config
