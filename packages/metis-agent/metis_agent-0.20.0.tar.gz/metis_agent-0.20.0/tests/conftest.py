"""
Pytest configuration and shared fixtures for Metis Agent test suite.

This module provides comprehensive test fixtures and utilities for testing
all components of the Metis Agent framework.
"""

import os
import sys
import pytest
import tempfile
import shutil
from unittest.mock import Mock, MagicMock
from pathlib import Path
from typing import Dict, Any, Optional

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from metis_agent.core import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.memory.sqlite_store import SQLiteMemory
from metis_agent.tools.base import BaseTool


# Test environment setup
@pytest.fixture(scope="session")
def test_env():
    """Set up test environment variables."""
    os.environ["METIS_TEST_MODE"] = "true"
    os.environ["METIS_LOG_LEVEL"] = "DEBUG"
    yield
    # Cleanup
    if "METIS_TEST_MODE" in os.environ:
        del os.environ["METIS_TEST_MODE"]


# Temporary directory fixtures
@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp(prefix="metis_test_")
    yield temp_path
    # Cleanup
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)


@pytest.fixture
def temp_memory_db(temp_dir):
    """Create a temporary SQLite memory database."""
    db_path = os.path.join(temp_dir, "test_memory.db")
    memory = SQLiteMemory(db_path)
    yield memory
    # Cleanup is handled by temp_dir fixture


# Mock fixtures for LLM providers
@pytest.fixture
def mock_openai_llm():
    """Mock OpenAI LLM provider."""
    mock_llm = MagicMock()
    mock_llm.provider = "openai"
    mock_llm.model = "gpt-4"
    mock_llm.chat.return_value = "Mock OpenAI response"
    mock_llm.stream_chat.return_value = iter(["Mock ", "streaming ", "response"])
    return mock_llm


@pytest.fixture
def mock_groq_llm():
    """Mock Groq LLM provider."""
    mock_llm = MagicMock()
    mock_llm.provider = "groq"
    mock_llm.model = "mixtral-8x7b-32768"
    mock_llm.chat.return_value = "Mock Groq response"
    mock_llm.stream_chat.return_value = iter(["Mock ", "Groq ", "stream"])
    return mock_llm


@pytest.fixture
def mock_llm_factory(mock_openai_llm, mock_groq_llm):
    """Factory for creating mock LLM instances."""
    def _create_mock_llm(provider="openai", model=None):
        if provider == "openai":
            return mock_openai_llm
        elif provider == "groq":
            return mock_groq_llm
        else:
            mock = MagicMock()
            mock.provider = provider
            mock.model = model or "default-model"
            mock.chat.return_value = f"Mock {provider} response"
            return mock
    return _create_mock_llm


# Agent configuration fixtures
@pytest.fixture
def basic_agent_config():
    """Create a basic agent configuration for testing."""
    config = AgentConfig()
    config.name = "test-agent"
    config.description = "Test agent for unit tests"
    config.llm_provider = "openai"
    config.llm_model = "gpt-4"
    config.max_iterations = 5
    config.enable_memory = True
    return config


@pytest.fixture
def agent_with_memory(temp_memory_db, mock_openai_llm, monkeypatch):
    """Create an agent instance with memory for testing."""
    def mock_get_llm(*args, **kwargs):
        return mock_openai_llm

    monkeypatch.setattr("metis_agent.core.llm_interface.get_llm", mock_get_llm)

    agent = SingleAgent(
        memory_path=temp_memory_db.db_path,
        use_titans_memory=False,
        use_enhanced_memory=False,
        enhanced_processing=False  # Disable for simpler testing
    )
    return agent


# Tool-related fixtures
class MockTool(BaseTool):
    """Mock tool for testing."""

    def get_description(self) -> str:
        return "Mock tool for testing"

    def get_parameters(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "input": {"type": "string", "description": "Test input"}
            },
            "required": ["input"]
        }

    def run(self, input: str) -> Dict[str, Any]:
        return {
            "success": True,
            "result": f"Processed: {input}"
        }


@pytest.fixture
def mock_tool():
    """Create a mock tool instance."""
    return MockTool()


@pytest.fixture
def mock_tool_registry():
    """Create a mock tool registry with test tools."""
    registry = {
        "MockTool": MockTool,
        "Calculator": Mock(spec=BaseTool),
        "FileReader": Mock(spec=BaseTool),
        "WebScraper": Mock(spec=BaseTool)
    }
    return registry


# Knowledge base fixtures
@pytest.fixture
def temp_knowledge_db(temp_dir):
    """Create a temporary knowledge database."""
    from metis_agent.knowledge.knowledge_base import KnowledgeBase
    from metis_agent.knowledge.knowledge_config import KnowledgeConfig

    config = KnowledgeConfig(
        database_path=os.path.join(temp_dir, "test_knowledge.db"),
        enable_graph=False  # Disable for simpler testing
    )
    kb = KnowledgeBase(config)
    return kb


# CLI testing fixtures
@pytest.fixture
def cli_runner():
    """Create a Click CLI test runner."""
    from click.testing import CliRunner
    return CliRunner()


@pytest.fixture
def mock_console():
    """Mock Rich console for CLI testing."""
    from unittest.mock import MagicMock
    console = MagicMock()
    console.print = MagicMock()
    console.status = MagicMock()
    return console


# Async testing support
@pytest.fixture
def event_loop():
    """Create an event loop for async tests."""
    import asyncio
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# Test data fixtures
@pytest.fixture
def sample_conversation():
    """Sample conversation data for testing."""
    return [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you!"},
        {"role": "user", "content": "Can you help me with Python?"},
        {"role": "assistant", "content": "Of course! I'd be happy to help with Python."}
    ]


@pytest.fixture
def sample_knowledge_entries():
    """Sample knowledge entries for testing."""
    return [
        {
            "title": "Python Basics",
            "content": "Python is a high-level programming language.",
            "category": "programming",
            "tags": ["python", "basics", "programming"]
        },
        {
            "title": "Machine Learning",
            "content": "ML is a subset of artificial intelligence.",
            "category": "ai",
            "tags": ["ml", "ai", "data science"]
        }
    ]


# Performance testing fixtures
@pytest.fixture
def performance_timer():
    """Timer for performance testing."""
    import time

    class Timer:
        def __init__(self):
            self.start_time = None
            self.end_time = None

        def start(self):
            self.start_time = time.perf_counter()

        def stop(self):
            self.end_time = time.perf_counter()
            return self.elapsed

        @property
        def elapsed(self):
            if self.start_time and self.end_time:
                return self.end_time - self.start_time
            return None

    return Timer()


# Cleanup fixtures
@pytest.fixture(autouse=True)
def cleanup_test_files():
    """Automatically cleanup test files after each test."""
    test_files = []
    yield test_files
    # Cleanup any files added to the list
    for filepath in test_files:
        if os.path.exists(filepath):
            if os.path.isfile(filepath):
                os.remove(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)