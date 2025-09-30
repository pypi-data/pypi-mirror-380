"""Command-line interface for ASTODOJO."""

import os
import sys
from pathlib import Path
from typing import Optional

import click

from .core import ASTODOJO
from .config import ASTODOJOConfig, init_config, load_config


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """ASTODOJO: Intelligent TODO scanner for Python codebases.

    Scan your Python code for TODO comments and tags, with intelligent
    filtering, context awareness, and GitHub integration.
    """
    pass


@cli.command()
@click.argument('path', default='.')
@click.option('--exclude', '-e', multiple=True,
              help='Exclude patterns (can be used multiple times)')
@click.option('--format', '-f', type=click.Choice(['tree', 'json', 'report']),
              default='tree', help='Output format')
@click.option('--recursive', '-r', is_flag=True, default=True,
              help='Scan directories recursively')
@click.option('--config', '-c', type=click.Path(),
              help='Path to config file (default: .astodojorc)')
@click.option('--github-token', envvar='GITHUB_TOKEN',
              help='GitHub token for integration')
@click.option('--github-repo', envvar='GITHUB_REPOSITORY',
              help='GitHub repository in owner/repo format')
def scan(path: str, exclude: tuple, format: str, recursive: bool,
         config: Optional[str], github_token: Optional[str],
         github_repo: Optional[str]):
    """Scan Python files for TODO items.

    PATH can be a file or directory. Defaults to current directory.
    """
    # Load configuration
    if config:
        astodojo_config = ASTODOJOConfig.from_file(config)
    else:
        astodojo_config = load_config()

    # Override config with CLI options
    if exclude:
        astodojo_config.exclude_patterns = list(exclude)
    if format:
        astodojo_config.output_format = format
    if github_token:
        astodojo_config.github_token = github_token
    if github_repo:
        astodojo_config.github_repo = github_repo

    # Initialize scanner
    scanner = ASTODOJO(exclude_patterns=astodojo_config.exclude_patterns)

    # Determine what to scan
    path_obj = Path(path)
    if path_obj.is_file():
        if not path.endswith('.py'):
            click.echo("Error: Can only scan Python files", err=True)
            sys.exit(1)
        todos = scanner.scan_file(str(path_obj))
    elif path_obj.is_dir():
        todos = scanner.scan_directory(str(path_obj), recursive=recursive)
    else:
        click.echo(f"Error: Path {path} does not exist", err=True)
        sys.exit(1)

    # Output results
    if format == 'json':
        output = scanner.format_json_output(todos)
    elif format == 'report':
        output = scanner.format_report_output(todos)
    else:  # tree
        output = scanner.format_tree_output(todos)

    click.echo(output)


@cli.command()
@click.option('--directory', '-d', default='.',
              help='Directory to initialize config in')
def init(directory: str):
    """Initialize ASTODOJO configuration in the current directory."""
    init_config(directory)


@cli.command()
@click.argument('path', default='.')
@click.option('--config', '-c', type=click.Path(),
              help='Path to config file (default: .astodojorc)')
@click.option('--github-token', envvar='GITHUB_TOKEN',
              help='GitHub token for integration')
@click.option('--github-repo', envvar='GITHUB_REPOSITORY',
              help='GitHub repository in owner/repo format')
