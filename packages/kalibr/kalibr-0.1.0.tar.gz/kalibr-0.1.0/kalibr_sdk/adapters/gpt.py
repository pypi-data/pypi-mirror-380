"""GPT/ChatGPT adapter - generates OpenAPI configs"""
import json

class GPTAdapter:
    @staticmethod
    def generate_config(actions, base_url):
        """Generate OpenAPI spec that ChatGPT understands"""
        paths = {}
        
        for action in actions:
            path = f"/proxy/{action.name}"
            
            # Build the operation
            operation = {
                "operationId": action.name,
                "summary": action.description or f"Execute {action.name}",
                "responses": {
                    "200": {"description": "Success"}
                }
            }
            
            # Add request body if there are parameters
            if action.params:
                operation["requestBody"] = {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    name: {"type": ptype} 
                                    for name, ptype in action.params.items()
                                }
                            }
                        }
                    }
                }
            
            paths[path] = {"post": operation}
        
        return {
            "openapi": "3.1.0",
            "info": {
                "title": "Kalibr Actions",
                "version": "1.0.0",
                "description": "API actions via Kalibr SDK"
            },
            "servers": [{"url": base_url}],
            "paths": paths
        }
