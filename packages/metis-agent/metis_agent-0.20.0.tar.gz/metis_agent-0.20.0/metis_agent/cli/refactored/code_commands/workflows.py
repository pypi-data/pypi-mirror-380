"""
Code workflow orchestration.

This module handles different types of code workflows including
development, testing, documentation generation, and deployment.
"""

from typing import Dict, Any, Optional, List
import os
from pathlib import Path

from ...core.agent import SingleAgent


class WorkflowOrchestrator:
    """Orchestrates various code-related workflows."""

    def __init__(self):
        self.workflow_handlers = {
            'development': self._handle_development_workflow,
            'testing': self._handle_testing_workflow,
            'documentation': self._handle_documentation_workflow,
            'deployment': self._handle_deployment_workflow,
            'refactoring': self._handle_refactoring_workflow,
            'debugging': self._handle_debugging_workflow,
            'analysis': self._handle_analysis_workflow
        }

    def execute(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                session: Optional[str] = None, operation_mode: str = 'balanced',
                confirmation_level: str = 'normal', options: Optional[Dict[str, Any]] = None):
        """Execute appropriate workflow based on request type."""
        options = options or {}

        # Determine workflow type
        workflow_type = self._determine_workflow_type(request, project_context)

        # Execute workflow
        handler = self.workflow_handlers.get(workflow_type, self._handle_general_workflow)
        return handler(agent, request, project_context, session, operation_mode, confirmation_level, options)

    def _determine_workflow_type(self, request: str, project_context: Dict[str, Any]) -> str:
        """Determine the appropriate workflow type for the request."""
        request_lower = request.lower()

        # Testing workflow indicators
        if any(keyword in request_lower for keyword in ['test', 'testing', 'unit test', 'integration test']):
            return 'testing'

        # Documentation workflow indicators
        if any(keyword in request_lower for keyword in ['document', 'docs', 'documentation', 'readme']):
            return 'documentation'

        # Deployment workflow indicators
        if any(keyword in request_lower for keyword in ['deploy', 'deployment', 'build', 'package']):
            return 'deployment'

        # Refactoring workflow indicators
        if any(keyword in request_lower for keyword in ['refactor', 'restructure', 'optimize', 'clean up']):
            return 'refactoring'

        # Debugging workflow indicators
        if any(keyword in request_lower for keyword in ['debug', 'fix', 'bug', 'error', 'issue']):
            return 'debugging'

        # Analysis workflow indicators
        if any(keyword in request_lower for keyword in ['analyze', 'analysis', 'review', 'audit']):
            return 'analysis'

        # Default to development workflow
        return 'development'

    def _handle_development_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                   session: Optional[str], operation_mode: str, confirmation_level: str,
                                   options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general development workflow."""
        # Check if this is a complete project request
        if self._is_complete_project_request(request):
            return self._handle_project_creation_workflow(agent, request, project_context, session, options)

        # Check if blueprint detection is needed
        if self._should_use_blueprints(request, project_context):
            return self._handle_blueprint_workflow(agent, request, project_context, session, options)

        # Standard development workflow
        return self._handle_standard_development(agent, request, project_context, session, options)

    def _handle_testing_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                               session: Optional[str], operation_mode: str, confirmation_level: str,
                               options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle testing workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'testing')

        # Add testing-specific context
        testing_context = f"""
Testing Context:
- Project languages: {', '.join(project_context.get('languages', []))}
- Frameworks: {', '.join(project_context.get('frameworks', []))}
- Existing test files: {self._find_test_files(project_context)}

Request: {enhanced_request}
"""

        response = agent.process_query(testing_context, session_id=session)
        return {'type': 'testing', 'response': response}

    def _handle_documentation_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                     session: Optional[str], operation_mode: str, confirmation_level: str,
                                     options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle documentation workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'documentation')

        # Add documentation-specific context
        doc_context = f"""
