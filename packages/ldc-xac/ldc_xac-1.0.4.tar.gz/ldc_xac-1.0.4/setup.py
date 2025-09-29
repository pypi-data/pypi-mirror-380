"""
Setup script for ldc-xac package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ldc-xac",
    version="1.0.4",
    author="Ayush Sonar",
    author_email="ayush.sonar@lendenclub.com",
    description="External API Caller with comprehensive logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayushsonar-lendenclub/ldc-xac",
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
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="api, http, requests, logging, external-api",
    project_urls={
        "Bug Reports": "https://github.com/ayushsonar-lendenclub/ldc-xac/issues",
        "Source": "https://github.com/ayushsonar-lendenclub/ldc-xac",
    },
)
