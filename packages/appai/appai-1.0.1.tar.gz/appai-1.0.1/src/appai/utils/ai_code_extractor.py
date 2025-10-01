"""AI-powered code extractor using cheap LLM for intelligent extraction."""

import logging
import json
from typing import List, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class ExtractedFile(BaseModel):
    """Pydantic model for extracted file."""

    file_path: str = Field(..., description="Relative file path (e.g., 'app/models.py')")
    content: str = Field(..., description="Complete file content")
    language: str = Field(default="python", description="Programming language")
    description: Optional[str] = Field(None, description="Brief description of file purpose")


class CodeExtractionResult(BaseModel):
    """Result of AI code extraction."""

    files: List[ExtractedFile] = Field(default_factory=list, description="Extracted files")
    has_code: bool = Field(..., description="Whether any code was found")
    extraction_confidence: float = Field(..., description="Confidence score (0-1)", ge=0, le=1)


class AICodeExtractor:
    """
    AI-powered code extractor using cheap LLM.

    Uses gpt-4o-mini (~$0.15/1M tokens) for intelligent extraction.
    """

    EXTRACTION_PROMPT = """You are a code extraction specialist. Your job is to extract code from text responses.

INPUT TEXT:
{response_text}

TASK CONTEXT:
- Category: {category}
- Expected files: {expected_files}

INSTRUCTIONS:
1. Find ALL code blocks in the text (markdown ```, indented, or inline)
2. For each code block, determine:
   - What file it should be in (infer from context, comments, or code content)
   - The programming language
   - A brief description
3. Return structured JSON following this schema

Return JSON with this structure:
{{
  "files": [
    {{
      "file_path": "path/to/file.py",
      "content": "complete file content here",
      "language": "python",
      "description": "Brief description"
    }}
  ],
  "has_code": true,
  "extraction_confidence": 0.95
}}

RULES:
- file_path should be relative (e.g., "app/models.py", not absolute)
- content should be complete and ready to write to file
- Remove markdown formatting, keep only code
- If file path is mentioned in text, use it
- Otherwise infer from code content (class names, imports, etc.)
- confidence 0-1: how sure you are about the extraction

Return ONLY valid JSON, no explanations."""

    def __init__(self, api_key: str):
        """
        Initialize AI extractor.

        Args:
            api_key: OpenRouter API key
        """
        from openai import AsyncOpenAI

        self.api_key = api_key
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    async def extract_code(
        self,
        response_text: str,
        task_category: Optional[str] = None,
        expected_files: Optional[List[str]] = None
    ) -> CodeExtractionResult:
        """
        Extract code using AI.

        Args:
            response_text: Agent's text response
            task_category: Task category for context
            expected_files: List of expected file paths

        Returns:
            CodeExtractionResult with extracted files
        """
        # Prepare prompt
        prompt = self.EXTRACTION_PROMPT.format(
            response_text=response_text[:8000],  # Limit to 8K chars
            category=task_category or "unknown",
            expected_files=", ".join(expected_files) if expected_files else "none specified"
        )

        try:
            # Call cheap model (gpt-4o-mini)
            response = await self.client.chat.completions.create(
                model="openai/gpt-4o-mini",  # ~$0.15/1M tokens
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.1,  # Low temp for consistent extraction
                max_tokens=2000
            )

            content = response.choices[0].message.content
            data = json.loads(content)

            # Parse into Pydantic model
            result = CodeExtractionResult(**data)

            logger.info(
                f"AI extraction: {len(result.files)} files, "
                f"confidence: {result.extraction_confidence:.2f}"
            )

            return result

        except Exception as e:
            logger.error(f"AI extraction failed: {e}")
            # Return empty result
            return CodeExtractionResult(
                files=[],
                has_code=False,
                extraction_confidence=0.0
            )

    async def extract_with_retry(
        self,
        response_text: str,
        task_category: Optional[str] = None,
        expected_files: Optional[List[str]] = None,
        max_retries: int = 2
    ) -> CodeExtractionResult:
        """
        Extract with retries if AI fails.

        Args:
            response_text: Agent's text response
            task_category: Task category
            expected_files: Expected files
            max_retries: Maximum retry attempts

        Returns:
            CodeExtractionResult
        """
        for attempt in range(max_retries):
            result = await self.extract_code(response_text, task_category, expected_files)

            # If AI found code, return
            if result.has_code and result.files:
                return result

            if attempt < max_retries - 1:
                logger.warning(f"AI extraction attempt {attempt + 1} failed, retrying...")

        # All retries failed
        logger.error("AI extraction failed after all retries")
        return CodeExtractionResult(
            files=[],
            has_code=False,
            extraction_confidence=0.0
        )
