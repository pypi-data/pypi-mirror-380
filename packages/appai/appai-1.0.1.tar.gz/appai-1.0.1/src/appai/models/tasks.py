"""Task-related Pydantic v2 models."""

from enum import Enum
from typing import List, Set
from pydantic import BaseModel, Field, ConfigDict


class TaskComplexity(str, Enum):
    """Task complexity levels for model selection."""

    TRIVIAL = "trivial"  # 1-5 lines
    SIMPLE = "simple"  # 5-50 lines
    MODERATE = "moderate"  # 50-200 lines
    COMPLEX = "complex"  # 200-500 lines
    EPIC = "epic"  # 500+ lines


class SubTask(BaseModel):
    """Atomic unit of work for swarm execution."""

    model_config = ConfigDict(frozen=False)

    id: str = Field(..., description="Unique task identifier")
    description: str = Field(..., description="Task description")
    category: str = Field(..., description="Task category (model, viewset, serializer, admin, tests)")
    dependencies: Set[str] = Field(default_factory=set, description="IDs of dependent tasks")
    estimated_complexity: TaskComplexity = Field(..., description="Estimated task complexity")
    files_to_create: List[str] = Field(default_factory=list, description="Files to create")
    acceptance_criteria: List[str] = Field(default_factory=list, description="Acceptance criteria")


class TaskPlan(BaseModel):
    """Complete task decomposition with execution order."""

    model_config = ConfigDict(frozen=False)

    goal: str = Field(..., description="High-level goal description")
    subtasks: List[SubTask] = Field(..., description="List of subtasks")
    execution_order: List[List[str]] = Field(..., description="Waves of parallel task IDs")
    estimated_duration: float = Field(..., description="Estimated duration in minutes", gt=0)
    estimated_cost: float = Field(..., description="Estimated cost in USD", ge=0)
