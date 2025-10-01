"""Public API for memg-core - designed for long-running servers.

Provides MemgClient for explicit initialization and module-level functions for
environment-based usage.
"""

from __future__ import annotations

import os
from typing import Any

from ..core.config import get_config
from ..core.interfaces.embedder_protocol import EmbedderProtocol
from ..core.models import SearchResult
from ..core.pipelines.indexer import MemoryService, create_memory_service
from ..core.pipelines.retrieval import SearchService, create_search_service
from ..core.yaml_translator import YamlTranslator
from ..utils.db_clients import DatabaseClients


class MemgClient:
    """Client for memg-core operations - initialize once, use throughout server lifetime.

    Provides a clean interface for memory operations with explicit resource management.
    """

    def __init__(self, yaml_path: str, db_path: str, embedder: EmbedderProtocol | None = None):
        """Initialize client for long-running server usage.

        Args:
            yaml_path: Path to YAML schema configuration file.
            db_path: Base directory path for database storage.
            embedder: Optional custom embedder. If provided, will be used instead
                of the default FastEmbed-based embedder. Must implement EmbedderProtocol
                (get_embedding and get_embeddings methods).
        """
        self._db_clients = DatabaseClients(yaml_path=yaml_path, embedder=embedder)
        config = get_config()
        self._db_clients.init_dbs(db_path=db_path, db_name=config.memg.qdrant_collection_name)

        self._memory_service = create_memory_service(self._db_clients)
        self._search_service = create_search_service(self._db_clients)

        if not all([self._memory_service, self._search_service]):
            raise RuntimeError("Failed to initialize memg-core services")

    def add_memory(self, memory_type: str, payload: dict[str, Any], user_id: str) -> str:
        """Add memory and return HRID.

        Args:
            memory_type: Entity type from YAML schema (e.g., 'task', 'note').
            payload: Memory data conforming to YAML schema.
            user_id: Owner of the memory.

        Returns:
            str: Human-readable ID (HRID) for the created memory.
        """
        return self._memory_service.add_memory(memory_type, payload, user_id)

    def search(
        self,
        query: str,
        user_id: str,
        memory_type: str | None = None,
        limit: int = 10,
        score_threshold: float | None = None,
        decay_rate: float | None = None,
        decay_threshold: float | None = None,
        datetime_format: str | None = None,
        **kwargs,
    ) -> SearchResult:
        """Search memories with explicit seed/neighbor separation.

        Args:
            query: Text to search for.
            user_id: User ID for filtering results.
            memory_type: Optional memory type filter.
            limit: Maximum number of results to return.
            score_threshold: Minimum similarity score threshold (0.0-1.0).
            decay_rate: Score decay factor per hop (default: 1.0 = no decay).
            decay_threshold: Explicit neighbor score threshold (overrides decay_rate).
            datetime_format: Optional datetime format string (e.g., "%Y-%m-%d %H:%M:%S").
            **kwargs: Additional search parameters.

        Returns:
            SearchResult: Search result with explicit seed/neighbor separation,
                including full payloads for seeds and relationships.
        """
        clean_query = query.strip() if query else ""
        return self._search_service.search(
            clean_query,
            user_id,
            memory_type=memory_type,
            limit=limit,
            score_threshold=score_threshold,
            decay_rate=decay_rate,
            decay_threshold=decay_threshold,
            datetime_format=datetime_format,
            **kwargs,
        )

    def delete_memory(self, hrid: str, user_id: str, memory_type: str | None = None) -> bool:
        """Delete memory by HRID.

        Args:
            hrid: Human-readable ID of the memory to delete.
            user_id: User ID for ownership verification.
            memory_type: Optional memory type hint.

        Returns:
            bool: True if deletion succeeded, False otherwise.
        """
        if memory_type is None:
            memory_type = "_".join(hrid.split("_")[:-1])
        return self._memory_service.delete_memory(hrid, memory_type, user_id)

    def update_memory(
        self,
        hrid: str,
        payload_updates: dict[str, Any],
        user_id: str,
        memory_type: str | None = None,
    ) -> bool:
        """Update memory with partial payload changes (patch-style update).

        Args:
            hrid: Memory HRID to update.
            payload_updates: Dictionary of fields to update (only changed fields).
            user_id: User ID for ownership verification.
            memory_type: Optional memory type hint (inferred from HRID if not provided).

        Returns:
            bool: True if update succeeded, False otherwise.
        """
        return self._memory_service.update_memory(hrid, payload_updates, user_id, memory_type)

    def add_relationship(
        self,
        from_memory_hrid: str,
        to_memory_hrid: str,
        relation_type: str,
        from_memory_type: str,
        to_memory_type: str,
        user_id: str,
        properties: dict[str, Any] | None = None,
    ) -> None:
        """Add relationship between memories.

        Args:
            from_memory_hrid: Source memory HRID.
            to_memory_hrid: Target memory HRID.
            relation_type: Relationship type from YAML schema.
            from_memory_type: Source memory entity type.
            to_memory_type: Target memory entity type.
            user_id: User ID for ownership verification.
            properties: Optional relationship properties.
        """
        self._memory_service.add_relationship(
            from_memory_hrid,
            to_memory_hrid,
            relation_type,
            from_memory_type,
            to_memory_type,
            user_id,
            properties,
        )

    def delete_relationship(
        self,
        from_memory_hrid: str,
        to_memory_hrid: str,
        relation_type: str,
        from_memory_type: str | None = None,
        to_memory_type: str | None = None,
        user_id: str | None = None,
    ) -> bool:
        """Delete relationship between memories.

        Args:
            from_memory_hrid: Source memory HRID.
            to_memory_hrid: Target memory HRID.
            relation_type: Relationship type from YAML schema.
            from_memory_type: Source memory entity type (inferred from HRID if not provided).
            to_memory_type: Target memory entity type (inferred from HRID if not provided).
            user_id: User ID for ownership verification (required).

        Returns:
            bool: True if deletion succeeded, False if relationship not found.
        """
        return self._memory_service.delete_relationship(
            from_memory_hrid,
            to_memory_hrid,
            relation_type,
            from_memory_type,
            to_memory_type,
            user_id,
        )

    def get_memory(
        self,
        hrid: str,
        user_id: str,
        memory_type: str | None = None,
        include_neighbors: bool = False,
        hops: int = 1,
        relation_types: list[str] | None = None,
        neighbor_limit: int = 5,
    ) -> SearchResult | None:
        """Get a single memory by HRID with optional neighbor expansion.

        Args:
            hrid: Human-readable identifier of the memory.
            user_id: User ID for ownership verification.
            memory_type: Optional memory type hint (inferred from HRID if not provided).
            include_neighbors: Whether to include neighbor nodes via graph traversal.
            hops: Number of hops for neighbor expansion (default 1).
            relation_types: Filter by specific relationship types (None = all relations).
            neighbor_limit: Maximum neighbors to return per hop (default 5).

        Returns:
            SearchResult | None: SearchResult with single memory as seed and optional neighbors, or None if not found.
        """
        return self._search_service.get_memory(
            hrid,
            user_id,
            memory_type,
            include_neighbors,
            hops,
            relation_types,
            neighbor_limit,
        )

    def get_memories(
        self,
        user_id: str,
        memory_type: str | None = None,
        filters: dict[str, Any] | None = None,
        limit: int = 50,
        offset: int = 0,
        include_neighbors: bool = False,
        hops: int = 1,
    ) -> SearchResult:
        """Get multiple memories with filtering and optional graph expansion.

        Args:
            user_id: User ID for ownership verification.
            memory_type: Optional memory type filter (e.g., "task", "note").
            filters: Optional field filters (e.g., {"status": "open", "priority": "high"}).
            limit: Maximum number of memories to return (default 50).
            offset: Number of memories to skip for pagination (default 0).
            include_neighbors: Whether to include neighbor nodes via graph traversal.
            hops: Number of hops for neighbor expansion (default 1).

        Returns:
            SearchResult: SearchResult with memories as seeds and optional neighbors.
        """
        return self._search_service.get_memories(
            user_id, memory_type, filters, limit, offset, include_neighbors, hops
        )

    def close(self):
        """Close client and cleanup resources.

        Should be called when the client is no longer needed to free database connections.
        """
        if hasattr(self, "_db_clients") and self._db_clients:
            self._db_clients.close()


