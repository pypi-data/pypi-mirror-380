"""
Common Exclusion Patterns.

Shared constants for file and directory exclusion patterns used across
the aiapp system for consistent filtering behavior.

Copied from old aiapp implementation - proven utility.
"""

from typing import Set, FrozenSet

# Python-specific exclusions
PYTHON_EXCLUDES: FrozenSet[str] = frozenset({
    "__pycache__", "*.pyc", "*.pyo", "*.pyd", ".Python",
    "build", "develop-eggs", "dist", "downloads", "eggs", ".eggs",
    "lib", "lib64", "parts", "sdist", "var", "wheels", "*.egg-info",
    ".installed.cfg", "*.egg", "MANIFEST",
})

# Virtual environment exclusions
VENV_EXCLUDES: FrozenSet[str] = frozenset({
    "venv", "env", ".venv", ".env", "ENV", "env.bak", "venv.bak",
    ".virtualenv", "virtualenv", "pyvenv.cfg",
})

# Testing and coverage exclusions
TESTING_EXCLUDES: FrozenSet[str] = frozenset({
    "htmlcov", ".tox", ".nox", ".coverage", ".coverage.*", ".cache",
    "nosetests.xml", "coverage.xml", "*.cover", ".hypothesis", ".pytest_cache",
})

# Jupyter and IPython exclusions
JUPYTER_EXCLUDES: FrozenSet[str] = frozenset({
    ".ipynb_checkpoints", "profile_default", "ipython_config.py",
})

# Type checkers and linters exclusions
LINTER_EXCLUDES: FrozenSet[str] = frozenset({
    ".mypy_cache", ".dmypy.json", "dmypy.json", ".pyre",
})

# JavaScript/Node.js exclusions
NODEJS_EXCLUDES: FrozenSet[str] = frozenset({
    "node_modules", "npm-debug.log*", "yarn-debug.log*", "yarn-error.log*",
    "lerna-debug.log*", ".npm", ".eslintcache", ".stylelintcache",
    ".rpt2_cache", ".rts2_cache_cjs", ".rts2_cache_es", ".rts2_cache_umd",
    ".nyc_output", ".grunt", "bower_components", ".lock-wscript",
    ".wafpickle-N", ".node_repl_history", "*.tgz", ".yarn-integrity",
    ".parcel-cache", ".next", ".nuxt", ".vuepress/dist", ".serverless",
    ".fusebox", ".dynamodb", ".tern-port", ".vscode-test",
    ".yarn/cache", ".yarn/unplugged", ".yarn/build-state.yml",
    ".yarn/install-state.gz", ".pnp.*",
})

# Build outputs and caches exclusions
BUILD_EXCLUDES: FrozenSet[str] = frozenset({
    "dist", "build", "out", "target", "bin", "obj", ".webpack",
    ".rollup.cache", ".vite", ".svelte-kit", ".react", ".cache",
    "public", ".docusaurus", ".turbo",
})

# IDEs and editors exclusions
IDE_EXCLUDES: FrozenSet[str] = frozenset({
    ".idea", ".vscode", "*.swp", "*.swo", "*~",
})

# OS files exclusions
OS_EXCLUDES: FrozenSet[str] = frozenset({
    ".DS_Store", ".DS_Store?", "._*", ".Spotlight-V100", ".Trashes",
    "ehthumbs.db", "Thumbs.db",
})

# Version control exclusions
VCS_EXCLUDES: FrozenSet[str] = frozenset({
    ".git", ".svn", ".hg", ".bzr",
})

# Logs and temporary files exclusions
TEMP_EXCLUDES: FrozenSet[str] = frozenset({
    "logs", "*.log", "log", "tmp", "temp", ".tmp", ".temp",
})

# Documentation-specific exclusions (lighter set for docs scanning)
DOC_LIGHT_EXCLUDES: FrozenSet[str] = frozenset({
    ".git", ".svn", ".hg", ".bzr",  # VCS
    "node_modules", "venv", ".venv", "env", ".env",  # Dependencies
    "__pycache__", ".pytest_cache", ".mypy_cache",  # Python cache
    "build", "dist", "out", "target", "_build", ".build",  # Build outputs
    ".idea", ".vscode", ".vs",  # IDEs
    "tmp", "temp", ".tmp", ".temp",  # Temporary
    ".DS_Store", "Thumbs.db",  # OS files
})

# Complete standard exclusions (for comprehensive scanning)
STANDARD_EXCLUDES: FrozenSet[str] = frozenset(
    PYTHON_EXCLUDES |
    VENV_EXCLUDES |
    TESTING_EXCLUDES |
    JUPYTER_EXCLUDES |
    LINTER_EXCLUDES |
    NODEJS_EXCLUDES |
    BUILD_EXCLUDES |
    IDE_EXCLUDES |
    OS_EXCLUDES |
    VCS_EXCLUDES |
    TEMP_EXCLUDES
)

# Documentation-specific exclusions (balanced set)
DOC_EXCLUDES: FrozenSet[str] = frozenset(
    DOC_LIGHT_EXCLUDES |
    PYTHON_EXCLUDES |  # Include Python excludes for mixed repos
    NODEJS_EXCLUDES    # Include Node excludes for mixed repos
)


def get_excludes_for_context(context: str) -> Set[str]:
    """
    Get appropriate exclusion patterns for specific context.

    Args:
        context: Context type ('standard', 'documentation', 'light', 'python', 'nodejs')

    Returns:
        Set of exclusion patterns
    """
    context_map = {
        'standard': STANDARD_EXCLUDES,
        'documentation': DOC_EXCLUDES,
        'light': DOC_LIGHT_EXCLUDES,
        'python': PYTHON_EXCLUDES | VENV_EXCLUDES | TESTING_EXCLUDES,
        'nodejs': NODEJS_EXCLUDES | BUILD_EXCLUDES,
        'vcs': VCS_EXCLUDES,
        'build': BUILD_EXCLUDES,
        'temp': TEMP_EXCLUDES,
        'ide': IDE_EXCLUDES,
    }

    return set(context_map.get(context, STANDARD_EXCLUDES))


def merge_excludes(*exclude_sets: Set[str]) -> Set[str]:
    """
    Merge multiple exclusion sets.

    Args:
        exclude_sets: Variable number of exclusion sets

    Returns:
        Merged set of exclusions
    """
    result = set()
    for exclude_set in exclude_sets:
        result.update(exclude_set)
    return result
