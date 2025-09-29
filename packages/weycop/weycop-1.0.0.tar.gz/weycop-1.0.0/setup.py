"""
Setup script for WeyCP Python client
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="weycop",
    version="1.0.0",
    author="WeyCP Team",
    author_email="dev@weycop.com",
    description="Python client for WeyCP API - OpenAI-compatible chat completions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weycop/weycop-python",
    project_urls={
        "Bug Tracker": "https://github.com/weycop/weycop-python/issues",
        "Documentation": "https://docs.weycop.com",
        "Homepage": "https://weycop.com",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-httpx>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    keywords="weycop, ai, chat, completions, openai, llama, ollama, api",
    include_package_data=True,
    zip_safe=False,
)