#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Lark Language Detection Package
"""

from setuptools import setup, find_packages
import os

# 读取README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="lark-language-detector",
    version="1.0.9",
    author="Farshore Team",
    author_email="your-email@example.com",
    description="A lightweight language detection library similar to fasttext and Google's implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/lark-language-detector",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    install_requires=[
        "torch>=1.9.0",
        "requests>=2.25.0",
        "numpy>=1.21.0",
        "zhconv>=1.4.0",
        "tiktoken>=0.5.0",
    ],
    include_package_data=True,
    package_data={
        "lark": [
            "farshore/save_lark/*.pth",
            "farshore/*.json",
        ],
    },
    entry_points={
        "console_scripts": [
            "lark=lark.cli:main",
        ],
    },
    keywords="language-detection, nlp, machine-learning, ai",
)
