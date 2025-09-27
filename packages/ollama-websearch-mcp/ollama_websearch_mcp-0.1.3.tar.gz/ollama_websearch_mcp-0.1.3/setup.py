from setuptools import setup
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from pyproject.toml
def get_version():
    with open(os.path.join(this_directory, "pyproject.toml"), encoding="utf-8") as f:
        for line in f:
            if line.startswith("version ="):
                return line.split("=")[1].strip().strip('"')

setup(
    name="ollama-websearch-mcp",
    version=get_version(),
    author="huangxinping",
    author_email="monor.huang@gmail.com",
    description="MCP Service for Ollama Web Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huangxinping/ollama-websearch-mcp",
    py_modules=["mcp_service"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=[
        "python-dotenv>=0.19.0",
        "ollama>=0.6.0",
        "mcp>=1.15.0",
    ],
    entry_points={
        "console_scripts": [
            "ollama-websearch-mcp=mcp_service:cli",
        ],
    },
    include_package_data=True,
)