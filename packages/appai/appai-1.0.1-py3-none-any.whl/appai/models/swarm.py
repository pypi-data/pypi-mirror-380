"""Swarm-level Pydantic v2 models for decentralized coordination."""

from typing import Dict, List, Any, Set
from pydantic import BaseModel, Field, ConfigDict

from aiapp.models.communication import AgentState, TaskBid


class SwarmConfig(BaseModel):
    """Configuration for decentralized swarm."""

    model_config = ConfigDict(frozen=False)

    # Task distribution
    bidding_window: float = Field(
        default=10.0,
        description="Time window for agents to bid on tasks (seconds)",
        gt=0
    )
    max_bidders_per_task: int = Field(
        default=3,
        description="Maximum number of bids to consider per task",
        ge=1
    )

    # Parallel execution
    max_parallel_tasks: int = Field(
        default=5,
        description="Maximum tasks to execute in parallel",
        ge=1
    )

    # Peer communication
    enable_peer_to_peer: bool = Field(
        default=True,
        description="Enable direct agent-to-agent communication"
    )

    # Knowledge sharing
    enable_knowledge_sharing: bool = Field(
        default=True,
        description="Enable shared knowledge accumulation"
    )

    # Timeouts
    task_timeout: float = Field(
        default=300.0,
        description="Maximum time for task execution (seconds)",
        gt=0
    )


class HubState(BaseModel):
    """State of the decentralized swarm hub."""

    model_config = ConfigDict(frozen=False)

    # Tasks
    available_tasks: Set[str] = Field(
        default_factory=set,
        description="Tasks available for claiming"
    )
    active_tasks: Dict[str, str] = Field(
        default_factory=dict,
        description="Task ID -> Agent name mapping"
    )
    completed_tasks: Set[str] = Field(
        default_factory=set,
        description="Completed task IDs"
    )
    failed_tasks: Dict[str, str] = Field(
        default_factory=dict,
        description="Failed task IDs with error messages"
    )

    # Agents
    agent_states: Dict[str, AgentState] = Field(
        default_factory=dict,
        description="Agent name -> state mapping"
    )

    # Bidding
    pending_bids: Dict[str, List[TaskBid]] = Field(
        default_factory=dict,
        description="Task ID -> list of bids"
    )

    # Knowledge sharing
    shared_knowledge: Dict[str, Any] = Field(
        default_factory=dict,
        description="Shared context across agents"
    )

    # Metrics
    start_time: float = Field(default=0.0, description="Swarm start time")
    total_messages: int = Field(default=0, description="Total messages exchanged", ge=0)
    total_bids: int = Field(default=0, description="Total bids received", ge=0)


class SwarmMetrics(BaseModel):
    """Performance metrics for swarm execution."""

    model_config = ConfigDict(frozen=False)

    # Time
    total_time: float = Field(..., description="Total execution time (seconds)", ge=0)
    avg_task_time: float = Field(..., description="Average task time (seconds)", ge=0)

    # Tasks
    tasks_completed: int = Field(..., description="Number of completed tasks", ge=0)
    tasks_failed: int = Field(..., description="Number of failed tasks", ge=0)
    success_rate: float = Field(..., description="Task success rate (0-1)", ge=0, le=1)

    # Parallelism
    parallelism_factor: float = Field(
        ...,
        description="Actual parallel execution factor",
        ge=0
    )
    max_concurrent_tasks: int = Field(
        ...,
        description="Maximum tasks running simultaneously",
        ge=0
    )

    # Communication
    total_messages: int = Field(..., description="Total messages exchanged", ge=0)
    total_bids: int = Field(..., description="Total bids received", ge=0)
    avg_bids_per_task: float = Field(..., description="Average bids per task", ge=0)

    # Cost
    total_cost: float = Field(..., description="Total cost in USD", ge=0)
    cost_per_task: float = Field(..., description="Average cost per task", ge=0)

    # Quality
    avg_quality: float = Field(..., description="Average quality score (0-1)", ge=0, le=1)

    # Autonomy metrics
    self_selected_tasks: int = Field(
        default=0,
        description="Tasks claimed via autonomous bidding",
        ge=0
    )
    peer_to_peer_messages: int = Field(
        default=0,
        description="Direct agent-to-agent messages",
        ge=0
    )
