"""Agent pool with specialized agents and capability-based selection."""

import os
import time
import logging
from typing import Dict, Set, Any, TYPE_CHECKING
from pathlib import Path

from openai import AsyncOpenAI
from agency_swarm import Agent, OpenAIChatCompletionsModel

from aiapp.agents.capabilities import AgentCapability
from aiapp.models import AgentProfile, SubTask
from aiapp.tools import SearchDocumentation
from aiapp.utils.ai_code_extractor import AICodeExtractor

if TYPE_CHECKING:
    from aiapp.core import DocumentationEngine

logger = logging.getLogger(__name__)


class SpecializedAgent:
    """Agent with specific capabilities and performance tracking."""

    def __init__(
        self,
        profile: AgentProfile,
        docs_engine: "DocumentationEngine",
        mcp_server,
        project_path: Path = None,
        swarm_logger=None
    ):
        self.profile = profile
        self.docs = docs_engine
        self.mcp_server = mcp_server
        self.project_path = project_path or Path.cwd()
        self.swarm_logger = swarm_logger

        # Create AgentLogger for structured logging
        if swarm_logger:
            self.agent_logger = swarm_logger.get_agent_logger(profile.name)
        else:
            self.agent_logger = None

        self.agent = self._create_agent()

        # AI-powered code extractor (uses cheap model)
        api_key = os.getenv("OPENROUTER_API_KEY")
        self.ai_extractor = AICodeExtractor(api_key) if api_key else None

    def _create_agent(self) -> Agent:
        """Create Agency Swarm agent with configuration."""
        instructions = self._build_instructions()
        model = self._get_model()

        return Agent(
            name=self.profile.name,
            instructions=instructions,
            tools=[SearchDocumentation],  # Add documentation search tool
            mcp_servers=[self.mcp_server] if self.mcp_server else [],
            model=model
        )

    def _build_instructions(self) -> str:
        """Build capability-specific instructions with documentation context."""
        capabilities_text = "\n".join(
            f"- {cap.value if hasattr(cap, 'value') else cap}" for cap in self.profile.capabilities
        )

        # Get documentation context (specialization-specific)
        docs_context = ""
        if self.docs:
            # Get patterns relevant to agent's specialization
            spec_query = f"Django {self.profile.specialization} patterns examples"
            patterns = self.docs.search_patterns(spec_query, category=None, top_k=3)

            if patterns:
                docs_context = f"\n\n## 📚 Django Documentation Patterns\n"
                docs_context += f"**Relevant to your specialization ({self.profile.specialization}):**\n\n"

                for idx, pattern in enumerate(patterns, 1):
                    metadata = pattern.get('metadata', {})
                    file_name = metadata.get('file', 'Unknown')
                    docs_context += f"\n### Example {idx} (from {file_name})\n"
                    docs_context += f"{pattern.get('content', '')}\n"
                    docs_context += "---\n"

        return f"""You are {self.profile.name}, specialized in {self.profile.specialization}.

## Your Capabilities
{capabilities_text}
{docs_context}

## ⚡ MANDATORY ACTION PROTOCOL

**YOU MUST USE TOOLS TO CREATE FILES. TEXT RESPONSES ARE NOT ACCEPTABLE.**

When given a task, you MUST:

1. **IF UNCERTAIN** → Use SearchDocumentation tool to find patterns
2. **ALWAYS** → Use write_file tool to create files
3. **NEVER** → Just describe what you would do

## 🛠️ Tool Usage Examples

### Creating a Django Model (CORRECT):
```
STEP 1: Use write_file tool
write_file(
  path="myapp/models.py",
  content='''from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
'''
)
```

### What NOT to do (WRONG):
```
❌ "I will create a models.py file with Post model..."
❌ "Here's the code you should add..."
❌ Explaining without using tools
```

## 🔥 CRITICAL RULES

1. **TOOL CALLS ONLY** - Every response must include tool calls
2. **write_file for all files** - Use the tool, don't explain
3. **CREATE, DON'T DESCRIBE** - Action over words
4. **NO EXPLANATIONS WITHOUT ACTIONS** - Tools first, context later

## 📋 Available MCP Tools (YOU MUST USE THESE):

- **write_file(path: str, content: str)** - Create or update a file
  Example: write_file(path="app/models.py", content="from django...")

- **create_directory(path: str)** - Create a directory
  Example: create_directory(path="blog_app")

- **read_file(path: str)** - Read existing file
  Example: read_file(path="app/settings.py")

## 📚 Documentation Tool (Optional):

- **SearchDocumentation(query, framework, top_k)** - Find code patterns
  Example: SearchDocumentation(query="Django ForeignKey", framework="django", top_k=3)

## ⚠️ REMEMBER

Your job is to CREATE FILES using tools, not to explain how to create them.
Use write_file tool immediately. No explanations first.
Think → Tool Call → Done.

You are part of a swarm. Execute autonomously."""

    def _get_model(self) -> OpenAIChatCompletionsModel:
        """Get OpenRouter model configuration."""
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable not set")

        client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        return OpenAIChatCompletionsModel(
            model=self.profile.model_name,
            openai_client=client
        )

    def can_handle(self, subtask: SubTask) -> float:
        """
        Calculate confidence score for handling task.

        Score components:
        - 50% capability match
        - 30% specialization match
        - 20% historical performance

        Returns:
            Confidence score (0-1)
        """
        confidence = 0.0
        breakdown = []  # For debug logging

        # 1. Capability match (50% weight)
        required_caps = self._map_category_to_caps(subtask.category)
        if required_caps:
            matching = len(required_caps & self.profile.capabilities)
            total = len(required_caps)
            cap_score = (matching / total) * 0.5
            confidence += cap_score
            breakdown.append(f"cap:{cap_score:.2f}({matching}/{total})")
        else:
            # Unknown category - base confidence on agent versatility
            confidence += 0.3  # Moderate confidence for unknown tasks
            breakdown.append("cap:0.30(unknown)")

        # 2. Specialization match (30% weight)
        if subtask.category in self.profile.specialization:
            confidence += 0.3
            breakdown.append("spec:0.30")
        elif subtask.category == "general":
            # General tasks - agents can handle
            confidence += 0.2
            breakdown.append("spec:0.20(gen)")
        else:
            breakdown.append("spec:0.00")

        # 3. Historical performance (20% weight)
        similar_tasks = [
            t for t in self.profile.performance_history
            if t.get("category") == subtask.category
        ]
        if similar_tasks:
            recent = similar_tasks[-10:]  # Last 10 similar tasks
            avg_success = sum(t.get("success", 0) for t in recent) / len(recent)
            hist_score = avg_success * 0.2
            confidence += hist_score
            breakdown.append(f"hist:{hist_score:.2f}")
        else:
            # No history - add baseline confidence
            confidence += 0.1
            breakdown.append("hist:0.10")

        final_confidence = min(confidence, 1.0)

        # Debug logging
        logger.info(
            f"🎯 {self.profile.name} evaluating {subtask.id} ({subtask.category}): "
            f"{' + '.join(breakdown)} = {final_confidence:.2f}"
        )

        # Structured logging for bidding decisions
        if self.agent_logger:
            self.agent_logger.log_decision(
                decision_type="task_bidding",
                reasoning=f"Confidence: {' + '.join(breakdown)}",
                chosen_option=f"bid_{final_confidence:.2f}" if final_confidence >= 0.3 else "decline",
                confidence=final_confidence
            )

        return final_confidence

    def _map_category_to_caps(self, category: str) -> Set[str]:
        """Map task category to required capabilities."""
        mapping = {
            "model": {AgentCapability.DJANGO_MODELS, AgentCapability.DATABASE_DESIGN},
            "viewset": {AgentCapability.DRF_VIEWSETS, AgentCapability.DJANGO_VIEWS},
            "serializer": {AgentCapability.DRF_SERIALIZERS},
            "admin": {AgentCapability.DJANGO_ADMIN},
            "forms": {AgentCapability.DJANGO_FORMS},
            "tests": {AgentCapability.TESTING},
            "review": {AgentCapability.CODE_REVIEW},
            "optimize": {AgentCapability.OPTIMIZATION},
        }
        return mapping.get(category, set())

    async def execute_task(self, subtask: SubTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task with this agent."""
        # Build prompt
        prompt = self._build_task_prompt(subtask, context)

        # Execute
        start_time = time.time()
        response = await self.agent.get_response(prompt)
        execution_time = time.time() - start_time

        # Parse result (async)
        result = await self._parse_response_async(response, subtask)
        result["execution_time"] = execution_time
        result["agent"] = self.profile.name

        # Update performance
        self._update_performance(subtask, result)

        return result

    def _build_task_prompt(self, subtask: SubTask, context: Dict[str, Any]) -> str:
        """Build task-specific prompt with context."""
        sections = []

        sections.append(f"# Task: {subtask.description}")
        sections.append(f"\n**Category**: {subtask.category}")
        sections.append(f"**Complexity**: {subtask.estimated_complexity.value}")
        sections.append(f"**Files to create**: {', '.join(subtask.files_to_create)}")

        # Patterns from context (documentation)
        if "patterns" in context and context["patterns"]:
            patterns = context["patterns"]

            # Log pattern usage
            logger.info(
                f"📚 [{self.profile.name}] Adding {len(patterns)} documentation patterns to prompt for {subtask.id}"
            )
            for idx, pattern in enumerate(patterns, 1):
                metadata = pattern.get('metadata', {})
                file_name = metadata.get('file', 'Unknown')
                score = pattern.get('score', 0.0)
                logger.info(f"  Pattern {idx}: {file_name} (score: {score:.2f})")

            # Structured logging
            if self.agent_logger:
                self.agent_logger.log_doc_query(
                    query=subtask.description,
                    results_count=len(patterns),
                    patterns_found=[p.get('metadata', {}).get('file', 'Unknown') for p in patterns],
                    relevance_scores=[p.get('score', 0.0) for p in patterns]
                )

            sections.append("\n## Relevant Documentation Patterns")
            sections.append("\n**Use these patterns from Django documentation:**\n")
            for idx, pattern in enumerate(patterns, 1):
                # Extract metadata
                metadata = pattern.get('metadata', {})
                file_name = metadata.get('file', 'Unknown')
                source = metadata.get('source', 'unknown')
                score = pattern.get('score', 0.0)

                # Add pattern with context
                sections.append(f"\n### Pattern {idx} (from {file_name}, relevance: {score:.2f})")
                sections.append(f"**Source**: {source}")
                sections.append(f"\n{pattern.get('content', '')}\n")
                sections.append("---")

            # Explicit instructions to use patterns
            sections.append("\n" + "!" * 70)
            sections.append("\n⚠️  MANDATORY: YOU MUST FOLLOW THE DOCUMENTATION PATTERNS ABOVE")
            sections.append("\n")
            sections.append("\n📋 Required Actions:")
            sections.append("\n  1. Study EACH pattern carefully before coding")
            sections.append("\n  2. Apply best practices from the patterns to your code")
            sections.append("\n  3. Use similar code structure and naming conventions")
            sections.append("\n  4. Reference pattern numbers in your response (e.g., 'Following Pattern 1...')")
            sections.append("\n  5. If patterns are not sufficient, use SearchDocumentation tool for more specific guidance")
            sections.append("\n")
            sections.append("\n✅ Examples from patterns you MUST follow:")
            sections.append("\n  - Use ForeignKey with related_name parameter")
            sections.append("\n  - Add __str__ methods to all models")
            sections.append("\n  - Include created_at/updated_at timestamps")
            sections.append("\n  - Follow Django REST framework serializer patterns")
            sections.append("\n")
            sections.append("!" * 70)
        else:
            logger.warning(
                f"⚠️ [{self.profile.name}] No documentation patterns in context for {subtask.id}"
            )

        # Dependencies
        if "dependency_results" in context:
            sections.append("\n## Dependency Results")
            for dep_id, result in context["dependency_results"].items():
                sections.append(f"- {dep_id}: {result.get('summary', 'completed')}")

        # Shared knowledge
        if "shared_knowledge" in context:
            knowledge = context["shared_knowledge"]
            if knowledge.get("created_models"):
                sections.append("\n## 🔗 Previously Created Models - MUST USE FOR RELATIONSHIPS!")
                sections.append("")
                sections.append("**⚠️ CRITICAL: If your model needs a ForeignKey/ManyToMany to these models:**")
                sections.append("**YOU MUST ADD IMPORT AT THE TOP OF YOUR FILE!**")
                sections.append("")
                sections.append("Available models:")
                for model in knowledge["created_models"]:
                    name = model.get('name', 'Unknown')
                    app = model.get('app', 'unknown')
                    file = model.get('file', 'unknown')
                    import_path = model.get('import_path', f'{app}.models')
                    sections.append(f"  • **{name}** - located in `{file}`")

                sections.append("")
                sections.append("**Example: If you need to reference Author model:**")
                sections.append("```python")
                sections.append("from django.db import models")
                sections.append("from authors.models import Author  # ← IMPORT FROM OTHER APP!")
                sections.append("")
                sections.append("class Post(models.Model):")
                sections.append("    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')")
                sections.append("    # ...")
                sections.append("```")
                sections.append("")
                sections.append("**DO NOT use string references like ForeignKey('Author')!**")
                sections.append("**ALWAYS import the model class and use it directly!**")

        # Framework-specific guidelines (agent-driven selection)
        if hasattr(self, 'docs') and self.docs:
            framework = getattr(self.docs, 'framework', None)
            if framework:
                from aiapp.prompts.registry import build_framework_prompt

                # Agent selects and builds relevant prompt sections
                framework_prompt = build_framework_prompt(
                    framework=framework,
                    agent_name=self.profile.name,
                    task_category=subtask.category,
                    context=context
                )

                if framework_prompt:
                    sections.append(framework_prompt)

        # Acceptance criteria
        sections.append("\n## Acceptance Criteria")
        for criterion in subtask.acceptance_criteria:
            sections.append(f"- [ ] {criterion}")

        # MANDATORY action instructions
        sections.append("\n" + "=" * 60)
        sections.append("## ⚡ MANDATORY ACTIONS - EXECUTE IMMEDIATELY")
        sections.append("=" * 60)
        sections.append("")
        sections.append("**YOU MUST PERFORM THESE ACTIONS RIGHT NOW:**")
        sections.append("")

        if subtask.files_to_create:
            sections.append("### FILES TO CREATE (Use write_file tool for EACH):")
            for file_path in subtask.files_to_create:
                sections.append(f"")
                sections.append(f"**File: {file_path}**")
                sections.append(f"```")
                sections.append(f"write_file(")
                sections.append(f'  path="{file_path}",')
                sections.append(f"  content='''<YOUR CODE HERE>'''")
                sections.append(f")")
                sections.append(f"```")
        else:
            sections.append("### CREATE APPROPRIATE FILES:")
            sections.append("1. Analyze the task requirements")
            sections.append("2. Determine which files are needed")
            sections.append("3. Use write_file tool for EACH file")
            sections.append("")
            sections.append("Example:")
            sections.append("```")
            sections.append('write_file(path="myapp/models.py", content="""')
            sections.append("from django.db import models")
            sections.append("# Your code here")
            sections.append('""")')
            sections.append("```")

        sections.append("")
        sections.append("## ❌ WHAT NOT TO DO:")
        sections.append("- ❌ Do NOT write explanations without tool calls")
        sections.append("- ❌ Do NOT say 'I will create...' or 'Here's the code...'")
        sections.append("- ❌ Do NOT provide code snippets in text")
        sections.append("")
        sections.append("## ✅ WHAT TO DO:")
        sections.append("- ✅ Call write_file tool immediately")
        sections.append("- ✅ Include complete, runnable code")
        sections.append("- ✅ Follow documentation patterns above")
        sections.append("- ✅ Create ALL required files")
        sections.append("")
        sections.append("=" * 60)
        sections.append("START NOW! Use write_file tool!")
        sections.append("=" * 60)

        return "\n".join(sections)

    async def _parse_response_async(self, response: Any, subtask: SubTask) -> Dict[str, Any]:
        """
        Parse agent response into structured result (async).

        If agent didn't use MCP tools, extract code from text response using AI.
        """
        response_text = str(response)
        created_files = []

        # Check if response contains code blocks
        if '```' in response_text or 'class ' in response_text or 'def ' in response_text:
            logger.info(f"Agent {self.profile.name} returned text response, using AI extraction...")

            if self.ai_extractor:
                # AI extraction with retries
                extraction = await self.ai_extractor.extract_with_retry(
                    response_text,
                    task_category=subtask.category,
                    expected_files=subtask.files_to_create,
                    max_retries=2
                )

                if extraction.has_code:
                    logger.info(
                        f"🤖 AI extracted {len(extraction.files)} files "
                        f"(confidence: {extraction.extraction_confidence:.2f})"
                    )

                    # Write extracted files
                    for extracted_file in extraction.files:
                        try:
                            self._write_file_fallback(
                                extracted_file.file_path,
                                extracted_file.content
                            )
                            created_files.append(extracted_file.file_path)
                            logger.info(
                                f"✅ Saved {extracted_file.file_path} "
                                f"({len(extracted_file.content)} chars) - {extracted_file.description}"
                            )

                            # Structured logging
                            if self.agent_logger:
                                self.agent_logger.log_action(
                                    action_type="file_created",
                                    description=f"Created {extracted_file.file_path}",
                                    context={
                                        "file": extracted_file.file_path,
                                        "size": len(extracted_file.content),
                                        "description": extracted_file.description,
                                        "extraction_method": "AI"
                                    }
                                )
                        except Exception as e:
                            logger.error(f"❌ Failed to write {extracted_file.file_path}: {e}")
            else:
                logger.warning("AI extractor not available (no API key)")

        return {
            "task_id": subtask.id,
            "success": len(created_files) > 0 or 'successfully' in response_text.lower(),
            "files": created_files,
            "summary": response_text[:200] if len(response_text) > 200 else response_text,
            "full_response": response_text,
        }

    def _parse_response(self, response: Any, subtask: SubTask) -> Dict[str, Any]:
        """Sync wrapper for _parse_response_async (fallback if not awaited)."""
        import asyncio

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Already in async context, create task
                return asyncio.create_task(self._parse_response_async(response, subtask))
            else:
                # Not in async context, run directly
                return loop.run_until_complete(self._parse_response_async(response, subtask))
        except RuntimeError:
            # No event loop, create new one
            return asyncio.run(self._parse_response_async(response, subtask))

    def _write_file_fallback(self, file_path: str, content: str) -> None:
        """
        Fallback file writer when agent doesn't use MCP tools.

        This creates files directly in the filesystem as a last resort.
        """
        full_path = self.project_path / file_path

        # Create parent directory if needed
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        full_path.write_text(content, encoding='utf-8')

        logger.info(f"💾 [FALLBACK] Created {file_path} ({len(content)} chars)")
        logger.debug(f"Content preview: {content[:200]}...")

    def _update_performance(self, subtask: SubTask, result: Dict[str, Any]):
        """Update performance tracking."""
        self.profile.performance_history.append({
            "category": subtask.category,
            "complexity": subtask.estimated_complexity.value,
            "success": result.get("success", False),
            "quality": result.get("quality_score", 0.0),
            "time": result.get("execution_time", 0.0)
        })

        self.profile.tasks_completed += 1

        # Update running averages
        recent = self.profile.performance_history[-20:]
        self.profile.success_rate = sum(t["success"] for t in recent) / len(recent)
        self.profile.avg_quality = sum(t["quality"] for t in recent) / len(recent)


class AgentPool:
    """Pool of specialized agents with capability-based selection."""

    def __init__(
        self,
        docs_engine: "DocumentationEngine",
        mcp_server,
        project_path: Path = None,
        swarm_logger=None
    ):
        self.docs = docs_engine
        self.mcp_server = mcp_server
        self.project_path = project_path or Path.cwd()
        self.swarm_logger = swarm_logger
        self.agents: list[SpecializedAgent] = []

        self._initialize_agents()

    def _initialize_agents(self):
        """Create specialized agent pool."""
        profiles = [
            AgentProfile(
                name="ModelArchitect",
                capabilities={
                    AgentCapability.DJANGO_MODELS,
                    AgentCapability.DATABASE_DESIGN,
                    AgentCapability.DJANGO_ADMIN,  # Added for admin interface
                    AgentCapability.ARCHITECTURE
                },
                specialization="django_models",
                model_name="mistralai/codestral-2501",
                cost_per_1m_tokens=0.60
            ),
            AgentProfile(
                name="APIBuilder",
                capabilities={
                    AgentCapability.DRF_VIEWSETS,
                    AgentCapability.DRF_SERIALIZERS,
                    AgentCapability.DJANGO_VIEWS,
                    AgentCapability.DRF_PERMISSIONS
                },
                specialization="api_development",
                model_name="mistralai/codestral-2501",
                cost_per_1m_tokens=0.60
            ),
            AgentProfile(
                name="QualityGuard",
                capabilities={
                    AgentCapability.TESTING,
                    AgentCapability.CODE_REVIEW,
                    AgentCapability.TEST_FIXTURES
                },
                specialization="quality_assurance",
                model_name="openai/gpt-4o-mini",
                cost_per_1m_tokens=0.375
            ),
        ]

        for profile in profiles:
            agent = SpecializedAgent(
                profile,
                self.docs,
                self.mcp_server,
                self.project_path,
                swarm_logger=self.swarm_logger
            )
            self.agents.append(agent)
            logger.info(
                f"🤖 Created agent: {profile.name} "
                f"(caps:{len(profile.capabilities)}, spec:{profile.specialization})"
            )

        logger.info(f"✅ Initialized {len(self.agents)} specialized agents")

    async def select_agent(self, subtask: SubTask) -> SpecializedAgent:
        """Select best agent for task based on capability matching."""
        scores = []
        for agent in self.agents:
            confidence = agent.can_handle(subtask)
            scores.append((confidence, agent))

        # Sort by confidence
        scores.sort(key=lambda x: x[0], reverse=True)

        # Select best
        best_confidence, best_agent = scores[0]

        logger.info(
            f"Selected {best_agent.profile.name} for {subtask.id} "
            f"(confidence: {best_confidence:.2f})"
        )

        return best_agent

    def get_performance_report(self) -> Dict[str, Dict[str, Any]]:
        """Generate performance report for all agents."""
        return {
            agent.profile.name: {
                "success_rate": agent.profile.success_rate,
                "avg_quality": agent.profile.avg_quality,
                "tasks_completed": agent.profile.tasks_completed,
                "specialization": agent.profile.specialization,
                "capabilities": [str(c.value) for c in agent.profile.capabilities]
            }
            for agent in self.agents
        }
