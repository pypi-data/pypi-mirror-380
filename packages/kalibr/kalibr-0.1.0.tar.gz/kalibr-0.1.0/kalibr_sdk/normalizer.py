"""
Platform Normalization Layer
This handles the messy reality of how different AI platforms behave
"""
from typing import Dict, Any, Optional
import json

class PlatformNormalizer:
    """Handles behavioral differences between platforms"""
    
    PLATFORM_BEHAVIORS = {
        'gpt': {
            'invocation_tendency': 'aggressive',
            'retry_needed': True,
            'rate_limit': 30,
            'error_format': 'http_codes'
        },
        'claude': {
            'invocation_tendency': 'conservative',
            'retry_needed': False,
            'rate_limit': 100,
            'error_format': 'descriptive'
        },
        'gemini': {
            'invocation_tendency': 'moderate',
            'retry_needed': True,
            'rate_limit': 60,
            'error_format': 'google_style'
        },
        'assistants': {
            'invocation_tendency': 'moderate',
            'retry_needed': True,
            'rate_limit': 500,
            'error_format': 'openai_style'
        }
    }
    
    def normalize_for_platform(self, tool_config: Dict, platform: str) -> Dict:
        """Adjust tool configuration based on platform behavior"""
        normalized = tool_config.copy()
        behavior = self.PLATFORM_BEHAVIORS.get(platform, {})
        
        if platform == 'gpt' and behavior.get('invocation_tendency') == 'aggressive':
            # Add rate limiting for GPT's over-invocation
            normalized['x_rate_limit'] = 30
            normalized['x_dedupe_window'] = 5
            
        elif platform == 'claude' and behavior.get('invocation_tendency') == 'conservative':
            # Make Claude more likely to use tools
            for action in normalized.get('actions', []):
                if 'description' in action:
                    action['description'] = f"USE THIS TOOL: {action['description']}"
                    
        return normalized

class ErrorNormalizer:
    """Standardizes error handling across platforms"""
    
    ERROR_MAP = {
        'rate_limit': {
            'gpt': {'status': 429, 'code': 'rate_limit_exceeded'},
            'claude': {'status': 429, 'code': 'RATE_LIMITED'},
            'gemini': {'status': 429, 'code': 'RESOURCE_EXHAUSTED'},
            'universal': {'status': 429, 'code': 'RATE_LIMIT', 'message': 'Too many requests'}
        }
    }
    
    def normalize_error(self, error: Dict, from_platform: str) -> Dict:
        """Convert platform-specific errors to universal format"""
        for error_type, mappings in self.ERROR_MAP.items():
            platform_error = mappings.get(from_platform, {})
            if platform_error.get('code') in str(error):
                return mappings['universal']
        return {'status': 500, 'code': 'UNKNOWN', 'message': str(error)}
