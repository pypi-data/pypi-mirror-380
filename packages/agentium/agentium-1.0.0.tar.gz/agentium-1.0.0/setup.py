from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt if it exists
requirements = []
requirements_file = "requirements.txt"
if os.path.exists(requirements_file):
    with open(requirements_file, "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
else:
    # Fallback requirements if file doesn't exist
    requirements = [
        "numpy>=1.21.0",
        "pandas>=1.3.0", 
        "requests>=2.25.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.0.0",
        "python-dotenv>=0.19.0",
        "asyncio-throttle>=1.0.0",
        "aiohttp>=3.8.0",
        "openai>=1.0.0",
        "anthropic>=0.3.0"
    ]

setup(
    name="agentium",
    version="1.0.0",
    author="Sanjay N",
    author_email="2005sanjaynrs@gmail.com",
    description="A comprehensive toolkit for AI agent development and workflow orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RNSsanjay/Agentium-Python-Library",
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
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=0.991",
        ],
        "langchain": [
            "langchain>=0.1.0",
            "langchain-community>=0.0.10",
        ],
        "langgraph": [
            "langgraph>=0.0.20",
        ],
        "crewai": [
            "crewai>=0.1.0",
        ],
    },
    keywords="ai, agents, langchain, langgraph, crewai, nlp, automation, workflow",
)