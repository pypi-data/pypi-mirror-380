#!/usr/bin/env python3
"""
Setup script for Callosum Personality DSL Python package
"""

import os
import sys
from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README_PYTHON.md").read_text()

# Read version from package
version = "0.1.0"
try:
    exec(open('callosum_dsl/__init__.py').read())
    version = __version__
except:
    pass

# Determine the binary name based on platform
binary_name = "dsl-parser"
if sys.platform == "win32":
    binary_name = "dsl-parser.exe"

setup(
    name="callosum-dsl",
    version=version,
    description="Python wrapper for Callosum Personality DSL - Create rich, dynamic AI personalities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Callosum Team",
    author_email="contact@callosum.ai",
    url="https://github.com/your-org/callosum",
    packages=find_packages(),
    python_requires=">=3.8",
    
    # Include the DSL compiler binary
    package_data={
        "callosum_dsl": [
            "bin/dsl-parser",
            "bin/dsl-parser.exe",  # For Windows
        ]
    },
    
    # Include data files in manifest
    include_package_data=True,
    
    # No required dependencies - uses only stdlib!
    install_requires=[
        # Core package has no dependencies
    ],
    
    # Optional dependencies for AI integration
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.7.0"],
        "all": ["openai>=1.0.0", "anthropic>=0.7.0"],
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "twine>=4.0.0",
            "build>=0.10.0",
        ],
    },
    
    # Entry points for command line usage
    entry_points={
        "console_scripts": [
            "callosum-compile=callosum_dsl.core:_cli_main",
        ],
    },
    
    # Classifiers for PyPI
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    
    # Keywords for discoverability
    keywords=[
        "ai", "personality", "dsl", "language-model", "chatbot", 
        "artificial-intelligence", "openai", "anthropic", "llm"
    ],
    
    # Project URLs
    project_urls={
        "Bug Reports": "https://github.com/your-org/callosum/issues",
        "Documentation": "https://github.com/your-org/callosum/blob/main/README_PYTHON.md",
        "Source": "https://github.com/your-org/callosum",
    },
)
