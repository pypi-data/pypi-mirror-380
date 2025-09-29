"""
Core code command entry points.

This module contains the main Click command definitions and routing logic.
Extracted from the original code_commands.py to improve maintainability.
"""

import click
import os
from typing import Optional, Tuple, List
from pathlib import Path

from ...core.agent import SingleAgent
from ...core.agent_config import AgentConfig
from .collaboration import CollaborationManager
from .project import ProjectManager
from .workflows import WorkflowOrchestrator
from .utils import determine_operation_mode, determine_confirmation_level


@click.group(invoke_without_command=True)
@click.pass_context
@click.argument('request', nargs=-1, required=False)
@click.option('--session', '-s', help='Session ID for context')
@click.option('--branch', '-b', type=str, help='Create specific named feature branch')
@click.option('--no-branch', is_flag=True, help='Skip automatic branch creation')
@click.option('--auto', '-a', is_flag=True, help='Auto mode - skip prompts and execute directly')
@click.option('--fast', '-f', is_flag=True, help='Fast mode - optimized for speed')
@click.option('--stream', is_flag=True, help='Stream output in real-time')
@click.option('--yes', '-y', is_flag=True, help='Skip all confirmations')
@click.option('--review', is_flag=True, help='Force review mode for all operations')
@click.option('--interface', type=click.Choice(['simple', 'advanced', 'expert']),
              help='Interface complexity level')
@click.option('--project', '-p', type=str, help='Target project directory')
@click.option('--file', '-F', type=str, help='Target specific file')
@click.option('--blueprint', '-bp', type=str, help='Use specific blueprint')
@click.option('--template', '-t', type=str, help='Use project template')
@click.option('--branch-from', type=str, help='Create branch from specific commit/branch')
@click.option('--commit-msg', type=str, help='Custom commit message')
@click.option('--no-commit', is_flag=True, help='Skip automatic commits')
@click.option('--interactive', '-i', is_flag=True, help='Interactive mode with guided prompts')
@click.option('--config', type=str, help='Path to custom configuration file')
@click.option('--provider', type=str, help='LLM provider to use')
@click.option('--model', type=str, help='Specific model to use')
@click.option('--context-file', type=str, multiple=True, help='Additional context files')
@click.option('--exclude', type=str, multiple=True, help='Files/patterns to exclude')
@click.option('--output', '-o', type=str, help='Output directory/file')
@click.option('--format', type=str, help='Output format')
@click.option('--dry-run', is_flag=True, help='Show what would be done without executing')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--quiet', '-q', is_flag=True, help='Minimal output')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def code(ctx, request, session, branch, no_branch, auto, fast, stream, yes, review,
         interface, project, file, blueprint, template, branch_from, commit_msg,
         no_commit, interactive, config, provider, model, context_file, exclude,
         output, format, dry_run, verbose, quiet, debug):
    """
    Natural Language Code Interface

    Examples:
      metis code "Create a Python web server"
      metis code "Fix the bug in authentication.py" --file auth.py
      metis code "Add tests for the user module" --fast
      metis code "Refactor the database layer" --review
    """
    if ctx.invoked_subcommand is not None:
        return

    if not request:
        if interactive:
            _start_interactive_mode(session, **locals())
        else:
            click.echo(ctx.get_help())
        return

    request_text = ' '.join(request)

    try:
        # Initialize managers
        collab_manager = CollaborationManager()
        project_manager = ProjectManager()
        workflow_orchestrator = WorkflowOrchestrator()

        # Parse mentions for collaboration
        cleaned_request, mentioned_agents = collab_manager.parse_mentions(request_text)

        # Determine operation parameters
        operation_mode = determine_operation_mode(cleaned_request, auto, fast, stream)
        confirmation_level = determine_confirmation_level(operation_mode, yes, review)

        # Handle multi-agent collaboration if needed
        if mentioned_agents:
            responses = collab_manager.process_collaboration(
                mentioned_agents, cleaned_request, session
            )
            collab_manager.display_responses(responses)
            return

        # Initialize single agent
        agent_config = _create_agent_config(config, provider, model)
        agent = SingleAgent(config=agent_config)

        # Detect project context
        project_context = project_manager.detect_project_context(
            project or os.getcwd(), file, context_file
        )

        # Execute workflow
        workflow_orchestrator.execute(
            agent=agent,
            request=cleaned_request,
            project_context=project_context,
            session=session,
            operation_mode=operation_mode,
            confirmation_level=confirmation_level,
            options={
                'branch': branch,
                'no_branch': no_branch,
                'blueprint': blueprint,
                'template': template,
                'output': output,
                'format': format,
                'dry_run': dry_run,
                'verbose': verbose,
                'quiet': quiet,
                'debug': debug
            }
        )

    except Exception as e:
        if debug:
            raise
        click.echo(f"Error: {e}", err=True)
        ctx.exit(1)


