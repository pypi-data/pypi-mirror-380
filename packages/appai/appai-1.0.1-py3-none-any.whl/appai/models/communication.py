"""Communication-related Pydantic v2 models for decentralized swarm."""

from enum import Enum
from typing import Optional, Any, Dict
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class MessageType(str, Enum):
    """Types of messages in swarm communication."""

    # Coordination
    TASK_BROADCAST = "task_broadcast"  # Hub broadcasts available task
    TASK_BID = "task_bid"             # Agent bids to handle task
    TASK_CLAIM = "task_claim"         # Agent claims task
    TASK_COMPLETE = "task_complete"   # Agent reports completion
    TASK_FAILED = "task_failed"       # Agent reports failure

    # Peer-to-peer
    REQUEST_HELP = "request_help"     # Agent needs assistance
    OFFER_HELP = "offer_help"         # Agent offers to help
    SHARE_KNOWLEDGE = "share_knowledge"  # Agent shares learned info

    # Status
    AGENT_READY = "agent_ready"       # Agent ready for tasks
    AGENT_BUSY = "agent_busy"         # Agent working
    AGENT_IDLE = "agent_idle"         # Agent idle


class AgentStatus(str, Enum):
    """Agent availability status."""

    IDLE = "idle"          # Ready for tasks
    BUSY = "busy"          # Working on task
    HELPING = "helping"    # Assisting another agent
    BLOCKED = "blocked"    # Waiting for dependencies


class Message(BaseModel):
    """Base message for swarm communication."""

    model_config = ConfigDict(frozen=False)

    id: str = Field(..., description="Unique message ID")
    type: MessageType = Field(..., description="Message type")
    sender: str = Field(..., description="Sender agent name")
    recipient: Optional[str] = Field(default=None, description="Recipient agent (None = broadcast)")
    timestamp: datetime = Field(default_factory=datetime.now, description="Message timestamp")
    payload: Dict[str, Any] = Field(default_factory=dict, description="Message payload")
    priority: int = Field(default=0, description="Message priority (higher = more urgent)", ge=0, le=10)


class TaskBid(BaseModel):
    """Agent's bid to handle a task."""

    model_config = ConfigDict(frozen=False)

    task_id: str = Field(..., description="Task identifier")
    agent_name: str = Field(..., description="Bidding agent name")
    confidence: float = Field(..., description="Confidence score (0-1)", ge=0, le=1)
    estimated_time: float = Field(..., description="Estimated time in seconds", gt=0)
    estimated_cost: float = Field(..., description="Estimated cost in USD", ge=0)
    capabilities_match: float = Field(..., description="Capability match score (0-1)", ge=0, le=1)
    current_load: int = Field(default=0, description="Number of active tasks", ge=0)
    timestamp: datetime = Field(default_factory=datetime.now, description="Bid timestamp")


class TaskAnnouncement(BaseModel):
    """Task announced to swarm for bidding."""

    model_config = ConfigDict(frozen=False)

    task_id: str = Field(..., description="Task identifier")
    description: str = Field(..., description="Task description")
    category: str = Field(..., description="Task category")
    complexity: str = Field(..., description="Task complexity level")
    dependencies_met: bool = Field(..., description="Whether dependencies are satisfied")
    max_bidders: int = Field(default=3, description="Max number of bids to accept", ge=1)
    bidding_deadline: float = Field(default=5.0, description="Bidding window in seconds", gt=0)
    announced_at: datetime = Field(default_factory=datetime.now, description="Announcement time")


class AgentState(BaseModel):
    """Current state of an agent in the swarm."""

    model_config = ConfigDict(frozen=False)

    agent_name: str = Field(..., description="Agent identifier")
    status: AgentStatus = Field(default=AgentStatus.IDLE, description="Current status")
    active_task: Optional[str] = Field(default=None, description="Current task ID")
    tasks_completed: int = Field(default=0, description="Number of completed tasks", ge=0)
    success_rate: float = Field(default=1.0, description="Success rate (0-1)", ge=0, le=1)
    current_load: int = Field(default=0, description="Number of active tasks", ge=0)
    last_activity: datetime = Field(default_factory=datetime.now, description="Last activity time")
