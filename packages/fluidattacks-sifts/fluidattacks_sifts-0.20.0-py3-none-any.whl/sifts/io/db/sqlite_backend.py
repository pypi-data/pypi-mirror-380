"""SQLite backend implementation."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from sifts.io.db.base import DatabaseBackend
from sifts.io.db.types import AnalysisFacet, SafeFacet, SnippetFacet, VulnerableFacet


class SQLiteBackend(DatabaseBackend):
    """SQLite implementation of the database backend."""

    def __init__(self, database_path: str | Path = "sifts.db") -> None:
        """Initialize SQLite backend."""
        self.database_path = Path(database_path)
        self.connection: sqlite3.Connection | None = None

    async def startup(self) -> None:
        """Initialize the SQLite connection and create tables."""
        if self.connection is not None:
            return

        # Ensure the directory exists
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(str(self.database_path))
        self.connection.row_factory = sqlite3.Row  # Enable column access by name

        # Create tables
        await self._create_tables()

    async def shutdown(self) -> None:
        """Close the SQLite connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def _get_connection(self) -> sqlite3.Connection:
        """Get the SQLite connection."""
        if self.connection is None:
            msg = "SQLite backend not initialized. Call startup() first."
            raise RuntimeError(msg)
        return self.connection

    async def _create_tables(self) -> None:
        """Create the necessary tables."""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Create snippets table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS snippets (
                group_name TEXT NOT NULL,
                root_id TEXT NOT NULL,
                file_path TEXT NOT NULL,
                snippet_hash TEXT NOT NULL,
                hash_type TEXT NOT NULL,
                language TEXT NOT NULL,
                last_seen_at TEXT NOT NULL,
                snippet_content TEXT NOT NULL,
                line_start INTEGER NOT NULL,
                line_end INTEGER NOT NULL,
                column_start INTEGER NOT NULL,
                column_end INTEGER NOT NULL,
                byte_start INTEGER NOT NULL,
                byte_end INTEGER NOT NULL,
                name TEXT,
                PRIMARY KEY (group_name, root_id, file_path, snippet_hash)
            )
        """)

        # Create analysis table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis (
                group_name TEXT NOT NULL,
                root_id TEXT NOT NULL,
                version TEXT NOT NULL,
                file_path TEXT NOT NULL,
                path TEXT NOT NULL,
                snippet_hash TEXT NOT NULL,
                vulnerability_id_candidates TEXT NOT NULL,  -- JSON array
                analyzed_at TEXT NOT NULL,
                candidate_index INTEGER,
                "commit" TEXT NOT NULL,
                cost REAL NOT NULL,
                input_tokens INTEGER NOT NULL,
                output_tokens INTEGER NOT NULL,
                total_tokens INTEGER NOT NULL,
                vulnerable BOOLEAN NOT NULL,
                ranking_score REAL,
                reason TEXT NOT NULL,
                vulnerable_lines TEXT,  -- JSON array
                suggested_criteria_code TEXT,
                suggested_finding_title TEXT,
                trace_id TEXT,
                PRIMARY KEY (group_name, root_id, version,
                file_path, snippet_hash, vulnerability_id_candidates)
            )
        """)

        # Create indexes for better performance
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_snippets_group_root
            ON snippets (group_name, root_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_snippets_file_path
            ON snippets (group_name, root_id, file_path)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_analysis_group_root_version
            ON analysis (group_name, root_id, version)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_analysis_snippet
            ON analysis (group_name, root_id, version, file_path, snippet_hash)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_analysis_vulnerable
            ON analysis (group_name, root_id, version, vulnerable)
        """)

        conn.commit()

    @staticmethod
    def _serialize_for_sqlite(value: Any) -> Any:  # noqa: ANN401
        """Convert Python types to SQLite-compatible types."""
        if isinstance(value, datetime):
            return value.isoformat()
        if isinstance(value, (list, tuple, set)):
            return json.dumps(list(value))
        if isinstance(value, dict):
            return json.dumps(value)
        return value

    @staticmethod
    def _deserialize_from_sqlite(value: str, field_type: str) -> Any:  # noqa: ANN401
        """Convert SQLite values back to Python types."""
        if field_type in ("vulnerability_id_candidates", "vulnerable_lines") and value:
            return json.loads(value)
        return value

    async def insert_snippet(self, snippet: SnippetFacet) -> None:
        """Insert a snippet into SQLite."""
        conn = self._get_connection()
        cursor = conn.cursor()

        data = snippet.model_dump()
        cursor.execute(
            """
            INSERT OR REPLACE INTO snippets (
                group_name, root_id, file_path, snippet_hash, hash_type, language,
                last_seen_at, snippet_content, line_start, line_end, column_start,
                column_end, byte_start, byte_end, name
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                data["group_name"],
                data["root_id"],
                data["file_path"],
                data["snippet_hash"],
                data["hash_type"],
                data["language"],
                data["last_seen_at"],
                data["snippet_content"],
                data["line_start"],
                data["line_end"],
                data["column_start"],
                data["column_end"],
                data["byte_start"],
                data["byte_end"],
                data.get("name"),
            ),
        )

        conn.commit()

    async def insert_analysis(self, analysis: AnalysisFacet) -> None:
        """Insert an analysis result into SQLite."""
        conn = self._get_connection()
        cursor = conn.cursor()

        data = analysis.model_dump()
        vulnerability_candidates = self._serialize_for_sqlite(data["vulnerability_id_candidates"])
        vulnerable_lines = self._serialize_for_sqlite(data.get("vulnerable_lines", []))

        cursor.execute(
            """
            INSERT OR REPLACE INTO analysis (
                group_name, root_id, version, file_path, path, snippet_hash,
                vulnerability_id_candidates, analyzed_at, candidate_index, "commit",
                cost, input_tokens, output_tokens, total_tokens, vulnerable,
                ranking_score, reason, vulnerable_lines, suggested_criteria_code,
                suggested_finding_title, trace_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                data["group_name"],
                data["root_id"],
                data["version"],
                data["file_path"],
                data["path"],
                data["snippet_hash"],
                vulnerability_candidates,
                data["analyzed_at"].isoformat()
                if isinstance(data["analyzed_at"], datetime)
                else data["analyzed_at"],
                data.get("candidate_index"),
                data["commit"],
                data["cost"],
                data["input_tokens"],
                data["output_tokens"],
                data["total_tokens"],
                data["vulnerable"],
                data.get("ranking_score"),
                data["reason"],
                vulnerable_lines,
                data.get("suggested_criteria_code"),
                data.get("suggested_finding_title"),
                data.get("trace_id"),
            ),
        )

        conn.commit()

    async def get_snippets_by_root(self, group_name: str, root_id: str) -> list[SnippetFacet]:
        """Get all snippets for a specific root."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM snippets
            WHERE group_name = ? AND root_id = ?
        """,
            (group_name, root_id),
        )

        rows = cursor.fetchall()
        return [self._row_to_snippet(row) for row in rows]

    async def get_snippets_by_file_path(
        self,
        group_name: str,
        root_id: str,
        file_path: str,
    ) -> list[SnippetFacet]:
        """Get all snippets for a specific file path."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM snippets
            WHERE group_name = ? AND root_id = ? AND file_path = ?
        """,
            (group_name, root_id, file_path),
        )

        rows = cursor.fetchall()
        return [self._row_to_snippet(row) for row in rows]

    async def get_analyses_for_snippet(
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
        snippet_hash: str,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a specific snippet and version."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM analysis
            WHERE group_name = ? AND root_id = ? AND version = ?
            AND file_path = ? AND snippet_hash = ?
        """,
            (group_name, root_id, version, file_path, snippet_hash),
        )

        rows = cursor.fetchall()
        return [self._row_to_analysis(row) for row in rows]

    async def get_analyses_by_file_path_version(
        self,
        group_name: str,
        root_id: str,
        version: str,
        file_path: str,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a file path within a given version."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM analysis
            WHERE group_name = ? AND root_id = ? AND version = ? AND file_path = ?
        """,
            (group_name, root_id, version, file_path),
        )

        rows = cursor.fetchall()
        return [self._row_to_analysis(row) for row in rows]

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
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM analysis
            WHERE group_name = ? AND root_id = ? AND version = ?
            AND file_path = ? AND snippet_hash = ?
            AND vulnerability_id_candidates LIKE ?
        """,
            (group_name, root_id, version, file_path, snippet_hash, f'%"{vulnerability_id}"%'),
        )

        rows = cursor.fetchall()
        return [self._row_to_analysis(row) for row in rows]

    async def get_snippet_by_hash(
        self,
        group_name: str,
        root_id: str,
        file_path: str,
        snippet_hash: str,
    ) -> SnippetFacet | None:
        """Get a specific snippet by its hash."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM snippets
            WHERE group_name = ? AND root_id = ? AND file_path = ? AND snippet_hash = ?
        """,
            (group_name, root_id, file_path, snippet_hash),
        )

        row = cursor.fetchone()
        if row is None:
            return None

        return self._row_to_snippet(row)

    async def get_analyses_by_root(
        self,
        group_name: str,
        root_id: str,
        version: str,
        commit: str | None = None,
    ) -> list[AnalysisFacet]:
        """Get all analyses for a root, optionally filtered by commit."""
        conn = self._get_connection()
        cursor = conn.cursor()

        query = """
            SELECT * FROM analysis
            WHERE group_name = ? AND root_id = ? AND version = ? AND vulnerable = 1
        """
        params = [group_name, root_id, version]

        if commit:
            query += ' AND "commit" = ?'
            params.append(commit)

        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [self._row_to_analysis(row) for row in rows]

    @staticmethod
    def _row_to_snippet(row: sqlite3.Row) -> SnippetFacet:
        """Convert a SQLite row to a SnippetFacet."""
        return SnippetFacet(
            group_name=row["group_name"],
            root_id=row["root_id"],
            file_path=row["file_path"],
            snippet_hash=row["snippet_hash"],
            line_start=row["line_start"],
            line_end=row["line_end"],
            column_start=row["column_start"],
            column_end=row["column_end"],
            snippet_content=row["snippet_content"],
            hash_type=row["hash_type"],
            language=row["language"],
            last_seen_at=row["last_seen_at"],
            byte_start=row["byte_start"],
            byte_end=row["byte_end"],
            name=row["name"],
        )

    @staticmethod
    def _row_to_analysis(row: sqlite3.Row) -> AnalysisFacet:
        """Convert a SQLite row to an AnalysisFacet."""
        # Parse JSON fields
        vulnerability_candidates = SQLiteBackend._deserialize_from_sqlite(
            row["vulnerability_id_candidates"], "vulnerability_id_candidates"
        )
        vulnerable_lines = SQLiteBackend._deserialize_from_sqlite(
            row["vulnerable_lines"], "vulnerable_lines"
        )

        # Convert analyzed_at to datetime if it's a string
        analyzed_at = row["analyzed_at"]
        if isinstance(analyzed_at, str):
            analyzed_at = datetime.fromisoformat(analyzed_at)

        # Base fields common to both Vulnerable and Safe facets
        base_fields = {
            "group_name": row["group_name"],
            "root_id": row["root_id"],
            "version": row["version"],
            "commit": row["commit"],
            "snippet_hash": row["snippet_hash"],
            "analyzed_at": analyzed_at,
            "file_path": row["file_path"],
            "path": row["path"],
            "cost": row["cost"],
            "candidate_index": row["candidate_index"],
            "trace_id": row["trace_id"],
            "vulnerability_id_candidates": vulnerability_candidates,
            "input_tokens": row["input_tokens"],
            "output_tokens": row["output_tokens"],
            "total_tokens": row["total_tokens"],
            "reason": row["reason"],
        }

        if row["vulnerable"]:
            return VulnerableFacet(
                **base_fields,
                vulnerable=True,
                vulnerable_lines=vulnerable_lines or [],
                ranking_score=row["ranking_score"],
                suggested_criteria_code=row["suggested_criteria_code"],
                suggested_finding_title=row["suggested_finding_title"],
            )
        return SafeFacet(
            **base_fields,
            vulnerable=False,
            vulnerable_lines=vulnerable_lines,
            ranking_score=row["ranking_score"],
            suggested_criteria_code=row["suggested_criteria_code"],
            suggested_finding_title=row["suggested_finding_title"],
        )
