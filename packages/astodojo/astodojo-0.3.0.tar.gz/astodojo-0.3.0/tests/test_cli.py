"""Tests for the CLI interface."""

import tempfile
import os
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from astodojo.cli import cli, scan, init, github_report, github_sync


class TestCLI:
    """Test the CLI commands."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_scan_command_file(self):
        """Test scanning a single file."""
        code = '''
def test_func():
    # TODO: Implement this
    pass
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            result = self.runner.invoke(scan, [temp_file])

            assert result.exit_code == 0
            assert "TODO" in result.output
            assert "Implement this" in result.output

        finally:
            os.unlink(temp_file)

    def test_scan_command_directory(self):
        """Test scanning a directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a Python file with TODO
            py_file = Path(temp_dir) / "test.py"
            py_file.write_text('''
def func():
    # BLAME: Review this
    pass
''')

            result = self.runner.invoke(scan, [temp_dir])

            assert result.exit_code == 0
            assert "BLAME" in result.output
            assert "Review this" in result.output

    def test_scan_command_json_format(self):
        """Test scanning with JSON output format."""
        code = '''
# TODO: Test task
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            result = self.runner.invoke(scan, [temp_file, '--format', 'json'])

            assert result.exit_code == 0
            assert '"tag": "TODO"' in result.output
            assert '"content": "Test task"' in result.output

        finally:
            os.unlink(temp_file)

    def test_scan_command_report_format(self):
        """Test scanning with report output format."""
        code = '''
# TODO: Task 1
# BLAME: Issue 1
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            result = self.runner.invoke(scan, [temp_file, '--format', 'report'])

            assert result.exit_code == 0
            assert "Total TODO items: 2" in result.output
            assert "TODO: 1" in result.output
            assert "BLAME: 1" in result.output

        finally:
            os.unlink(temp_file)

    def test_scan_command_exclude_pattern(self):
        """Test scanning with exclude patterns."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create included and excluded files
            included_file = Path(temp_dir) / "included.py"
            excluded_file = Path(temp_dir) / "excluded.py"

            included_file.write_text('# TODO: Should be found')
            excluded_file.write_text('# BLAME: Should be excluded')

            result = self.runner.invoke(scan, [temp_dir, '--exclude', 'excluded.py'])

            assert result.exit_code == 0
            assert "Should be found" in result.output
            assert "Should be excluded" not in result.output

    def test_init_command(self):
        """Test the init command."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.runner.invoke(init, ['--directory', temp_dir])

            assert result.exit_code == 0
            assert "Created config file" in result.output

            config_path = Path(temp_dir) / '.astodojorc'
            assert config_path.exists()

    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPOSITORY': 'test/repo'})
    def test_github_report_command_missing_creds(self):
        """Test GitHub report command with missing credentials."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Clear environment variables for this test
            with patch.dict(os.environ, {}, clear=True):
                result = self.runner.invoke(github_report, [temp_dir])

                assert result.exit_code == 1
                assert "🔐 GitHub Authentication Required" in result.output

    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPOSITORY': 'test/repo'})
    @patch('astodojo.github.GitHubIntegration')
    def test_github_report_command_with_mock(self, mock_github_class):
        """Test GitHub report command with mocked GitHub integration."""
        mock_github = mock_github_class.return_value
        mock_github.generate_report.return_value = {
            'new_todos': 1,
            'changed_todos': 0,
            'todos_needing_issues': 1,
            'existing_issues': 0,
            'sync_recommendations': [{
                'action': 'create_issue',
                'todo': {
                    'tag': 'BLAME',
                    'file_path': 'test.py',
                    'line_number': 10,
                    'content': 'Test issue'
                },
                'reason': 'BLAME tag requires human review'
            }]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test Python file
            py_file = Path(temp_dir) / "test.py"
            py_file.write_text('# BLAME: Test issue')

            result = self.runner.invoke(github_report, [temp_dir])

            assert result.exit_code == 0
            assert "GitHub Sync Report" in result.output
            assert "Create issue for BLAME" in result.output

    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPOSITORY': 'test/repo'})
    def test_github_sync_command_missing_creds(self):
        """Test GitHub sync command with missing credentials."""
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.dict(os.environ, {}, clear=True):
                result = self.runner.invoke(github_sync, [temp_dir])

                assert result.exit_code == 1
                assert "🔐 GitHub Authentication Required" in result.output

    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPOSITORY': 'test/repo'})
    @patch('astodojo.github.GitHubIntegration')
    def test_github_sync_command_with_mock(self, mock_github_class):
        """Test GitHub sync command with mocked GitHub integration."""
        mock_github = mock_github_class.return_value
        mock_github.sync_to_github.return_value = [{
            'action': 'created',
            'todo': {
                'tag': 'BLAME',
                'file_path': 'test.py',
                'line_number': 10,
                'content': 'Test issue'
            },
            'issue_number': 42,
            'issue_url': 'https://github.com/test/repo/issues/42'
        }]

        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test Python file
            py_file = Path(temp_dir) / "test.py"
            py_file.write_text('# BLAME: Test issue')

            result = self.runner.invoke(github_sync, [temp_dir, '--tag', 'BLAME', '--count', '1'])

            assert result.exit_code == 0
            assert "Created issue #42" in result.output
            assert "https://github.com/test/repo/issues/42" in result.output

    def test_scan_nonexistent_file(self):
        """Test scanning a nonexistent file."""
        result = self.runner.invoke(scan, ['nonexistent.py'])

        assert result.exit_code == 1
        assert "does not exist" in result.output

    def test_scan_non_python_file(self):
        """Test scanning a non-Python file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write('not python code')
            temp_file = f.name

        try:
            result = self.runner.invoke(scan, [temp_file])

            assert result.exit_code == 1
            assert "Can only scan Python files" in result.output

        finally:
            os.unlink(temp_file)
