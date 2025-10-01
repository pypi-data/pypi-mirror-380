"""Quality checking utilities for code review."""

import ast
import re
from pathlib import Path
from typing import List, Dict, Optional
from aiapp.models.quality import QualityIssue, QualityReport


class QualityChecker:
    """Analyzes code quality across multiple dimensions."""

    def __init__(self, project_path: Path, docs_engine=None):
        self.project_path = project_path
        self.docs_engine = docs_engine
        self.threshold = 0.85

    def check_file(self, file_path: str) -> QualityReport:
        """
        Perform comprehensive quality check on a file.

        Returns:
            QualityReport with scores and issues
        """
        full_path = self.project_path / file_path

        if not full_path.exists():
            return QualityReport(
                file_path=file_path,
                overall_score=0.0,
                passed=False,
                issues=[
                    QualityIssue(
                        type="completeness",
                        severity="critical",
                        file=file_path,
                        description="File does not exist"
                    )
                ]
            )

        content = full_path.read_text()

        # Run all quality checks
        issues: List[QualityIssue] = []
        scores: Dict[str, float] = {}

        # 1. Syntax check
        syntax_issues, syntax_score = self._check_syntax(file_path, content)
        issues.extend(syntax_issues)
        scores["syntax"] = syntax_score

        # 2. Pattern compliance (Django best practices)
        pattern_issues, pattern_score = self._check_patterns(file_path, content)
        issues.extend(pattern_issues)
        scores["patterns"] = pattern_score

        # 3. Consistency with project
        consistency_issues, consistency_score = self._check_consistency(file_path, content)
        issues.extend(consistency_issues)
        scores["consistency"] = consistency_score

        # 4. Completeness (required methods/fields)
        completeness_issues, completeness_score = self._check_completeness(file_path, content)
        issues.extend(completeness_issues)
        scores["completeness"] = completeness_score

        # 5. Best practices
        best_practice_issues, best_practice_score = self._check_best_practices(file_path, content)
        issues.extend(best_practice_issues)
        scores["best_practices"] = best_practice_score

        # Calculate overall score (average of dimension scores)
        overall_score = sum(scores.values()) / len(scores)
        passed = overall_score >= self.threshold

        return QualityReport(
            file_path=file_path,
            overall_score=overall_score,
            scores=scores,
            issues=issues,
            passed=passed,
            threshold=self.threshold
        )

    def _check_syntax(self, file_path: str, content: str) -> tuple[List[QualityIssue], float]:
        """Check Python syntax validity."""
        issues = []

        try:
            ast.parse(content)
            return issues, 1.0
        except SyntaxError as e:
            issues.append(
                QualityIssue(
                    type="syntax",
                    severity="critical",
                    file=file_path,
                    line=e.lineno,
                    description=f"Syntax error: {e.msg}",
                    suggestion="Fix syntax error before proceeding"
                )
            )
            return issues, 0.0

    def _check_patterns(self, file_path: str, content: str) -> tuple[List[QualityIssue], float]:
        """Check Django pattern compliance."""
        issues = []
        score = 1.0

        # Django models.py checks
        if "models.py" in file_path:
            # Check for __str__ method in models
            if "class " in content and "models.Model" in content:
                model_pattern = re.compile(r"class (\w+)\(.*models\.Model.*?\):", re.MULTILINE)
                models = model_pattern.findall(content)

                for model_name in models:
                    # Check if __str__ method exists for this model
                    str_pattern = re.compile(
                        rf"class {model_name}\(.*?\):.*?def __str__\(self\):",
                        re.DOTALL
                    )
                    if not str_pattern.search(content):
                        issues.append(
                            QualityIssue(
                                type="pattern",
                                severity="warning",
                                file=file_path,
                                description=f"Missing __str__ method in {model_name} model",
                                suggestion=f"Add: def __str__(self): return self.<field>",
                                pattern_reference="Django model best practices"
                            )
                        )
                        score -= 0.1

            # Check for proper ForeignKey usage
            fk_without_related = re.findall(
                r"models\.ForeignKey\([^)]*\)(?![^)]*related_name)",
                content
            )
            if fk_without_related:
                issues.append(
                    QualityIssue(
                        type="pattern",
                        severity="warning",
                        file=file_path,
                        description="ForeignKey without related_name",
                        suggestion="Add related_name parameter to ForeignKey",
                        pattern_reference="Django ForeignKey best practices"
                    )
                )
                score -= 0.1

        # Serializers.py checks
        if "serializers.py" in file_path:
            if "class " in content and "serializers." in content:
                # Check for Meta class
                if "class Meta:" not in content:
                    issues.append(
                        QualityIssue(
                            type="pattern",
                            severity="warning",
                            file=file_path,
                            description="Serializer missing Meta class",
                            suggestion="Add Meta class with model and fields",
                            pattern_reference="Django REST framework serializers"
                        )
                    )
                    score -= 0.2

        # Admin.py checks
        if "admin.py" in file_path:
            if "admin.site.register" in content:
                # Check if using decorator or register() without ModelAdmin
                simple_register = re.findall(r"admin\.site\.register\(\w+\)$", content, re.MULTILINE)
                if simple_register:
                    issues.append(
                        QualityIssue(
                            type="pattern",
                            severity="info",
                            file=file_path,
                            description="Simple admin registration without ModelAdmin",
                            suggestion="Consider creating ModelAdmin class for better admin interface",
                            pattern_reference="Django admin best practices"
                        )
                    )
                    score -= 0.05

        return issues, max(0.0, min(1.0, score))

    def _check_consistency(self, file_path: str, content: str) -> tuple[List[QualityIssue], float]:
        """Check consistency with other project files."""
        issues = []
        score = 1.0

        # Check import style consistency
        if self.project_path.exists():
            # Find other Python files in the project
            other_files = list(self.project_path.rglob("*.py"))

            if len(other_files) > 1:
                # Check if using consistent import style
                uses_absolute = bool(re.search(r"^from \w+\.\w+", content, re.MULTILINE))
                uses_relative = bool(re.search(r"^from \.", content, re.MULTILINE))

                # Sample other files to determine project convention
                absolute_count = 0
                relative_count = 0

                for other_file in other_files[:5]:  # Check first 5 files
                    if other_file.name == Path(file_path).name:
                        continue
                    try:
                        other_content = other_file.read_text()
                        if re.search(r"^from \w+\.\w+", other_content, re.MULTILINE):
                            absolute_count += 1
                        if re.search(r"^from \.", other_content, re.MULTILINE):
                            relative_count += 1
                    except:
                        pass

                # Check for inconsistency
                if absolute_count > relative_count and uses_relative and not uses_absolute:
                    issues.append(
                        QualityIssue(
                            type="consistency",
                            severity="info",
                            file=file_path,
                            description="Uses relative imports while project prefers absolute",
                            suggestion="Consider using absolute imports for consistency"
                        )
                    )
                    score -= 0.1
                elif relative_count > absolute_count and uses_absolute and not uses_relative:
                    issues.append(
                        QualityIssue(
                            type="consistency",
                            severity="info",
                            file=file_path,
                            description="Uses absolute imports while project prefers relative",
                            suggestion="Consider using relative imports for consistency"
                        )
                    )
                    score -= 0.1

        return issues, max(0.0, min(1.0, score))

    def _check_completeness(self, file_path: str, content: str) -> tuple[List[QualityIssue], float]:
        """Check if all required elements are present."""
        issues = []
        score = 1.0

        # Django models.py completeness
        if "models.py" in file_path:
            # Check for timestamp fields
            if "models.Model" in content:
                if "created_at" not in content and "created" not in content:
                    issues.append(
                        QualityIssue(
                            type="completeness",
                            severity="info",
                            file=file_path,
                            description="Model missing created timestamp field",
                            suggestion="Consider adding: created_at = models.DateTimeField(auto_now_add=True)"
                        )
                    )
                    score -= 0.05

                if "updated_at" not in content and "modified" not in content:
                    issues.append(
                        QualityIssue(
                            type="completeness",
                            severity="info",
                            file=file_path,
                            description="Model missing updated timestamp field",
                            suggestion="Consider adding: updated_at = models.DateTimeField(auto_now=True)"
                        )
                    )
                    score -= 0.05

        # Check for docstrings
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if not ast.get_docstring(node):
                        issues.append(
                            QualityIssue(
                                type="completeness",
                                severity="info",
                                file=file_path,
                                line=node.lineno,
                                description=f"Class {node.name} missing docstring",
                                suggestion="Add docstring to explain class purpose"
                            )
                        )
                        score -= 0.05
        except:
            pass

        return issues, max(0.0, min(1.0, score))

    def _check_best_practices(self, file_path: str, content: str) -> tuple[List[QualityIssue], float]:
        """Check Python and Django best practices."""
        issues = []
        score = 1.0

        # Check line length
        lines = content.split('\n')
        long_lines = [i + 1 for i, line in enumerate(lines) if len(line) > 120]
        if long_lines:
            issues.append(
                QualityIssue(
                    type="best_practice",
                    severity="info",
                    file=file_path,
                    line=long_lines[0],
                    description=f"{len(long_lines)} lines exceed 120 characters",
                    suggestion="Break long lines for better readability"
                )
            )
            score -= 0.05

        # Check for print statements (should use logging)
        if re.search(r"^\s*print\(", content, re.MULTILINE):
            issues.append(
                QualityIssue(
                    type="best_practice",
                    severity="info",
                    file=file_path,
                    description="Using print() instead of logging",
                    suggestion="Use logging module instead of print()"
                )
            )
            score -= 0.1

        # Check for bare except
        if re.search(r"except\s*:", content):
            issues.append(
                QualityIssue(
                    type="best_practice",
                    severity="warning",
                    file=file_path,
                    description="Bare except clause found",
                    suggestion="Specify exception types to catch"
                )
            )
            score -= 0.15

        # Django-specific: Check for timezone-aware datetime
        if "models.py" in file_path and "DateTimeField" in content:
            if "from django.utils import timezone" not in content and "timezone.now" not in content:
                issues.append(
                    QualityIssue(
                        type="best_practice",
                        severity="info",
                        file=file_path,
                        description="DateTimeField without timezone import",
                        suggestion="Use timezone.now() for timezone-aware datetimes"
                    )
                )
                score -= 0.05

        return issues, max(0.0, min(1.0, score))
