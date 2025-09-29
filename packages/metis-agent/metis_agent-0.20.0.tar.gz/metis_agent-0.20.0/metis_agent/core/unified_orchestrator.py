"""
Unified Orchestrator for Metis Agent.

This module consolidates the functionality from SmartOrchestrator and CodingOrchestrator
into a single, configurable orchestrator with multiple execution strategies.
"""

import json
import time
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Union, Tuple
from pathlib import Path
from enum import Enum
from dataclasses import dataclass, field

from .models import (
    QueryAnalysis, ExecutionResult, ToolExecutionResult,
    ExecutionStrategy, ExecutionError, QueryComplexity
)
from .llm_interface import get_llm
from ..tools.registry import get_tool


class OrchestratorMode(Enum):
    """Different orchestrator modes for specialized behavior."""
    GENERAL = "general"        # General purpose orchestration
    CODING = "coding"          # Specialized for coding tasks
    RESEARCH = "research"      # Optimized for research tasks
    ANALYSIS = "analysis"      # For data analysis tasks
    CREATIVE = "creative"      # For creative tasks


class QuestionPriority(Enum):
    """Priority levels for clarification questions."""
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class ClarificationQuestion:
    """Represents a clarification question."""
    question: str
    category: str
    priority: QuestionPriority = QuestionPriority.MEDIUM
    context: str = ""
    answer: Optional[str] = None
    follow_up: bool = False


@dataclass
class EnhancedAnalysis:
    """Enhanced analysis with clarification support."""
    query: str
    complexity: QueryComplexity
    mode: OrchestratorMode
    project_type: Optional[str] = None
    missing_context: List[str] = field(default_factory=list)
    questions: List[ClarificationQuestion] = field(default_factory=list)
    confidence: float = 0.8
    requires_clarification: bool = False
    suggested_strategy: Optional[ExecutionStrategy] = None

    def __post_init__(self):
        self.requires_clarification = len(self.questions) > 0


@dataclass
class OrchestratorConfig:
    """Configuration for the unified orchestrator."""
    mode: OrchestratorMode = OrchestratorMode.GENERAL
    enable_clarification: bool = True
    max_clarification_questions: int = 5
    auto_execute_simple: bool = True
    enable_planning_docs: bool = True
    enable_blueprints: bool = True
    memory_context_limit: int = 2000
    execution_timeout: int = 300  # 5 minutes


