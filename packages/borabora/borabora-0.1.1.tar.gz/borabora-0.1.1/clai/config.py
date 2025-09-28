"""
Configuration management for CLAI
"""

import os
import json
from pathlib import Path
from typing import Optional


class Config:
    """Manages configuration for CLAI"""
    
    def __init__(self):
        """Initialize configuration manager"""
        self.config_dir = Path.home() / ".clai"
        self.config_file = self.config_dir / "config.json"
        self._ensure_config_dir()
        self._load_config()
    
    def _ensure_config_dir(self):
        """Ensure configuration directory exists"""
        self.config_dir.mkdir(exist_ok=True)
    
    def _load_config(self):
        """Load configuration from file"""
        self._config = {}
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self._config = json.load(f)
            except (json.JSONDecodeError, IOError):
                # If config is corrupted, start fresh
                self._config = {}
    
    def _save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self._config, f, indent=2)
        except IOError as e:
            raise Exception(f"Failed to save configuration: {e}")
    
    @property
    def api_key(self) -> Optional[str]:
        """Get the Groq API key"""
        # First check environment variable
        env_key = os.getenv('GROQ_API_KEY')
        if env_key:
            return env_key
        
        # Then check config file
        return self._config.get('api_key')
    
    def set_api_key(self, api_key: str):
        """Set the Groq API key"""
        self._config['api_key'] = api_key
        self._save_config()
    
    def get_setting(self, key: str, default=None):
        """Get a configuration setting"""
        return self._config.get(key, default)
    
    def set_setting(self, key: str, value):
        """Set a configuration setting"""
        self._config[key] = value
        self._save_config()
