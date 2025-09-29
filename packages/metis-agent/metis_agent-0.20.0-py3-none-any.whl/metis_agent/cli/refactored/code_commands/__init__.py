"""
Refactored code commands module.

This package breaks down the large code_commands.py file into focused modules:
- core: Main command entry points
- collaboration: Multi-agent collaboration features
- project: Project detection and management
- workflows: Code workflow orchestration
- utils: Utility functions and helpers
"""

from .core import code
from .collaboration import CollaborationManager
from .project import ProjectManager
from .workflows import WorkflowOrchestrator

__all__ = [
    'code',
    'CollaborationManager',
    'ProjectManager',
    'WorkflowOrchestrator'
]