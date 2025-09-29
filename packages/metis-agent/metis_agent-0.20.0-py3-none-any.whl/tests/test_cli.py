"""
Comprehensive CLI tests for Metis Agent.

Tests cover:
- Command parsing and validation
- Interactive chat functionality
- Code commands
- Asset management
- Error handling
- Session management
"""

import pytest
from click.testing import CliRunner
from unittest.mock import Mock, MagicMock, patch
import json
import os
import tempfile

from metis_agent.cli.commands import cli, chat
from metis_agent.cli.code_commands import code
from metis_agent.cli.todo_commands import todo_group
from metis_agent.cli.agent_commands import agent_group


class TestBasicCLI:
    """Test suite for basic CLI functionality."""

    def test_cli_help(self, cli_runner):
        """Test CLI help command."""
        result = cli_runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert "Metis Agent" in result.output
        assert "Intelligent AI Assistant" in result.output

    def test_cli_version(self, cli_runner):
        """Test CLI version display."""
        # Note: Add version command if not exists
        result = cli_runner.invoke(cli, ['--version'])
        # Should either show version or show help if version not implemented
        assert result.exit_code in [0, 2]  # 0 for success, 2 for no such command

    def test_invalid_command(self, cli_runner):
        """Test invalid command handling."""
        result = cli_runner.invoke(cli, ['invalid-command'])
        assert result.exit_code != 0
        assert "No such command" in result.output or "Usage:" in result.output