class UnifiedOrchestrator:
    """
    Unified orchestrator combining functionality from multiple specialized orchestrators.
    """

    def __init__(self, config: Optional[OrchestratorConfig] = None, tools_registry: Dict[str, Any] = None):
        self.config = config or OrchestratorConfig()
        self.tools_registry = tools_registry or {}

        # Initialize specialized engines
        self._init_engines()

    def _init_engines(self):
        """Initialize specialized processing engines."""
        # Clarification engine for asking intelligent questions
        self.clarification_engine = ClarificationEngine()

        # Planning engine for generating project plans
        self.planning_engine = PlanningEngine()

        # Blueprint engine for pattern-based solutions
        try:
            from ..blueprints.core.engine import BlueprintEngine
            self.blueprint_engine = BlueprintEngine()
        except ImportError:
            self.blueprint_engine = None

    def analyze_and_execute(
        self,
        query: str,
        tools: Dict[str, Any],
        llm: Any,
        memory_context: str = "",
        session_id: Optional[str] = None,
        system_message: Optional[str] = None,
        config: Optional[Any] = None,
        clarification_answers: Optional[Dict[str, str]] = None
    ) -> ExecutionResult:
        """
        Analyze query and execute with appropriate strategy.

        Args:
            query: User query to process
            tools: Available tools dictionary
            llm: LLM instance for processing
            memory_context: Context from memory
            session_id: Session identifier
            system_message: System message for LLM
            config: Agent configuration
            clarification_answers: Answers to clarification questions

        Returns:
            ExecutionResult with response and metadata
        """
        start_time = time.time()

        try:
            # Step 1: Enhanced analysis
            analysis = self._analyze_query(query, llm, config)

            # Step 2: Handle clarification if needed
            if analysis.requires_clarification and not clarification_answers:
                return self._handle_clarification_needed(analysis, start_time)

            if clarification_answers:
                analysis = self._apply_clarification_answers(analysis, clarification_answers, llm)

            # Step 3: Execute based on strategy
            execution_context = {
                'tools': tools,
                'llm': llm,
                'memory_context': memory_context,
                'session_id': session_id,
                'system_message': system_message,
                'config': config,
                'analysis': analysis
            }

            return self._execute_with_strategy(analysis, execution_context, start_time)

        except Exception as e:
            return ExecutionResult(
                success=False,
                response=f"Orchestration error: {str(e)}",
                execution_time=time.time() - start_time,
                error=ExecutionError(str(e), "orchestration_error")
            )

    def _analyze_query(self, query: str, llm: Any, config: Optional[Any] = None) -> EnhancedAnalysis:
        """Perform enhanced query analysis."""

        # Determine orchestrator mode based on query content
        mode = self._determine_mode(query)

        # Analyze complexity
        complexity = self._analyze_complexity(query, llm)

        # Generate clarification questions if enabled
        questions = []
        if self.config.enable_clarification and complexity != QueryComplexity.SIMPLE:
            questions = self.clarification_engine.generate_questions(query, mode, llm)

        # Determine project type for coding tasks
        project_type = None
        if mode == OrchestratorMode.CODING:
            project_type = self._detect_project_type(query, llm)

        # Calculate confidence
        confidence = self._calculate_confidence(query, complexity, len(questions))

        # Suggest execution strategy
        strategy = self._suggest_strategy(complexity, mode, len(questions))

        return EnhancedAnalysis(
            query=query,
            complexity=complexity,
            mode=mode,
            project_type=project_type,
            questions=questions[:self.config.max_clarification_questions],
            confidence=confidence,
            suggested_strategy=strategy
        )

    def _determine_mode(self, query: str) -> OrchestratorMode:
        """Determine the appropriate orchestrator mode."""
        query_lower = query.lower()

        # Coding indicators
        coding_keywords = [
            'code', 'program', 'function', 'class', 'api', 'web app', 'database',
            'algorithm', 'framework', 'library', 'debug', 'test', 'deploy',
            'refactor', 'optimize', 'implement', 'develop', 'build'
        ]

        # Research indicators
        research_keywords = [
            'research', 'analyze', 'compare', 'study', 'investigate', 'explore',
            'find information', 'learn about', 'understand', 'explain'
        ]

        # Analysis indicators
        analysis_keywords = [
            'data analysis', 'statistics', 'trends', 'patterns', 'metrics',
            'performance', 'benchmark', 'evaluate', 'measure'
        ]

        # Creative indicators
        creative_keywords = [
            'write', 'create', 'generate', 'design', 'brainstorm', 'story',
            'content', 'marketing', 'creative'
        ]

        if any(keyword in query_lower for keyword in coding_keywords):
            return OrchestratorMode.CODING
        elif any(keyword in query_lower for keyword in research_keywords):
            return OrchestratorMode.RESEARCH
        elif any(keyword in query_lower for keyword in analysis_keywords):
            return OrchestratorMode.ANALYSIS
        elif any(keyword in query_lower for keyword in creative_keywords):
            return OrchestratorMode.CREATIVE
        else:
            return OrchestratorMode.GENERAL

    def _analyze_complexity(self, query: str, llm: Any) -> QueryComplexity:
        """Analyze query complexity using LLM."""

        # Simple heuristics first
        word_count = len(query.split())

        if word_count <= 5:
            return QueryComplexity.SIMPLE
        elif word_count <= 15:
            base_complexity = QueryComplexity.MEDIUM
        else:
            base_complexity = QueryComplexity.COMPLEX

        # Check for complexity indicators
        complex_indicators = [
            'architecture', 'full implementation', 'complete solution',
            'multiple', 'integration', 'scalable', 'production ready',
            'comprehensive', 'enterprise', 'distributed'
        ]

        simple_indicators = [
            'simple', 'basic', 'quick', 'small', 'minimal', 'just'
        ]

        query_lower = query.lower()

        if any(indicator in query_lower for indicator in complex_indicators):
            return QueryComplexity.COMPLEX
        elif any(indicator in query_lower for indicator in simple_indicators):
            return QueryComplexity.SIMPLE

        return base_complexity

    def _detect_project_type(self, query: str, llm: Any) -> Optional[str]:
        """Detect project type for coding tasks."""
        query_lower = query.lower()

        project_types = {
            'web app': ['web app', 'website', 'web application', 'web service'],
            'api': ['api', 'rest api', 'web api', 'microservice'],
            'cli': ['cli', 'command line', 'terminal app', 'console app'],
            'desktop': ['desktop app', 'gui', 'desktop application'],
            'mobile': ['mobile app', 'android', 'ios', 'mobile'],
            'data science': ['data analysis', 'machine learning', 'ai model', 'jupyter'],
            'game': ['game', 'gaming', 'pygame', 'unity'],
            'library': ['library', 'package', 'module', 'framework']
        }

        for project_type, keywords in project_types.items():
            if any(keyword in query_lower for keyword in keywords):
                return project_type

        return None

    def _calculate_confidence(self, query: str, complexity: QueryComplexity,
                            num_questions: int) -> float:
        """Calculate confidence level for the analysis."""
        base_confidence = 0.8

        # Adjust based on complexity
        if complexity == QueryComplexity.SIMPLE:
            base_confidence += 0.1
        elif complexity == QueryComplexity.COMPLEX:
            base_confidence -= 0.1

        # Adjust based on clarification needs
        if num_questions > 0:
            base_confidence -= (num_questions * 0.05)

        # Ensure bounds
        return max(0.1, min(1.0, base_confidence))

    def _suggest_strategy(self, complexity: QueryComplexity, mode: OrchestratorMode,
                         num_questions: int) -> ExecutionStrategy:
        """Suggest execution strategy based on analysis."""

        if complexity == QueryComplexity.SIMPLE and num_questions == 0:
            return ExecutionStrategy.DIRECT
        elif complexity == QueryComplexity.COMPLEX or mode == OrchestratorMode.CODING:
            return ExecutionStrategy.MULTI_STEP
        elif num_questions > 0:
            return ExecutionStrategy.INTERACTIVE
        else:
            return ExecutionStrategy.PARALLEL

    def _handle_clarification_needed(self, analysis: EnhancedAnalysis,
                                   start_time: float) -> ExecutionResult:
        """Handle case where clarification is needed."""
        questions_text = "\n".join([
            f"{i+1}. {q.question} ({q.category})"
            for i, q in enumerate(analysis.questions)
        ])

        response = f"""I need some clarification to provide the best solution:

{questions_text}

Please provide answers to these questions, and I'll create a comprehensive solution for you."""

        return ExecutionResult(
            success=True,
            response=response,
            execution_time=time.time() - start_time,
            metadata={
                'requires_clarification': True,
                'questions': [
                    {
                        'question': q.question,
                        'category': q.category,
                        'priority': q.priority.value
                    }
                    for q in analysis.questions
                ],
                'analysis': analysis
            }
        )

    def _apply_clarification_answers(self, analysis: EnhancedAnalysis,
                                   answers: Dict[str, str], llm: Any) -> EnhancedAnalysis:
        """Apply clarification answers to enhance the analysis."""

        # Update questions with answers
        for i, question in enumerate(analysis.questions):
            if str(i) in answers or question.question in answers:
                question.answer = answers.get(str(i), answers.get(question.question))

        # Re-analyze with enhanced context
        enhanced_context = "\n".join([
            f"Q: {q.question}\nA: {q.answer}"
            for q in analysis.questions if q.answer
        ])

        # Update analysis with new information
        analysis.requires_clarification = False
        analysis.confidence = min(1.0, analysis.confidence + 0.2)

        return analysis

    def _execute_with_strategy(self, analysis: EnhancedAnalysis,
                             context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute based on the determined strategy."""

        strategy = analysis.suggested_strategy or ExecutionStrategy.DIRECT

        if strategy == ExecutionStrategy.DIRECT:
            return self._execute_direct(analysis, context, start_time)
        elif strategy == ExecutionStrategy.MULTI_STEP:
            return self._execute_multi_step(analysis, context, start_time)
        elif strategy == ExecutionStrategy.PARALLEL:
            return self._execute_parallel(analysis, context, start_time)
        else:
            return self._execute_interactive(analysis, context, start_time)

    def _execute_direct(self, analysis: EnhancedAnalysis,
                       context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute using direct strategy."""
        llm = context['llm']

        # Build enhanced prompt
        prompt = self._build_enhanced_prompt(analysis, context)

        try:
            response = llm.chat(prompt)

            return ExecutionResult(
                success=True,
                response=response,
                execution_time=time.time() - start_time,
                strategy=ExecutionStrategy.DIRECT,
                metadata={'analysis': analysis}
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                response=f"Direct execution failed: {str(e)}",
                execution_time=time.time() - start_time,
                error=ExecutionError(str(e), "direct_execution")
            )

    def _execute_multi_step(self, analysis: EnhancedAnalysis,
                           context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute using multi-step strategy."""

        # Generate planning documents if enabled and appropriate
        if (self.config.enable_planning_docs and
            analysis.mode == OrchestratorMode.CODING and
            analysis.complexity in [QueryComplexity.MEDIUM, QueryComplexity.COMPLEX]):

            return self._execute_with_planning(analysis, context, start_time)

        # Regular multi-step execution
        return self._execute_step_by_step(analysis, context, start_time)

    def _execute_with_planning(self, analysis: EnhancedAnalysis,
                             context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute with comprehensive planning for coding tasks."""

        try:
            # Generate project plan
            plan = self.planning_engine.generate_plan(analysis, context['llm'])

            # Execute based on plan
            response = f"""I've created a comprehensive plan for your project:

## Project Overview
{plan.get('overview', 'Project analysis complete')}

## Implementation Plan
{plan.get('plan', 'Plan generated')}

## Next Steps
{plan.get('next_steps', 'Ready to implement')}

Would you like me to proceed with implementation, or would you like to review/modify the plan first?"""

            return ExecutionResult(
                success=True,
                response=response,
                execution_time=time.time() - start_time,
                strategy=ExecutionStrategy.MULTI_STEP,
                metadata={
                    'analysis': analysis,
                    'plan': plan,
                    'has_planning_docs': True
                }
            )

        except Exception as e:
            # Fallback to regular execution
            return self._execute_step_by_step(analysis, context, start_time)

    def _execute_step_by_step(self, analysis: EnhancedAnalysis,
                            context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute step by step without full planning."""

        llm = context['llm']
        prompt = self._build_enhanced_prompt(analysis, context)

        try:
            response = llm.chat(prompt)

            return ExecutionResult(
                success=True,
                response=response,
                execution_time=time.time() - start_time,
                strategy=ExecutionStrategy.MULTI_STEP,
                metadata={'analysis': analysis}
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                response=f"Multi-step execution failed: {str(e)}",
                execution_time=time.time() - start_time,
                error=ExecutionError(str(e), "multi_step_execution")
            )

    def _execute_parallel(self, analysis: EnhancedAnalysis,
                         context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute using parallel strategy."""
        # For now, fallback to direct execution
        # TODO: Implement true parallel execution
        return self._execute_direct(analysis, context, start_time)

    def _execute_interactive(self, analysis: EnhancedAnalysis,
                           context: Dict[str, Any], start_time: float) -> ExecutionResult:
        """Execute using interactive strategy."""
        # For now, fallback to multi-step
        return self._execute_multi_step(analysis, context, start_time)

    def _build_enhanced_prompt(self, analysis: EnhancedAnalysis,
                             context: Dict[str, Any]) -> str:
        """Build enhanced prompt with all context."""

        base_prompt = analysis.query

        # Add mode-specific context
        if analysis.mode == OrchestratorMode.CODING:
            base_prompt = f"""Coding Task: {base_prompt}

Mode: Software Development
Project Type: {analysis.project_type or 'General'}
Complexity: {analysis.complexity.value}"""

        # Add clarification answers if available
        if analysis.questions and any(q.answer for q in analysis.questions):
            clarifications = "\n".join([
                f"Q: {q.question}\nA: {q.answer}"
                for q in analysis.questions if q.answer
            ])
            base_prompt += f"\n\nClarifications:\n{clarifications}"

        # Add memory context
        if context.get('memory_context'):
            base_prompt += f"\n\nContext from previous interactions:\n{context['memory_context']}"

        # Add system message if available
        if context.get('system_message'):
            base_prompt = f"{context['system_message']}\n\n{base_prompt}"

        return base_prompt


class ClarificationEngine:
    """Engine for generating intelligent clarification questions."""

    def generate_questions(self, query: str, mode: OrchestratorMode,
                         llm: Any) -> List[ClarificationQuestion]:
        """Generate clarification questions based on query and mode."""

        if mode == OrchestratorMode.CODING:
            return self._generate_coding_questions(query, llm)
        elif mode == OrchestratorMode.RESEARCH:
            return self._generate_research_questions(query, llm)
        else:
            return self._generate_general_questions(query, llm)

    def _generate_coding_questions(self, query: str, llm: Any) -> List[ClarificationQuestion]:
        """Generate coding-specific clarification questions."""
        questions = []

        # Analyze what's missing for coding tasks
        if 'web' in query.lower() and 'framework' not in query.lower():
            questions.append(ClarificationQuestion(
                "What web framework would you prefer (React, Vue, Django, Flask, etc.)?",
                "tech_stack",
                QuestionPriority.HIGH
            ))

        if 'database' in query.lower() and not any(db in query.lower() for db in ['sqlite', 'postgres', 'mysql', 'mongo']):
            questions.append(ClarificationQuestion(
                "What database system should I use?",
                "tech_stack",
                QuestionPriority.MEDIUM
            ))

        # Add more coding questions based on common patterns
        return questions

    def _generate_research_questions(self, query: str, llm: Any) -> List[ClarificationQuestion]:
        """Generate research-specific clarification questions."""
        questions = []

        # Research depth and scope questions
        questions.append(ClarificationQuestion(
            "How comprehensive should the research be (quick overview vs. in-depth analysis)?",
            "scope",
            QuestionPriority.HIGH
        ))

        return questions

    def _generate_general_questions(self, query: str, llm: Any) -> List[ClarificationQuestion]:
        """Generate general clarification questions."""
        # For general queries, fewer questions needed
        return []


class PlanningEngine:
    """Engine for generating comprehensive project plans."""

    def generate_plan(self, analysis: EnhancedAnalysis, llm: Any) -> Dict[str, str]:
        """Generate a comprehensive project plan."""

        plan_prompt = f"""Create a comprehensive project plan for: {analysis.query}

Please provide:
1. Project Overview
2. Technical Requirements
3. Implementation Steps
4. Timeline Estimate
5. Key Considerations

Mode: {analysis.mode.value}
Complexity: {analysis.complexity.value}
"""

        if analysis.questions and any(q.answer for q in analysis.questions):
            clarifications = "\n".join([
                f"- {q.question}: {q.answer}"
                for q in analysis.questions if q.answer
            ])
            plan_prompt += f"\n\nRequirements clarified:\n{clarifications}"

        try:
            plan_response = llm.chat(plan_prompt)

            return {
                'overview': 'Project analysis complete',
                'plan': plan_response,
                'next_steps': 'Ready to implement based on plan'
            }
        except Exception as e:
            return {
                'overview': 'Basic project structure identified',
                'plan': f'Will implement: {analysis.query}',
                'next_steps': 'Proceeding with implementation'
            }