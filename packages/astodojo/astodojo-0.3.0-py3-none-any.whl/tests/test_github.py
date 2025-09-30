"""Tests for GitHub integration."""

import tempfile
import json
from unittest.mock import patch, MagicMock

import pytest

from astodojo.core import TodoItem, TagType
from astodojo.github import GitHubCache, GitHubClient, GitHubIntegration


class TestGitHubCache:
    """Test the GitHub cache functionality."""

    def test_cache_initialization(self):
        """Test cache initialization."""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_file = f"{temp_dir}/test_cache.json"
            cache = GitHubCache(cache_file)

            assert str(cache.cache_file) == cache_file
            assert cache.data == {}

    def test_cache_save_and_load(self):
        """Test saving and loading cache data."""
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_file = f"{temp_dir}/test_cache.json"
            cache = GitHubCache(cache_file)

            # Set some data - create actual TodoItem objects
            from astodojo.core import TodoItem, TagType
            test_todos = [
                TodoItem('test.py', 1, TagType.TODO, 'Test todo')
            ]
            cache.set_cached_todos(test_todos)

            test_issues = [{'number': 1, 'title': 'Test issue'}]
            cache.set_github_issues(test_issues)

            # Create new cache instance to test loading
            cache2 = GitHubCache(cache_file)

            cached_todos = cache2.get_cached_todos()
            assert len(cached_todos) == 1
            assert cached_todos[0]['file_path'] == 'test.py'
            assert cached_todos[0]['tag'] == 'TODO'
            assert cache2.get_github_issues() == test_issues


class TestGitHubClient:
    """Test the GitHub client."""

    def test_client_initialization(self):
        """Test GitHub client initialization."""
        with patch('requests.Session') as mock_session:
            client = GitHubClient('test_token', 'owner/repo')

            assert client.token == 'test_token'
            assert client.owner == 'owner'
            assert client.repo == 'repo'

            # Check that session was configured
            mock_session.assert_called_once()
            mock_session.return_value.headers.update.assert_called()

    @patch('requests.Session')
    def test_get_issues(self, mock_session_class):
        """Test getting issues from GitHub."""
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session

        # Mock the API responses - first page has data, second page is empty
        mock_response1 = MagicMock()
        mock_response1.status_code = 200
        mock_response1.json.return_value = [
            {'number': 1, 'title': 'Issue 1'},
            {'number': 2, 'title': 'Issue 2'}
        ]

        mock_response2 = MagicMock()
        mock_response2.status_code = 200
        mock_response2.json.return_value = []  # Empty to stop pagination

        mock_session.get.side_effect = [mock_response1, mock_response2]

        client = GitHubClient('token', 'owner/repo')
        issues = client.get_issues()

        assert len(issues) == 2
        assert issues[0]['title'] == 'Issue 1'
        assert issues[1]['title'] == 'Issue 2'

        # Check that the API was called correctly
        assert mock_session.get.call_count >= 1
        # The exact call depends on the pagination logic

    @patch('requests.Session')
    def test_create_issue(self, mock_session_class):
        """Test creating an issue on GitHub."""
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session

        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {
            'number': 42,
            'title': 'Test Issue',
            'html_url': 'https://github.com/owner/repo/issues/42'
        }
        mock_session.post.return_value = mock_response

        client = GitHubClient('token', 'owner/repo')
        issue = client.create_issue('Test Issue', 'Issue body', ['bug'])

        assert issue['number'] == 42
        assert issue['title'] == 'Test Issue'

        # Check that the API was called correctly
        expected_data = {
            'title': 'Test Issue',
            'body': 'Issue body',
            'labels': ['bug']
        }
        mock_session.post.assert_called_with(
            'https://api.github.com/repos/owner/repo/issues',
            json=expected_data
        )


class TestGitHubIntegration:
    """Test the GitHub integration functionality."""

    @patch('astodojo.github.GitHubClient')
    def test_generate_report(self, mock_client_class):
        """Test generating a sync report."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # Mock cache data
        with patch('astodojo.github.GitHubCache') as mock_cache_class:
            mock_cache = MagicMock()
            mock_cache_class.return_value = mock_cache
            mock_cache.get_cached_todos.return_value = []
            mock_cache.get_github_issues.return_value = []

            integration = GitHubIntegration('token', 'owner/repo')

            # Create test TODOs
            todos = [
                TodoItem('test.py', 1, TagType.BLAME, 'Test blame')
            ]

            report = integration.generate_report(todos)

            assert 'new_todos' in report
            assert 'todos_needing_issues' in report
            assert 'sync_recommendations' in report

    @patch('astodojo.github.GitHubClient')
    def test_sync_to_github(self, mock_client_class):
        """Test syncing TODOs to GitHub."""
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # Mock the create_issue response
        mock_client.create_issue.return_value = {
            'number': 1,
            'html_url': 'https://github.com/test/repo/issues/1'
        }

        with patch('astodojo.github.GitHubCache'):
            integration = GitHubIntegration('token', 'owner/repo')

            todos = [
                TodoItem('test.py', 1, TagType.BLAME, 'Test blame')
            ]

            results = integration.sync_to_github(todos, TagType.BLAME, 1)

            assert len(results) == 1
            assert results[0]['action'] == 'created'
            assert results[0]['issue_number'] == 1

            # Check that create_issue was called
            mock_client.create_issue.assert_called_once()
            call_args = mock_client.create_issue.call_args
            if call_args:
                args, kwargs = call_args
                if args:
                    assert 'BLAME: Test blame' in args[0]  # title

    def test_generate_issue_body(self):
        """Test generating issue body for TODO items."""
        with patch('astodojo.github.GitHubClient'), \
             patch('astodojo.github.GitHubCache'):
            integration = GitHubIntegration('token', 'owner/repo')

            todo = TodoItem(
                'test.py',
                42,
                TagType.BLAME,
                'Test blame content',
                parent_function='test_func',
                parent_class='TestClass'
            )

            body = integration._generate_issue_body(todo)

            assert 'BLAME: Human Review Required' in body
            assert 'test.py' in body
            assert '42' in body
            assert 'TestClass' in body
            assert 'test_func' in body
            assert 'Test blame content' in body

    def test_find_new_todos(self):
        """Test finding new TODOs compared to cache."""
        with patch('astodojo.github.GitHubClient'), \
             patch('astodojo.github.GitHubCache'):
            integration = GitHubIntegration('token', 'owner/repo')

            current_todos = [
                TodoItem('test.py', 1, TagType.TODO, 'New todo')
            ]
            cached_todos = []  # No cached todos

            new_todos = integration._find_new_todos(current_todos, cached_todos)

            assert len(new_todos) == 1
            assert new_todos[0].content == 'New todo'
