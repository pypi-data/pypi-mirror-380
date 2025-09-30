"""Configuration management for ASTODOJO."""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class ASTODOJOConfig:
    """Configuration for ASTODOJO scanner."""

    # Default exclude patterns
    exclude_patterns: List[str] = None

    # Output format: 'tree', 'json', 'report'
    output_format: str = 'tree'

    # Color scheme preferences
    colors: Dict[str, str] = None

    # GitHub integration settings
    github_token: Optional[str] = None
    github_repo: Optional[str] = None

    # Cache settings
    cache_enabled: bool = True
    cache_file: str = '.astodojo/cache.json'

    def __post_init__(self):
        if self.exclude_patterns is None:
            self.exclude_patterns = [
                '**/__pycache__/**',
                '**/*.pyc',
                '**/.git/**',
                '**/.pytest_cache/**',
                '**/.tox/**',
                '**/.venv/**',
                '**/venv/**',
                '**/env/**',
                '**/node_modules/**',
                '**/dist/**',
                '**/build/**',
                '**/.DS_Store',
                '**/*.egg-info/**',
            ]

        if self.colors is None:
            self.colors = {
                'TODO': 'blue',
                'BLAME': 'red',
                'DEV-CRUFT': 'yellow',
                'PAY-ATTENTION': 'purple',
                'BUG': 'red'
            }

    @classmethod
    def from_file(cls, config_path: str = '.astodojorc') -> 'ASTODOJOConfig':
        """Load configuration from a YAML file.

        Args:
            config_path: Path to the configuration file

        Returns:
            ASTODOJOConfig instance
        """
        config = cls()

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f) or {}

                # Update config with file values
                for key, value in data.items():
                    if hasattr(config, key):
                        setattr(config, key, value)

            except (yaml.YAMLError, IOError) as e:
                print(f"Warning: Could not load config from {config_path}: {e}")

        # Override with environment variables
        config.github_token = os.getenv('GITHUB_TOKEN', config.github_token)
        config.github_repo = os.getenv('GITHUB_REPOSITORY', config.github_repo)

        return config

    def save_to_file(self, config_path: str = '.astodojorc') -> None:
        """Save configuration to a YAML file.

        Args:
            config_path: Path to save the configuration file
        """
        # Create directory if it doesn't exist
        Path(config_path).parent.mkdir(parents=True, exist_ok=True)

        # Convert to dict, excluding None values for cleaner YAML
        data = {}
        for key, value in self.__dict__.items():
            if value is not None:
                data[key] = value

        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)

        except IOError as e:
            print(f"Error: Could not save config to {config_path}: {e}")

    def merge_from_args(self, args: Any) -> None:
        """Merge configuration from command-line arguments.

        Args:
            args: Parsed command-line arguments
        """
        # Override config with CLI args
        if hasattr(args, 'exclude') and args.exclude:
            self.exclude_patterns = args.exclude

        if hasattr(args, 'format') and args.format:
            self.output_format = args.format

        if hasattr(args, 'github_token') and args.github_token:
            self.github_token = args.github_token

        if hasattr(args, 'github_repo') and args.github_repo:
            self.github_repo = args.github_repo


def init_config(directory: str = '.') -> None:
    """Initialize a new .astodojorc file in the given directory.

    Args:
        directory: Directory to create the config file in
    """
    config_path = os.path.join(directory, '.astodojorc')
    config = ASTODOJOConfig()

    if os.path.exists(config_path):
        print(f"Config file already exists at {config_path}")
        return

    config.save_to_file(config_path)
    print(f"Created config file at {config_path}")
    print("\nYou can customize the following settings:")
    print("- exclude_patterns: List of glob patterns to ignore")
    print("- output_format: Default output format ('tree', 'json', 'report')")
    print("- colors: Custom colors for different tag types")
    print("- github_token: GitHub token for integration (also set GITHUB_TOKEN env var)")
    print("- github_repo: GitHub repository in 'owner/repo' format")
    print("\nExample customization:")
    print("exclude_patterns:")
    print("  - '**/*.test.py'")
    print("  - '**/legacy/**'")
    print("colors:")
    print("  TODO: 'cyan'")
    print("  BUG: 'red'")


def load_config(directory: str = '.') -> ASTODOJOConfig:
    """Load configuration for the given directory.

    Args:
        directory: Directory to load config from

    Returns:
        ASTODOJOConfig instance
    """
    config_path = os.path.join(directory, '.astodojorc')
    return ASTODOJOConfig.from_file(config_path)
