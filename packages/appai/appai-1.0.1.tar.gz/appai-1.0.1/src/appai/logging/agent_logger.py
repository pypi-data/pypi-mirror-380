"""Agent-level logging wrapper for tracking agent behavior."""

import logging
from typing import Dict, Any, Optional
from functools import wraps

logger = logging.getLogger(__name__)


class AgentLogger:
    """Wrapper for logging agent-specific activities.

    Provides decorators and methods to log:
    - Agent actions
    - Tool usage
    - Decision making
    - Documentation queries
    """

    def __init__(self, agent_name: str, log_manager):
        """Initialize agent logger.

        Args:
            agent_name: Name of the agent
            log_manager: Reference to LogManager instance
        """
        self.agent_name = agent_name
        self.log_manager = log_manager

    # =========================================================================
    # Action Logging
    # =========================================================================

    def log_action(
        self,
        action_type: str,
        description: str,
        context: Optional[Dict[str, Any]] = None,
        result: Optional[Any] = None
    ):
        """Log an action performed by this agent.

        Args:
            action_type: Type of action
            description: Description of action
            context: Additional context
            result: Action result
        """
        self.log_manager.log_action(
            agent_name=self.agent_name,
            action_type=action_type,
            action_description=description,
            context=context,
            result=result
        )

    def action(self, action_type: str, description: Optional[str] = None):
        """Decorator to log function calls as actions.

        Args:
            action_type: Type of action
            description: Optional description (uses function name if not provided)

        Example:
            @agent_logger.action("file_creation", "Creating Django model file")
            def create_model_file(self, path, content):
                ...
        """
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                desc = description or f"{func.__name__}({', '.join(map(str, args[:2]))})"
                self.log_action(action_type, desc, context={"args": str(args[:2])})

                try:
                    result = await func(*args, **kwargs)
                    self.log_action(
                        action_type,
                        f"{desc} - Success",
                        result=str(result)[:200]
                    )
                    return result
                except Exception as e:
                    self.log_action(
                        action_type,
                        f"{desc} - Failed",
                        result=f"Error: {str(e)}"
                    )
                    raise

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                desc = description or f"{func.__name__}({', '.join(map(str, args[:2]))})"
                self.log_action(action_type, desc, context={"args": str(args[:2])})

                try:
                    result = func(*args, **kwargs)
                    self.log_action(
                        action_type,
                        f"{desc} - Success",
                        result=str(result)[:200]
                    )
                    return result
                except Exception as e:
                    self.log_action(
                        action_type,
                        f"{desc} - Failed",
                        result=f"Error: {str(e)}"
                    )
                    raise

            # Return appropriate wrapper based on function type
            import asyncio
            if asyncio.iscoroutinefunction(func):
                return async_wrapper
            else:
                return sync_wrapper

        return decorator

    # =========================================================================
    # Communication Logging
    # =========================================================================

    def log_send_message(
        self,
        recipient: str,
        message: str,
        message_type: str = "request",
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log a message sent to another agent.

        Args:
            recipient: Recipient agent name
            message: Message content
            message_type: Type of message
            metadata: Additional metadata
        """
        self.log_manager.log_communication(
            from_agent=self.agent_name,
            to_agent=recipient,
            message=message,
            message_type=message_type,
            metadata=metadata
        )

    def log_receive_message(
        self,
        sender: str,
        message: str,
        message_type: str = "request",
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Log a message received from another agent.

        Args:
            sender: Sender agent name
            message: Message content
            message_type: Type of message
            metadata: Additional metadata
        """
        self.log_manager.log_communication(
            from_agent=sender,
            to_agent=self.agent_name,
            message=message,
            message_type=message_type,
            metadata=metadata
        )

    # =========================================================================
    # Decision Logging
    # =========================================================================

    def log_decision(
        self,
        decision_type: str,
        reasoning: str,
        options_considered: Optional[list] = None,
        chosen_option: Optional[str] = None,
        confidence: Optional[float] = None
    ):
        """Log a decision made by this agent.

        Args:
            decision_type: Type of decision
            reasoning: Reasoning behind decision
            options_considered: Options that were considered
            chosen_option: Selected option
            confidence: Confidence level (0-1)
        """
        self.log_manager.log_decision(
            agent_name=self.agent_name,
            decision_type=decision_type,
            reasoning=reasoning,
            options_considered=options_considered,
            chosen_option=chosen_option,
            confidence=confidence
        )

    # =========================================================================
    # Documentation Usage
    # =========================================================================

    def log_doc_query(
        self,
        query: str,
        results_count: int,
        patterns_found: Optional[list] = None,
        relevance_scores: Optional[list] = None
    ):
        """Log a documentation query.

        Args:
            query: Search query
            results_count: Number of results
            patterns_found: List of patterns found
            relevance_scores: Relevance scores
        """
        self.log_manager.log_documentation_query(
            agent_name=self.agent_name,
            query=query,
            results_count=results_count,
            patterns_found=patterns_found,
            relevance_scores=relevance_scores
        )

    # =========================================================================
    # Tool Logging
    # =========================================================================

    def log_tool(
        self,
        tool_name: str,
        tool_args: Dict[str, Any],
        result: Optional[str] = None,
        success: bool = True
    ):
        """Log a tool invocation.

        Args:
            tool_name: Name of the tool
            tool_args: Tool arguments
            result: Tool result
            success: Whether tool succeeded
        """
        self.log_manager.log_tool_call(
            agent_name=self.agent_name,
            tool_name=tool_name,
            tool_args=tool_args,
            result=result,
            success=success
        )

    def tool_call(self, tool_name: str):
        """Decorator to log tool calls.

        Args:
            tool_name: Name of the tool

        Example:
            @agent_logger.tool_call("file_writer")
            def write_file(self, path, content):
                ...
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Extract kwargs for logging
                tool_args = {k: str(v)[:100] for k, v in kwargs.items()}

                try:
                    result = func(*args, **kwargs)
                    self.log_tool(
                        tool_name=tool_name,
                        tool_args=tool_args,
                        result=str(result)[:200],
                        success=True
                    )
                    return result
                except Exception as e:
                    self.log_tool(
                        tool_name=tool_name,
                        tool_args=tool_args,
                        result=f"Error: {str(e)}",
                        success=False
                    )
                    raise

            return wrapper
        return decorator
