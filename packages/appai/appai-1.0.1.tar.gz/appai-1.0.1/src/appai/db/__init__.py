"""Database directory for pre-built vector indexes."""

from pathlib import Path

# Database directory inside aiapp package
DB_DIR = Path(__file__).parent

__all__ = ["DB_DIR"]
