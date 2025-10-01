"""Main CLI interface for AIApp using Click."""

import os
import asyncio
import logging
from pathlib import Path
from typing import Optional

import click

from aiapp import __version__
from aiapp.core import DocumentationEngine, TaskDecomposer
from aiapp.agents import AgentPool
from aiapp.orchestration import SwarmCoordinator
from aiapp.models import SystemConfig
from aiapp.utils.mcp_servers import create_filesystem_server
from aiapp.cache import CacheManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version=__version__)
def cli():
    """AIApp - Swarm Intelligence System for Documentation-Driven Code Generation."""
    pass


@cli.command()
@click.argument('task_description')
@click.option('--project-path', type=click.Path(), default=".", help="Project root path")
@click.option('--docs-path', type=click.Path(), default=None, help="Custom documentation path (optional)")
@click.option('--framework', default="django", help="Target framework (django, nextjs, etc.)")
@click.option('--no-builtin', is_flag=True, help="Don't use built-in documentation")
@click.option('--budget-mode/--no-budget-mode', default=True, help="Use budget-friendly models")
def generate(
    task_description: str,
    project_path: str,
    docs_path: Optional[str],
    framework: str,
    no_builtin: bool,
    budget_mode: bool
):
    """
    Generate code based on task description.

    By default, uses built-in framework documentation.
    Use --docs-path to add custom documentation (merged with built-in).
    Use --no-builtin to use only custom documentation.
    """
    asyncio.run(_generate_async(
        task_description,
        Path(project_path),
        Path(docs_path) if docs_path else None,
        framework,
        not no_builtin,  # include_builtin
        budget_mode
    ))


async def _generate_async(
    task_description: str,
    project_path: Path,
    docs_path: Optional[Path],
    framework: str,
    include_builtin: bool,
    budget_mode: bool
):
    """Async implementation of generate command."""
    # Get API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        click.echo("❌ Error: OPENROUTER_API_KEY environment variable not set", err=True)
        return

    click.echo(f"🚀 AIApp v{__version__}")
    click.echo(f"📝 Task: {task_description}")
    click.echo(f"📁 Project: {project_path}")

    # Documentation source description
    if docs_path and include_builtin:
        click.echo(f"📚 Docs: Built-in {framework} + custom ({docs_path})")
    elif docs_path:
        click.echo(f"📚 Docs: Custom only ({docs_path})")
    else:
        click.echo(f"📚 Docs: Built-in {framework}")

    click.echo(f"🎯 Framework: {framework}")
    click.echo(f"💰 Budget mode: {'ON' if budget_mode else 'OFF'}")
    click.echo()

    try:
        # Initialize components
        click.echo("🔧 Initializing components...")

        # Documentation engine (with built-in support)
        docs_engine = DocumentationEngine(
            docs_path=docs_path,
            framework=framework,
            include_builtin=include_builtin
        )

        # Task decomposer
        decomposer = TaskDecomposer(docs_engine, api_key)

        # Decompose task
        click.echo("🔍 Decomposing task...")
        plan = await decomposer.decompose(task_description)

        click.echo(f"\n📊 Plan created:")
        click.echo(f"  • {len(plan.subtasks)} subtasks")
        click.echo(f"  • {len(plan.execution_order)} execution waves")
        click.echo(f"  • ~{plan.estimated_duration:.1f} minutes")
        click.echo(f"  • ~${plan.estimated_cost:.3f} estimated cost")
        click.echo()

        # Create MCP server
        mcp_server = create_filesystem_server(project_path)

        # Agent pool
        agent_pool = AgentPool(docs_engine, mcp_server)

        # Swarm coordinator with logging
        log_dir = project_path / "logs"
        coordinator = SwarmCoordinator(agent_pool, plan, docs_engine, log_dir=log_dir)

        # Execute
        click.echo("🐝 Executing swarm...")
        result = await coordinator.execute()

        # Display results
        click.echo("\n" + "="*60)
        if result["success"]:
            click.echo("✅ SUCCESS")
            click.echo(f"\n📈 Results:")
            click.echo(f"  • Completed: {result['completed']} tasks")
            click.echo(f"  • Failed: {result['failed']} tasks")

            metrics = result["metrics"]
            click.echo(f"\n📊 Metrics:")
            click.echo(f"  • Total time: {metrics['total_time']:.1f}s")
            click.echo(f"  • Parallelism: {metrics['parallelism_factor']:.2f}x")
            click.echo(f"  • Total cost: ${metrics['total_cost']:.3f}")
            click.echo(f"  • Avg quality: {metrics['avg_quality']:.2f}")
        else:
            click.echo("❌ FAILED")
            click.echo(f"\n  Error: {result.get('error', 'Unknown error')}")
            click.echo(f"  Completed: {result['completed']} tasks")
            click.echo(f"  Failed: {result['failed']} tasks")

        click.echo("="*60)

    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        logger.exception("Generation failed")
        raise click.Abort()


@cli.command()
@click.option('--docs-path', type=click.Path(), default=None, help="Custom documentation path (optional)")
@click.option('--framework', default="django", help="Framework")
@click.option('--no-builtin', is_flag=True, help="Don't include built-in documentation")
def index_docs(docs_path: Optional[str], framework: str, no_builtin: bool):
    """
    Index documentation for vector search.

    By default, indexes built-in framework documentation.
    Use --docs-path to add custom documentation.
    """
    if docs_path and no_builtin:
        click.echo(f"📚 Indexing custom {framework} documentation from {docs_path}")
    elif docs_path:
        click.echo(f"📚 Indexing built-in + custom {framework} documentation")
    else:
        click.echo(f"📚 Indexing built-in {framework} documentation")

    try:
        docs_engine = DocumentationEngine(
            docs_path=Path(docs_path) if docs_path else None,
            framework=framework,
            include_builtin=not no_builtin
        )
        click.echo(f"✅ Documentation indexed successfully")

        if docs_engine.collection:
            count = docs_engine.collection.count()
            click.echo(f"  • {count} chunks indexed")

            # Show sources
            if docs_engine.doc_paths:
                click.echo(f"  • Sources:")
                for path in docs_engine.doc_paths:
                    click.echo(f"    - {path}")

    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        raise click.Abort()


@cli.command()
def clear_cache():
    """Clear in-memory cache and show statistics."""
    click.echo("📊 Cache statistics...")

    try:
        cache = CacheManager()
        stats = cache.get_stats()

        click.echo(f"  • Size: {stats['size']}/{stats['max_size']}")
        click.echo(f"  • Hits: {stats['hits']}")
        click.echo(f"  • Misses: {stats['misses']}")
        click.echo(f"  • Hit rate: {stats['hit_rate']}")

        cache.clear_cache()
        click.echo("\n✅ Cache cleared")

    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)


@cli.command()
def version():
    """Show version information."""
    click.echo(f"AIApp version {__version__}")


if __name__ == "__main__":
    cli()
