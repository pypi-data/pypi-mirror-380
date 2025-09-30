"""Base interface for database backends."""

from abc import ABC, abstractmethod
from typing import Protocol

from sifts.io.db.types import AnalysisFacet, SnippetFacet


class DatabaseBackend(ABC):
    """Abstract base class for database backends."""

    @abstractmethod
    async def startup(self) -> None:
        """Initialize the database connection."""
        ...

    @abstractmethod
    async def shutdown(self) -> None:
        """Close the database connection."""
        ...

    @abstractmethod
    async def insert_snippet(self, snippet: SnippetFacet) -> None:
        """Insert a snippet into the database."""
        ...

    @abstractmethod
    async def insert_analysis(self, analysis: AnalysisFacet) -> None:
        """Insert an analysis result into the database."""
        ...

    @abstractmethod
    async def get_snippets_by_root(self, group_name: str, root_id: str) -> list[SnippetFacet]:
        """Get all snippets for a specific root."""
        ...

    @abstractmethod
    async def get_snippets_by_file_path(
        self,
        group_name: str,
        root_id: str,
        file_path: str,
    ) -> list[SnippetFacet]:
        """Get all snippets for a specific file path."""
        ...

    @abstractmethod
    async def get_analyses_for_snippet(
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
        snippet_hash: str,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a specific snippet and version."""
        ...

    @abstractmethod
    async def get_analyses_by_file_path_version(
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a file path within a given version."""
        ...

    @abstractmethod
    async def get_analyses_for_snippet_vulnerability(  # noqa: PLR0913
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
        snippet_hash: str,
        vulnerability_id: str,
    ) -> list[AnalysisFacet]:
        """Get analyses for a specific snippet and vulnerability."""
        ...

    @abstractmethod
    async def get_snippet_by_hash(
        self,
        group_name: str,
        root_id: str,
        file_path: str,
        snippet_hash: str,
    ) -> SnippetFacet | None:
        """Get a specific snippet by its hash."""
        ...

    @abstractmethod
    async def get_analyses_by_root(
        self,
        group_name: str,
        root_id: str,
        version: str,
        commit: str | None = None,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a root, optionally filtered by commit."""
        ...


class DatabaseBackendProtocol(Protocol):
    """Protocol for database backend compatibility."""

    async def startup(self) -> None: ...
    async def shutdown(self) -> None: ...
    async def insert_snippet(self, snippet: SnippetFacet) -> None: ...
    async def insert_analysis(self, analysis: AnalysisFacet) -> None: ...
    async def get_snippets_by_root(self, group_name: str, root_id: str) -> list[SnippetFacet]: ...
    async def get_snippets_by_file_path(
        self, group_name: str, root_id: str, file_path: str
    ) -> list[SnippetFacet]: ...
    async def get_analyses_for_snippet(
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
        snippet_hash: str,
    ) -> list[AnalysisFacet]: ...
    async def get_analyses_by_file_path_version(
        self, group_name: str, root_id: str, version: str, file_path: str
    ) -> list[AnalysisFacet]: ...
    async def get_analyses_for_snippet_vulnerability(  # noqa: PLR0913
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
        snippet_hash: str,
        vulnerability_id: str,
    ) -> list[AnalysisFacet]: ...
    async def get_snippet_by_hash(
        self, group_name: str, root_id: str, file_path: str, snippet_hash: str
    ) -> SnippetFacet | None: ...
    async def get_analyses_by_root(
        self, group_name: str, root_id: str, version: str, commit: str | None = None
    ) -> list[AnalysisFacet]: ...
