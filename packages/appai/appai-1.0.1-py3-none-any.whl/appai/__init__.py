"""
AIApp - Decentralized Swarm Intelligence System for Documentation-Driven Code Generation.

Built on Agency Swarm 1.0.2 with autonomous agent task selection and parallel execution.
"""

__version__ = "2.0.2"
__author__ = "AIApp Team"

# Core components
from aiapp.core import DocumentationEngine, TaskDecomposer

# Agents
from aiapp.agents import AgentPool, AgentCapability

# Decentralized orchestration
from aiapp.orchestration import SwarmHub, TaskBroker, ExecutionEngine

# Models
from aiapp.models import (
    SubTask,
    TaskPlan,
    TaskComplexity,
    AgentProfile,
    SwarmState,
    SwarmConfig,
    SwarmMetrics,
)

__all__ = [
    # Core
    "DocumentationEngine",
    "TaskDecomposer",
    # Agents
    "AgentPool",
    "AgentCapability",
    # Orchestration
    "SwarmHub",
    "TaskBroker",
    "ExecutionEngine",
    # Models
    "SubTask",
    "TaskPlan",
    "TaskComplexity",
    "AgentProfile",
    "SwarmState",
    "SwarmConfig",
    "SwarmMetrics",
]