Documentation Context:
- Project type: {', '.join(project_context.get('languages', []))}
- Main files: {project_context.get('structure', {}).get('main_files', [])}
- Existing documentation: {self._find_documentation_files(project_context)}

Request: {enhanced_request}
"""

        response = agent.process_query(doc_context, session_id=session)
        return {'type': 'documentation', 'response': response}

    def _handle_deployment_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                  session: Optional[str], operation_mode: str, confirmation_level: str,
                                  options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle deployment workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'deployment')

        # Add deployment-specific context
        deploy_context = f"""
Deployment Context:
- Project languages: {', '.join(project_context.get('languages', []))}
- Frameworks: {', '.join(project_context.get('frameworks', []))}
- Existing deployment configs: {self._find_deployment_configs(project_context)}

Request: {enhanced_request}
"""

        response = agent.process_query(deploy_context, session_id=session)
        return {'type': 'deployment', 'response': response}

    def _handle_refactoring_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                   session: Optional[str], operation_mode: str, confirmation_level: str,
                                   options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle refactoring workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'refactoring')

        # Add refactoring-specific context
        refactor_context = f"""
Refactoring Context:
- Project structure: {self._summarize_structure(project_context)}
- Target file: {options.get('target_file', 'Not specified')}
- Code quality considerations for: {', '.join(project_context.get('languages', []))}

Request: {enhanced_request}
"""

        response = agent.process_query(refactor_context, session_id=session)
        return {'type': 'refactoring', 'response': response}

    def _handle_debugging_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                 session: Optional[str], operation_mode: str, confirmation_level: str,
                                 options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle debugging workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'debugging')

        # Add debugging-specific context
        debug_context = f"""
Debugging Context:
- Project languages: {', '.join(project_context.get('languages', []))}
- Target file: {options.get('target_file', 'Not specified')}
- Error logs or symptoms should be included in the request

Request: {enhanced_request}
"""

        response = agent.process_query(debug_context, session_id=session)
        return {'type': 'debugging', 'response': response}

    def _handle_analysis_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                session: Optional[str], operation_mode: str, confirmation_level: str,
                                options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle code analysis workflow."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'analysis')

        # Add analysis-specific context
        analysis_context = f"""
Analysis Context:
- Project overview: {self._create_project_summary(project_context)}
- Analysis scope: {options.get('scope', 'Full project')}
- Focus areas: {options.get('focus_areas', 'General code quality')}

