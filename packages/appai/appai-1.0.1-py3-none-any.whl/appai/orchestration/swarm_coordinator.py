"""Swarm coordinator for parallel agent execution with knowledge sharing."""

import time
import asyncio
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path

from aiapp.models import TaskPlan, SwarmState
from aiapp.agents import AgentPool
from aiapp.core import DocumentationEngine
from aiapp.logging import SwarmLogger

logger = logging.getLogger(__name__)


class SwarmCoordinator:
    """Coordinate parallel agent execution with shared knowledge."""

    def __init__(
        self,
        agent_pool: AgentPool,
        task_plan: TaskPlan,
        docs_engine: DocumentationEngine,
        log_dir: Optional[Path] = None
    ):
        self.agents = agent_pool
        self.plan = task_plan
        self.docs = docs_engine

        # State
        self.state = SwarmState(start_time=time.time())

        # Results
        self.task_results: Dict[str, Dict[str, Any]] = {}
        self.performance_metrics: Dict[str, Dict[str, Any]] = {}

        # Logging
        self.swarm_logger = SwarmLogger(log_dir=log_dir)

    async def execute(self) -> Dict[str, Any]:
        """Execute task plan with swarm intelligence."""
        # Log swarm start
        self.swarm_logger.log_swarm_start(
            task_description=self.plan.goal,
            num_agents=len(self.agents.agents),
            num_tasks=len(self.plan.subtasks)
        )

        try:
            # Initialize swarm
            await self._initialize_swarm()

            # Execute waves
            for wave_idx, parallel_tasks in enumerate(self.plan.execution_order):
                self.swarm_logger.log_wave_start(
                    wave_number=wave_idx + 1,
                    total_waves=len(self.plan.execution_order),
                    task_count=len(parallel_tasks)
                )

                await self._execute_wave(parallel_tasks, wave_idx + 1)

                # Count completed/failed in this wave
                wave_completed = sum(1 for tid in parallel_tasks if tid in self.state.completed_tasks)
                wave_failed = sum(1 for tid in parallel_tasks if tid in self.state.failed_tasks)

                self.swarm_logger.log_wave_end(
                    wave_number=wave_idx + 1,
                    completed=wave_completed,
                    failed=wave_failed
                )

            # Finalize
            results = await self._finalize()

            success = len(self.state.failed_tasks) == 0

            # Log swarm end
            self.swarm_logger.log_swarm_end(
                success=success,
                completed_tasks=len(self.state.completed_tasks),
                failed_tasks=len(self.state.failed_tasks)
            )

            # Save logs
            self.swarm_logger.save_logs()

            # Print report
            self.swarm_logger.print_report()

            return {
                "success": success,
                "completed": len(self.state.completed_tasks),
                "failed": len(self.state.failed_tasks),
                "results": results,
                "metrics": self._calculate_metrics()
            }

        except Exception as e:
            logger.error(f"❌ Swarm execution failed: {e}", exc_info=True)
            self.swarm_logger.log_swarm_end(
                success=False,
                completed_tasks=len(self.state.completed_tasks),
                failed_tasks=len(self.state.failed_tasks)
            )
            self.swarm_logger.save_logs()
            return self._handle_failure(e)

    async def _initialize_swarm(self):
        """Initialize swarm state and shared knowledge."""
        logger.info("🚀 Initializing swarm...")

        # Initialize shared knowledge
        self.state.shared_knowledge = {
            "project_structure": {},
            "created_models": [],
            "api_endpoints": [],
            "patterns_used": [],
            "decisions": []
        }

        logger.info("✅ Swarm initialized")

    async def _execute_wave(self, task_ids: List[str], wave_number: int):
        """Execute parallel wave of tasks."""
        tasks_map = {t.id: t for t in self.plan.subtasks}

        # Create coroutines for parallel execution
        coroutines = [
            self._execute_task(tasks_map[tid])
            for tid in task_ids
            if tid in tasks_map
        ]

        if not coroutines:
            logger.warning(f"No valid tasks in wave: {task_ids}")
            return

        # Execute in parallel
        results = await asyncio.gather(*coroutines, return_exceptions=True)

        # Process results
        for task_id, result in zip(task_ids, results):
            if isinstance(result, Exception):
                self.state.failed_tasks[task_id] = str(result)
                logger.error(f"❌ Task {task_id} failed: {result}")
            else:
                self.state.completed_tasks.add(task_id)
                self.task_results[task_id] = result
                logger.info(f"✅ Task {task_id} completed")

    async def _execute_task(self, subtask) -> Dict[str, Any]:
        """Execute single task with best-matched agent."""
        self.state.active_tasks.add(subtask.id)

        try:
            # Select agent
            agent = await self.agents.select_agent(subtask)
            self.state.agent_assignments[subtask.id] = agent.profile.name

            # Log task assignment
            self.swarm_logger.log_task_assignment(
                task_id=subtask.id,
                agent_name=agent.profile.name,
                task_description=subtask.description
            )

            # Get agent logger
            agent_logger = self.swarm_logger.get_agent_logger(agent.profile.name)

            # Prepare context
            context = await self._prepare_context(subtask)

            # Log documentation search
            if "patterns" in context and context["patterns"]:
                self.swarm_logger.log_pattern_search(
                    agent_name=agent.profile.name,
                    query=subtask.description,
                    patterns_found=context["patterns"],
                    task_context=subtask.id
                )

            # Log action start
            agent_logger.log_action(
                action_type="task_execution",
                description=f"Executing task: {subtask.description}",
                context={"task_id": subtask.id, "category": subtask.category}
            )

            # Execute
            start_time = time.time()
            result = await agent.execute_task(subtask, context)
            execution_time = time.time() - start_time

            # Log action complete
            agent_logger.log_action(
                action_type="task_execution",
                description=f"Task completed: {subtask.id}",
                context={"task_id": subtask.id, "execution_time": execution_time},
                result=f"Files: {result.get('files', [])}"
            )

            # Update knowledge
            await self._update_knowledge(subtask, result)

            # Record metrics
            self.performance_metrics[subtask.id] = {
                "agent": agent.profile.name,
                "time": execution_time,
                "tokens": result.get("tokens_used", 0),
                "cost": result.get("cost", 0.0),
                "quality": result.get("quality_score", 0.0)
            }

            return result

        finally:
            self.state.active_tasks.discard(subtask.id)

    async def _prepare_context(self, subtask) -> Dict[str, Any]:
        """Prepare task execution context with patterns and dependencies."""
        context = {
            "task": subtask,
            "shared_knowledge": dict(self.state.shared_knowledge),
            "completed_tasks": list(self.state.completed_tasks),
        }

        # Add relevant patterns from documentation
        # Search for patterns relevant to the task
        # Don't use category filter (metadata doesn't have 'category' field)
        patterns = self.docs.search_patterns(
            query=subtask.description,
            category=None,  # Metadata only has: file, path, source, chunk_idx
            top_k=5  # Get more patterns for better context
        )
        context["patterns"] = patterns

        # Log pattern search
        if patterns:
            logger.info(f"📚 Found {len(patterns)} documentation patterns for task {subtask.id}")
            for p in patterns[:2]:  # Show top 2
                logger.debug(f"   Pattern from {p.get('metadata', {}).get('file', 'unknown')}: {p.get('content', '')[:100]}...")

        # Add dependency results
        if subtask.dependencies:
            context["dependency_results"] = {
                dep_id: self.task_results.get(dep_id)
                for dep_id in subtask.dependencies
                if dep_id in self.task_results
            }

        return context

    async def _update_knowledge(self, subtask, result: Dict[str, Any]):
        """Update shared knowledge based on task results."""
        knowledge = self.state.shared_knowledge

        # Extract information based on task category
        if subtask.category == "model":
            knowledge["created_models"].append({
                "name": result.get("model_name"),
                "fields": result.get("fields", []),
                "file": result.get("file_path")
            })

        elif subtask.category == "viewset":
            knowledge["api_endpoints"].append({
                "resource": result.get("resource"),
                "model": result.get("model"),
                "path": result.get("url_path")
            })

        # Track patterns used
        if "pattern" in result:
            knowledge["patterns_used"].append(result["pattern"])

    async def _finalize(self) -> Dict[str, Any]:
        """Finalize execution and aggregate results."""
        logger.info("🏁 Finalizing swarm execution...")

        # Collect all created files
        all_files = []
        for result in self.task_results.values():
            if "files" in result:
                all_files.extend(result["files"])

        # Calculate average quality
        quality_scores = [
            m["quality"] for m in self.performance_metrics.values()
            if "quality" in m and m["quality"] > 0
        ]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0.0

        return {
            "files_created": all_files,
            "quality_score": avg_quality,
            "shared_knowledge": self.state.shared_knowledge,
            "performance": self.performance_metrics
        }

    def _calculate_metrics(self) -> Dict[str, Any]:
        """Calculate execution metrics."""
        total_time = time.time() - self.state.start_time

        # Parallelism factor
        total_task_time = sum(m.get("time", 0) for m in self.performance_metrics.values())
        parallelism = total_task_time / total_time if total_time > 0 else 0

        # Cost efficiency
        total_cost = sum(m.get("cost", 0) for m in self.performance_metrics.values())
        cost_per_task = total_cost / len(self.performance_metrics) if self.performance_metrics else 0

        # Quality average
        quality_scores = [m.get("quality", 0) for m in self.performance_metrics.values()]
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0.0

        metrics = {
            "total_time": total_time,
            "tasks_completed": len(self.state.completed_tasks),
            "tasks_failed": len(self.state.failed_tasks),
            "parallelism_factor": parallelism,
            "total_cost": total_cost,
            "cost_per_task": cost_per_task,
            "avg_quality": avg_quality,
        }

        logger.info(f"📊 Metrics: {metrics}")

        return metrics

    def _handle_failure(self, error: Exception) -> Dict[str, Any]:
        """Handle critical failure."""
        return {
            "success": False,
            "error": str(error),
            "completed": len(self.state.completed_tasks),
            "failed": len(self.state.failed_tasks),
            "state": self.state.model_dump()
        }
