#!/usr/bin/env python3
"""
Setup script for CLAI - Command Line AI Assistant
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "CLAI - Command Line AI Assistant that converts natural language to Unix commands"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="borabora",
    version="0.1.1",
    author="AndreyZ",
    author_email="andrey@invisible-hand.dev",
    description="Command Line AI Assistant that converts natural language to Unix commands using Groq AI",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/invisible-hand/borabora",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "borabora=clai.main:main",
        ],
    },
    keywords="cli ai assistant unix commands groq natural language",
    project_urls={
        "Bug Reports": "https://github.com/invisible-hand/borabora/issues",
        "Source": "https://github.com/invisible-hand/borabora",
    },
)
