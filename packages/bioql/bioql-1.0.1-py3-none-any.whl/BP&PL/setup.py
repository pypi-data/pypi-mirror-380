#!/usr/bin/env python3
"""
Setup script for BioQL Billing & Pricing System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bioql-billing",
    version="1.0.0",
    author="BioQL Team",
    author_email="team@bioql.com",
    description="Production-ready billing and monetization system for BioQL quantum computing platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bioql/billing",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-flask>=1.3.0",
            "pytest-cov>=4.1.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
        ],
        "production": [
            "gunicorn>=21.2.0",
            "celery>=5.3.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "bioql-billing-api=api.main:main",
            "bioql-billing-dashboard=dashboard.app:main",
            "bioql-billing-cli=utils.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.sql"],
        "dashboard": ["templates/*", "static/css/*", "static/js/*"],
    },
    zip_safe=False,
    keywords="bioql quantum computing billing payment monetization",
    project_urls={
        "Documentation": "https://docs.bioql.com/billing",
        "Source": "https://github.com/bioql/billing",
        "Tracker": "https://github.com/bioql/billing/issues",
    },
)