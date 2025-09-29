"""
Integration tests for orchestrator modules.

Tests the interaction between SmartOrchestrator, AdvancedQueryAnalyzer,
and ResponseSynthesizer components.
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
import json

from metis_agent.core.smart_orchestrator import SmartOrchestrator
from metis_agent.core.advanced_analyzer import AdvancedQueryAnalyzer
from metis_agent.core.response_synthesizer import ResponseSynthesizer
from metis_agent.core.models import QueryComplexity, ExecutionStrategy


class TestOrchestratorIntegration:
    """Test suite for orchestrator component integration."""

    @pytest.fixture
    def mock_llm(self):
        """Mock LLM for orchestrator testing."""
        llm = MagicMock()
        llm.chat.return_value = json.dumps({
            "complexity": "COMPLEX",
            "required_tools": ["Calculator", "WebScraper"],
            "execution_strategy": "MULTI_STEP",
            "confidence": 0.85
        })
        return llm

    @pytest.fixture
    def analyzer(self, mock_llm):
        """Create analyzer with mock LLM."""
        return AdvancedQueryAnalyzer(llm=mock_llm)

    @pytest.fixture
    def orchestrator(self, mock_llm):
        """Create orchestrator with mock LLM."""
        return SmartOrchestrator(llm=mock_llm)

    @pytest.fixture
    def synthesizer(self, mock_llm):
        """Create synthesizer with mock LLM."""
        return ResponseSynthesizer(llm=mock_llm)

    def test_full_pipeline_simple_query(self, analyzer, orchestrator, synthesizer):
        """Test full pipeline with a simple query."""
        query = "What is 2 + 2?"

        # Mock analyzer response for simple query
        analyzer.llm.chat.return_value = json.dumps({
            "complexity": "SIMPLE",
            "required_tools": ["Calculator"],
            "execution_strategy": "DIRECT",
            "confidence": 0.95
        })

        # Mock tool results
        mock_tools = {
            "Calculator": Mock(run=Mock(return_value={"result": "4"}))
        }

        # Analyze query
        analysis = analyzer.analyze(query)
        assert analysis["complexity"] == QueryComplexity.SIMPLE

        # Orchestrate execution
        strategy = orchestrator.select_strategy(analysis)
        assert strategy == ExecutionStrategy.DIRECT

        # Execute tools
        results = orchestrator.execute_tools(analysis["required_tools"], mock_tools, {"query": query})
        assert "Calculator" in results
        assert results["Calculator"]["result"] == "4"

        # Synthesize response
        synthesizer.llm.chat.return_value = "The answer is 4."
        response = synthesizer.synthesize(query, results, analysis)
        assert "4" in response

    def test_full_pipeline_complex_query(self, analyzer, orchestrator, synthesizer):
        """Test full pipeline with a complex multi-step query."""
        query = "Research the latest trends in AI and create a summary report"

        # Mock analyzer response for complex query
        analyzer.llm.chat.return_value = json.dumps({
            "complexity": "COMPLEX",
            "required_tools": ["WebScraper", "DataAnalyzer", "ContentGenerator"],
            "execution_strategy": "MULTI_STEP",
            "subtasks": [
                "Search for AI trends",
                "Analyze gathered data",
                "Generate summary report"
            ],
            "confidence": 0.88
        })

        # Mock tools
        mock_tools = {
            "WebScraper": Mock(run=Mock(return_value={
                "result": "Found 10 articles about AI trends"
            })),
            "DataAnalyzer": Mock(run=Mock(return_value={
                "result": "Key trends: LLMs, Multimodal AI, Edge AI"
            })),
            "ContentGenerator": Mock(run=Mock(return_value={
                "result": "Generated comprehensive report"
            }))
        }

        # Full pipeline execution
        analysis = analyzer.analyze(query)
        assert analysis["complexity"] == QueryComplexity.COMPLEX
        assert len(analysis["subtasks"]) == 3

        strategy = orchestrator.select_strategy(analysis)
        assert strategy == ExecutionStrategy.MULTI_STEP

        # Execute multi-step workflow
        workflow_results = orchestrator.execute_workflow(analysis, mock_tools, query)
        assert len(workflow_results) == 3

        # Synthesize final response
        synthesizer.llm.chat.return_value = "Generated a comprehensive AI trends report."
        response = synthesizer.synthesize(query, workflow_results, analysis)
        assert "report" in response.lower()

    def test_orchestrator_error_handling(self, analyzer, orchestrator, synthesizer):
        """Test error handling in orchestrator pipeline."""
        query = "Process data that doesn't exist"

        # Mock analyzer with error scenario
        analyzer.llm.chat.return_value = json.dumps({
            "complexity": "MEDIUM",
            "required_tools": ["DataProcessor"],
            "execution_strategy": "DIRECT",
            "confidence": 0.7
        })

        # Mock failing tool
        failing_tool = Mock()
        failing_tool.run.side_effect = Exception("Data not found")
        mock_tools = {"DataProcessor": failing_tool}

        analysis = analyzer.analyze(query)

        # Test error handling in orchestrator
        with pytest.raises(Exception) as exc_info:
            orchestrator.execute_tools(analysis["required_tools"], mock_tools, {"query": query})

        assert "Data not found" in str(exc_info.value)

    def test_tool_dependency_resolution(self, orchestrator):
        """Test tool dependency resolution in complex workflows."""
        analysis = {
            "required_tools": ["FileReader", "DataProcessor", "ReportGenerator"],
            "tool_dependencies": {
                "DataProcessor": ["FileReader"],
                "ReportGenerator": ["DataProcessor"]
            }
        }

        # Mock tools with dependencies
        file_data = {"content": "sample data"}
        processed_data = {"processed": "sample data processed"}

        mock_tools = {
            "FileReader": Mock(run=Mock(return_value=file_data)),
            "DataProcessor": Mock(run=Mock(return_value=processed_data)),
            "ReportGenerator": Mock(run=Mock(return_value={"report": "Generated report"}))
        }

        # Execute with dependency resolution
        results = orchestrator.execute_with_dependencies(analysis, mock_tools, {})

        # Verify execution order
        assert "FileReader" in results
        assert "DataProcessor" in results
        assert "ReportGenerator" in results

        # Verify dependencies were passed correctly
        mock_tools["DataProcessor"].run.assert_called()
        mock_tools["ReportGenerator"].run.assert_called()

    def test_parallel_execution(self, orchestrator):
        """Test parallel execution of independent tools."""
        analysis = {
            "required_tools": ["WebScraper", "Calculator", "DateFormatter"],
            "parallel_groups": [
                ["WebScraper", "Calculator"],  # Can run in parallel
                ["DateFormatter"]  # Depends on results
            ]
        }

        mock_tools = {
            "WebScraper": Mock(run=Mock(return_value={"data": "scraped"})),
            "Calculator": Mock(run=Mock(return_value={"result": 42})),
            "DateFormatter": Mock(run=Mock(return_value={"formatted": "2024-01-01"}))
        }

        # Execute with parallelization
        results = orchestrator.execute_parallel(analysis, mock_tools, {})

        assert len(results) == 3
        assert all(tool in results for tool in analysis["required_tools"])

    def test_response_synthesis_with_context(self, synthesizer):
        """Test response synthesis with various context types."""
        query = "Summarize the analysis results"

        tool_results = {
            "DataAnalyzer": {"insights": ["Trend 1", "Trend 2", "Trend 3"]},
            "Calculator": {"statistics": {"mean": 75, "median": 80}},
            "WebScraper": {"sources": ["source1.com", "source2.com"]}
        }

        analysis = {
            "complexity": QueryComplexity.MEDIUM,
            "confidence": 0.85
        }

        # Mock synthesizer response
        synthesizer.llm.chat.return_value = "Based on analysis of multiple sources..."

        response = synthesizer.synthesize(query, tool_results, analysis)

        assert response is not None
        assert len(response) > 0

    def test_adaptive_strategy_selection(self, orchestrator):
        """Test adaptive strategy selection based on context."""
        # Test with different user contexts
        contexts = [
            {"user_type": "beginner", "time_constraint": "low"},
            {"user_type": "expert", "time_constraint": "high"},
            {"user_type": "analyst", "time_constraint": "medium"}
        ]

        query_analysis = {
            "complexity": QueryComplexity.MEDIUM,
            "required_tools": ["DataAnalyzer"]
        }

        for context in contexts:
            strategy = orchestrator.select_adaptive_strategy(query_analysis, context)
            assert strategy in [
                ExecutionStrategy.DIRECT,
                ExecutionStrategy.MULTI_STEP,
                ExecutionStrategy.PARALLEL
            ]

    def test_memory_integration(self, analyzer, orchestrator, temp_memory_db):
        """Test integration with memory system."""
        query = "What did we discuss about Python earlier?"

        # Mock memory retrieval
        temp_memory_db.search_similar = Mock(return_value=[
            {"content": "Discussed Python programming basics"},
            {"content": "Talked about Python libraries"}
        ])

        # Analyze with memory context
        analysis = analyzer.analyze_with_memory(query, temp_memory_db)

        assert "memory_context" in analysis
        assert len(analysis["memory_context"]) == 2

        # Execute with memory-aware orchestration
        strategy = orchestrator.select_strategy_with_memory(analysis)
        assert strategy in ExecutionStrategy


class TestCodingOrchestratorIntegration:
    """Test suite for coding orchestrator integration."""

    def test_code_generation_workflow(self, mock_llm):
        """Test code generation workflow integration."""
        from metis_agent.core.coding_orchestrator import CodingOrchestrator

        coding_orchestrator = CodingOrchestrator(llm=mock_llm)

        request = "Create a Python function to calculate fibonacci numbers"

        # Mock the workflow stages
        mock_llm.chat.side_effect = [
            # Analysis stage
            json.dumps({
                "language": "python",
                "complexity": "medium",
                "requirements": ["function", "fibonacci", "recursion"]
            }),
            # Code generation stage
            "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
            # Testing stage
            json.dumps({
                "test_cases": [
                    {"input": 0, "expected": 0},
                    {"input": 1, "expected": 1},
                    {"input": 5, "expected": 5}
                ]
            })
        ]

        # Execute full coding workflow
        result = coding_orchestrator.execute_coding_workflow(request)

        assert "code" in result
        assert "tests" in result
        assert "fibonacci" in result["code"]

    def test_code_review_integration(self, mock_llm):
        """Test code review and improvement workflow."""
        from metis_agent.core.coding_orchestrator import CodingOrchestrator

        coding_orchestrator = CodingOrchestrator(llm=mock_llm)

        code_to_review = """
        def bad_function(x):
            result = 0
            for i in range(x):
                result = result + i
            return result
        """

        # Mock review stages
        mock_llm.chat.side_effect = [
            # Code analysis
            json.dumps({
                "issues": ["inefficient loop", "poor naming", "missing docstring"],
                "suggestions": ["use built-in sum", "rename function", "add documentation"]
            }),
            # Improved code
            """def sum_range(n):
    \"\"\"Calculate sum of numbers from 0 to n-1.\"\"\"
    return sum(range(n))"""
        ]

        result = coding_orchestrator.review_and_improve(code_to_review)

        assert "improved_code" in result
        assert "issues" in result
        assert "sum_range" in result["improved_code"]

    def test_blueprint_orchestration(self, mock_llm):
        """Test blueprint-based orchestration."""
        from metis_agent.blueprints.core.engine import BlueprintEngine

        blueprint_engine = BlueprintEngine(llm=mock_llm)

        # Mock blueprint detection and execution
        mock_llm.chat.side_effect = [
            json.dumps({
                "detected_blueprints": ["code_generation", "testing"],
                "execution_order": ["code_generation", "testing"],
                "parameters": {
                    "language": "python",
                    "test_framework": "pytest"
                }
            }),
            "Generated code successfully",
            "Tests created and passed"
        ]

        request = "Create a tested Python class for user management"
        result = blueprint_engine.execute_blueprints(request)

        assert result["status"] == "completed"
        assert len(result["steps"]) == 2


class TestPerformanceIntegration:
    """Test suite for performance aspects of orchestrator integration."""

    def test_large_workflow_performance(self, analyzer, orchestrator, performance_timer):
        """Test performance with large workflows."""
        # Simulate large workflow
        large_query = "Process 100 data files and generate comprehensive analysis"

        analyzer.llm.chat.return_value = json.dumps({
            "complexity": "COMPLEX",
            "required_tools": [f"Tool_{i}" for i in range(20)],
            "execution_strategy": "PARALLEL"
        })

        # Mock many tools
        mock_tools = {
            f"Tool_{i}": Mock(run=Mock(return_value={"result": f"Result {i}"}))
            for i in range(20)
        }

        performance_timer.start()

        analysis = analyzer.analyze(large_query)
        results = orchestrator.execute_tools(analysis["required_tools"], mock_tools, {})

        elapsed = performance_timer.stop()

        assert len(results) == 20
        assert elapsed < 5.0  # Should complete within 5 seconds

    def test_memory_usage_optimization(self, orchestrator):
        """Test memory usage optimization during execution."""
        import psutil
        import os

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Execute memory-intensive workflow simulation
        large_analysis = {
            "required_tools": [f"MemoryTool_{i}" for i in range(50)],
            "execution_strategy": "PARALLEL"
        }

        mock_tools = {
            f"MemoryTool_{i}": Mock(run=Mock(return_value={"data": "x" * 1000}))
            for i in range(50)
        }

        orchestrator.execute_tools(large_analysis["required_tools"], mock_tools, {})

        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory

        # Memory increase should be reasonable (less than 100MB)
        assert memory_increase < 100 * 1024 * 1024