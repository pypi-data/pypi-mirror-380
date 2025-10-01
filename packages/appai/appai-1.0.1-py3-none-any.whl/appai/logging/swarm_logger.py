"""Swarm-level logger for coordinating multi-agent logging."""

import logging
from typing import Dict, List, Optional
from pathlib import Path

from aiapp.logging.log_manager import LogManager
from aiapp.logging.agent_logger import AgentLogger

logger = logging.getLogger(__name__)


class SwarmLogger:
    """Central coordinator for all swarm logging activities.

    Manages:
    - Individual agent loggers
    - Cross-agent event tracking
    - Session-wide statistics
    - Log persistence and reporting
    """

    def __init__(self, log_dir: Optional[Path] = None):
        """Initialize swarm logger.

        Args:
            log_dir: Directory for log files
        """
        self.log_manager = LogManager(log_dir=log_dir)
        self.agent_loggers: Dict[str, AgentLogger] = {}

        logger.info(f"🐝 SwarmLogger initialized (session: {self.log_manager.session_id})")

    def get_agent_logger(self, agent_name: str) -> AgentLogger:
        """Get or create logger for specific agent.

        Args:
            agent_name: Name of the agent

        Returns:
            AgentLogger instance for this agent
        """
        if agent_name not in self.agent_loggers:
            self.agent_loggers[agent_name] = AgentLogger(
                agent_name=agent_name,
                log_manager=self.log_manager
            )
            logger.debug(f"Created logger for agent: {agent_name}")

        return self.agent_loggers[agent_name]

    # =========================================================================
    # Swarm-Level Events
    # =========================================================================

    def log_swarm_start(self, task_description: str, num_agents: int, num_tasks: int):
        """Log start of swarm execution.

        Args:
            task_description: Main task description
            num_agents: Number of agents in swarm
            num_tasks: Number of subtasks
        """
        logger.info("=" * 70)
        logger.info(f"🚀 SWARM EXECUTION STARTED")
        logger.info(f"   Task: {task_description}")
        logger.info(f"   Agents: {num_agents}")
        logger.info(f"   Subtasks: {num_tasks}")
        logger.info(f"   Session: {self.log_manager.session_id}")
        logger.info("=" * 70)

        self.log_manager.log_action(
            agent_name="SwarmCoordinator",
            action_type="swarm_start",
            action_description=f"Starting swarm: {task_description}",
            context={
                "num_agents": num_agents,
                "num_tasks": num_tasks,
                "task": task_description
            }
        )

    def log_swarm_end(self, success: bool, completed_tasks: int, failed_tasks: int):
        """Log end of swarm execution.

        Args:
            success: Whether swarm succeeded
            completed_tasks: Number of completed tasks
            failed_tasks: Number of failed tasks
        """
        status = "✅ SUCCESS" if success else "❌ FAILED"
        logger.info("=" * 70)
        logger.info(f"{status} - SWARM EXECUTION FINISHED")
        logger.info(f"   Completed: {completed_tasks} tasks")
        logger.info(f"   Failed: {failed_tasks} tasks")
        logger.info("=" * 70)

        self.log_manager.log_action(
            agent_name="SwarmCoordinator",
            action_type="swarm_end",
            action_description=f"Swarm finished: {status}",
            context={
                "success": success,
                "completed": completed_tasks,
                "failed": failed_tasks
            }
        )

    def log_wave_start(self, wave_number: int, total_waves: int, task_count: int):
        """Log start of execution wave.

        Args:
            wave_number: Current wave number (1-indexed)
            total_waves: Total number of waves
            task_count: Number of tasks in this wave
        """
        logger.info("")
        logger.info(f"🌊 WAVE {wave_number}/{total_waves}")
        logger.info(f"   Tasks: {task_count} (parallel execution)")
        logger.info("")

        self.log_manager.log_action(
            agent_name="SwarmCoordinator",
            action_type="wave_start",
            action_description=f"Starting wave {wave_number}/{total_waves}",
            context={
                "wave": wave_number,
                "total_waves": total_waves,
                "task_count": task_count
            }
        )

    def log_wave_end(self, wave_number: int, completed: int, failed: int):
        """Log end of execution wave.

        Args:
            wave_number: Wave number
            completed: Completed tasks in wave
            failed: Failed tasks in wave
        """
        logger.info(f"✅ Wave {wave_number} completed: {completed} succeeded, {failed} failed")

        self.log_manager.log_action(
            agent_name="SwarmCoordinator",
            action_type="wave_end",
            action_description=f"Wave {wave_number} finished",
            context={
                "wave": wave_number,
                "completed": completed,
                "failed": failed
            }
        )

    def log_task_assignment(self, task_id: str, agent_name: str, task_description: str):
        """Log task assignment to agent.

        Args:
            task_id: Task identifier
            agent_name: Agent assigned to task
            task_description: Task description
        """
        logger.info(f"📋 Task Assignment: {task_id} → {agent_name}")
        logger.debug(f"   Description: {task_description}")

        self.log_manager.log_action(
            agent_name="SwarmCoordinator",
            action_type="task_assignment",
            action_description=f"Assigned {task_id} to {agent_name}",
            context={
                "task_id": task_id,
                "agent": agent_name,
                "description": task_description
            }
        )

    # =========================================================================
    # Documentation Usage Tracking
    # =========================================================================

    def log_pattern_search(
        self,
        agent_name: str,
        query: str,
        patterns_found: List[Dict],
        task_context: Optional[str] = None
    ):
        """Log documentation pattern search.

        Args:
            agent_name: Agent performing search
            query: Search query
            patterns_found: List of found patterns with metadata
            task_context: Context/reason for search
        """
        relevance_scores = [p.get("score", 0.0) for p in patterns_found]
        pattern_names = [p.get("content", "")[:50] for p in patterns_found]

        agent_logger = self.get_agent_logger(agent_name)
        agent_logger.log_doc_query(
            query=query,
            results_count=len(patterns_found),
            patterns_found=pattern_names,
            relevance_scores=relevance_scores
        )

        logger.info(f"📚 [{agent_name}] Found {len(patterns_found)} patterns for: \"{query}\"")
        if patterns_found:
            logger.debug(f"   Top pattern score: {max(relevance_scores):.3f}")

    # =========================================================================
    # Inter-Agent Communication
    # =========================================================================

    def log_agent_message(
        self,
        from_agent: str,
        to_agent: str,
        message: str,
        message_type: str = "request"
    ):
        """Log message between agents.

        Args:
            from_agent: Sender agent
            to_agent: Recipient agent
            message: Message content
            message_type: Type of message
        """
        from_logger = self.get_agent_logger(from_agent)
        from_logger.log_send_message(
            recipient=to_agent,
            message=message,
            message_type=message_type
        )

        logger.info(f"💬 {from_agent} → {to_agent}: {message[:80]}...")

    # =========================================================================
    # Reporting & Persistence
    # =========================================================================

    def save_logs(self):
        """Save all logs to disk."""
        self.log_manager.save_logs()
        logger.info(f"💾 All logs saved to: {self.log_manager.log_dir / self.log_manager.session_id}")

    def print_report(self):
        """Print execution report to console."""
        self.log_manager.print_report()

    def get_report(self) -> str:
        """Get execution report as string.

        Returns:
            Formatted report
        """
        return self.log_manager.generate_report()

    def get_agent_timeline(self, agent_name: str) -> List[Dict]:
        """Get chronological timeline for specific agent.

        Args:
            agent_name: Agent name

        Returns:
            List of events in chronological order
        """
        return self.log_manager.get_agent_timeline(agent_name)

    def get_communication_graph(self) -> Dict[str, List[str]]:
        """Get agent communication graph.

        Returns:
            Dict mapping agent -> list of agents they communicated with
        """
        return self.log_manager.get_communication_graph()

    # =========================================================================
    # Statistics
    # =========================================================================

    def get_statistics(self) -> Dict:
        """Get current session statistics.

        Returns:
            Statistics dictionary
        """
        return self.log_manager.stats.copy()
