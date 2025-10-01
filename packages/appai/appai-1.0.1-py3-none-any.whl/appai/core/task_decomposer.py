"""Task decomposer with LLM-based analysis and dependency graphs."""

import json
import logging
from typing import List, Dict, Set

from openai import AsyncOpenAI

from aiapp.models import SubTask, TaskPlan, TaskComplexity
from aiapp.core.documentation import DocumentationEngine

logger = logging.getLogger(__name__)


class TaskDecomposer:
    """Decompose high-level tasks into swarm-executable subtasks with dependencies."""

    def __init__(self, docs_engine: DocumentationEngine, api_key: str):
        self.docs = docs_engine
        self.api_key = api_key
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    async def decompose(self, task_description: str) -> TaskPlan:
        """
        Decompose task into parallel-executable plan.

        Args:
            task_description: High-level task description

        Returns:
            TaskPlan with subtasks and execution order
        """
        logger.info(f"🔍 Decomposing task: {task_description}")

        # Use LLM to analyze task
        analysis = await self._analyze_task(task_description)

        # Extract subtasks
        subtasks = self._extract_subtasks(analysis)

        if not subtasks:
            logger.warning("No subtasks extracted, creating default single task")
            subtasks = [SubTask(
                id="default_task",
                description=task_description,
                category="general",
                dependencies=set(),
                estimated_complexity=TaskComplexity.MODERATE,
                files_to_create=[],
                acceptance_criteria=["Task completed"]
            )]

        # Build dependency graph
        dep_graph = self._build_dependency_graph(subtasks)

        # Calculate execution order (topological sort)
        execution_order = self._calculate_waves(dep_graph)

        # Estimate metrics
        estimated_duration = self._estimate_duration(subtasks, execution_order)
        estimated_cost = self._estimate_cost(subtasks)

        plan = TaskPlan(
            goal=task_description,
            subtasks=subtasks,
            execution_order=execution_order,
            estimated_duration=estimated_duration,
            estimated_cost=estimated_cost
        )

        logger.info(
            f"✅ Created plan: {len(subtasks)} tasks, "
            f"{len(execution_order)} waves, "
            f"~{estimated_duration:.1f}min, "
            f"~${estimated_cost:.3f}"
        )

        return plan

    async def _analyze_task(self, description: str) -> Dict:
        """Use LLM to analyze task and extract components."""
        # Get relevant docs
        docs_context = self.docs.to_prompt_injection()

        prompt = f"""Analyze this Django task and break it into atomic components.

TASK:
{description}

{docs_context}

IMPORTANT: Return ONLY valid JSON, no explanations or markdown.

Required JSON structure:
{{
  "components": [
    {{
      "type": "model",
      "name": "Post",
      "dependencies": [],
      "complexity": "simple",
      "files": ["blog/models.py"],
      "acceptance": ["Model created", "Fields defined"]
    }},
    {{
      "type": "serializer",
      "name": "PostSerializer",
      "dependencies": ["model_Post"],
      "complexity": "simple",
      "files": ["blog/serializers.py"],
      "acceptance": ["Serializer created", "Fields match model"]
    }}
  ]
}}

Component types: model, viewset, serializer, admin, tests
Complexity levels: trivial, simple, moderate, complex, epic

Dependency order:
1. Models first (no dependencies)
2. Serializers (depend on models)
3. Viewsets (depend on models + serializers)
4. Admin (depend on models)
5. Tests (depend on everything)

Return ONLY the JSON object, nothing else."""

        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = await self.client.chat.completions.create(
                    model="anthropic/claude-3.5-sonnet",
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                    temperature=0.3
                )

                content = response.choices[0].message.content

                # Validate JSON before parsing
                if not content or content.strip() == "":
                    raise ValueError("Empty response from LLM")

                parsed = json.loads(content)

                # Validate structure
                if "components" not in parsed:
                    raise ValueError("Missing 'components' key in response")

                logger.info(f"✅ Task analysis successful: {len(parsed.get('components', []))} components")
                return parsed

            except json.JSONDecodeError as e:
                logger.error(f"Task analysis JSON error (attempt {attempt+1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    logger.info("Retrying task analysis...")
                    continue
            except Exception as e:
                logger.error(f"Task analysis failed (attempt {attempt+1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    logger.info("Retrying task analysis...")
                    continue

        # All retries failed
        logger.error("Task analysis failed after all retries, returning empty components")
        return {"components": []}

    def _extract_subtasks(self, analysis: Dict) -> List[SubTask]:
        """Convert analysis to SubTask objects."""
        subtasks = []

        for comp in analysis.get("components", []):
            try:
                subtask = SubTask(
                    id=f"{comp['type']}_{comp['name']}",
                    description=f"Create {comp['type']} {comp['name']}",
                    category=comp['type'],
                    dependencies=set(comp.get('dependencies', [])),
                    estimated_complexity=TaskComplexity(comp.get('complexity', 'moderate')),
                    files_to_create=comp.get('files', []),
                    acceptance_criteria=comp.get('acceptance', [])
                )
                subtasks.append(subtask)
            except Exception as e:
                logger.warning(f"Failed to parse component {comp.get('name')}: {e}")

        return subtasks

    def _build_dependency_graph(self, subtasks: List[SubTask]) -> Dict[str, Set[str]]:
        """Build adjacency list for dependency graph."""
        graph = {task.id: task.dependencies for task in subtasks}
        return graph

    def _calculate_waves(self, graph: Dict[str, Set[str]]) -> List[List[str]]:
        """
        Topological sort into parallel execution waves.

        Returns:
            List of waves, where each wave is a list of task IDs that can run in parallel
        """
        # Calculate in-degrees
        in_degree = {node: 0 for node in graph}
        for node in graph:
            for dep in graph[node]:
                if dep in in_degree:
                    in_degree[node] += 1

        waves = []
        remaining = set(graph.keys())

        while remaining:
            # Find nodes with no dependencies
            wave = [node for node in remaining if in_degree[node] == 0]

            if not wave:
                # Circular dependency or error - execute all remaining
                logger.warning("Circular dependency detected, executing remaining tasks")
                wave = list(remaining)

            waves.append(wave)

            # Update remaining
            for node in wave:
                remaining.remove(node)
                # Decrease in-degree for dependent nodes
                for dep_node in remaining:
                    if node in graph.get(dep_node, set()):
                        in_degree[dep_node] -= 1

        logger.info(f"📊 Execution plan: {len(waves)} waves")
        for i, wave in enumerate(waves):
            logger.info(f"  Wave {i+1}: {len(wave)} tasks - {', '.join(wave)}")

        return waves

    def _estimate_duration(self, subtasks: List[SubTask], waves: List[List[str]]) -> float:
        """Estimate total duration in minutes (parallel execution considered)."""
        complexity_time = {
            TaskComplexity.TRIVIAL: 0.5,
            TaskComplexity.SIMPLE: 1.0,
            TaskComplexity.MODERATE: 2.0,
            TaskComplexity.COMPLEX: 5.0,
            TaskComplexity.EPIC: 10.0
        }

        task_map = {t.id: t for t in subtasks}

        total = 0.0
        for wave in waves:
            # Parallel execution - use max time in wave
            wave_max = max(
                complexity_time.get(task_map[tid].estimated_complexity, 2.0)
                for tid in wave
                if tid in task_map
            )
            total += wave_max

        return total

    def _estimate_cost(self, subtasks: List[SubTask]) -> float:
        """Estimate total cost in USD."""
        complexity_cost = {
            TaskComplexity.TRIVIAL: 0.001,
            TaskComplexity.SIMPLE: 0.005,
            TaskComplexity.MODERATE: 0.02,
            TaskComplexity.COMPLEX: 0.05,
            TaskComplexity.EPIC: 0.10
        }

        return sum(
            complexity_cost.get(t.estimated_complexity, 0.02)
            for t in subtasks
        )