Request: {enhanced_request}
"""

        response = agent.process_query(analysis_context, session_id=session)
        return {'type': 'analysis', 'response': response}

    def _handle_general_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                               session: Optional[str], operation_mode: str, confirmation_level: str,
                               options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general code requests."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'general')

        response = agent.process_query(enhanced_request, session_id=session)
        return {'type': 'general', 'response': response}

    def _handle_project_creation_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                        session: Optional[str], options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle complete project creation workflow."""
        # Enhanced context for project creation
        creation_context = f"""
Project Creation Request: {request}

Please create a complete project structure including:
1. Project setup and configuration files
2. Basic directory structure
3. Initial code files
4. Documentation (README)
5. Testing setup
6. Dependency management files

Current directory: {project_context.get('directory', 'unknown')}
"""

        response = agent.process_query(creation_context, session_id=session)
        return {'type': 'project_creation', 'response': response}

    def _handle_blueprint_workflow(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                 session: Optional[str], options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle blueprint-based development workflow."""
        blueprint_context = f"""
Blueprint Development Request: {request}

Project Context:
{self._create_project_summary(project_context)}

Please use appropriate blueprints to handle this request systematically.
"""

        response = agent.process_query(blueprint_context, session_id=session)
        return {'type': 'blueprint', 'response': response}

    def _handle_standard_development(self, agent: SingleAgent, request: str, project_context: Dict[str, Any],
                                   session: Optional[str], options: Dict[str, Any]) -> Dict[str, Any]:
        """Handle standard development requests."""
        enhanced_request = self._enhance_request_with_context(request, project_context, 'development')

        response = agent.process_query(enhanced_request, session_id=session)
        return {'type': 'development', 'response': response}

    def execute_test_workflow(self, target: str, test_type: Optional[str] = None,
                            framework: Optional[str] = None, coverage: bool = False,
                            session: Optional[str] = None):
        """Execute testing workflow."""
        # Implementation for test workflow
        pass

    def execute_docs_workflow(self, target: str, format: Optional[str] = None,
                            api: bool = False, session: Optional[str] = None):
        """Execute documentation workflow."""
        # Implementation for docs workflow
        pass

    def _enhance_request_with_context(self, request: str, project_context: Dict[str, Any],
                                    workflow_type: str) -> str:
        """Enhance request with relevant project context."""
        context_summary = self._create_project_summary(project_context)

        enhanced_request = f"""
Request: {request}

Project Context:
{context_summary}

Workflow Type: {workflow_type}
"""

        # Add file-specific context if available
        if 'file_context' in project_context:
            file_context = project_context['file_context']
            enhanced_request += f"""
Target File: {file_context.get('relative_path', 'unknown')}
File Language: {file_context.get('language', 'unknown')}
File Size: {file_context.get('lines', 0)} lines
"""

        return enhanced_request

    def _create_project_summary(self, project_context: Dict[str, Any]) -> str:
        """Create a concise project summary."""
        languages = ', '.join(project_context.get('languages', ['unknown']))
        frameworks = ', '.join(project_context.get('frameworks', ['none']))
        structure = project_context.get('structure', {})

        summary = f"""
- Languages: {languages}
- Frameworks: {frameworks}
- Total files: {structure.get('total_files', 0)}
- Project directory: {project_context.get('directory', 'unknown')}
- Git repository: {project_context.get('is_git_repo', False)}
"""

        return summary.strip()

    def _summarize_structure(self, project_context: Dict[str, Any]) -> str:
        """Summarize project structure."""
        structure = project_context.get('structure', {})
        return f"{structure.get('total_files', 0)} files in {len(structure.get('directories', []))} directories"

    def _find_test_files(self, project_context: Dict[str, Any]) -> List[str]:
        """Find existing test files in the project."""
        # Implementation to find test files
        return []

    def _find_documentation_files(self, project_context: Dict[str, Any]) -> List[str]:
        """Find existing documentation files."""
        structure = project_context.get('structure', {})
        doc_files = []

        main_files = structure.get('main_files', [])
        for file in main_files:
            if any(doc_pattern in file.lower() for doc_pattern in ['readme', 'doc', 'guide']):
                doc_files.append(file)

        return doc_files

    def _find_deployment_configs(self, project_context: Dict[str, Any]) -> List[str]:
        """Find existing deployment configuration files."""
        structure = project_context.get('structure', {})
        deploy_files = []

        main_files = structure.get('main_files', [])
        for file in main_files:
            if any(deploy_pattern in file.lower() for deploy_pattern in [
                'dockerfile', 'docker-compose', 'deploy', 'k8s', 'kubernetes'
            ]):
                deploy_files.append(file)

        return deploy_files

    def _is_complete_project_request(self, request: str) -> bool:
        """Check if request is for complete project creation."""
        request_lower = request.lower()
        project_indicators = [
            'create project', 'new project', 'build project',
            'setup project', 'initialize project', 'start project',
            'generate project', 'scaffold project'
        ]

        return any(indicator in request_lower for indicator in project_indicators)

    def _should_use_blueprints(self, request: str, project_context: Dict[str, Any]) -> bool:
        """Determine if blueprints should be used for this request."""
        request_lower = request.lower()
        blueprint_indicators = [
            'blueprint', 'template', 'pattern', 'architecture',
            'full implementation', 'complete solution'
        ]

        # Use blueprints for complex requests or when explicitly mentioned
        return any(indicator in request_lower for indicator in blueprint_indicators)