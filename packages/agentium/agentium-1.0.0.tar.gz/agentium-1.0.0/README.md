# Agentium - AI Agent Development Toolkit

[![PyPI version](https://badge.fury.io/py/agentium.svg)](https://badge.fury.io/py/agentium)
[![Python Support](https://img.shields.io/pypi/pyversions/agentium.svg)](https://pypi.org/project/agentium/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python library designed for AI agent development and workflow orchestration. Agentium provides a rich set of tools and utilities that seamlessly integrate with popular AI frameworks like LangChain, LangGraph, and CrewAI.

## Features

- **🗜️ Condense**: Intelligent content condensation and compression
- **⚡ Optimizer**: Refine text, code, and workflows for better performance
- **📋 Rearranger**: Organize and restructure content logically
- **🔍 Extractor**: Extract structured information from various data sources
- **📢 Communicator**: Send messages and notifications across platforms
- **🌐 Translator**: Multi-language translation with tone adaptation
- **💡 Insight Generator**: Generate actionable insights from data
- **🔄 Workflow Helper**: Orchestrate complex tasks and triggers
- **📄 Template Manager**: Standardize outputs with customizable templates
- **🧠 Memory Helper**: Context storage and retrieval system
- **📝 Custom Summarizer**: Create summaries tailored to specific needs
- **📊 Logger Utils**: Track and debug operations with detailed logging

## Installation

```bash
pip install agentium
```

### Framework-specific installations:

```bash
# For LangChain integration
pip install agentium[langchain]

# For LangGraph integration
pip install agentium[langgraph]

# For CrewAI integration
pip install agentium[crewai]

# For development
pip install agentium[dev]
```

## Quick Start

```python
from agentium import Condenser, Optimizer, Communicator

# Initialize components
condenser = Condenser()
optimizer = Optimizer()
communicator = Communicator()

# Condense text
condensed = condenser.condense("Your long text here...")

# Optimize content
optimized = optimizer.optimize_text("Text to optimize")

# Send notification
communicator.send_notification("Process completed!", channel="email")
```

## Framework Integration

### LangChain Integration

```python
from agentium.integrations.langchain import AgentiumTool
from langchain.agents import initialize_agent

# Create Agentium tools for LangChain
tools = AgentiumTool.create_all_tools()
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
```

### LangGraph Integration

```python
from agentium.integrations.langgraph import AgentiumNode
from langgraph import Graph

# Add Agentium nodes to LangGraph
graph = Graph()
graph.add_node("condenser", AgentiumNode.condenser_node)
graph.add_node("optimizer", AgentiumNode.optimizer_node)
```

### CrewAI Integration

```python
from agentium.integrations.crewai import AgentiumCrewTool
from crewai import Agent, Task, Crew

# Create tools for CrewAI agents
tools = AgentiumCrewTool.get_all_tools()
agent = Agent(tools=tools, ...)
```

## Documentation

For detailed documentation and examples, visit [our documentation site](https://agentium.readthedocs.io).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/RNSsanjay/Agentium-Python-Library/issues) on GitHub.