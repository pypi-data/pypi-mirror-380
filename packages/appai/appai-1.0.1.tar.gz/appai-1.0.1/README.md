# AppAI - Swarm Intelligence System

**Documentation-driven code generation powered by decentralized agent swarms.**

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-2.0.2-green.svg)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## What is AppAI?

AppAI is a **swarm intelligence system** that generates production-ready code using **decentralized autonomous agents**. Agents compete for tasks through async bidding, collaborate on complex projects, and learn from framework documentation patterns.

### Key Innovation: Cross-App Intelligence

AppAI agents understand **relationships between models in different Django apps** - automatically creating ForeignKey relationships with proper imports:

```python
# agents/models.py
class Author(models.Model):
    name = models.CharField(max_length=200)

# blog/models.py - DIFFERENT APP!
from authors.models import Author  # ✅ Auto-generated import

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=CASCADE, related_name='posts')
```

## Quick Start

```bash
# Install
pip install appai

# Run example
python examples/example_blog_with_relations.py
```

## Features

### 🤖 Decentralized Swarm Architecture
- **Async Task Bidding** - Agents compete for tasks based on expertise
- **No Central Coordinator** - Self-organizing agent network
- **Real-time Communication** - Agents share knowledge and progress

### 📚 Documentation-Driven Development
- **ChromaDB Vector Store** - Pattern matching from framework docs
- **Framework-Aware Prompts** - Django, FastAPI, Flask support
- **Shared Knowledge System** - Agents track models across apps

### 🎯 Smart Code Generation
- **Multi-Agent Roles** - ModelArchitect, APIBuilder, QualityGuard
- **Type-Safe Models** - Pydantic2 validation
- **Test Generation** - Automatic test suite creation

## Installation

```bash
# From PyPI
pip install appai

# From source
git clone https://github.com/yourusername/appai.git
cd appai2
poetry install
```

## Usage

### Basic Example

```python
from appai.orchestration import SwarmHub
from appai.documentation import DocumentationEngine

# Initialize
docs = DocumentationEngine(framework="django")
hub = SwarmHub(docs_engine=docs)

# Run swarm
await hub.run_swarm(
    goal="Create blog system with Author, Post, Comment models",
    config={"output_dir": "generated/blog"}
)
```

### Cross-App Model Relationships

```python
# AppAI automatically:
# 1. Creates Author in authors/models.py
# 2. Creates Post in blog/models.py with ForeignKey to Author
# 3. Generates proper imports: from authors.models import Author
# 4. Adds related_name for reverse lookups

goal = """
Create Django apps:
- authors app with Author model
- blog app with Post model (ForeignKey to Author)
- comments app with Comment model (ForeignKey to Post)
"""

await hub.run_swarm(goal=goal)
```

## Development

### DevOps CLI

```bash
# Version management & packaging
npm run cli

# Show version info
npm run version

# Build package
npm run build
```

See [DEVOPS.md](DEVOPS.md) for details.

### Run Examples

```bash
# Blog with cross-app relationships
poetry run python examples/example_blog_with_relations.py

# Decentralized task bidding
poetry run python examples/example_decentralized.py

# Auto catalog generation
poetry run python examples/example_auto_catalog.py
```

### Run Tests

```bash
poetry run pytest
```

## Architecture

```
appai/
├── src/appai/
│   ├── agents/              # Agent implementations
│   │   ├── agent_pool.py   # Agent coordination
│   │   └── profiles/       # Agent role definitions
│   │
│   ├── orchestration/       # Swarm coordination
│   │   └── swarm_hub.py    # Decentralized task bidding
│   │
│   ├── prompts/             # Framework-aware prompts
│   │   ├── registry.py     # Prompt builder registry
│   │   └── django.py       # Django-specific prompts
│   │
│   ├── documentation/       # ChromaDB pattern matching
│   └── tools/               # MCP file operations
│
├── devops/                  # Package management CLI
│   ├── cli/                # Interactive CLI
│   ├── managers/           # Version & package managers
│   └── models/             # Pydantic models
│
├── examples/               # Usage examples
└── @progress/              # Development docs
```

## How It Works

### 1. Task Decomposition
```
User Goal → Planning Agent → Subtasks (model, api, tests)
```

### 2. Async Bidding
```
Subtasks → Broadcast → Agents bid → Winner selected → Task executed
```

### 3. Shared Knowledge
```
Agent completes task → Updates shared_knowledge → Other agents see new models
```

### 4. Framework-Aware Prompts
```
Agent receives task → Registry selects prompts → Agent gets Django-specific guidelines
```

## Documentation

- **Session Summary**: [`@progress/SESSION_SUMMARY.md`](@progress/SESSION_SUMMARY.md) - Cross-app model relationships
- **Framework Prompts**: [`@progress/FRAMEWORK_PROMPT_SYSTEM.md`](@progress/FRAMEWORK_PROMPT_SYSTEM.md) - Agent-driven prompts
- **DevOps CLI**: [`@progress/DEVOPS_CLI_SUMMARY.md`](@progress/DEVOPS_CLI_SUMMARY.md) - Packaging system

## Key Innovations

### 1. Shared Knowledge System
Agents automatically track created models across different apps:

```python
shared_knowledge = {
    "created_models": [
        {"name": "Author", "app": "authors", "file": "authors/models.py"},
        {"name": "Post", "app": "blog", "file": "blog/models.py"}
    ]
}
```

### 2. Framework-Aware Prompts
Agent prompts adapt based on framework and task:

```python
@PromptBuilderRegistry.register('django')
class DjangoPromptBuilder:
    def get_cross_app_imports_guide():
        """Django-specific cross-app import instructions"""
```

### 3. Decentralized Task Bidding
No central coordinator - agents self-organize:

```python
# Agent calculates bid based on:
# - Task category match (model, api, tests)
# - Previous experience
# - Current workload
```

## Requirements

- Python 3.12+
- OpenAI API key
- ChromaDB (for documentation patterns)

## License

MIT

## Contributing

Contributions welcome! See issues for current development priorities.

## Credits

Built with:
- [agency-swarm](https://github.com/VRSEN/agency-swarm) - Agent framework
- [Pydantic](https://docs.pydantic.dev/) - Type safety
- [ChromaDB](https://www.trychroma.com/) - Vector storage
- [Rich](https://rich.readthedocs.io/) - Terminal UI
