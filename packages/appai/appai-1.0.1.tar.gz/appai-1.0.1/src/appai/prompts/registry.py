"""Framework prompt builder registry with agent-driven selection."""

from typing import Dict, Type, List, Optional, Any
import logging

logger = logging.getLogger(__name__)


class PromptBuilderRegistry:
    """
    Registry for framework-specific prompt builders.

    Allows:
    - Automatic registration of prompt builders
    - Agent-driven selection of prompt sections
    - Framework-agnostic prompt building
    """

    _builders: Dict[str, Type] = {}

    @classmethod
    def register(cls, framework: str):
        """
        Decorator to register a prompt builder for a framework.

        Usage:
            @PromptBuilderRegistry.register('django')
            class DjangoPromptBuilder:
                ...
        """
        def decorator(builder_class):
            cls._builders[framework.lower()] = builder_class
            logger.debug(f"📋 Registered prompt builder: {framework} -> {builder_class.__name__}")
            return builder_class
        return decorator

    @classmethod
    def get_builder(cls, framework: str) -> Optional[Type]:
        """Get prompt builder for a framework."""
        return cls._builders.get(framework.lower())

    @classmethod
    def has_builder(cls, framework: str) -> bool:
        """Check if builder exists for framework."""
        return framework.lower() in cls._builders

    @classmethod
    def list_frameworks(cls) -> List[str]:
        """List all registered frameworks."""
        return list(cls._builders.keys())


class AgentPromptSelector:
    """
    Agent-driven prompt section selection.

    Agents can specify which sections they need based on:
    - Task category (model, api, admin, etc.)
    - Agent capabilities
    - Task context
    """

    # Agent-specific section preferences
    AGENT_SECTION_PREFERENCES = {
        "ModelArchitect": {
            "model": ["cross_app_imports", "relationships", "best_practices", "app_structure"],
            "admin": ["best_practices"],
            "default": ["best_practices"]
        },
        "APIBuilder": {
            "api": ["cross_app_imports", "relationships"],
            "serializer": ["cross_app_imports", "relationships"],
            "default": ["cross_app_imports"]
        },
        "QualityGuard": {
            "tests": ["best_practices"],
            "default": []
        }
    }

    @classmethod
    def select_sections(
        cls,
        agent_name: str,
        task_category: str,
        has_created_models: bool = False
    ) -> List[str]:
        """
        Agent decides which prompt sections to include.

        Args:
            agent_name: Name of the agent (e.g., "ModelArchitect")
            task_category: Task category (e.g., "model", "api")
            has_created_models: Whether there are previously created models

        Returns:
            List of section names to include
        """
        # Get agent preferences
        agent_prefs = cls.AGENT_SECTION_PREFERENCES.get(agent_name, {})

        # Get sections for this task category
        sections = agent_prefs.get(task_category, agent_prefs.get("default", []))

        # Always include cross_app_imports if models exist
        if has_created_models and "cross_app_imports" not in sections:
            sections = ["cross_app_imports"] + sections

        logger.debug(
            f"🎯 {agent_name} selected sections for {task_category}: {sections}"
        )

        return sections

    @classmethod
    def build_prompt_for_agent(
        cls,
        framework: str,
        agent_name: str,
        task_category: str,
        context: Dict[str, Any]
    ) -> str:
        """
        Build framework-specific prompt based on agent selection.

        Args:
            framework: Framework name (e.g., "django")
            agent_name: Agent name
            task_category: Task category
            context: Task context with shared_knowledge, etc.

        Returns:
            Formatted prompt sections
        """
        # Get builder for framework
        builder_class = PromptBuilderRegistry.get_builder(framework)
        if not builder_class:
            logger.warning(f"No prompt builder for framework: {framework}")
            return ""

        # Check if we have created models
        created_models = context.get('shared_knowledge', {}).get('created_models', [])
        has_models = len(created_models) > 0

        # Agent selects which sections to include
        sections = cls.select_sections(agent_name, task_category, has_models)

        if not sections:
            return ""

        # Build prompt using selected sections
        if hasattr(builder_class, 'build_selected_sections'):
            return builder_class.build_selected_sections(
                sections=sections,
                task_category=task_category,
                created_models=created_models
            )
        else:
            # Fallback to full guidelines
            logger.warning(
                f"{builder_class.__name__} doesn't support section selection, "
                f"using build_django_guidelines"
            )
            return builder_class.build_django_guidelines(
                task_category=task_category,
                created_models=created_models
            )


# Convenience function for agent_pool.py
def build_framework_prompt(
    framework: str,
    agent_name: str,
    task_category: str,
    context: Dict[str, Any]
) -> str:
    """
    Main entry point for building framework-specific prompts.

    This function:
    1. Checks if builder exists for framework
    2. Lets agent select relevant sections
    3. Builds prompt with selected sections

    Usage in agent_pool.py:
        from aiapp.prompts.registry import build_framework_prompt

        prompt = build_framework_prompt(
            framework=self.docs.framework,
            agent_name=self.profile.name,
            task_category=subtask.category,
            context=context
        )
    """
    return AgentPromptSelector.build_prompt_for_agent(
        framework=framework,
        agent_name=agent_name,
        task_category=task_category,
        context=context
    )
