"""Core action definition"""
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Action:
    """A single action/tool that AI platforms can call"""
    name: str
    endpoint: str
    method: str = "GET"
    params: Optional[Dict[str, str]] = None
    description: str = ""
    
    def to_dict(self):
        return {
            "name": self.name,
            "endpoint": self.endpoint,
            "method": self.method,
            "params": self.params or {},
            "description": self.description
        }
