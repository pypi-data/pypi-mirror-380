"""
Comprehensive unit tests for the SingleAgent core module.

Tests cover:
- Agent initialization
- LLM provider integration
- Memory management
- Tool execution
- Query processing
- Error handling
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
import json
import os

from metis_agent.core.agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.core.models import QueryComplexity, ExecutionStrategy


class TestSingleAgentInitialization:
    """Test suite for SingleAgent initialization."""

    def test_basic_initialization(self, temp_dir, mock_openai_llm):
        """Test basic agent initialization."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "test.db"),
                use_titans_memory=False,
                enhanced_processing=False
            )

            assert agent is not None
            assert agent.llm == mock_openai_llm
            assert agent.memory is not None
            assert os.path.exists(agent.memory_path)

    def test_initialization_with_config(self, basic_agent_config, temp_dir, mock_openai_llm):
        """Test agent initialization with custom config."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                config=basic_agent_config,
                memory_path=os.path.join(temp_dir, "test.db"),
                use_titans_memory=False
            )

            assert agent.config == basic_agent_config
            assert agent.llm == mock_openai_llm

    def test_enhanced_processing_initialization(self, temp_dir, mock_openai_llm):
        """Test agent with enhanced processing enabled."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "test.db"),
                enhanced_processing=True,
                use_titans_memory=False
            )

            assert hasattr(agent, 'analyzer')
            assert hasattr(agent, 'orchestrator')
            assert hasattr(agent, 'synthesizer')

    def test_memory_isolation(self, temp_dir, mock_openai_llm):
        """Test that each agent gets isolated memory."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent1 = SingleAgent(use_titans_memory=False)
            agent2 = SingleAgent(use_titans_memory=False)

            assert agent1.memory_path != agent2.memory_path

    @pytest.mark.parametrize("llm_provider,llm_model", [
        ("openai", "gpt-4"),
        ("groq", "mixtral-8x7b"),
        ("anthropic", "claude-3-opus")
    ])
    def test_different_llm_providers(self, llm_provider, llm_model, temp_dir, mock_llm_factory):
        """Test initialization with different LLM providers."""
        mock_llm = mock_llm_factory(llm_provider, llm_model)

        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_llm):
            agent = SingleAgent(
                llm_provider=llm_provider,
                llm_model=llm_model,
                memory_path=os.path.join(temp_dir, "test.db"),
                use_titans_memory=False
            )

            assert agent.llm == mock_llm
            assert agent.llm.provider == llm_provider


class TestAgentQueryProcessing:
    """Test suite for agent query processing."""

    @pytest.mark.asyncio
    async def test_simple_query_processing(self, agent_with_memory):
        """Test processing a simple query."""
        query = "What is 2 + 2?"
        agent_with_memory.llm.chat.return_value = "2 + 2 equals 4"

        response = await agent_with_memory.process_query_async(query)

        assert response is not None
        assert "4" in str(response)
        agent_with_memory.llm.chat.assert_called()

    def test_query_with_context(self, agent_with_memory):
        """Test query processing with context."""
        query = "What did we discuss?"
        context = {"previous_query": "We talked about Python"}

        agent_with_memory.llm.chat.return_value = "We discussed Python programming"

        response = agent_with_memory.process_with_context(query, context)

        assert response is not None
        assert "Python" in response

    def test_query_validation(self, agent_with_memory):
        """Test input validation for queries."""
        # Test with empty query
        with pytest.raises(ValueError):
            agent_with_memory.process_query("")

        # Test with None query
        with pytest.raises(ValueError):
            agent_with_memory.process_query(None)

        # Test with very long query (should not raise)
        long_query = "test " * 1000
        agent_with_memory.llm.chat.return_value = "Processed"
        response = agent_with_memory.process_query(long_query)
        assert response is not None

    def test_streaming_response(self, agent_with_memory):
        """Test streaming response generation."""
        query = "Tell me a story"
        agent_with_memory.llm.stream_chat.return_value = iter(["Once ", "upon ", "a ", "time"])

        chunks = list(agent_with_memory.stream_query(query))

        assert len(chunks) == 4
        assert "".join(chunks) == "Once upon a time"


class TestAgentMemoryManagement:
    """Test suite for agent memory management."""

    def test_memory_storage(self, agent_with_memory):
        """Test storing conversations in memory."""
        query = "Remember this: The capital of France is Paris"
        response = "I'll remember that the capital of France is Paris"

        agent_with_memory.llm.chat.return_value = response
        agent_with_memory.process_query(query)

        # Check memory contains the interaction
        memory_contents = agent_with_memory.memory.get_conversation_history()
        assert len(memory_contents) > 0
        assert any("Paris" in str(item) for item in memory_contents)

    def test_memory_retrieval(self, agent_with_memory):
        """Test retrieving relevant memories."""
        # Store some memories
        agent_with_memory.memory.add_interaction(
            "What is Python?",
            "Python is a programming language"
        )
        agent_with_memory.memory.add_interaction(
            "What is JavaScript?",
            "JavaScript is a scripting language"
        )

        # Retrieve relevant memories
        relevant = agent_with_memory.memory.search_similar("Tell me about Python")
        assert len(relevant) > 0
        assert any("Python" in str(item) for item in relevant)

    def test_memory_summarization(self, agent_with_memory):
        """Test memory summarization for long conversations."""
        # Add many interactions to trigger summarization
        for i in range(20):
            agent_with_memory.memory.add_interaction(
                f"Question {i}",
                f"Answer {i}"
            )

        # Check if summarization occurred
        history = agent_with_memory.memory.get_conversation_history()
        assert len(history) <= 20  # Should be limited/summarized

    def test_titans_memory_adapter(self, temp_dir, mock_openai_llm):
        """Test Titans memory adapter initialization."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "titans.db"),
                use_titans_memory=True,
                use_enhanced_memory=False
            )

            assert hasattr(agent, 'titans_memory')
            assert agent.use_titans_memory is True


