#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mumu-emulator-api",
    version="1.0.1",
    author="wlkjyy",
    author_email="wlkjyy@vip.qq.com",
    description="Python API for MuMu Android Emulator",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/wlkjyy/mumu-python-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Emulators",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "gui": ["opencv-python"],
        "scrcpy": ["scrcpy-client"],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="mumu emulator android automation api",
    project_urls={
        "Bug Reports": "https://github.com/wlkjyy/mumu-python-api/issues",
        "Source": "https://github.com/wlkjyy/mumu-python-api",
    },
)

