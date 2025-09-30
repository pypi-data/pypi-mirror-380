"""Enhanced Kalibr SDK that registers with proxy"""
import json
import os
import requests
from typing import Optional, Dict
from .schemas.action import Action
from .adapters.gpt import GPTAdapter

class Kalibr:
    def __init__(self, api_url: str, api_key: Optional[str] = None):
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.actions = []
        self.proxy_url = "http://localhost:8000"
    
    def add_action(self, name: str, endpoint: str, method: str = "GET", 
                   params: Optional[Dict] = None, description: str = ""):
        """Add an action"""
        action = Action(name, endpoint, method, params, description)
        self.actions.append(action)
        
        # Register with proxy if it's running
        try:
            requests.post(f"{self.proxy_url}/register/{name}", 
                         json={"endpoint": endpoint, "method": method, "base_url": self.api_url})
            print(f"  Registered {name} with proxy")
        except:
            pass  # Proxy not running yet
        
        return self
    
    def generate_configs(self, proxy_url: str = "http://localhost:8000"):
        """Generate configs AND save action mappings"""
        os.makedirs("kalibr_generated", exist_ok=True)
        
        # Generate GPT config
        gpt_config = GPTAdapter.generate_config(self.actions, proxy_url)
        with open("kalibr_generated/gpt_config.json", "w") as f:
            json.dump(gpt_config, f, indent=2)
        
        # Save action mappings for the proxy
        mappings = {}
        for action in self.actions:
            mappings[action.name] = {
                "url": f"{self.api_url}{action.endpoint}",
                "method": action.method
            }
        
        with open("kalibr_generated/action_mappings.json", "w") as f:
            json.dump(mappings, f, indent=2)
        
        print("✅ Generated configs and action mappings")
        return gpt_config
