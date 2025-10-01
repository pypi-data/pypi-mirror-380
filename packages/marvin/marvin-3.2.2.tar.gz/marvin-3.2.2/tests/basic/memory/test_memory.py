import chromadb
import pytest
from qdrant_client import AsyncQdrantClient

import marvin
from marvin.memory.memory import MemoryProvider
from marvin.memory.providers.chroma import ChromaEphemeralMemory, ChromaMemory
from marvin.memory.providers.qdrant import QdrantMemory


@pytest.mark.parametrize(
    "provider",
    [
        ChromaEphemeralMemory(),
        QdrantMemory(client=AsyncQdrantClient(location=":memory:")),
    ],
)
class TestMemory:
    async def test_store_and_retrieve(self, provider: MemoryProvider):
        m = marvin.Memory(key="test", instructions="test", provider=provider)
        await m.add("The number is 42")
        result = await m.search("numbers")
        assert len(result) == 1
        assert "The number is 42" in result.values()

    async def test_delete(self, provider: MemoryProvider):
        m = marvin.Memory(key="test2", instructions="test", provider=provider)
        m_id = await m.add("The number is 42")
        await m.delete(m_id)
        result = await m.search("numbers")
        assert len(result) == 0

    async def test_search(self, provider: MemoryProvider):
        m = marvin.Memory(key="test3", instructions="test", provider=provider)
        await m.add("The number is 42")
        await m.add("The number is 43")
        result = await m.search("numbers")
        assert len(result) == 2
        assert "The number is 42" in result.values()
        assert "The number is 43" in result.values()


class TestMemoryProvider:
    def test_load_from_string_invalid(self):
        with pytest.raises(ValueError):
            marvin.Memory(key="test", instructions="test", provider="invalid")

    def test_load_from_string_chroma_db(self):
        m = marvin.Memory(key="test", instructions="test", provider="chroma-db")
        assert isinstance(m.provider, ChromaMemory)

    def test_load_from_instance(self, tmp_path):
        mp = ChromaMemory(
            client=chromadb.PersistentClient(path=str(tmp_path / "test_path")),
        )
        m = marvin.Memory(key="test", instructions="test", provider=mp)
        assert m
