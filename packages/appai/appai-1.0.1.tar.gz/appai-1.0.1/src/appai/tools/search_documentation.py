"""Tool for agents to search documentation autonomously."""

from typing import Optional
from pydantic import Field
from agency_swarm.tools import BaseTool


class SearchDocumentation(BaseTool):
    """
    Search framework documentation for relevant patterns and examples.

    Use this tool when you need to find:
    - Code examples
    - Best practices
    - Framework patterns
    - Implementation guidelines

    The tool searches through indexed documentation and returns the most relevant patterns.
    """

    query: str = Field(
        ...,
        description="What you're looking for. Examples: 'Django model with ForeignKey', 'NextJS API routes', 'Django REST Framework serializers'"
    )

    framework: Optional[str] = Field(
        default=None,
        description="Framework to search (django, nextjs, fastapi). Leave empty to search all frameworks."
    )

    top_k: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of results to return (1-10)"
    )

    def run(self) -> str:
        """
        Search documentation and return formatted results.

        Returns:
            Formatted string with found patterns, or error message
        """
        try:
            # Import here to avoid circular dependencies
            from aiapp.core import DocumentationEngine

            # Get documentation engine
            # If framework specified, search specific collection
            # Otherwise search across all available frameworks
            if self.framework:
                docs = DocumentationEngine(framework=self.framework)
            else:
                # Default to django for now
                # TODO: Support cross-framework search
                docs = DocumentationEngine(framework="django")

            # Search patterns with framework filter
            where_filter = {"framework": self.framework} if self.framework else None
            patterns = docs.search_patterns(
                query=self.query,
                category=None,
                top_k=self.top_k
            )

            if not patterns:
                return f"❌ No documentation found for query: '{self.query}'"

            # Format results
            results = []
            results.append(f"📚 Found {len(patterns)} relevant documentation patterns:\n")

            for idx, pattern in enumerate(patterns, 1):
                metadata = pattern.get('metadata', {})
                file_name = metadata.get('file', 'Unknown')
                fw = metadata.get('framework', 'unknown')
                score = pattern.get('score', 0.0)
                content = pattern.get('content', '')

                results.append(f"\n{'='*60}")
                results.append(f"Pattern #{idx} - {file_name} ({fw})")
                results.append(f"Relevance: {score:.2f}")
                results.append(f"{'='*60}")
                results.append(content[:800])  # Limit content length
                if len(content) > 800:
                    results.append("\n... (truncated)")
                results.append("")

            return "\n".join(results)

        except Exception as e:
            return f"❌ Error searching documentation: {str(e)}\nPlease try a different query or framework."

    class ToolConfig:
        """Tool configuration."""
        one_call_at_a_time = False  # Allow parallel searches
