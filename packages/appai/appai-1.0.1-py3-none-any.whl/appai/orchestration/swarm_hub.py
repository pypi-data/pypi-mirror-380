"""Decentralized swarm hub for broadcasting and coordination."""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any
from pathlib import Path

from aiapp.models import TaskPlan, SubTask
from aiapp.models.swarm import SwarmConfig, HubState, SwarmMetrics
from aiapp.models.communication import (
    Message, MessageType, AgentState, AgentStatus, TaskBid
)
from aiapp.orchestration.task_broker import TaskBroker
from aiapp.core import DocumentationEngine
from aiapp.logging import SwarmLogger

logger = logging.getLogger(__name__)


class SwarmHub:
    """
    Decentralized swarm coordination hub.

    Responsibilities:
    - Broadcast tasks to all agents
    - Facilitate bidding and task assignment
    - Maintain shared knowledge
    - Track execution metrics

    Does NOT:
    - Assign tasks directly (agents bid)
    - Control agent execution (agents self-manage)
    - Dictate communication (peer-to-peer enabled)
    """

    def __init__(
        self,
        task_plan: TaskPlan,
        docs_engine: DocumentationEngine,
        config: Optional[SwarmConfig] = None,
        log_dir: Optional[Path] = None
    ):
        self.plan = task_plan
        self.docs = docs_engine
        self.config = config or SwarmConfig()

        # State
        self.state = HubState(start_time=time.time())

        # Task broker for bidding
        self.broker = TaskBroker(self.config)

        # Logging
        self.logger = SwarmLogger(log_dir=log_dir)

        # Message queue for async communication
        self.message_queue: asyncio.Queue[Message] = asyncio.Queue()

        # Task results
        self.task_results: Dict[str, Dict[str, Any]] = {}

    async def initialize(self, agent_names: List[str]) -> None:
        """Initialize hub and register agents."""
        logger.info(f"🚀 Initializing swarm hub with {len(agent_names)} agents")

        # Register agents
        for name in agent_names:
            self.state.agent_states[name] = AgentState(
                agent_name=name,
                status=AgentStatus.IDLE
            )

        # Initialize shared knowledge
        self.state.shared_knowledge = {
            "project_structure": {},
            "created_models": [],
            "api_endpoints": [],
            "patterns_used": [],
            "decisions": []
        }

        # Add all tasks to available pool
        for task in self.plan.subtasks:
            # Only tasks with no dependencies are initially available
            if not task.dependencies:
                self.state.available_tasks.add(task.id)

        logger.info(
            f"✅ Hub initialized: "
            f"{len(self.state.available_tasks)} tasks available, "
            f"{len(agent_names)} agents ready"
        )

        # Log start
        self.logger.log_swarm_start(
            task_description=self.plan.goal,
            num_agents=len(agent_names),
            num_tasks=len(self.plan.subtasks)
        )

    async def broadcast_available_tasks(self) -> List[str]:
        """
        Broadcast all available tasks to swarm.

        Returns list of task IDs announced.
        """
        if not self.state.available_tasks:
            return []

        announced = []
        tasks_map = {t.id: t for t in self.plan.subtasks}

        for task_id in list(self.state.available_tasks):
            task = tasks_map.get(task_id)
            if not task:
                continue

            # Announce task for bidding
            announcement = await self.broker.announce_task(task)
            announced.append(task_id)

            logger.info(
                f"📢 BROADCAST: Task {task_id} ({task.category}) "
                f"available for bidding"
            )

        return announced

    async def process_bid(self, bid: TaskBid) -> bool:
        """
        Process bid from agent.

        Returns True if accepted.
        """
        accepted = await self.broker.receive_bid(bid)

        if accepted:
            self.state.total_bids += 1

        return accepted

    async def assign_task(self, task_id: str) -> Optional[str]:
        """
        Assign task to winning bidder after bidding window.

        Returns agent name if assigned, None if no winner.
        """
        # Wait for bidding window
        await self.broker.wait_for_bids(task_id)

        # Select winner
        winner = await self.broker.select_winner(task_id)

        if not winner:
            logger.warning(f"⚠️  No winner for task {task_id}")
            return None

        # Update state
        self.state.available_tasks.discard(task_id)
        self.state.active_tasks[task_id] = winner.agent_name

        # Update agent state
        if winner.agent_name in self.state.agent_states:
            agent_state = self.state.agent_states[winner.agent_name]
            agent_state.status = AgentStatus.BUSY
            agent_state.active_task = task_id
            agent_state.current_load += 1

        logger.info(f"✅ Task {task_id} assigned to {winner.agent_name}")

        return winner.agent_name

    async def report_task_complete(
        self,
        task_id: str,
        agent_name: str,
        result: Dict[str, Any]
    ) -> None:
        """Agent reports task completion."""
        # Update state
        self.state.active_tasks.pop(task_id, None)
        self.state.completed_tasks.add(task_id)

        # Store result
        self.task_results[task_id] = result

        # Update shared knowledge with information from completed task
        await self._update_shared_knowledge(task_id, result)

        # Update agent state
        if agent_name in self.state.agent_states:
            agent_state = self.state.agent_states[agent_name]
            agent_state.status = AgentStatus.IDLE
            agent_state.active_task = None
            agent_state.current_load = max(0, agent_state.current_load - 1)
            agent_state.tasks_completed += 1

        # Check if new tasks are now available (dependencies met)
        await self._unlock_dependent_tasks(task_id)

        logger.info(
            f"✅ Task {task_id} completed by {agent_name}, "
            f"new available: {len(self.state.available_tasks)}"
        )

    async def report_task_failed(
        self,
        task_id: str,
        agent_name: str,
        error: str
    ) -> None:
        """Agent reports task failure."""
        # Update state
        self.state.active_tasks.pop(task_id, None)
        self.state.failed_tasks[task_id] = error

        # Update agent state
        if agent_name in self.state.agent_states:
            agent_state = self.state.agent_states[agent_name]
            agent_state.status = AgentStatus.IDLE
            agent_state.active_task = None
            agent_state.current_load = max(0, agent_state.current_load - 1)

        logger.error(f"❌ Task {task_id} failed by {agent_name}: {error}")

    async def _unlock_dependent_tasks(self, completed_task_id: str) -> None:
        """Check and unlock tasks that depended on completed task."""
        tasks_map = {t.id: t for t in self.plan.subtasks}

        for task in self.plan.subtasks:
            # Skip if already processed
            if (task.id in self.state.completed_tasks or
                task.id in self.state.failed_tasks or
                task.id in self.state.active_tasks or
                task.id in self.state.available_tasks):
                continue

            # Check if all dependencies are met
            if task.dependencies:
                deps_met = all(
                    dep_id in self.state.completed_tasks
                    for dep_id in task.dependencies
                )

                if deps_met:
                    self.state.available_tasks.add(task.id)
                    logger.info(
                        f"🔓 Unlocked task {task.id} "
                        f"(dependencies met: {task.dependencies})"
                    )

    def is_complete(self) -> bool:
        """Check if all tasks are complete or failed."""
        total = len(self.plan.subtasks)
        processed = len(self.state.completed_tasks) + len(self.state.failed_tasks)
        return processed >= total

    def get_metrics(self) -> SwarmMetrics:
        """Calculate and return swarm execution metrics."""
        total_time = time.time() - self.state.start_time
        total_completed = len(self.state.completed_tasks)
        total_failed = len(self.state.failed_tasks)

        return SwarmMetrics(
            total_time=total_time,
            avg_task_time=total_time / max(total_completed, 1),
            tasks_completed=total_completed,
            tasks_failed=total_failed,
            success_rate=total_completed / max(total_completed + total_failed, 1),
            parallelism_factor=0.0,  # Calculated by execution engine
            max_concurrent_tasks=0,
            total_messages=self.state.total_messages,
            total_bids=self.state.total_bids,
            avg_bids_per_task=self.state.total_bids / max(total_completed, 1),
            total_cost=0.0,  # Calculated from agent reports
            cost_per_task=0.0,
            avg_quality=0.0,
            self_selected_tasks=total_completed,
            peer_to_peer_messages=0
        )

    # Async Bidding Support

    async def get_available_tasks_for_bidding(self) -> List[SubTask]:
        """
        Get tasks available for agents to bid on.
        Used by background bidding loops.
        """
        available = []
        for task in self.plan.subtasks:
            if (task.id in self.state.available_tasks
                and task.id not in self.state.active_tasks):
                available.append(task)
        return available

    async def has_agent_bid(self, agent_name: str, task_id: str) -> bool:
        """Check if agent already submitted bid for task."""
        bids = self.broker.pending_bids.get(task_id, [])
        return any(bid.agent_name == agent_name for bid in bids)

    # Shared Knowledge Management

    async def _update_shared_knowledge(self, task_id: str, result: Dict[str, Any]) -> None:
        """
        Update shared knowledge with information from completed task.
        Parses created files to extract models, APIs, etc.
        """
        files = result.get("files", [])

        for file_path in files:
            # Extract models from models.py files
            if file_path.endswith("models.py"):
                models = await self._extract_models_from_file(file_path)

                for model_info in models:
                    # Add to shared knowledge
                    self.state.shared_knowledge["created_models"].append({
                        "name": model_info["name"],
                        "file": file_path,
                        "app": self._get_app_name(file_path),
                        "task_id": task_id,
                        "import_path": f"{self._get_app_name(file_path)}.models"
                    })

                    logger.info(
                        f"📝 Registered model: {model_info['name']} "
                        f"(from {self._get_app_name(file_path)}.models)"
                    )

            # Extract API endpoints from views.py, urls.py, etc.
            elif "views.py" in file_path or "urls.py" in file_path:
                # TODO: Parse API endpoints if needed
                pass

    async def _extract_models_from_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Extract Django model names from a models.py file.
        Uses simple regex to find class definitions that inherit from models.Model.
        """
        import re

        models = []

        try:
            # Read file content
            full_path = Path(file_path)
            if not full_path.exists():
                # Try relative to project root
                full_path = self.log_dir.parent / file_path

            if not full_path.exists():
                logger.warning(f"File not found for model extraction: {file_path}")
                return models

            content = full_path.read_text()

            # Find all class definitions that inherit from models.Model
            # Pattern: class ModelName(models.Model): or class ModelName(Model):
            pattern = r"class\s+(\w+)\s*\([^)]*models\.Model[^)]*\)"
            matches = re.finditer(pattern, content)

            for match in matches:
                model_name = match.group(1)
                models.append({
                    "name": model_name,
                    "line": content[:match.start()].count('\n') + 1
                })

            logger.debug(f"Extracted {len(models)} models from {file_path}")

        except Exception as e:
            logger.error(f"Error extracting models from {file_path}: {e}")

        return models

    def _get_app_name(self, file_path: str) -> str:
        """
        Extract Django app name from file path.
        Examples:
        - "authors/models.py" -> "authors"
        - "blog/api/serializers.py" -> "blog"
        """
        parts = Path(file_path).parts
        if len(parts) > 0:
            # First directory is usually the app name
            return parts[0]
        return "unknown"
