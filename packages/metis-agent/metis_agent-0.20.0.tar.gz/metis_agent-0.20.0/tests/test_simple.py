"""
Simple tests to verify basic functionality.
"""

import pytest
import os
import tempfile


def test_basic_imports():
    """Test that we can import core modules."""
    from metis_agent.core.agent import SingleAgent
    from metis_agent.tools.registry import get_available_tools
    from metis_agent.memory.sqlite_store import SQLiteMemory

    assert SingleAgent is not None
    assert get_available_tools is not None
    assert SQLiteMemory is not None


def test_memory_creation():
    """Test that we can create a memory instance."""
    from metis_agent.memory.sqlite_store import SQLiteMemory

    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        memory_path = f.name

    try:
        memory = SQLiteMemory(memory_path)
        assert memory is not None
        memory.close()
    finally:
        if os.path.exists(memory_path):
            os.unlink(memory_path)


def test_connection_pool():
    """Test the new connection pool functionality."""
    from metis_agent.memory.connection_pool import SQLiteConnectionPool, PoolConfig

    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db_path = f.name

    try:
        config = PoolConfig(max_connections=2, min_connections=1)
        pool = SQLiteConnectionPool(db_path, config)

        # Test getting a connection
        with pool.get_connection() as conn:
            cursor = conn.execute("SELECT 1")
            result = cursor.fetchone()
            assert result[0] == 1

        # Test pool stats
        stats = pool.get_stats()
        assert 'total_connections' in stats

        pool.close()

    finally:
        if os.path.exists(db_path):
            os.unlink(db_path)


def test_response_cache():
    """Test the new response cache functionality."""
    from metis_agent.core.response_cache import LLMResponseCache, CacheConfig

    with tempfile.TemporaryDirectory() as temp_dir:
        config = CacheConfig(max_cache_size_mb=10)
        cache = LLMResponseCache(temp_dir, config)

        # Test caching a response
        cache_key = cache.put(
            prompt="What is 2+2?",
            response="4",
            provider="test",
            model="test-model"
        )

        assert cache_key is not None

        # Test retrieving cached response
        cached_entry = cache.get("What is 2+2?", "test", "test-model")
        assert cached_entry is not None
        assert cached_entry.response == "4"

        # Test cache stats
        stats = cache.get_stats()
        assert stats['entry_count'] == 1

        cache.close()


def test_unified_orchestrator():
    """Test the new unified orchestrator."""
    from metis_agent.core.unified_orchestrator import (
        UnifiedOrchestrator, OrchestratorConfig, OrchestratorMode
    )

    config = OrchestratorConfig(mode=OrchestratorMode.GENERAL)
    orchestrator = UnifiedOrchestrator(config)

    assert orchestrator is not None
    assert orchestrator.config.mode == OrchestratorMode.GENERAL


def test_unified_streaming():
    """Test the new unified streaming interface."""
    from metis_agent.cli.unified_streaming import (
        UnifiedStreamingInterface, StreamingConfig, StreamingMode
    )

    config = StreamingConfig(mode=StreamingMode.INSTANT)
    # We'll test without an actual agent for now
    streaming = UnifiedStreamingInterface(
        agent=None,
        config=config
    )

    assert streaming is not None
    assert streaming.config.mode == StreamingMode.INSTANT


def test_tools_registry():
    """Test that tools can be loaded."""
    from metis_agent.tools.registry import get_available_tools, get_tool

    tools = get_available_tools()
    assert len(tools) > 0  # Should have some tools

    # Test getting a specific tool
    calculator_tool = get_tool('CalculatorTool')
    assert calculator_tool is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])