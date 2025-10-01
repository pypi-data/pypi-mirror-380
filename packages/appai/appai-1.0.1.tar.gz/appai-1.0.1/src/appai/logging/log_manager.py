"""Central log manager for AIApp swarm system."""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import defaultdict

logger = logging.getLogger(__name__)


class LogManager:
    """Centralized log manager for all AIApp swarm activities.

    Manages:
    - Agent action logs
    - Agent communication logs
    - Decision-making logs
    - Documentation usage logs
    - Performance metrics
    """

    def __init__(self, log_dir: Optional[Path] = None):
        """Initialize log manager.

        Args:
            log_dir: Directory for log files (default: ./logs/)
        """
        self.log_dir = log_dir or Path("./logs")
        self.log_dir.mkdir(exist_ok=True, parents=True)

        # Session ID for this run
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # In-memory log buffers
        self.agent_actions: List[Dict[str, Any]] = []
        self.agent_communications: List[Dict[str, Any]] = []
        self.agent_decisions: List[Dict[str, Any]] = []
        self.documentation_usage: List[Dict[str, Any]] = []
        self.tool_calls: List[Dict[str, Any]] = []

        # Statistics
        self.stats = {
            "actions_count": 0,
            "messages_count": 0,
            "decisions_count": 0,
            "docs_queries": 0,
            "tool_calls_count": 0,
        }

        logger.info(f"📊 LogManager initialized (session: {self.session_id})")

    # =========================================================================
    # Agent Action Logging
    # =========================================================================

    def log_action(
        self,
        agent_name: str,
        action_type: str,
        action_description: str,
        context: Optional[Dict[str, Any]] = None,
        result: Optional[Any] = None
    ):
        """Log agent action.

        Args:
            agent_name: Name of the agent
            action_type: Type of action (e.g., 'create_file', 'analyze_task', 'execute_tool')
            action_description: Human-readable description
            context: Additional context data
            result: Action result
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "agent": agent_name,
            "action_type": action_type,
            "description": action_description,
            "context": context or {},
            "result": str(result) if result else None
        }

        self.agent_actions.append(entry)
        self.stats["actions_count"] += 1

        # Console output
        logger.info(f"🎯 [{agent_name}] {action_type}: {action_description}")

    # =========================================================================
    # Agent Communication Logging
    # =========================================================================

    def log_communication(
        self,
        from_agent: str,
        to_agent: str,
        message: str,
        message_type: str = "request",
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log inter-agent communication.

        Args:
            from_agent: Sender agent name
            to_agent: Recipient agent name
            message: Message content
            message_type: Type (request, response, info)
            metadata: Additional metadata
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "from": from_agent,
            "to": to_agent,
            "type": message_type,
            "message": message,
            "metadata": metadata or {}
        }

        self.agent_communications.append(entry)
        self.stats["messages_count"] += 1

        # Console output
        icon = "📨" if message_type == "request" else "📬"
        logger.info(f"{icon} {from_agent} → {to_agent}: {message[:100]}...")

    # =========================================================================
    # Decision Logging
    # =========================================================================

    def log_decision(
        self,
        agent_name: str,
        decision_type: str,
        reasoning: str,
        options_considered: Optional[List[str]] = None,
        chosen_option: Optional[str] = None,
        confidence: Optional[float] = None
    ):
        """Log agent decision-making process.

        Args:
            agent_name: Agent making the decision
            decision_type: Type of decision
            reasoning: Why this decision was made
            options_considered: List of options evaluated
            chosen_option: Selected option
            confidence: Confidence score (0-1)
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "agent": agent_name,
            "decision_type": decision_type,
            "reasoning": reasoning,
            "options_considered": options_considered or [],
            "chosen_option": chosen_option,
            "confidence": confidence
        }

        self.agent_decisions.append(entry)
        self.stats["decisions_count"] += 1

        # Console output
        logger.info(
            f"🤔 [{agent_name}] Decision ({decision_type}): "
            f"{chosen_option or 'N/A'} (confidence: {confidence or 'N/A'})"
        )
        logger.debug(f"   Reasoning: {reasoning}")

    # =========================================================================
    # Documentation Usage Logging
    # =========================================================================

    def log_documentation_query(
        self,
        agent_name: str,
        query: str,
        results_count: int,
        patterns_found: Optional[List[str]] = None,
        relevance_scores: Optional[List[float]] = None
    ):
        """Log documentation search by agent.

        Args:
            agent_name: Agent performing search
            query: Search query
            results_count: Number of results returned
            patterns_found: List of patterns found
            relevance_scores: Relevance scores for results
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "agent": agent_name,
            "query": query,
            "results_count": results_count,
            "patterns": patterns_found or [],
            "relevance_scores": relevance_scores or []
        }

        self.documentation_usage.append(entry)
        self.stats["docs_queries"] += 1

        # Console output
        logger.info(
            f"📚 [{agent_name}] Documentation query: \"{query}\" "
            f"→ {results_count} patterns found"
        )

    # =========================================================================
    # Tool Call Logging
    # =========================================================================

    def log_tool_call(
        self,
        agent_name: str,
        tool_name: str,
        tool_args: Dict[str, Any],
        result: Optional[str] = None,
        success: bool = True
    ):
        """Log tool invocation by agent.

        Args:
            agent_name: Agent using the tool
            tool_name: Name of the tool
            tool_args: Tool arguments
            result: Tool execution result
            success: Whether tool call succeeded
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "agent": agent_name,
            "tool": tool_name,
            "args": tool_args,
            "result": result,
            "success": success
        }

        self.tool_calls.append(entry)
        self.stats["tool_calls_count"] += 1

        # Console output
        icon = "🔧" if success else "❌"
        logger.info(f"{icon} [{agent_name}] Tool: {tool_name}")
        logger.debug(f"   Args: {tool_args}")

    # =========================================================================
    # Persistence & Reporting
    # =========================================================================

    def save_logs(self):
        """Save all logs to disk."""
        session_dir = self.log_dir / self.session_id
        session_dir.mkdir(exist_ok=True, parents=True)

        # Save each log type
        logs = {
            "actions": self.agent_actions,
            "communications": self.agent_communications,
            "decisions": self.agent_decisions,
            "documentation": self.documentation_usage,
            "tool_calls": self.tool_calls,
        }

        for log_type, entries in logs.items():
            if entries:
                log_file = session_dir / f"{log_type}.json"
                with open(log_file, "w", encoding="utf-8") as f:
                    json.dump(entries, f, indent=2, ensure_ascii=False)
                logger.info(f"💾 Saved {len(entries)} {log_type} entries to {log_file}")

        # Save statistics
        stats_file = session_dir / "statistics.json"
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(self.stats, f, indent=2)

        logger.info(f"✅ Logs saved to {session_dir}")

    def generate_report(self) -> str:
        """Generate human-readable report of session.

        Returns:
            Formatted report string
        """
        lines = [
            "=" * 70,
            f"AIApp Swarm Execution Report",
            f"Session ID: {self.session_id}",
            "=" * 70,
            "",
            "📊 Statistics:",
            f"  • Actions logged: {self.stats['actions_count']}",
            f"  • Messages exchanged: {self.stats['messages_count']}",
            f"  • Decisions made: {self.stats['decisions_count']}",
            f"  • Documentation queries: {self.stats['docs_queries']}",
            f"  • Tool calls: {self.stats['tool_calls_count']}",
            "",
        ]

        # Agent activity summary
        if self.agent_actions:
            agent_activity = defaultdict(int)
            for action in self.agent_actions:
                agent_activity[action["agent"]] += 1

            lines.append("🤖 Agent Activity:")
            for agent, count in sorted(agent_activity.items(), key=lambda x: -x[1]):
                lines.append(f"  • {agent}: {count} actions")
            lines.append("")

        # Communication summary
        if self.agent_communications:
            comm_pairs = defaultdict(int)
            for comm in self.agent_communications:
                pair = f"{comm['from']} → {comm['to']}"
                comm_pairs[pair] += 1

            lines.append("💬 Communication Flows:")
            for pair, count in sorted(comm_pairs.items(), key=lambda x: -x[1]):
                lines.append(f"  • {pair}: {count} messages")
            lines.append("")

        # Documentation usage summary
        if self.documentation_usage:
            total_patterns = sum(doc["results_count"] for doc in self.documentation_usage)
            lines.append("📚 Documentation Usage:")
            lines.append(f"  • Total queries: {len(self.documentation_usage)}")
            lines.append(f"  • Total patterns found: {total_patterns}")
            lines.append("")

        lines.append("=" * 70)

        return "\n".join(lines)

    def print_report(self):
        """Print report to console."""
        print(self.generate_report())

    # =========================================================================
    # Query & Analysis
    # =========================================================================

    def get_agent_timeline(self, agent_name: str) -> List[Dict[str, Any]]:
        """Get chronological timeline of all events for specific agent.

        Args:
            agent_name: Agent to get timeline for

        Returns:
            List of events in chronological order
        """
        events = []

        # Collect all events for this agent
        for action in self.agent_actions:
            if action["agent"] == agent_name:
                events.append({"type": "action", **action})

        for comm in self.agent_communications:
            if comm["from"] == agent_name or comm["to"] == agent_name:
                events.append({"type": "communication", **comm})

        for decision in self.agent_decisions:
            if decision["agent"] == agent_name:
                events.append({"type": "decision", **decision})

        for doc_query in self.documentation_usage:
            if doc_query["agent"] == agent_name:
                events.append({"type": "documentation", **doc_query})

        for tool_call in self.tool_calls:
            if tool_call["agent"] == agent_name:
                events.append({"type": "tool_call", **tool_call})

        # Sort chronologically
        events.sort(key=lambda x: x["timestamp"])

        return events

    def get_communication_graph(self) -> Dict[str, List[str]]:
        """Get directed graph of agent communications.

        Returns:
            Dict mapping agent -> list of agents they communicated with
        """
        graph = defaultdict(list)

        for comm in self.agent_communications:
            from_agent = comm["from"]
            to_agent = comm["to"]
            if to_agent not in graph[from_agent]:
                graph[from_agent].append(to_agent)

        return dict(graph)