# ----------------------------- ENVIRONMENT-BASED SINGLETON API -----------------------------

_CLIENT: MemgClient | None = None


def _get_client() -> MemgClient:
    """Get or create singleton client from environment variables.

    Returns:
        MemgClient: Singleton client instance.

    Raises:
        RuntimeError: If required environment variables are not set.
    """
    global _CLIENT
    if _CLIENT is None:
        yaml_path = os.environ.get("MEMG_YAML_PATH")
        db_path = os.environ.get("MEMG_DB_PATH")

        if not yaml_path or not db_path:
            raise RuntimeError("MEMG_YAML_PATH and MEMG_DB_PATH environment variables must be set")

        _CLIENT = MemgClient(yaml_path, db_path)
    return _CLIENT


def add_memory(memory_type: str, payload: dict[str, Any], user_id: str) -> str:
    """Add memory using environment-based client.

    Args:
        memory_type: Entity type from YAML schema (e.g., 'task', 'note').
        payload: Memory data conforming to YAML schema.
        user_id: Owner of the memory.

    Returns:
        str: Human-readable ID (HRID) for the created memory.
    """
    return _get_client().add_memory(memory_type, payload, user_id)


def search(
    query: str,
    user_id: str,
    memory_type: str | None = None,
    limit: int = 10,
    score_threshold: float | None = None,
    decay_rate: float | None = None,
    decay_threshold: float | None = None,
    datetime_format: str | None = None,
    **kwargs,
) -> SearchResult:
    """Search memories using environment-based client.

    Args:
        query: Text to search for.
        user_id: User ID for filtering results.
        memory_type: Optional memory type filter.
        limit: Maximum number of results to return.
        score_threshold: Minimum similarity score threshold (0.0-1.0).
        decay_rate: Score decay factor per hop (default: 1.0 = no decay).
        decay_threshold: Explicit neighbor score threshold (overrides decay_rate).
        datetime_format: Optional datetime format string (e.g., "%Y-%m-%d %H:%M:%S").
        **kwargs: Additional search parameters.

    Returns:
        SearchResult: Search result with explicit seed/neighbor separation,
            including full payloads for seeds and relationships.
    """
    return _get_client().search(
        query,
        user_id,
        memory_type,
        limit,
        score_threshold=score_threshold,
        decay_rate=decay_rate,
        decay_threshold=decay_threshold,
        datetime_format=datetime_format,
        **kwargs,
    )


