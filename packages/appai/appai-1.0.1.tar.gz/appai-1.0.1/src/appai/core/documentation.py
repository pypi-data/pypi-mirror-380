"""Documentation engine with vector search and pattern extraction."""

import hashlib
import logging
from pathlib import Path
from typing import List, Dict, Optional

from aiapp.docs import BUILTIN_DOCS_DIR
from aiapp.db import DB_DIR

logger = logging.getLogger(__name__)


class DocumentationEngine:
    """Pre-loaded documentation with semantic understanding and vector search."""

    def __init__(
        self,
        docs_path: Optional[Path] = None,
        framework: str = "django",
        include_builtin: bool = True
    ):
        """
        Initialize documentation engine.

        Args:
            docs_path: Custom documentation path (optional)
            framework: Target framework (django, nextjs, etc.)
            include_builtin: Include built-in aiapp documentation (default: True)
        """
        self.framework = framework
        self.include_builtin = include_builtin

        # Use internal DB directory instead of ~/.aiapp
        self.db_path = DB_DIR / f"{framework}_docs"
        self.db_path.mkdir(parents=True, exist_ok=True)

        # Determine documentation sources
        self.doc_paths = self._resolve_doc_paths(docs_path, framework, include_builtin)

        # ChromaDB (optional)
        self.client = None
        self.collection = None

        # Try to initialize ChromaDB
        self._init_chromadb()

        # Load documentation
        self._load_docs()

    def _resolve_doc_paths(
        self,
        custom_path: Optional[Path],
        framework: str,
        include_builtin: bool
    ) -> List[Path]:
        """
        Resolve documentation paths from custom and/or built-in sources.

        Args:
            custom_path: Custom documentation path
            framework: Target framework
            include_builtin: Include built-in docs

        Returns:
            List of paths to load documentation from
        """
        paths = []

        # Add built-in documentation if enabled
        if include_builtin:
            builtin_framework_path = BUILTIN_DOCS_DIR / framework
            if builtin_framework_path.exists():
                paths.append(builtin_framework_path)
                logger.info(f"📚 Using built-in {framework} documentation")
            else:
                logger.warning(
                    f"⚠️  Built-in {framework} docs not found at {builtin_framework_path}"
                )

        # Add custom documentation if provided
        if custom_path:
            if custom_path.exists():
                paths.append(custom_path)
                logger.info(f"📚 Using custom documentation from {custom_path}")
            else:
                logger.warning(f"⚠️  Custom docs path does not exist: {custom_path}")

        if not paths:
            logger.warning("⚠️  No documentation sources available")

        return paths

    def _init_chromadb(self):
        """Initialize ChromaDB if available."""
        try:
            import chromadb

            # Use internal DB path for vector storage
            self.client = chromadb.PersistentClient(path=str(self.db_path))
            self.collection = self._get_or_create_collection()
            logger.info(f"✅ ChromaDB initialized at {self.db_path}")
        except ImportError:
            logger.warning(
                "⚠️  ChromaDB not available, using simple pattern matching. "
                "Install with: pip install chromadb"
            )
        except Exception as e:
            logger.warning(f"⚠️  Failed to initialize ChromaDB: {e}")

    def _get_or_create_collection(self):
        """Get or create collection for framework."""
        if not self.client:
            return None

        collection_name = f"{self.framework}_docs"

        try:
            return self.client.get_collection(name=collection_name)
        except Exception:
            return self.client.create_collection(
                name=collection_name,
                metadata={"framework": self.framework}
            )

    def _load_docs(self):
        """Load and index documentation from all sources."""
        if not self.doc_paths:
            logger.warning("No documentation paths to load")
            return

        # Check if already loaded
        if self.collection and self.collection.count() > 0:
            logger.info(f"📚 Using cached docs ({self.collection.count()} chunks)")
            return

        logger.info(f"📖 Loading {self.framework} documentation from {len(self.doc_paths)} sources")

        # Find all markdown files from all sources
        all_doc_files = []
        for doc_path in self.doc_paths:
            doc_files = list(doc_path.rglob("*.md"))
            all_doc_files.extend(doc_files)
            logger.info(f"  • Found {len(doc_files)} files in {doc_path.name}")

        if not all_doc_files:
            logger.warning("No .md files found in any documentation source")
            return

        # If ChromaDB available, index documents
        if self.collection:
            self._index_documents(all_doc_files)
        else:
            logger.info(f"Found {len(all_doc_files)} documentation files (no indexing)")

    def _index_documents(self, doc_files: List[Path]):
        """Index documents into ChromaDB."""
        chunks = []
        metadatas = []
        ids = []

        for doc_file in doc_files:
            try:
                content = doc_file.read_text(encoding="utf-8")
            except Exception as e:
                logger.warning(f"Failed to read {doc_file}: {e}")
                continue

            # Determine source (builtin or custom)
            source = "builtin"
            relative_path = doc_file.name  # fallback

            for doc_path in self.doc_paths:
                try:
                    relative_path = str(doc_file.relative_to(doc_path))
                    if doc_path == (BUILTIN_DOCS_DIR / self.framework):
                        source = "builtin"
                    else:
                        source = "custom"
                    break
                except ValueError:
                    continue

            # Split into chunks
            file_chunks = self._split_content(content)

            for idx, chunk in enumerate(file_chunks):
                # Use absolute path + index to ensure unique IDs across sources
                chunk_id = hashlib.md5(
                    f"{source}:{relative_path}_{idx}_{len(chunk)}".encode()
                ).hexdigest()

                chunks.append(chunk)
                metadatas.append({
                    "file": doc_file.name,
                    "path": relative_path,
                    "source": source,
                    "framework": self.framework,  # NEW: Add framework identifier
                    "chunk_idx": idx
                })
                ids.append(chunk_id)

        # Add to collection
        if chunks:
            self.collection.add(
                documents=chunks,
                metadatas=metadatas,
                ids=ids
            )

            logger.info(f"✅ Indexed {len(chunks)} chunks from {len(doc_files)} files")

    def _split_content(self, content: str, chunk_size: int = 1000) -> List[str]:
        """Split content into chunks for vector search."""
        # Simple split by paragraphs
        paragraphs = content.split("\n\n")

        chunks = []
        current = []
        current_size = 0

        for para in paragraphs:
            para_size = len(para)

            if current_size + para_size > chunk_size and current:
                chunks.append("\n\n".join(current))
                current = [para]
                current_size = para_size
            else:
                current.append(para)
                current_size += para_size

        if current:
            chunks.append("\n\n".join(current))

        return chunks

    def search_patterns(
        self,
        query: str,
        category: Optional[str] = None,
        top_k: int = 5
    ) -> List[Dict]:
        """
        Search for relevant patterns using vector search.

        Args:
            query: Search query
            category: Optional category filter
            top_k: Number of results to return

        Returns:
            List of pattern dictionaries with content and metadata
        """
        if not self.collection:
            logger.warning("ChromaDB not available, returning empty patterns")
            return []

        try:
            # Build where clause if category specified
            where = {"category": category} if category else None

            results = self.collection.query(
                query_texts=[query],
                n_results=min(top_k, self.collection.count()),
                where=where
            )

            patterns = []
            if results and results.get('documents'):
                for i in range(len(results['documents'][0])):
                    patterns.append({
                        "content": results['documents'][0][i],
                        "metadata": results['metadatas'][0][i],
                        "score": results['distances'][0][i] if 'distances' in results else 1.0
                    })

            return patterns

        except Exception as e:
            logger.error(f"Pattern search failed: {e}")
            return []

    def to_prompt_injection(self, category: Optional[str] = None) -> str:
        """
        Generate prompt injection for agents with relevant documentation.

        Args:
            category: Optional category to filter patterns

        Returns:
            Formatted documentation string for prompt injection
        """
        if not self.collection:
            return f"## 📚 {self.framework.title()} Documentation\n\nDocumentation indexed but ChromaDB not available."

        # Get relevant patterns
        if category:
            patterns = self.search_patterns(f"{category} patterns", category=category, top_k=3)
        else:
            patterns = self.search_patterns("framework overview", top_k=3)

        if not patterns:
            return f"## 📚 {self.framework.title()} Documentation\n\nNo patterns found."

        sections = [f"## 📚 {self.framework.title()} Documentation\n"]

        for pattern in patterns:
            file_name = pattern['metadata'].get('file', 'Unknown')
            sections.append(f"### From {file_name}")
            sections.append(pattern['content'])
            sections.append("")

        return "\n".join(sections)