@code.command()
@click.argument('action', type=str, default='create')
@click.argument('name', type=str, required=False)
@click.option('--template', '-t', type=str, help='Project template to use')
@click.option('--language', '-l', type=str, help='Primary programming language')
@click.option('--framework', '-f', type=str, help='Framework/library to use')
@click.option('--features', type=str, multiple=True, help='Features to include')
@click.option('--session', '-s', help='Session ID for context')
def project(action, name, template, language, framework, features, session):
    """Project management commands."""
    project_manager = ProjectManager()

    if action == 'create':
        project_manager.create_project(
            name=name,
            template=template,
            language=language,
            framework=framework,
            features=list(features)
        )
    elif action == 'analyze':
        project_manager.analyze_project(name or os.getcwd())
    elif action == 'status':
        project_manager.show_status(name or os.getcwd())
    else:
        click.echo(f"Unknown action: {action}")


@code.command()
@click.argument('target', type=str, required=False)
@click.option('--type', '-t', type=str, help='Test type (unit, integration, e2e)')
@click.option('--framework', '-f', type=str, help='Testing framework to use')
@click.option('--coverage', is_flag=True, help='Include coverage analysis')
@click.option('--session', '-s', help='Session ID for context')
def test(target, type, framework, coverage, session):
    """Generate and run tests."""
    workflow_orchestrator = WorkflowOrchestrator()

    workflow_orchestrator.execute_test_workflow(
        target=target or os.getcwd(),
        test_type=type,
        framework=framework,
        coverage=coverage,
        session=session
    )


@code.command()
@click.argument('target', type=str, required=False)
@click.option('--format', '-f', type=str, help='Documentation format (markdown, rst, html)')
@click.option('--api', is_flag=True, help='Generate API documentation')
@click.option('--session', '-s', help='Session ID for context')
def docs(target, format, api, session):
    """Generate documentation."""
    workflow_orchestrator = WorkflowOrchestrator()

    workflow_orchestrator.execute_docs_workflow(
        target=target or os.getcwd(),
        format=format,
        api=api,
        session=session
    )


@code.command()
def status():
    """Show current code project status."""
    project_manager = ProjectManager()
    project_manager.show_detailed_status(os.getcwd())


def _create_agent_config(config_path: Optional[str], provider: Optional[str],
                        model: Optional[str]) -> AgentConfig:
    """Create agent configuration."""
    if config_path and os.path.exists(config_path):
        config = AgentConfig.from_file(config_path)
    else:
        config = AgentConfig()

    if provider:
        config.llm_provider = provider
    if model:
        config.llm_model = model

    return config


def _start_interactive_mode(session: Optional[str], **kwargs):
    """Start interactive code interface."""
    from ..enhanced_input import create_enhanced_input

    click.echo("🚀 Interactive Code Mode")
    click.echo("Type your requests naturally or use /help for commands")

    input_handler = create_enhanced_input()

    while True:
        try:
            request = input_handler.prompt("metis code> ")
            if not request or request.lower() in ['/exit', '/quit']:
                break

            if request.startswith('/'):
                # Handle slash commands
                continue

            # Process as normal code request
            ctx = click.Context(code)
            ctx.invoke(code, request=request.split(), session=session, **kwargs)

        except KeyboardInterrupt:
            break
        except Exception as e:
            click.echo(f"Error: {e}", err=True)

    click.echo("Goodbye! 👋")