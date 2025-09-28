#!/usr/bin/env python3
"""
Main CLI interface for CLAI
"""

import argparse
import sys
import os
from typing import Optional
from .groq_client import GroqClient
from .config import Config


def main():
    """Main entry point for the CLI application"""
    parser = argparse.ArgumentParser(
        description="Borabora - Convert natural language to Unix commands using Groq AI",
        prog="borabora"
    )
    
    parser.add_argument(
        "command", 
        nargs="*", 
        help="Natural language description of the command you want to run"
    )
    
    parser.add_argument(
        "--config", 
        action="store_true", 
        help="Configure API key and settings"
    )
    
    parser.add_argument(
        "--dry-run", "-d",
        action="store_true",
        help="Show command without executing (default behavior is to execute)"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="%(prog)s 0.1.1"
    )
    
    args = parser.parse_args()
    
    # Handle configuration
    if args.config:
        setup_config()
        return
    
    # Check if command is provided
    if not args.command:
        parser.print_help()
        return
    
    # Join command parts into a single string
    natural_command = " ".join(args.command)
    
    try:
        # Initialize configuration and client
        config = Config()
        if not config.api_key:
            print("❌ Groq API key not configured. Run 'borabora --config' to set it up.")
            sys.exit(1)
        
        client = GroqClient(config.api_key)
        
        # Convert natural language to Unix command
        print(f"🤔 Converting: '{natural_command}'")
        unix_command = client.convert_to_command(natural_command)
        
        if not unix_command:
            print("❌ Could not generate a command. Please try rephrasing your request.")
            sys.exit(1)
        
        print(f"💡 Suggested command: {unix_command}")
        
        # Execute by default, unless dry-run is specified
        if args.dry_run:
            print("🔍 Dry-run mode: Command not executed.")
        else:
            confirm = input("Execute this command? (y/N): ").lower().strip()
            if confirm in ['y', 'yes']:
                print(f"🚀 Executing: {unix_command}")
                os.system(unix_command)
            else:
                print("❌ Command execution cancelled.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def setup_config():
    """Interactive configuration setup"""
    print("🔧 Borabora Configuration Setup")
    print("=" * 30)
    
    api_key = input("Enter your Groq API key: ").strip()
    
    if not api_key:
        print("❌ API key is required.")
        return
    
    config = Config()
    config.set_api_key(api_key)
    
    print("✅ Configuration saved successfully!")
    print("You can now use borabora to convert natural language to commands.")


if __name__ == "__main__":
    main()