def delete_memory(hrid: str, user_id: str, memory_type: str | None = None) -> bool:
    """Delete memory using environment-based client.

    Args:
        hrid: Human-readable ID of the memory to delete.
        user_id: User ID for ownership verification.
        memory_type: Optional memory type hint.

    Returns:
        bool: True if deletion succeeded, False otherwise.
    """
    return _get_client().delete_memory(hrid, user_id, memory_type)


def update_memory(
    hrid: str,
    payload_updates: dict[str, Any],
    user_id: str,
    memory_type: str | None = None,
) -> bool:
    """Update memory using environment-based client.

    Args:
        hrid: Memory HRID to update.
        payload_updates: Dictionary of fields to update (only changed fields).
        user_id: User ID for ownership verification.
        memory_type: Optional memory type hint (inferred from HRID if not provided).

    Returns:
        bool: True if update succeeded, False otherwise.
    """
    return _get_client().update_memory(hrid, payload_updates, user_id, memory_type)


def add_relationship(
    from_memory_hrid: str,
    to_memory_hrid: str,
    relation_type: str,
    from_memory_type: str,
    to_memory_type: str,
    user_id: str,
    properties: dict[str, Any] | None = None,
) -> None:
    """Add relationship using environment-based client.

    Args:
        from_memory_hrid: Source memory HRID.
        to_memory_hrid: Target memory HRID.
        relation_type: Relationship type from YAML schema.
        from_memory_type: Source memory entity type.
        to_memory_type: Target memory entity type.
        user_id: User ID for ownership verification.
        properties: Optional relationship properties.
    """
    _get_client().add_relationship(
        from_memory_hrid,
        to_memory_hrid,
        relation_type,
        from_memory_type,
        to_memory_type,
        user_id,
        properties,
    )


