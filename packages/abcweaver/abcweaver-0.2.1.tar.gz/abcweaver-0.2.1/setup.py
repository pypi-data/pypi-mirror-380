#!/usr/bin/env python3
"""
📡 Caelus Package Setup
ABC ↔ MusicXML Transformation Engine with Redis Stream Processing
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="abcweaver",
    version="0.2.1",
    author="Gerico1007",
    author_email="gerico@jgwill.com",
    description="🎼 ABC ↔ MusicXML Transformation Engine with Redis Stream Processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gerico1007/abcweaver",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "lxml>=4.9.0", 
        "nyro>=0.1.3",
        "pydantic>=2.0.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "abcweaver=abcweaver.cli:abcweaver",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)