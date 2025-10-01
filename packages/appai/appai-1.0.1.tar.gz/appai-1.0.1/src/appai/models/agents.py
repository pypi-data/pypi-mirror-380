"""Agent-related Pydantic v2 models."""

from typing import Dict, Set, List, Any
from pydantic import BaseModel, Field, ConfigDict


class AgentProfile(BaseModel):
    """Agent profile with capabilities and performance metrics."""

    model_config = ConfigDict(frozen=False)

    name: str = Field(..., description="Agent name")
    capabilities: Set[str] = Field(..., description="Set of agent capabilities")
    specialization: str = Field(..., description="Primary specialization area")
    model_name: str = Field(..., description="AI model name (e.g., mistralai/codestral-2501)")
    cost_per_1m_tokens: float = Field(..., description="Cost per 1M tokens in USD", gt=0)
    performance_history: List[Dict[str, Any]] = Field(
        default_factory=list, description="Historical performance data"
    )
    success_rate: float = Field(default=1.0, description="Success rate (0-1)", ge=0, le=1)
    avg_quality: float = Field(default=0.8, description="Average quality score (0-1)", ge=0, le=1)
    tasks_completed: int = Field(default=0, description="Number of completed tasks", ge=0)


class SwarmState(BaseModel):
    """Current state of swarm execution."""

    model_config = ConfigDict(frozen=False)

    active_tasks: Set[str] = Field(default_factory=set, description="Currently executing task IDs")
    completed_tasks: Set[str] = Field(default_factory=set, description="Completed task IDs")
    failed_tasks: Dict[str, str] = Field(default_factory=dict, description="Failed task IDs with error messages")
    agent_assignments: Dict[str, str] = Field(default_factory=dict, description="Task ID to agent name mapping")
    shared_knowledge: Dict[str, Any] = Field(default_factory=dict, description="Shared context across agents")
    start_time: float = Field(default=0.0, description="Execution start timestamp")
    metrics: Dict[str, float] = Field(default_factory=dict, description="Execution metrics")
