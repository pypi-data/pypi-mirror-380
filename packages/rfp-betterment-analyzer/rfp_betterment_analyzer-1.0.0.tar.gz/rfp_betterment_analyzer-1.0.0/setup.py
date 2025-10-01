#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rfp-betterment-analyzer",
    version="1.0.0",
    author="RFP Analysis Team",
    author_email="info@rfpanalysis.example.com",
    description="A tool to evaluate proposal content and identify betterments for U.S. Government RFP responses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rfpanalysis/rfp-betterment-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: Markup",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
    ],
    python_requires=">=3.8",
    install_requires=[
        "nltk>=3.6.0",
        "scikit-learn>=0.24.0",
        "pandas>=1.2.0",
        "tqdm>=4.62.0",
    ],
    entry_points={
        "console_scripts": [
            "rfp-analyzer=main:main",
        ],
    },
    include_package_data=True,
)
