"""System configuration Pydantic v2 models."""

from pathlib import Path
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator


class SystemConfig(BaseModel):
    """Main system configuration."""

    model_config = ConfigDict(frozen=False, arbitrary_types_allowed=True)

    # Paths
    project_path: Path = Field(..., description="Project root path")
    docs_path: Path = Field(..., description="Documentation path")
    cache_dir: Optional[Path] = Field(default=None, description="Cache directory (default: ~/.aiapp/cache)")

    # Framework
    framework: str = Field(default="django", description="Target framework (django, nextjs, etc.)")

    # OpenRouter
    openrouter_api_key: Optional[str] = Field(default=None, description="OpenRouter API key")
    budget_mode: bool = Field(default=True, description="Use budget-friendly models")

    # Redis (optional)
    redis_host: str = Field(default="localhost", description="Redis host")
    redis_port: int = Field(default=6379, description="Redis port", gt=0, lt=65536)
    redis_enabled: bool = Field(default=False, description="Enable Redis caching")

    # ChromaDB
    chroma_enabled: bool = Field(default=True, description="Enable ChromaDB vector search")

    # Execution
    max_parallel_tasks: int = Field(default=5, description="Max parallel task execution", gt=0)
    timeout_per_task: int = Field(default=300, description="Timeout per task in seconds", gt=0)

    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_to_file: bool = Field(default=False, description="Enable file logging")

    @field_validator("cache_dir", mode="before")
    @classmethod
    def set_default_cache_dir(cls, v: Optional[Path]) -> Path:
        """Set default cache directory if not provided."""
        if v is None:
            return Path.home() / ".aiapp" / "cache"
        return v

    @field_validator("project_path", "docs_path", "cache_dir")
    @classmethod
    def validate_path(cls, v: Path) -> Path:
        """Ensure Path objects are absolute."""
        return v.resolve()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for compatibility."""
        return self.model_dump(mode="python")