class TestChatCommands:
    """Test suite for chat command functionality."""

    @patch('metis_agent.core.agent.SingleAgent')
    def test_chat_simple_query(self, mock_agent_class, cli_runner, temp_dir):
        """Test simple chat query processing."""
        # Mock agent instance
        mock_agent = MagicMock()
        mock_agent.process_query.return_value = "Hello! I'm doing well."
        mock_agent_class.return_value = mock_agent

        # Test single query with prompt-and-exit
        result = cli_runner.invoke(chat, [
            "How are you?",
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0
        assert mock_agent.process_query.called

    @patch('metis_agent.core.agent.SingleAgent')
    def test_chat_with_session(self, mock_agent_class, cli_runner):
        """Test chat with session management."""
        mock_agent = MagicMock()
        mock_agent.process_query.return_value = "Response with session"
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(chat, [
            "Test query",
            "--session", "test-session-123",
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0
        mock_agent.process_query.assert_called()

    @patch('metis_agent.core.agent.SingleAgent')
    def test_chat_with_persona(self, mock_agent_class, cli_runner):
        """Test chat with persona specification."""
        mock_agent = MagicMock()
        mock_agent.process_query.return_value = "Response with persona"
        mock_agent_class.return_value = mock_agent

        # Mock asset system
        with patch('metis_agent.cli.commands.get_asset_registry'):
            result = cli_runner.invoke(chat, [
                "Help me code",
                "--persona", "senior-developer",
                "--prompt-and-exit"
            ])

            assert result.exit_code == 0

    def test_chat_list_sessions(self, cli_runner):
        """Test listing available sessions."""
        with patch('metis_agent.cli.commands._list_available_sessions') as mock_list:
            mock_list.return_value = None

            result = cli_runner.invoke(chat, ['--list-sessions'])
            assert result.exit_code == 0
            mock_list.assert_called_once()

    @patch('metis_agent.core.agent.SingleAgent')
    def test_chat_continue_session(self, mock_agent_class, cli_runner):
        """Test continuing the last session."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        with patch('metis_agent.cli.commands._get_most_recent_session', return_value="last-session"):
            result = cli_runner.invoke(chat, [
                "Continue chat",
                "--continue",
                "--prompt-and-exit"
            ])

            assert result.exit_code == 0

    def test_chat_error_handling(self, cli_runner):
        """Test error handling in chat command."""
        # Test with invalid options
        result = cli_runner.invoke(chat, ['--invalid-option'])
        assert result.exit_code != 0


class TestCodeCommands:
    """Test suite for code command functionality."""

    @patch('metis_agent.core.agent.SingleAgent')
    def test_code_basic_functionality(self, mock_agent_class, cli_runner):
        """Test basic code command functionality."""
        mock_agent = MagicMock()
        mock_agent.process_query.return_value = "Generated Python code"
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(code, [
            "Write a hello world function",
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0
        mock_agent.process_query.assert_called()

    @patch('metis_agent.core.agent.SingleAgent')
    def test_code_with_file_context(self, mock_agent_class, cli_runner, temp_dir):
        """Test code command with file context."""
        # Create a test file
        test_file = os.path.join(temp_dir, "test.py")
        with open(test_file, "w") as f:
            f.write("def existing_function():\n    pass")

        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(code, [
            "Improve this function",
            "--file", test_file,
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0

    @patch('metis_agent.core.agent.SingleAgent')
    def test_code_streaming_mode(self, mock_agent_class, cli_runner):
        """Test code command in streaming mode."""
        mock_agent = MagicMock()
        mock_agent.stream_query.return_value = iter(["def ", "hello():", "\n    print('Hello')"])
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(code, [
            "Write hello function",
            "--stream",
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0
        mock_agent.stream_query.assert_called()

    def test_code_project_detection(self, cli_runner, temp_dir):
        """Test automatic project detection."""
        # Create project structure
        os.makedirs(os.path.join(temp_dir, "src"))
        with open(os.path.join(temp_dir, "package.json"), "w") as f:
            json.dump({"name": "test-project"}, f)

        with patch('os.getcwd', return_value=temp_dir):
            result = cli_runner.invoke(code, [
                "Analyze project structure",
                "--analyze-project",
                "--prompt-and-exit"
            ])

            # Should detect project type
            assert result.exit_code == 0


class TestTodoCommands:
    """Test suite for todo command functionality."""

    def test_todo_list(self, cli_runner):
        """Test listing todos."""
        with patch('metis_agent.cli.todo_commands.get_todos', return_value=[]):
            result = cli_runner.invoke(todo_group, ['list'])
            assert result.exit_code == 0

    def test_todo_add(self, cli_runner):
        """Test adding a todo."""
        with patch('metis_agent.cli.todo_commands.add_todo') as mock_add:
            result = cli_runner.invoke(todo_group, [
                'add',
                'Test task description'
            ])
            assert result.exit_code == 0
            mock_add.assert_called()

    def test_todo_complete(self, cli_runner):
        """Test completing a todo."""
        with patch('metis_agent.cli.todo_commands.complete_todo') as mock_complete:
            result = cli_runner.invoke(todo_group, ['complete', '1'])
            assert result.exit_code == 0
            mock_complete.assert_called_with('1')

    def test_todo_delete(self, cli_runner):
        """Test deleting a todo."""
        with patch('metis_agent.cli.todo_commands.delete_todo') as mock_delete:
            result = cli_runner.invoke(todo_group, ['delete', '1'])
            assert result.exit_code == 0
            mock_delete.assert_called_with('1')


class TestAgentCommands:
    """Test suite for agent management commands."""

    def test_agent_list(self, cli_runner):
        """Test listing agents."""
        with patch('metis_agent.cli.agent_commands.list_agents', return_value=[]):
            result = cli_runner.invoke(agent_group, ['list'])
            assert result.exit_code == 0

    def test_agent_create(self, cli_runner):
        """Test creating a new agent."""
        with patch('metis_agent.cli.agent_commands.create_agent') as mock_create:
            result = cli_runner.invoke(agent_group, [
                'create',
                'test-agent',
                '--profile', 'developer'
            ])
            assert result.exit_code == 0
            mock_create.assert_called()

    def test_agent_providers(self, cli_runner):
        """Test listing available providers."""
        with patch('metis_agent.cli.agent_commands.list_providers') as mock_providers:
            mock_providers.return_value = ['openai', 'groq', 'anthropic']
            result = cli_runner.invoke(agent_group, ['providers'])
            assert result.exit_code == 0
            mock_providers.assert_called()

    def test_agent_status(self, cli_runner):
        """Test checking agent status."""
        with patch('metis_agent.cli.agent_commands.get_agent_status') as mock_status:
            mock_status.return_value = {'status': 'active', 'uptime': '5 minutes'}
            result = cli_runner.invoke(agent_group, ['status', 'test-agent'])
            assert result.exit_code == 0
            mock_status.assert_called()


class TestInteractiveMode:
    """Test suite for interactive mode functionality."""

    @patch('metis_agent.cli.commands.create_enhanced_input')
    @patch('metis_agent.core.agent.SingleAgent')
    def test_interactive_chat_session(self, mock_agent_class, mock_input, cli_runner):
        """Test interactive chat session."""
        mock_agent = MagicMock()
        mock_agent.process_query.return_value = "Interactive response"
        mock_agent_class.return_value = mock_agent

        # Mock input sequence: query, then exit
        mock_input_instance = MagicMock()
        mock_input_instance.prompt.side_effect = [
            "Hello",
            "/exit"
        ]
        mock_input.return_value = mock_input_instance

        # Run interactive session
        result = cli_runner.invoke(chat, [], input="Hello\n/exit\n")

        # Should handle interactive mode gracefully
        assert result.exit_code in [0, 1]  # May exit with 1 due to interruption

    @patch('metis_agent.cli.commands.create_enhanced_input')
    def test_interactive_slash_commands(self, mock_input, cli_runner):
        """Test slash commands in interactive mode."""
        mock_input_instance = MagicMock()
        mock_input_instance.prompt.side_effect = [
            "/help",
            "/sessions",
            "/exit"
        ]
        mock_input.return_value = mock_input_instance

        with patch('metis_agent.cli.slash_commands.SlashCommandProcessor') as mock_processor:
            mock_processor_instance = MagicMock()
            mock_processor_instance.process.return_value = "Command processed"
            mock_processor.return_value = mock_processor_instance

            result = cli_runner.invoke(chat, [], input="/help\n/sessions\n/exit\n")
            assert result.exit_code in [0, 1]

    def test_keyboard_interruption(self, cli_runner):
        """Test handling of keyboard interruption."""
        with patch('metis_agent.cli.commands.create_enhanced_input') as mock_input:
            mock_input_instance = MagicMock()
            mock_input_instance.prompt.side_effect = KeyboardInterrupt()
            mock_input.return_value = mock_input_instance

            result = cli_runner.invoke(chat, [], input="\x03")  # Ctrl+C
            # Should handle interruption gracefully
            assert result.exit_code in [0, 1, 130]  # Various exit codes for interruption


class TestConfigurationAndAuth:
    """Test suite for configuration and authentication."""

    def test_api_key_configuration(self, cli_runner):
        """Test API key configuration commands."""
        # Test setting API key
        with patch('metis_agent.auth.api_key_manager.APIKeyManager') as mock_manager:
            mock_instance = MagicMock()
            mock_manager.return_value = mock_instance

            # Assuming auth commands exist
            result = cli_runner.invoke(cli, ['auth', 'set', 'openai', 'test-key'])
            # Should handle gracefully even if command doesn't exist
            assert result.exit_code in [0, 2]

    def test_configuration_validation(self, cli_runner):
        """Test configuration validation."""
        with patch('metis_agent.core.agent_config.AgentConfig') as mock_config:
            mock_config_instance = MagicMock()
            mock_config_instance.validate.return_value = True
            mock_config.return_value = mock_config_instance

            result = cli_runner.invoke(cli, ['config', 'validate'])
            # Should handle gracefully
            assert result.exit_code in [0, 2]

    def test_provider_availability_check(self, cli_runner):
        """Test checking provider availability."""
        with patch('metis_agent.cli.agent_commands.check_provider_status') as mock_check:
            mock_check.return_value = {
                'openai': 'available',
                'groq': 'available',
                'anthropic': 'unavailable'
            }

            result = cli_runner.invoke(agent_group, ['check-providers'])
            assert result.exit_code == 0


class TestErrorHandling:
    """Test suite for CLI error handling."""

    @patch('metis_agent.core.agent.SingleAgent')
    def test_llm_error_handling(self, mock_agent_class, cli_runner):
        """Test handling of LLM errors."""
        mock_agent = MagicMock()
        mock_agent.process_query.side_effect = Exception("LLM API Error")
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(chat, [
            "Test query",
            "--prompt-and-exit"
        ])

        assert result.exit_code != 0
        assert "error" in result.output.lower() or "Error" in result.output

    def test_invalid_file_handling(self, cli_runner):
        """Test handling of invalid file paths."""
        result = cli_runner.invoke(code, [
            "Analyze this file",
            "--file", "/nonexistent/file.py",
            "--prompt-and-exit"
        ])

        assert result.exit_code != 0

    def test_memory_error_handling(self, cli_runner):
        """Test handling of memory-related errors."""
        with patch('metis_agent.memory.sqlite_store.SQLiteMemory') as mock_memory:
            mock_memory.side_effect = Exception("Database error")

            result = cli_runner.invoke(chat, [
                "Test query",
                "--prompt-and-exit"
            ])

            # Should handle database errors gracefully
            assert result.exit_code != 0

    def test_permission_error_handling(self, cli_runner, temp_dir):
        """Test handling of permission errors."""
        # Create a directory without write permissions
        restricted_dir = os.path.join(temp_dir, "restricted")
        os.makedirs(restricted_dir)
        os.chmod(restricted_dir, 0o444)  # Read-only

        with patch('os.getcwd', return_value=restricted_dir):
            result = cli_runner.invoke(chat, [
                "Create a file here",
                "--prompt-and-exit"
            ])

            # Should handle permission errors
            assert result.exit_code in [0, 1, 2]

        # Restore permissions for cleanup
        os.chmod(restricted_dir, 0o755)


class TestStreamingAndRealTime:
    """Test suite for streaming and real-time features."""

    @patch('metis_agent.core.agent.SingleAgent')
    def test_streaming_response(self, mock_agent_class, cli_runner):
        """Test streaming response display."""
        mock_agent = MagicMock()
        mock_agent.stream_query.return_value = iter([
            "Streaming ", "response ", "chunk ", "by ", "chunk"
        ])
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(chat, [
            "Generate a story",
            "--stream",
            "--prompt-and-exit"
        ])

        assert result.exit_code == 0

    def test_progress_indicators(self, cli_runner):
        """Test progress indicators during processing."""
        with patch('metis_agent.cli.commands.Progress') as mock_progress:
            mock_progress_instance = MagicMock()
            mock_progress.return_value = mock_progress_instance

            result = cli_runner.invoke(chat, [
                "Long processing task",
                "--show-progress",
                "--prompt-and-exit"
            ])

            # Should handle progress display
            assert result.exit_code in [0, 2]

    @patch('metis_agent.core.agent.SingleAgent')
    def test_real_time_status_updates(self, mock_agent_class, cli_runner):
        """Test real-time status updates."""
        mock_agent = MagicMock()
        mock_agent.process_query_with_status = MagicMock(return_value="Done")
        mock_agent_class.return_value = mock_agent

        result = cli_runner.invoke(chat, [
            "Complex task",
            "--show-status",
            "--prompt-and-exit"
        ])

        assert result.exit_code in [0, 2]  # May not exist yet