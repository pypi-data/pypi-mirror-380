"""Tests for the configuration system."""

import tempfile
import os
from pathlib import Path

import pytest

from astodojo.config import ASTODOJOConfig, init_config, load_config


class TestASTODOJOConfig:
    """Test the configuration dataclass."""

    def test_default_config(self):
        """Test default configuration values."""
        config = ASTODOJOConfig()

        assert config.output_format == 'tree'
        assert config.cache_enabled is True
        assert config.cache_file == '.astodojo/cache.json'
        assert config.github_token is None
        assert config.github_repo is None

        # Check default exclude patterns
        assert '**/__pycache__/**' in config.exclude_patterns
        assert '**/*.pyc' in config.exclude_patterns
        assert '**/.git/**' in config.exclude_patterns

        # Check default colors
        assert config.colors['TODO'] == 'blue'
        assert config.colors['BLAME'] == 'red'
        assert config.colors['BUG'] == 'red'

    def test_config_from_file(self):
        """Test loading configuration from YAML file."""
        import os
        # Clear environment variables that might interfere
        old_token = os.environ.get('GITHUB_TOKEN')
        old_repo = os.environ.get('GITHUB_REPOSITORY')
        try:
            os.environ.pop('GITHUB_TOKEN', None)
            os.environ.pop('GITHUB_REPOSITORY', None)

            config_yaml = """
output_format: json
exclude_patterns:
  - "**/*.test.py"
  - "**/legacy/**"
colors:
  TODO: cyan
  BUG: magenta
github_token: test_token
github_repo: test/repo
"""

            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
                f.write(config_yaml)
                config_file = f.name

            try:
                config = ASTODOJOConfig.from_file(config_file)

                assert config.output_format == 'json'
                assert '**/*.test.py' in config.exclude_patterns
                assert '**/legacy/**' in config.exclude_patterns
                assert config.colors['TODO'] == 'cyan'
                assert config.colors['BUG'] == 'magenta'
                assert config.github_token == 'test_token'
                assert config.github_repo == 'test/repo'

            finally:
                os.unlink(config_file)
        finally:
            if old_token:
                os.environ['GITHUB_TOKEN'] = old_token
            if old_repo:
                os.environ['GITHUB_REPOSITORY'] = old_repo

    def test_config_from_missing_file(self):
        """Test loading config when file doesn't exist."""
        import os
        # Clear environment variables that might interfere
        old_token = os.environ.get('GITHUB_TOKEN')
        old_repo = os.environ.get('GITHUB_REPOSITORY')
        try:
            os.environ.pop('GITHUB_TOKEN', None)
            os.environ.pop('GITHUB_REPOSITORY', None)
            config = ASTODOJOConfig.from_file('nonexistent.yaml')

            # Should return default config
            assert config.output_format == 'tree'
            assert config.github_token is None
        finally:
            if old_token:
                os.environ['GITHUB_TOKEN'] = old_token
            if old_repo:
                os.environ['GITHUB_REPOSITORY'] = old_repo

    def test_config_save_to_file(self):
        """Test saving configuration to YAML file."""
        config = ASTODOJOConfig()
        config.output_format = 'json'
        config.github_token = 'test_token'

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            config_file = f.name

        try:
            config.save_to_file(config_file)

            # Read back and verify
            with open(config_file, 'r') as f:
                content = f.read()

            assert 'output_format: json' in content
            assert 'github_token: test_token' in content

        finally:
            if os.path.exists(config_file):
                os.unlink(config_file)

    def test_merge_from_args(self):
        """Test merging configuration from command-line args."""
        config = ASTODOJOConfig()

        # Mock args object
        class MockArgs:
            def __init__(self):
                self.exclude = ['custom_exclude.py']
                self.format = 'report'
                self.github_token = 'cli_token'
                self.github_repo = 'cli/repo'

        args = MockArgs()
        config.merge_from_args(args)

        assert config.exclude_patterns == ['custom_exclude.py']
        assert config.output_format == 'report'
        assert config.github_token == 'cli_token'
        assert config.github_repo == 'cli/repo'


class TestConfigFunctions:
    """Test the configuration utility functions."""

    def test_init_config(self):
        """Test initializing a new config file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = os.path.join(temp_dir, '.astodojorc')

            # Should create the config file
            init_config(temp_dir)

            assert os.path.exists(config_path)

            # Check content
            with open(config_path, 'r') as f:
                content = f.read()

            assert 'output_format: tree' in content
            assert 'exclude_patterns:' in content

    def test_init_config_already_exists(self):
        """Test init_config when file already exists."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = os.path.join(temp_dir, '.astodojorc')

            # Create existing config
            with open(config_path, 'w') as f:
                f.write('existing: config')

            # Should not overwrite
            init_config(temp_dir)

            with open(config_path, 'r') as f:
                content = f.read()

            assert content == 'existing: config'

    def test_load_config(self):
        """Test loading configuration for a directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = os.path.join(temp_dir, '.astodojorc')

            # Create config file
            with open(config_path, 'w') as f:
                f.write('output_format: json\n')

            config = load_config(temp_dir)

            assert config.output_format == 'json'
