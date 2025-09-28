#!/usr/bin/env python3
"""
Development setup script for CLAI
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return None


def main():
    """Main development setup"""
    print("🛠️  CLAI Development Setup")
    print("=" * 30)
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Install in development mode
    run_command(f"{sys.executable} -m pip install -e .", "Installing CLAI in development mode")
    
    # Install development dependencies
    dev_deps = ["build", "twine", "pytest", "black", "flake8"]
    for dep in dev_deps:
        run_command(f"{sys.executable} -m pip install {dep}", f"Installing {dep}")
    
    print("\n✅ Development setup complete!")
    print("\nYou can now:")
    print("1. Run 'clai --help' to test the CLI")
    print("2. Run 'clai --config' to set up your API key")
    print("3. Test with: clai list files in current directory")
    print("4. Run 'python publish.py' when ready to publish")


if __name__ == "__main__":
    main()
