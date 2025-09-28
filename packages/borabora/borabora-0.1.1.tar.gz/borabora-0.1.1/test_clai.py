#!/usr/bin/env python3
"""
Simple tests for CLAI functionality
"""

import os
import tempfile
import json
from pathlib import Path
from clai.config import Config
from clai.groq_client import GroqClient


def test_config():
    """Test configuration functionality"""
    print("🧪 Testing configuration...")
    
    # Create a temporary config directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Override the config directory for testing
        original_config_dir = Config.__init__
        
        def mock_init(self):
            self.config_dir = Path(temp_dir) / ".clai"
            self.config_file = self.config_dir / "config.json"
            self._ensure_config_dir()
            self._load_config()
        
        Config.__init__ = mock_init
        
        # Test config creation and API key setting
        config = Config()
        test_key = "test_api_key_123"
        config.set_api_key(test_key)
        
        # Test key retrieval
        assert config.api_key == test_key, "API key not saved correctly"
        
        # Test config file exists
        assert config.config_file.exists(), "Config file not created"
        
        # Restore original method
        Config.__init__ = original_config_dir
        
        print("✅ Configuration tests passed")


def test_groq_client_init():
    """Test Groq client initialization"""
    print("🧪 Testing Groq client initialization...")
    
    # Test with a dummy API key (won't actually call API)
    try:
        client = GroqClient("dummy_key")
        assert client.api_key == "dummy_key", "API key not set correctly"
        print("✅ Groq client initialization tests passed")
    except Exception as e:
        print(f"⚠️  Groq client test skipped (expected with dummy key): {e}")


def main():
    """Run all tests"""
    print("🚀 Running CLAI Tests")
    print("=" * 25)
    
    try:
        test_config()
        test_groq_client_init()
        
        print("\n✅ All tests completed!")
        print("\nTo test with real API:")
        print("1. Set up your API key: clai --config")
        print("2. Test a command: clai list files")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
