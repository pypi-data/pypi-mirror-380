from setuptools import setup, find_packages
import os

# Read version from __init__.py
def get_version():
    with open(os.path.join("wathq_mcp_server", "__init__.py"), "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "0.1.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wathq-mcp-server",
    version=get_version(),
    author="WATHQ MCP Server",
    author_email="",
    description="MCP server for Saudi company lookup via WATHQ API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=["mcp", "aiohttp"],
    entry_points={
        "console_scripts": [
            "wathq-mcp-server=wathq_mcp_server.server:main",
        ],
    },
    keywords="mcp, wathq, saudi, company, lookup, api, commercial-registration",
)
