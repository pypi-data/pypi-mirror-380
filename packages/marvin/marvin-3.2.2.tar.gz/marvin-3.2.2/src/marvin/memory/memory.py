import abc
import inspect
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import marvin
from marvin.prompts import Template
from marvin.utilities.logging import get_logger
from marvin.utilities.tools import update_fn

logger = get_logger("marvin.memory")


def sanitize_memory_key(key: str) -> str:
    # Remove any characters that are not alphanumeric or underscore
    return re.sub(r"[^a-zA-Z0-9_]", "", key)


@dataclass(kw_only=True)
class MemoryProvider(abc.ABC):
    def configure(self, memory_key: str) -> None:
        """Configure the provider for a specific memory."""

    @abc.abstractmethod
    async def add(self, memory_key: str, content: str) -> str:
        """Create a new memory and return its ID."""

    @abc.abstractmethod
    async def delete(self, memory_key: str, memory_id: str) -> None:
        """Delete a memory by its ID."""

    @abc.abstractmethod
    async def search(self, memory_key: str, query: str, n: int = 20) -> dict[str, str]:
        """Search for n memories using a string query."""


@dataclass(kw_only=True)
class Memory:
    """A memory module is a partitioned collection of memories that are stored in a
    vector database, configured by a MemoryProvider.
    """

    key: str = field(kw_only=False)
    instructions: str | None = field(
        default=None,
        metadata={
            "description": "Explain what this memory is for and how it should be used.",
        },
    )
    provider: MemoryProvider = field(
        default_factory=lambda: marvin.defaults.memory_provider,
        repr=False,
    )
    auto_use: bool = field(
        default=False,
        metadata={
            "description": "If true, the memory will automatically be queried before the agent is run, using the most recent messages.",
        },
    )
    prompt: str | Path = field(
        default=Path("memory.jinja"),
        metadata={"description": "Template for the memory's prompt"},
        repr=False,
    )

    def __hash__(self) -> int:
        return id(self)

    def __post_init__(self):
        # Validate key
        sanitized = sanitize_memory_key(self.key)
        if sanitized != self.key:
            raise ValueError(
                "Memory key must contain only alphanumeric characters and underscores",
            )

        # Validate and process provider
        if isinstance(self.provider, str):
            self.provider = get_memory_provider(self.provider)
        if self.provider is None:
            raise ValueError(
                inspect.cleandoc(
                    """
                    Memory modules require a MemoryProvider to configure the
                    underlying vector database. No provider was passed as an
                    argument, and no default value has been configured. 
                    
                    For more information on configuring a memory provider, see
                    the [Memory
                    documentation](https://controlflow.ai/patterns/memory), and
                    please review the [default provider
                    guide](https://controlflow.ai/guides/default-memory) for
                    information on configuring a default provider.
                    
                    Please note that if you are using ControlFlow for the first
                    time, this error is expected because ControlFlow does not include
                    vector dependencies by default.
                    """,
                ),
            )

        # Configure provider
        self.provider.configure(self.key)

    def friendly_name(self) -> str:
        return f"<Memory key={self.key}>"

    async def add(self, content: str) -> str:
        return await self.provider.add(self.key, content)

    async def delete(self, memory_id: str) -> None:
        await self.provider.delete(self.key, memory_id)

    async def search(self, query: str, n: int = 20) -> dict[str, str]:
        return await self.provider.search(self.key, query, n)

    def get_tools(self) -> list[Callable[..., Any]]:
        return [
            update_fn(
                self.add,
                name=f"add_memory__{self.key}",
                description=f"Create a new memory in {self.friendly_name()}.",
            ),
            update_fn(
                self.delete,
                name=f"delete_memory__{self.key}",
                description=f"Delete a memory by ID from {self.friendly_name()}.",
            ),
            update_fn(
                self.search,
                name=f"search_memories__{self.key}",
                description=f"Provide a query string to search {self.friendly_name()}. {self.instructions or ''}".rstrip(),
            ),
        ]

    def get_prompt(self) -> str:
        return Template(source=self.prompt).render(memory=self)


def get_memory_provider(provider: str) -> MemoryProvider:
    logger.debug(f"Loading memory provider: {provider}")

    # --- CHROMA ---

    if provider.startswith("chroma"):
        import marvin.memory.providers.chroma as chroma_provider

        if provider == "chroma-ephemeral":
            return chroma_provider.ChromaEphemeralMemory()
        if provider == "chroma-db":
            return chroma_provider.ChromaPersistentMemory()
        if provider == "chroma-cloud":
            return chroma_provider.ChromaCloudMemory()

    # --- LanceDB ---

    elif provider.startswith("lancedb"):
        import marvin.memory.providers.lance as lance_provider

        return lance_provider.LanceMemory()

    # --- Postgres ---
    elif provider.startswith("postgres"):
        import marvin.memory.providers.postgres as postgres_provider

        return postgres_provider.PostgresMemory()

    # --- Qdrant ---
    elif provider.startswith("qdrant"):
        import marvin.memory.providers.qdrant as qdrant_provider

        return qdrant_provider.QdrantMemory()

    raise ValueError(f'Memory provider "{provider}" could not be loaded from a string.')
