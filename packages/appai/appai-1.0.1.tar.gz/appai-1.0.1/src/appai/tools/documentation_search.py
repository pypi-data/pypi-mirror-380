"""Documentation search tool for agents to query documentation autonomously."""

from typing import Optional
from pydantic import Field
from agency_swarm.tools import BaseTool


class SearchDocumentation(BaseTool):
    """
    Search through framework documentation to find relevant patterns, examples, and best practices.

    Use this tool when you need guidance on:
    - How to implement a specific feature
    - Best practices for a framework
    - Code examples and patterns
    - API usage and structure

    The tool will search through indexed documentation and return the most relevant sections.
    """

    query: str = Field(
        ...,
        description="What you're looking for in the documentation. Be specific. "
                    "Examples: 'Django model with ForeignKey', 'NextJS API routes', "
                    "'DRF serializer with nested objects'"
    )

    framework: Optional[str] = Field(
        default=None,
        description="Which framework documentation to search (django, nextjs, fastapi). "
                    "Leave empty to search all frameworks. "
                    "If you know the framework, specify it for better results."
    )

    max_results: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum number of documentation sections to return (1-10)"
    )

    def run(self) -> str:
        """
        Search documentation and return relevant sections.

        Returns:
            Formatted documentation sections with examples and patterns
        """
        # Get documentation engine from shared context
        try:
            from aiapp.core import DocumentationEngine

            # Determine framework to search
            # Priority: explicit parameter > context > default to django
            framework = self.framework or 'django'

            # Create documentation engine for the framework
            # This will use built-in documentation automatically
            docs_engine = DocumentationEngine(framework=framework, include_builtin=True)

            # Search for patterns
            patterns = docs_engine.search_patterns(
                query=self.query,
                category=None,
                top_k=self.max_results
            )

            if not patterns:
                return f"❌ No documentation found for: {self.query}\n" \
                       f"Framework: {framework}\n" \
                       f"Try rephrasing your query or check if documentation is indexed."

            # Format results
            result_lines = [
                f"📚 Found {len(patterns)} documentation sections for: {self.query}",
                f"Framework: {framework}",
                f"",
                "=" * 80,
                ""
            ]

            for idx, pattern in enumerate(patterns, 1):
                metadata = pattern.get('metadata', {})
                file_name = metadata.get('file', 'Unknown')
                doc_framework = metadata.get('framework', 'unknown')
                source = metadata.get('source', 'unknown')
                score = pattern.get('score', 0.0)
                content = pattern.get('content', '')

                result_lines.extend([
                    f"### 📖 Result {idx}/{len(patterns)}",
                    f"**File**: {file_name}",
                    f"**Framework**: {doc_framework}",
                    f"**Source**: {source}",
                    f"**Relevance**: {score:.2f}",
                    f"",
                    content,
                    "",
                    "-" * 80,
                    ""
                ])

            result_lines.extend([
                "",
                "💡 **How to use this information:**",
                "1. Read the patterns and examples above",
                "2. Adapt them to your specific use case",
                "3. Follow the same structure and best practices",
                "4. Use MCP tools (write_file, create_directory) to create your files",
                ""
            ])

            return "\n".join(result_lines)

        except Exception as e:
            return f"❌ Error searching documentation: {str(e)}\n" \
                   f"Query: {self.query}\n" \
                   f"Framework: {self.framework or 'auto'}"


class ListAvailableDocumentation(BaseTool):
    """
    List all available framework documentation that can be searched.

    Use this tool to:
    - See what frameworks have documentation available
    - Check if documentation is indexed
    - Understand what you can search for
    """

    def run(self) -> str:
        """
        List available documentation frameworks.

        Returns:
            List of available frameworks with statistics
        """
        try:
            from aiapp.docs import BUILTIN_DOCS_DIR
            from pathlib import Path

            # Check what documentation is available
            available = []

            if BUILTIN_DOCS_DIR.exists():
                for framework_dir in BUILTIN_DOCS_DIR.iterdir():
                    if framework_dir.is_dir() and framework_dir.name != "__pycache__":
                        # Count markdown files
                        md_files = list(framework_dir.rglob("*.md"))
                        available.append({
                            "name": framework_dir.name,
                            "files": len(md_files),
                            "path": str(framework_dir)
                        })

            if not available:
                return "❌ No built-in documentation found.\n" \
                       "Check if documentation is installed."

            # Format output
            result_lines = [
                "📚 Available Framework Documentation",
                "=" * 60,
                ""
            ]

            for fw in available:
                result_lines.extend([
                    f"### {fw['name'].upper()}",
                    f"  • Files: {fw['files']} markdown files",
                    f"  • Path: {fw['path']}",
                    f"  • Usage: search_documentation(query='...', framework='{fw['name']}')",
                    ""
                ])

            result_lines.extend([
                "",
                "💡 **How to search:**",
                "Use the search_documentation tool with your query:",
                "  search_documentation(",
                "    query='what you need',",
                "    framework='django'  # or leave empty to search all",
                "  )",
                ""
            ])

            return "\n".join(result_lines)

        except Exception as e:
            return f"❌ Error listing documentation: {str(e)}"
