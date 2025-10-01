"""Parallel execution engine for decentralized swarm."""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path

from aiapp.models import TaskPlan
from aiapp.models.swarm import SwarmConfig
from aiapp.orchestration.swarm_hub import SwarmHub
from aiapp.agents import AgentPool
from aiapp.core import DocumentationEngine

# Keep standard logger for backward compatibility, but use hub.logger for structured logging
logger = logging.getLogger(__name__)


class ExecutionEngine:
    """
    Manages parallel execution of autonomous agents.

    Pattern: Agents pull tasks from hub, hub doesn't push.
    """

    def __init__(
        self,
        agent_pool: AgentPool,
        swarm_hub: SwarmHub,
        docs_engine: DocumentationEngine,
        config: Optional[SwarmConfig] = None,
        project_path: Optional[Path] = None
    ):
        self.agents = agent_pool
        self.hub = swarm_hub
        self.docs = docs_engine
        self.config = config or SwarmConfig()
        self.project_path = project_path

        # Execution tracking
        self.running_tasks: Dict[str, asyncio.Task] = {}
        self.max_concurrent = 0

        # Async bidding support
        self.bidding_loops: Dict[str, asyncio.Task] = {}
        self.bidding_active = asyncio.Event()
        self.bidding_active.set()

    async def _agent_bidding_loop(self, agent) -> None:
        """
        Background loop: agent continuously monitors and bids on available tasks.
        Runs independently from task execution.
        """
        logger.info(f"🔄 {agent.profile.name} bidding loop started")

        while self.bidding_active.is_set() and not self.hub.is_complete():
            try:
                # Get available tasks from hub
                available_tasks = await self.hub.get_available_tasks_for_bidding()

                for task in available_tasks:
                    # Check if already bid on this task
                    already_bid = await self.hub.has_agent_bid(agent.profile.name, task.id)
                    if already_bid:
                        continue

                    # Evaluate task (quick, non-blocking)
                    confidence = agent.can_handle(task)

                    if confidence < 0.3:
                        # Not confident enough, skip
                        continue

                    # Create and submit bid
                    from aiapp.models.communication import TaskBid

                    bid = TaskBid(
                        task_id=task.id,
                        agent_name=agent.profile.name,
                        confidence=confidence,
                        estimated_time=30.0,
                        estimated_cost=0.01,
                        capabilities_match=confidence,
                        current_load=len([
                            t for t in self.running_tasks.values()
                            if not t.done()
                        ])
                    )

                    # Submit bid to hub
                    accepted = await self.hub.process_bid(bid)

                    if accepted:
                        logger.debug(
                            f"💰 {agent.profile.name} bid on {task.id} "
                            f"(confidence:{confidence:.2f}, load:{bid.current_load})"
                        )

                # Check every 500ms
                await asyncio.sleep(0.5)

            except Exception as e:
                logger.error(f"❌ Bidding loop error ({agent.profile.name}): {e}")
                await asyncio.sleep(1.0)

        logger.info(f"✅ {agent.profile.name} bidding loop stopped")

    async def execute(self) -> Dict[str, Any]:
        """
        Execute swarm with autonomous task selection.

        Flow:
        1. Hub broadcasts available tasks
        2. Agents bid on tasks they can handle (in background loops)
        3. Hub selects winners
        4. Agents execute tasks in parallel
        5. Agents report completion → unlocks new tasks
        6. Repeat until all tasks done
        """
        logger.info("🚀 Starting decentralized swarm execution")

        # Initialize hub with agent names
        agent_names = [agent.profile.name for agent in self.agents.agents]
        await self.hub.initialize(agent_names)

        try:
            # Start background bidding loops for all agents
            logger.info(f"🔄 Starting {len(self.agents.agents)} bidding loops")
            for agent in self.agents.agents:
                loop_task = asyncio.create_task(
                    self._agent_bidding_loop(agent),
                    name=f"bidding_{agent.profile.name}"
                )
                self.bidding_loops[agent.profile.name] = loop_task

            # Main execution loop
            while not self.hub.is_complete():
                # Broadcast available tasks
                announced = await self.hub.broadcast_available_tasks()

                if not announced:
                    # No tasks available, wait for completions
                    if self.running_tasks:
                        logger.debug("⏳ Waiting for task completions...")
                        await asyncio.sleep(1.0)
                        continue
                    else:
                        # No running tasks and no available tasks
                        logger.warning("⚠️  Deadlock detected: no tasks available or running")
                        break

                # Process bidding for each announced task
                for task_id in announced:
                    await self._process_task_bidding(task_id)

                # Update max concurrent
                self.max_concurrent = max(
                    self.max_concurrent,
                    len(self.running_tasks)
                )

            # Stop bidding loops
            logger.info("🛑 Stopping bidding loops")
            self.bidding_active.clear()

            # Wait for bidding loops to finish
            if self.bidding_loops:
                await asyncio.gather(
                    *self.bidding_loops.values(),
                    return_exceptions=True
                )

            # Wait for remaining tasks to complete
            if self.running_tasks:
                logger.info(f"⏳ Waiting for {len(self.running_tasks)} remaining tasks...")
                await asyncio.gather(*self.running_tasks.values(), return_exceptions=True)

            # Collect results
            metrics = self.hub.get_metrics()
            metrics.max_concurrent_tasks = self.max_concurrent

            # Calculate parallelism factor
            total_task_time = sum(
                result.get("execution_time", 0)
                for result in self.hub.task_results.values()
            )
            metrics.parallelism_factor = (
                total_task_time / metrics.total_time
                if metrics.total_time > 0 else 0
            )

            success = len(self.hub.state.failed_tasks) == 0

            logger.info(
                f"{'✅' if success else '❌'} Swarm execution complete: "
                f"{metrics.tasks_completed} completed, "
                f"{metrics.tasks_failed} failed, "
                f"{metrics.parallelism_factor:.2f}x parallelism"
            )

            # Log end
            self.hub.logger.log_swarm_end(
                success=success,
                completed_tasks=metrics.tasks_completed,
                failed_tasks=metrics.tasks_failed
            )
            self.hub.logger.save_logs()
            self.hub.logger.print_report()

            return {
                "success": success,
                "completed": metrics.tasks_completed,
                "failed": metrics.tasks_failed,
                "results": {
                    "files_created": self._collect_files(),
                    "shared_knowledge": self.hub.state.shared_knowledge
                },
                "metrics": metrics.model_dump()
            }

        except Exception as e:
            logger.error(f"❌ Execution engine error: {e}", exc_info=True)

            # Stop bidding loops on error
            self.bidding_active.clear()
            if self.bidding_loops:
                await asyncio.gather(
                    *self.bidding_loops.values(),
                    return_exceptions=True
                )

            return {
                "success": False,
                "error": str(e),
                "completed": len(self.hub.state.completed_tasks),
                "failed": len(self.hub.state.failed_tasks)
            }

    async def _process_task_bidding(self, task_id: str) -> None:
        """
        Process bidding cycle for a task.

        NOTE: Agents are bidding continuously in background loops.
        This method just waits for bidding window and assigns winner.

        1. Wait for bidding window (agents bidding in background)
        2. Hub selects winner
        3. Winner executes task
        """
        # Get task details
        task = next(
            (t for t in self.hub.plan.subtasks if t.id == task_id),
            None
        )
        if not task:
            logger.error(f"Task {task_id} not found in plan")
            return

        # Hub waits for bidding window and assigns task to winner
        winner_name = await self.hub.assign_task(task_id)

        if not winner_name:
            logger.warning(f"⚠️  No agent claimed task {task_id}")
            await self.hub.report_task_failed(
                task_id,
                "system",
                "No agent bid on task"
            )
            return

        # Get winning agent
        winner = next(
            (a for a in self.agents.agents if a.profile.name == winner_name),
            None
        )

        if not winner:
            logger.error(f"Winner {winner_name} not found in agent pool")
            return

        # Start task execution (non-blocking)
        execution_task = asyncio.create_task(
            self._execute_task(winner, task)
        )
        self.running_tasks[task_id] = execution_task

    async def _execute_task(self, agent, task) -> None:
        """Execute task with agent and report result."""
        try:
            # Prepare context with documentation patterns
            context = await self._prepare_context(task)

            # Execute task
            result = await agent.execute_task(task, context)

            # Quality check: Review generated files
            quality_passed = await self._check_quality(result, task, agent)

            if not quality_passed:
                logger.warning(
                    f"⚠️ Quality check FAILED for {task.id} (score < 0.85), "
                    f"but task marked complete (manual review recommended)"
                )
            else:
                logger.info(f"✅ Quality check PASSED for {task.id}")

            # Report success
            await self.hub.report_task_complete(
                task.id,
                agent.profile.name,
                result
            )

        except Exception as e:
            logger.error(
                f"❌ Task {task.id} execution failed: {e}",
                exc_info=True
            )
            await self.hub.report_task_failed(
                task.id,
                agent.profile.name,
                str(e)
            )

        finally:
            # Remove from running tasks
            self.running_tasks.pop(task.id, None)

    async def _prepare_context(self, task) -> Dict[str, Any]:
        """Prepare execution context with documentation patterns."""
        context = {
            "task": task,
            "shared_knowledge": dict(self.hub.state.shared_knowledge),
            "completed_tasks": list(self.hub.state.completed_tasks),
        }

        # Get relevant documentation patterns
        patterns = self.docs.search_patterns(
            query=task.description,
            category=None,
            top_k=5
        )
        context["patterns"] = patterns

        if patterns:
            # Log detailed pattern information
            scores = [p.get('score', 0) for p in patterns]
            logger.info(
                f"📚 Found {len(patterns)} documentation patterns for {task.id}"
            )
            logger.info(f"  Relevance scores: {[f'{s:.2f}' for s in scores[:3]]}")

            # Log pattern details
            for idx, pattern in enumerate(patterns[:3], 1):  # Show top 3
                metadata = pattern.get('metadata', {})
                file_name = metadata.get('file', 'Unknown')
                logger.debug(f"  Pattern {idx}: {file_name}")

            # Structured logging via SwarmLogger
            self.hub.logger.log_pattern_search(
                agent_name="ExecutionEngine",
                query=task.description,
                patterns_found=patterns,
                task_context=task.id
            )
        else:
            logger.warning(f"⚠️ No documentation patterns found for {task.id}")

        return context

    async def _check_quality(self, result: Dict[str, Any], task, agent) -> bool:
        """
        Check quality of generated files.

        Returns:
            True if quality passes threshold, False otherwise
        """
        # Import quality checker
        from aiapp.utils.quality_checker import QualityChecker
        from aiapp.models.quality import QualityReport

        # Check if any files were created
        files_created = result.get("files", [])
        if not files_created:
            # No files to check
            return True

        # Initialize quality checker
        checker = QualityChecker(
            project_path=self.project_path,
            docs_engine=self.docs
        )

        all_passed = True
        quality_reports = []

        for file_path in files_created:
            try:
                # Check file quality
                report = checker.check_file(file_path)
                quality_reports.append(report)

                # Log quality results
                logger.info(f"📊 Quality check for {file_path}: {report.summary()}")

                # Structured logging
                self.hub.logger.log_manager.log_action(
                    agent_name="QualityChecker",
                    action_type="quality_check",
                    action_description=f"Checked {file_path}",
                    context={
                        "file": file_path,
                        "score": report.overall_score,
                        "passed": report.passed,
                        "issues_count": len(report.issues),
                        "critical_issues": len(report.get_critical_issues())
                    }
                )

                # Log issues if any
                for issue in report.issues:
                    if issue.severity == "critical":
                        logger.error(
                            f"  🔴 CRITICAL: {issue.description} "
                            f"(line {issue.line})" if issue.line else ""
                        )
                    elif issue.severity == "warning":
                        logger.warning(
                            f"  ⚠️  WARNING: {issue.description}"
                        )
                    else:
                        logger.info(f"  ℹ️  INFO: {issue.description}")

                if not report.passed:
                    all_passed = False

            except Exception as e:
                logger.error(f"Error checking quality for {file_path}: {e}")
                all_passed = False

        # Store quality reports in result
        result["quality_reports"] = [
            {
                "file": r.file_path,
                "score": r.overall_score,
                "passed": r.passed,
                "issues": len(r.issues)
            }
            for r in quality_reports
        ]

        return all_passed

    def _collect_files(self) -> List[str]:
        """Collect all created files from task results."""
        files = []
        for result in self.hub.task_results.values():
            if "files" in result:
                files.extend(result["files"])
        return files