def github_report(path: str, config: Optional[str],
                  github_token: Optional[str], github_repo: Optional[str]):
    """Generate a report of TODO items that need GitHub sync.

    This compares local TODOs against GitHub issues and shows what needs
    to be synced.
    """
    # Load configuration
    if config:
        astodojo_config = ASTODOJOConfig.from_file(config)
    else:
        astodojo_config = load_config()

    if github_token:
        astodojo_config.github_token = github_token
    if github_repo:
        astodojo_config.github_repo = github_repo

    if not astodojo_config.github_token or not astodojo_config.github_repo:
        from .github import setup_github_auth
        if not setup_github_auth():
            sys.exit(1)

        # Try to reload config after setup
        astodojo_config = load_config()
        if github_token:
            astodojo_config.github_token = github_token
        if github_repo:
            astodojo_config.github_repo = github_repo

        if not astodojo_config.github_token or not astodojo_config.github_repo:
            click.echo("❌ GitHub token and repository still not configured.", err=True)
            click.echo("Please set GITHUB_TOKEN and GITHUB_REPOSITORY and try again.", err=True)
            sys.exit(1)

    # Scan for current TODOs
    scanner = ASTODOJO(exclude_patterns=astodojo_config.exclude_patterns)
    path_obj = Path(path)
    if path_obj.is_file():
        todos = scanner.scan_file(str(path_obj))
    elif path_obj.is_dir():
        todos = scanner.scan_directory(str(path_obj))
    else:
        click.echo(f"Error: Path {path} does not exist", err=True)
        sys.exit(1)

    # Generate GitHub report
    from .github import GitHubIntegration
    github = GitHubIntegration(
        astodojo_config.github_token,
        astodojo_config.github_repo,
        astodojo_config.cache_file
    )

    try:
        report = github.generate_report(todos)

        # Display report
        click.echo("📊 ASTODOJO GitHub Sync Report")
        click.echo("=" * 50)
        click.echo(f"📋 Current TODOs: {len(todos)}")
        click.echo(f"🆕 New TODOs: {report['new_todos']}")
        click.echo(f"🔄 Changed TODOs: {report['changed_todos']}")
        click.echo(f"🚨 TODOs needing issues: {report['todos_needing_issues']}")
        click.echo(f"📋 Existing GitHub issues: {report['existing_issues']}")
        click.echo()

        if report['sync_recommendations']:
            click.echo("🔧 Recommended Actions:")
            for rec in report['sync_recommendations']:
                todo = rec['todo']
                click.echo(f"  • Create issue for {todo['tag']} in {todo['file_path']}:{todo['line_number']}")
                click.echo(f"    \"{todo['content'][:60]}{'...' if len(todo['content']) > 60 else ''}\"")
                click.echo()
        else:
            click.echo("✅ Everything is in sync!")

    except Exception as e:
        click.echo(f"Error generating GitHub report: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('path', default='.')
@click.option('--tag', '-t', type=click.Choice(['TODO', 'BLAME', 'DEV-CRUFT', 'PAY-ATTENTION', 'BUG']),
              help='Tag type to sync')
@click.option('--count', '-n', type=int, default=1,
              help='Number of items to sync')
@click.option('--config', '-c', type=click.Path(),
              help='Path to config file (default: .astodojorc)')
@click.option('--github-token', envvar='GITHUB_TOKEN',
              help='GitHub token for integration')
@click.option('--github-repo', envvar='GITHUB_REPOSITORY',
              help='GitHub repository in owner/repo format')
def github_sync(path: str, tag: Optional[str], count: int, config: Optional[str],
                github_token: Optional[str], github_repo: Optional[str]):
    """Sync TODO items to GitHub issues.

    This creates GitHub issues for TODO items, with controlled batching
    to avoid rate limits.
    """
    # Load configuration
    if config:
        astodojo_config = ASTODOJOConfig.from_file(config)
    else:
        astodojo_config = load_config()

    if github_token:
        astodojo_config.github_token = github_token
    if github_repo:
        astodojo_config.github_repo = github_repo

    if not astodojo_config.github_token or not astodojo_config.github_repo:
        from .github import setup_github_auth
        if not setup_github_auth():
            sys.exit(1)

        # Try to reload config after setup
        astodojo_config = load_config()
        if github_token:
            astodojo_config.github_token = github_token
        if github_repo:
            astodojo_config.github_repo = github_repo

        if not astodojo_config.github_token or not astodojo_config.github_repo:
            click.echo("❌ GitHub token and repository still not configured.", err=True)
            click.echo("Please set GITHUB_TOKEN and GITHUB_REPOSITORY and try again.", err=True)
            sys.exit(1)

    # Scan for current TODOs
    scanner = ASTODOJO(exclude_patterns=astodojo_config.exclude_patterns)
    path_obj = Path(path)
    if path_obj.is_file():
        todos = scanner.scan_file(str(path_obj))
    elif path_obj.is_dir():
        todos = scanner.scan_directory(str(path_obj))
    else:
        click.echo(f"Error: Path {path} does not exist", err=True)
        sys.exit(1)

    # Convert tag string to TagType
    tag_filter = None
    if tag:
        from .core import TagType
        tag_filter = TagType[tag]

    # Sync to GitHub
    from .github import GitHubIntegration
    github = GitHubIntegration(
        astodojo_config.github_token,
        astodojo_config.github_repo,
        astodojo_config.cache_file
    )

    try:
        results = github.sync_to_github(todos, tag_filter, count)

        if not results:
            click.echo("No items to sync.")
            return

        click.echo(f"🔄 Synced {len(results)} items to GitHub:")
        click.echo()

        for result in results:
            if result['action'] == 'created':
                todo = result['todo']
                click.echo(f"✅ Created issue #{result['issue_number']} for {todo['tag']} in {todo['file_path']}:{todo['line_number']}")
                click.echo(f"   {result['issue_url']}")
            elif result['action'] == 'error':
                todo = result['todo']
                click.echo(f"❌ Failed to sync {todo['tag']} in {todo['file_path']}:{todo['line_number']}")
                click.echo(f"   Error: {result['error']}")
            click.echo()

    except Exception as e:
        click.echo(f"Error syncing to GitHub: {e}", err=True)
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
