"""Django-specific prompt instructions and guidelines."""

from typing import List, Dict, Any
from aiapp.prompts.registry import PromptBuilderRegistry


@PromptBuilderRegistry.register('django')
class DjangoPromptBuilder:
    """
    Builds Django-specific instructions for agent prompts.

    Contains universal guidelines that apply to all Django tasks:
    - Cross-app imports
    - Model relationships
    - Best practices
    """

    @staticmethod
    def get_cross_app_imports_guide() -> str:
        """
        Get instructions for cross-app imports.
        Critical for ForeignKey and ManyToMany relationships.
        """
        return """
## 🔗 Django Cross-App Imports - CRITICAL RULES

**When creating models that reference models from OTHER Django apps:**

### ✅ CORRECT - Import the model class:
```python
# blog/models.py
from django.db import models
from authors.models import Author  # ← IMPORT FROM OTHER APP

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
```

### ❌ WRONG - String reference (lazy import):
```python
# blog/models.py
class Post(models.Model):
    author = models.ForeignKey('authors.Author', ...)  # ❌ DON'T DO THIS
    # or
    author = models.ForeignKey('Author', ...)  # ❌ DON'T DO THIS
```

**String references should ONLY be used for:**
- Circular dependencies within the SAME app
- Self-referential relationships

### Key Rules:
1. **ALWAYS import model classes from other apps at the top of the file**
2. **Use the imported class directly in ForeignKey/ManyToManyField**
3. **ALWAYS use `related_name` parameter** (e.g., `related_name='posts'`)
4. **NEVER put all models in root models.py** - each app must have its own models.py
"""

    @staticmethod
    def get_model_relationships_guide() -> str:
        """Get instructions for Django model relationships."""
        return """
## 📊 Django Model Relationships Guide

### ForeignKey (One-to-Many)
```python
from authors.models import Author

class Post(models.Model):
    author = models.ForeignKey(
        Author,  # ← Imported class, NOT string
        on_delete=models.CASCADE,  # Required
        related_name='posts'  # Required for reverse access
    )
```

### ManyToManyField
```python
from blog.models import Tag

class Post(models.Model):
    tags = models.ManyToManyField(
        Tag,  # ← Imported class
        related_name='posts',  # Required
        blank=True  # Optional: allows empty
    )
```

### OneToOneField
```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
```

### on_delete Options:
- `CASCADE` - Delete related objects (most common)
- `SET_NULL` - Set to NULL (requires `null=True`)
- `PROTECT` - Prevent deletion if related objects exist
- `SET_DEFAULT` - Set to default value (requires `default=...`)
"""

    @staticmethod
    def get_app_structure_guide() -> str:
        """Get instructions for Django app structure."""
        return """
## 📁 Django App Structure Best Practices

**Each Django app should have its own models.py file:**

```
project_root/
├── authors/
│   ├── __init__.py
│   ├── models.py      ← Author model here
│   ├── admin.py
│   ├── views.py
│   └── serializers.py
│
├── blog/
│   ├── __init__.py
│   ├── models.py      ← Post, Category, Tag models here
│   ├── admin.py
│   ├── views.py
│   └── serializers.py
│
└── comments/
    ├── __init__.py
    ├── models.py      ← Comment model here
    ├── admin.py
    └── views.py
```

**NEVER create a single root models.py with all models!**
"""

    @staticmethod
    def get_model_best_practices() -> str:
        """Get Django model best practices."""
        return """
## ⭐ Django Model Best Practices

1. **Always include `__str__` method:**
   ```python
   def __str__(self):
       return self.title
   ```

2. **Use `auto_now_add` and `auto_now` for timestamps:**
   ```python
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   ```

3. **Always specify `related_name`:**
   ```python
   author = models.ForeignKey(Author, related_name='posts', ...)
   ```

4. **Import models explicitly, never use strings for cross-app references:**
   ```python
   from authors.models import Author  # ✅ CORRECT
   author = models.ForeignKey(Author, ...)
   ```

5. **Use Meta class for ordering and other options:**
   ```python
   class Meta:
       ordering = ['-created_at']
       verbose_name_plural = 'Posts'
   ```
"""

    @classmethod
    def build_django_guidelines(
        cls,
        task_category: str,
        created_models: List[Dict[str, Any]] = None
    ) -> str:
        """
        Build comprehensive Django guidelines based on task context.

        Args:
            task_category: Type of task (e.g., 'model', 'api', 'admin')
            created_models: List of previously created models

        Returns:
            Formatted guidelines string
        """
        sections = []

        # Always include cross-app imports for model tasks
        if task_category in ['model', 'serializer']:
            sections.append(cls.get_cross_app_imports_guide())

        # Include relationships guide for model tasks
        if task_category == 'model':
            sections.append(cls.get_model_relationships_guide())
            sections.append(cls.get_app_structure_guide())
            sections.append(cls.get_model_best_practices())

        # If models exist, add explicit reminder
        if created_models:
            sections.append("\n## ⚠️ AVAILABLE MODELS - MUST IMPORT IF NEEDED\n")
            sections.append("The following models already exist in OTHER apps:")
            sections.append("")
            for model in created_models:
                name = model.get('name', 'Unknown')
                file = model.get('file', 'unknown')
                app = model.get('app', 'unknown')
                sections.append(f"  • **{name}** - in `{file}` - import with: `from {app}.models import {name}`")

            sections.append("")
            sections.append("**If your task requires relationships to these models:**")
            sections.append("1. Add import at top: `from {app}.models import {ModelName}`")
            sections.append("2. Use imported class in ForeignKey: `ForeignKey(ModelName, ...)`")
            sections.append("3. NEVER use string references like `ForeignKey('{ModelName}', ...)`")
            sections.append("")

        return "\n".join(sections)

    @classmethod
    def build_selected_sections(
        cls,
        sections: List[str],
        task_category: str,
        created_models: List[Dict[str, Any]] = None
    ) -> str:
        """
        Build only selected sections (agent-driven).

        Args:
            sections: List of section names to include
            task_category: Task category
            created_models: Previously created models

        Returns:
            Formatted guidelines with only requested sections
        """
        # Map section names to methods
        section_map = {
            "cross_app_imports": cls.get_cross_app_imports_guide,
            "relationships": cls.get_model_relationships_guide,
            "app_structure": cls.get_app_structure_guide,
            "best_practices": cls.get_model_best_practices,
        }

        output = []

        # Build selected sections
        for section_name in sections:
            if section_name in section_map:
                output.append(section_map[section_name]())

        # Always include created models reminder if models exist
        if created_models and "cross_app_imports" in sections:
            output.append("\n## ⚠️ AVAILABLE MODELS - MUST IMPORT IF NEEDED\n")
            output.append("The following models already exist in OTHER apps:")
            output.append("")
            for model in created_models:
                name = model.get('name', 'Unknown')
                file = model.get('file', 'unknown')
                app = model.get('app', 'unknown')
                output.append(f"  • **{name}** - in `{file}` - import with: `from {app}.models import {name}`")

            output.append("")
            output.append("**If your task requires relationships to these models:**")
            output.append("1. Add import at top: `from {app}.models import {ModelName}`")
            output.append("2. Use imported class in ForeignKey: `ForeignKey(ModelName, ...)`")
            output.append("3. NEVER use string references like `ForeignKey('{ModelName}', ...)`")
            output.append("")

        return "\n".join(output)