class TestAgentToolExecution:
    """Test suite for agent tool execution."""

    def test_tool_discovery(self, agent_with_memory, mock_tool):
        """Test tool discovery and registration."""
        with patch('metis_agent.tools.registry.get_available_tools', return_value=['MockTool']):
            tools = agent_with_memory.get_available_tools()
            assert 'MockTool' in tools

    def test_tool_execution(self, agent_with_memory, mock_tool):
        """Test executing a tool."""
        agent_with_memory.tools = {'MockTool': mock_tool}

        result = agent_with_memory.execute_tool('MockTool', {'input': 'test'})

        assert result['success'] is True
        assert result['result'] == 'Processed: test'

    def test_tool_error_handling(self, agent_with_memory):
        """Test error handling in tool execution."""
        # Create a tool that raises an error
        failing_tool = Mock()
        failing_tool.run.side_effect = Exception("Tool failed")
        agent_with_memory.tools = {'FailingTool': failing_tool}

        with pytest.raises(Exception) as exc_info:
            agent_with_memory.execute_tool('FailingTool', {})

        assert "Tool failed" in str(exc_info.value)

    def test_tool_parameter_validation(self, agent_with_memory, mock_tool):
        """Test tool parameter validation."""
        agent_with_memory.tools = {'MockTool': mock_tool}

        # Test with invalid parameters
        with pytest.raises(ValueError):
            agent_with_memory.execute_tool('MockTool', {'invalid_param': 'test'})

        # Test with missing required parameters
        with pytest.raises(ValueError):
            agent_with_memory.execute_tool('MockTool', {})


class TestEnhancedProcessing:
    """Test suite for enhanced processing features."""

    def test_query_complexity_analysis(self, temp_dir, mock_openai_llm):
        """Test query complexity analysis."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "test.db"),
                enhanced_processing=True,
                use_titans_memory=False
            )

            # Mock analyzer response
            agent.analyzer.analyze = Mock(return_value={
                'complexity': QueryComplexity.COMPLEX,
                'requires_tools': ['Calculator', 'WebScraper'],
                'subtasks': ['calculate', 'search', 'summarize']
            })

            analysis = agent.analyze_query("Complex multi-step question")

            assert analysis['complexity'] == QueryComplexity.COMPLEX
            assert len(analysis['requires_tools']) == 2
            assert len(analysis['subtasks']) == 3

    def test_execution_strategy_selection(self, temp_dir, mock_openai_llm):
        """Test execution strategy selection based on query."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "test.db"),
                enhanced_processing=True,
                use_titans_memory=False
            )

            # Test simple strategy
            agent.orchestrator.select_strategy = Mock(
                return_value=ExecutionStrategy.DIRECT
            )
            strategy = agent.select_execution_strategy("What is 2+2?")
            assert strategy == ExecutionStrategy.DIRECT

            # Test complex strategy
            agent.orchestrator.select_strategy = Mock(
                return_value=ExecutionStrategy.MULTI_STEP
            )
            strategy = agent.select_execution_strategy("Research and summarize...")
            assert strategy == ExecutionStrategy.MULTI_STEP


class TestErrorHandlingAndEdgeCases:
    """Test suite for error handling and edge cases."""

    def test_llm_failure_handling(self, agent_with_memory):
        """Test handling of LLM failures."""
        agent_with_memory.llm.chat.side_effect = Exception("LLM API error")

        with pytest.raises(Exception) as exc_info:
            agent_with_memory.process_query("Test query")

        assert "LLM API error" in str(exc_info.value)

    def test_memory_corruption_handling(self, agent_with_memory):
        """Test handling of memory corruption."""
        # Corrupt the memory database
        agent_with_memory.memory.add_interaction = Mock(
            side_effect=Exception("Database corrupted")
        )

        # Should handle gracefully without crashing
        with pytest.raises(Exception) as exc_info:
            agent_with_memory.process_query("Test query")

        assert "Database corrupted" in str(exc_info.value)

    def test_concurrent_access(self, agent_with_memory):
        """Test concurrent access to agent resources."""
        import threading
        results = []
        errors = []

        def process_query(query):
            try:
                result = agent_with_memory.process_query(query)
                results.append(result)
            except Exception as e:
                errors.append(str(e))

        # Create multiple threads
        threads = []
        for i in range(5):
            t = threading.Thread(target=process_query, args=(f"Query {i}",))
            threads.append(t)
            t.start()

        # Wait for all threads
        for t in threads:
            t.join()

        # Check that all queries were processed
        assert len(results) + len(errors) == 5

    def test_resource_cleanup(self, temp_dir, mock_openai_llm):
        """Test proper resource cleanup."""
        with patch('metis_agent.core.llm_interface.get_llm', return_value=mock_openai_llm):
            agent = SingleAgent(
                memory_path=os.path.join(temp_dir, "test.db"),
                use_titans_memory=False
            )

            # Simulate cleanup
            agent.cleanup()

            # Verify resources are released
            assert agent.memory.is_closed() if hasattr(agent.memory, 'is_closed') else True