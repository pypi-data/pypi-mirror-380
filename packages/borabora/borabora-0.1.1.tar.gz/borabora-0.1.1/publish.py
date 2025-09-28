#!/usr/bin/env python3
"""
Publishing script for CLAI to PyPI
"""

import os
import sys
import subprocess
import shutil
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
        sys.exit(1)


def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    required_packages = ['build', 'twine']
    missing_packages = []
    
    for package in required_packages:
        try:
            subprocess.run([sys.executable, '-c', f'import {package}'], 
                         check=True, capture_output=True)
        except subprocess.CalledProcessError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        for package in missing_packages:
            run_command(f"{sys.executable} -m pip install {package}", 
                       f"Installing {package}")
    else:
        print("✅ All requirements satisfied")


def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous build artifacts...")
    
    dirs_to_clean = ['build', 'dist', 'clai.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    print("✅ Build artifacts cleaned")


def build_package():
    """Build the package"""
    run_command(f"{sys.executable} -m build", "Building package")


def check_package():
    """Check the built package"""
    run_command("twine check dist/*", "Checking package")


def upload_to_test_pypi():
    """Upload to Test PyPI"""
    print("\n📦 Uploading to Test PyPI...")
    print("You'll need to enter your Test PyPI credentials.")
    run_command("twine upload --repository testpypi dist/*", "Uploading to Test PyPI")


def upload_to_pypi():
    """Upload to PyPI"""
    print("\n📦 Uploading to PyPI...")
    print("You'll need to enter your PyPI credentials.")
    run_command("twine upload dist/*", "Uploading to PyPI")


def main():
    """Main publishing workflow"""
    print("🚀 CLAI Publishing Script")
    print("=" * 30)
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Check requirements
    check_requirements()
    
    # Clean previous builds
    clean_build()
    
    # Build package
    build_package()
    
    # Check package
    check_package()
    
    print("\n✅ Package built and checked successfully!")
    print("\nNext steps:")
    print("1. Test your package on Test PyPI first (recommended)")
    print("2. Then publish to PyPI")
    
    choice = input("\nWhat would you like to do?\n1) Upload to Test PyPI\n2) Upload to PyPI\n3) Exit\nChoice (1-3): ").strip()
    
    if choice == "1":
        upload_to_test_pypi()
        print("\n✅ Package uploaded to Test PyPI!")
        print("Test installation with: pip install --index-url https://test.pypi.org/simple/ clai")
    elif choice == "2":
        confirm = input("Are you sure you want to publish to PyPI? This cannot be undone. (y/N): ").lower().strip()
        if confirm in ['y', 'yes']:
            upload_to_pypi()
            print("\n🎉 Package published to PyPI!")
            print("Install with: pip install clai")
        else:
            print("❌ Publishing cancelled")
    else:
        print("👋 Exiting without publishing")


if __name__ == "__main__":
    main()