def delete_relationship(
    from_memory_hrid: str,
    to_memory_hrid: str,
    relation_type: str,
    from_memory_type: str | None = None,
    to_memory_type: str | None = None,
    user_id: str | None = None,
) -> bool:
    """Delete relationship using environment-based client.

    Args:
        from_memory_hrid: Source memory HRID.
        to_memory_hrid: Target memory HRID.
        relation_type: Relationship type from YAML schema.
        from_memory_type: Source memory entity type (inferred from HRID if not provided).
        to_memory_type: Target memory entity type (inferred from HRID if not provided).
        user_id: User ID for ownership verification (required).

    Returns:
        bool: True if deletion succeeded, False if relationship not found.
    """
    return _get_client().delete_relationship(
        from_memory_hrid,
        to_memory_hrid,
        relation_type,
        from_memory_type,
        to_memory_type,
        user_id,
    )


def get_memory(
    hrid: str,
    user_id: str,
    memory_type: str | None = None,
    include_neighbors: bool = False,
    hops: int = 1,
    relation_types: list[str] | None = None,
    neighbor_limit: int = 5,
) -> SearchResult | None:
    """Get memory using environment-based client with optional neighbor expansion.

    Args:
        hrid: Human-readable identifier of the memory.
        user_id: User ID for ownership verification.
        memory_type: Optional memory type hint (inferred from HRID if not provided).
        include_neighbors: Whether to include neighbor nodes via graph traversal.
        hops: Number of hops for neighbor expansion (default 1).
        relation_types: Filter by specific relationship types (None = all relations).
        neighbor_limit: Maximum neighbors to return per hop (default 5).

    Returns:
        SearchResult | None: SearchResult with single memory as seed and optional neighbors, or None if not found.
    """
    return _get_client().get_memory(
        hrid, user_id, memory_type, include_neighbors, hops, relation_types, neighbor_limit
    )


def get_memories(
    user_id: str,
    memory_type: str | None = None,
    filters: dict[str, Any] | None = None,
    limit: int = 50,
    offset: int = 0,
    include_neighbors: bool = False,
    hops: int = 1,
) -> SearchResult:
    """Get memories using environment-based client.

    Args:
        user_id: User ID for ownership verification.
        memory_type: Optional memory type filter (e.g., "task", "note").
        filters: Optional field filters (e.g., {"status": "open", "priority": "high"}).
        limit: Maximum number of memories to return (default 50).
        offset: Number of memories to skip for pagination (default 0).
        include_neighbors: Whether to include neighbor nodes via graph traversal.
        hops: Number of hops for neighbor expansion (default 1).

    Returns:
        SearchResult: SearchResult with memories as seeds and optional neighbors.
    """
    return _get_client().get_memories(
        user_id, memory_type, filters, limit, offset, include_neighbors, hops
    )


def shutdown_services():
    """Shutdown singleton client.

    Closes database connections and cleans up resources.
    """
    global _CLIENT
    if _CLIENT:
        _CLIENT.close()
        _CLIENT = None


# Legacy compatibility for MCP server
def get_services() -> tuple[MemoryService, SearchService, YamlTranslator]:
    """Get services from singleton client (MCP server compatibility).

    Returns:
        tuple[MemoryService, SearchService, YamlTranslator]: Service instances for direct access.
    """
    client = _get_client()
    yaml_translator = YamlTranslator(os.environ.get("MEMG_YAML_PATH"))
    return client._memory_service, client._search_service, yaml_translator
