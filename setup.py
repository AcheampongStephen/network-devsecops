
"""
The setup.py file is an essential part of Python projects. It is used for packaging and distributing Python projects.
It contains metadata about the project and instructions on how to install it. 
The file is written in Python and uses the setuptools library to handle the packaging process.
"""

from setuptools import setup, find_packages
import os
import sys
from typing import List


def get_requirements() -> List[str]:
    """
    Reads the requirements from the requirements.txt file and returns them as a list of strings.
    """
    requirement_list = []
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists.")

    return requirement_list


setup(
    name="NetworkPhisingDetection",
    version="0.0.1",
    author="Stephen Acheampong",
    author_email="acheampongstephen392024@gmail.com",
    description="A Python package for detecting phishing URLs using machine learning.",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)