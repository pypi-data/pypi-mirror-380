"""Setup configuration for entangle-matrix package."""

from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Python SDK for Entangle Matrix API - Create and manage AI-powered digital twins"

# Define requirements directly to avoid build issues
requirements = [
    "aiohttp>=3.8.0",
    "aiofiles>=23.2.1",
]

setup(
    name="entangle-matrix",
    version="0.2.0",
    author="QBit Codes",
    author_email="hello@qbitcodes.com",
    description="Python SDK for Entangle Matrix API - Create and manage AI-powered digital twins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qbit-codes/entangle-python-client",
    project_urls={
        "Bug Tracker": "https://github.com/qbit-codes/entangle-python-client/issues",
        "Documentation": "https://github.com/qbit-codes/entangle-python-client#readme",
        "Source Code": "https://github.com/qbit-codes/entangle-python-client",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ]
    },
    keywords="matrix, api, sdk, chat, messaging, digital-twin, ai",
    include_package_data=True,
    zip_safe=False,
)