"""Quality assessment models for code review."""

from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class QualityIssue(BaseModel):
    """Represents a quality issue found in code."""

    type: str = Field(
        ...,
        description="Issue type: syntax, pattern, consistency, completeness, best_practice"
    )
    severity: str = Field(
        ...,
        description="Severity level: critical, warning, info"
    )
    file: str = Field(
        ...,
        description="File path where issue was found"
    )
    line: Optional[int] = Field(
        None,
        description="Line number (if applicable)"
    )
    description: str = Field(
        ...,
        description="Human-readable issue description"
    )
    suggestion: Optional[str] = Field(
        None,
        description="Suggested fix for the issue"
    )
    pattern_reference: Optional[str] = Field(
        None,
        description="Documentation pattern that should be applied"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "type": "pattern",
                "severity": "warning",
                "file": "blog/models.py",
                "line": 5,
                "description": "Missing __str__ method in Post model",
                "suggestion": "Add: def __str__(self): return self.title",
                "pattern_reference": "Django model best practices"
            }
        }


class QualityReport(BaseModel):
    """Comprehensive quality assessment report for a file."""

    file_path: str = Field(
        ...,
        description="Path to the file that was reviewed"
    )
    overall_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Overall quality score (0.0 - 1.0)"
    )
    scores: Dict[str, float] = Field(
        default_factory=dict,
        description="Individual dimension scores (syntax, patterns, consistency, etc.)"
    )
    issues: List[QualityIssue] = Field(
        default_factory=list,
        description="List of quality issues found"
    )
    passed: bool = Field(
        ...,
        description="Whether quality check passed (score >= threshold)"
    )
    timestamp: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="When this report was generated"
    )
    threshold: float = Field(
        default=0.85,
        description="Quality threshold for passing"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "file_path": "blog/models.py",
                "overall_score": 0.78,
                "scores": {
                    "syntax": 1.0,
                    "patterns": 0.75,
                    "consistency": 0.8,
                    "completeness": 0.7,
                    "best_practices": 0.65
                },
                "issues": [
                    {
                        "type": "pattern",
                        "severity": "warning",
                        "file": "blog/models.py",
                        "description": "Missing __str__ method"
                    }
                ],
                "passed": False,
                "threshold": 0.85
            }
        }

    def get_critical_issues(self) -> List[QualityIssue]:
        """Get only critical issues."""
        return [issue for issue in self.issues if issue.severity == "critical"]

    def get_warnings(self) -> List[QualityIssue]:
        """Get only warnings."""
        return [issue for issue in self.issues if issue.severity == "warning"]

    def summary(self) -> str:
        """Generate human-readable summary."""
        critical = len(self.get_critical_issues())
        warnings = len(self.get_warnings())

        status = "✅ PASS" if self.passed else "❌ FAIL"
        return (
            f"{status} - Score: {self.overall_score:.2f} "
            f"({critical} critical, {warnings} warnings)"
        )


class QualityResult(BaseModel):
    """Result of quality improvement process (potentially multiple iterations)."""

    passed: bool = Field(
        ...,
        description="Whether final quality check passed"
    )
    score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Final quality score achieved"
    )
    iterations: int = Field(
        ...,
        ge=1,
        description="Number of review/refinement iterations"
    )
    initial_score: Optional[float] = Field(
        None,
        description="Initial quality score before improvements"
    )
    improvement: Optional[float] = Field(
        None,
        description="Score improvement (final - initial)"
    )
    reports: List[QualityReport] = Field(
        default_factory=list,
        description="Quality reports from each iteration"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "passed": True,
                "score": 0.90,
                "iterations": 2,
                "initial_score": 0.65,
                "improvement": 0.25,
                "reports": []
            }
        }

    def final_report(self) -> Optional[QualityReport]:
        """Get the final quality report."""
        return self.reports[-1] if self.reports else None

    def summary(self) -> str:
        """Generate human-readable summary."""
        status = "✅ PASS" if self.passed else "❌ FAIL"
        improvement_text = ""

        if self.initial_score is not None and self.improvement is not None:
            improvement_text = f" (+{self.improvement:.2f} improvement)"

        return (
            f"{status} - Final score: {self.score:.2f}{improvement_text} "
            f"after {self.iterations} iteration(s)"
        )
