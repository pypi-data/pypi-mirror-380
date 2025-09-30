"""GitHub integration for ASTODOJO."""

import json
import os
import time
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional, Any, Set

import requests

from .core import TodoItem, TagType


class GitHubCache:
    """Cache for GitHub operations."""

    def __init__(self, cache_file: str = '.astodojo/cache.json'):
        """Initialize the cache.

        Args:
            cache_file: Path to the cache file
        """
        self.cache_file = Path(cache_file)
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        self.data = self._load_cache()

    def _load_cache(self) -> Dict[str, Any]:
        """Load cache data from file.

        Returns:
            Cache data dictionary
        """
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def save_cache(self) -> None:
        """Save cache data to file."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save cache: {e}")

    def get_cached_todos(self) -> List[Dict[str, Any]]:
        """Get cached TODO items.

        Returns:
            List of cached TODO items
        """
        return self.data.get('todos', [])

    def set_cached_todos(self, todos: List[TodoItem]) -> None:
        """Cache TODO items.

        Args:
            todos: List of TodoItem objects to cache
        """
        self.data['todos'] = [todo.to_dict() for todo in todos]
        self.data['last_scan'] = time.time()
        self.save_cache()

    def get_github_issues(self) -> List[Dict[str, Any]]:
        """Get cached GitHub issues.

        Returns:
            List of cached GitHub issues
        """
        return self.data.get('github_issues', [])

    def set_github_issues(self, issues: List[Dict[str, Any]]) -> None:
        """Cache GitHub issues.

        Args:
            issues: List of GitHub issues to cache
        """
        self.data['github_issues'] = issues
        self.data['last_github_sync'] = time.time()
        self.save_cache()


def setup_github_auth():
    """Set up GitHub authentication by opening browser to token creation page.

    Returns:
        True if user wants to continue without setup, False if they want to exit
    """
    print("🔐 GitHub Authentication Required")
    print("=" * 50)
    print("ASTODOJO needs a GitHub Personal Access Token to access your repositories.")
    print()
    print("Opening GitHub token creation page in your browser...")
    print()

    # Open GitHub token creation page
    token_url = "https://github.com/settings/tokens"
    try:
        webbrowser.open(token_url)
        print(f"✅ Opened: {token_url}")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print(f"Please visit: {token_url}")

    print()
    print("📋 Instructions:")
    print("1. Sign in to GitHub (if not already signed in)")
    print("2. Click 'Generate new token (classic)'")
    print("3. Give it a descriptive name like 'ASTODOJO'")
    print("4. Select the 'repo' scope (full control of private repositories)")
    print("5. Click 'Generate token'")
    print("6. Copy the token (you won't see it again!)")
    print()
    print("🔧 Set up the token in one of these ways:")
    print(f"   export GITHUB_TOKEN=your_token_here")
    print(f"   export GITHUB_REPOSITORY=your_username/your_repo")
    print()
    print("Or add it to your .astodojorc config file:")
    print("   github_token: your_token_here")
    print("   github_repo: your_username/your_repo")
    print()

    try:
        response = input("Press Enter to continue once you've set up the token, or 'q' to quit: ").strip().lower()
        if response == 'q':
            print("❌ GitHub setup cancelled.")
            return False
    except (KeyboardInterrupt, EOFError):
        print("\n❌ GitHub setup cancelled.")
        return False

    return True


class GitHubClient:
    """Client for GitHub API operations."""

    BASE_URL = 'https://api.github.com'

    def __init__(self, token: str, repo: str):
        """Initialize the GitHub client.

        Args:
            token: GitHub API token
            repo: Repository in 'owner/repo' format
        """
        self.token = token
        self.owner, self.repo = repo.split('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'ASTODOJO/0.1.0'
        })

    def get_issues(self, labels: Optional[List[str]] = None,
                   state: str = 'open') -> List[Dict[str, Any]]:
        """Get issues from the repository.

        Args:
            labels: List of labels to filter by
            state: Issue state ('open', 'closed', 'all')

        Returns:
            List of GitHub issues
        """
        url = f'{self.BASE_URL}/repos/{self.owner}/{self.repo}/issues'
        params = {'state': state, 'per_page': 100}

        if labels:
            params['labels'] = ','.join(labels)

        issues = []
        page = 1

        while True:
            params['page'] = page
            response = self.session.get(url, params=params)

            if response.status_code != 200:
                raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

            page_issues = response.json()
            if not page_issues:
                break

            issues.extend(page_issues)
            page += 1

            # Rate limiting
            if len(issues) >= 1000:  # Safety limit
                break

        return issues

    def create_issue(self, title: str, body: str,
                     labels: Optional[List[str]] = None) -> Dict[str, Any]:
        """Create a new issue.

        Args:
            title: Issue title
            body: Issue body
            labels: List of labels to apply

        Returns:
            Created issue data
        """
        url = f'{self.BASE_URL}/repos/{self.owner}/{self.repo}/issues'
        data = {
            'title': title,
            'body': body
        }

        if labels:
            data['labels'] = labels

        response = self.session.post(url, json=data)

        if response.status_code != 201:
            raise Exception(f"Failed to create issue: {response.status_code} - {response.text}")

        return response.json()

    def update_issue(self, issue_number: int, title: Optional[str] = None,
                     body: Optional[str] = None,
                     labels: Optional[List[str]] = None) -> Dict[str, Any]:
        """Update an existing issue.

        Args:
            issue_number: Issue number to update
            title: New title (optional)
            body: New body (optional)
            labels: New labels (optional)

        Returns:
            Updated issue data
        """
        url = f'{self.BASE_URL}/repos/{self.owner}/{self.repo}/issues/{issue_number}'
        data = {}

        if title is not None:
            data['title'] = title
        if body is not None:
            data['body'] = body
        if labels is not None:
            data['labels'] = labels

        response = self.session.patch(url, json=data)

        if response.status_code != 200:
            raise Exception(f"Failed to update issue: {response.status_code} - {response.text}")

        return response.json()


class GitHubIntegration:
    """GitHub integration for ASTODOJO."""

    def __init__(self, token: str, repo: str, cache_file: str = '.astodojo/cache.json'):
        """Initialize GitHub integration.

        Args:
            token: GitHub API token
            repo: Repository in 'owner/repo' format
            cache_file: Path to cache file
        """
        self.client = GitHubClient(token, repo)
        self.cache = GitHubCache(cache_file)

    def generate_report(self, current_todos: List[TodoItem]) -> Dict[str, Any]:
        """Generate a report of what needs to be synced with GitHub.

        Args:
            current_todos: Current TODO items from codebase

        Returns:
            Report dictionary with sync recommendations
        """
        # Get cached data
        cached_todos = self.cache.get_cached_todos()
        github_issues = self.cache.get_github_issues()

        # Convert cached todos back to TodoItem objects
        cached_todo_items = []
        for todo_dict in cached_todos:
            try:
                tag = TagType(todo_dict['tag'])
                cached_todo_items.append(TodoItem(
                    file_path=todo_dict['file_path'],
                    line_number=todo_dict['line_number'],
                    tag=tag,
                    content=todo_dict['content'],
                    context=todo_dict.get('context'),
                    parent_function=todo_dict.get('parent_function'),
                    parent_class=todo_dict.get('parent_class')
                ))
            except (KeyError, ValueError):
                continue

        # Find new/changed todos
        new_todos = self._find_new_todos(current_todos, cached_todo_items)
        changed_todos = self._find_changed_todos(current_todos, cached_todo_items)

        # Find todos that need GitHub issues (BLAME tags should become issues)
        todos_needing_issues = [todo for todo in current_todos
                               if todo.tag == TagType.BLAME]

        # Find existing GitHub issues that correspond to todos
        existing_issue_map = self._map_todos_to_issues(current_todos, github_issues)

        report = {
            'new_todos': len(new_todos),
            'changed_todos': len(changed_todos),
            'todos_needing_issues': len(todos_needing_issues),
            'existing_issues': len(github_issues),
            'sync_recommendations': []
        }

        # Generate recommendations
        for todo in todos_needing_issues:
            key = f"{todo.file_path}:{todo.line_number}:{todo.tag.value}"
            if key not in existing_issue_map:
                report['sync_recommendations'].append({
                    'action': 'create_issue',
                    'todo': todo.to_dict(),
                    'reason': 'BLAME tag requires human review'
                })

        return report

    def sync_to_github(self, todos: List[TodoItem], tag_filter: Optional[TagType] = None,
                       max_count: int = 1) -> List[Dict[str, Any]]:
        """Sync TODO items to GitHub issues.

        Args:
            todos: TODO items to sync
            tag_filter: Only sync todos with this tag type
            max_count: Maximum number of items to sync

        Returns:
            List of sync results
        """
        if tag_filter:
            todos = [todo for todo in todos if todo.tag == tag_filter]

        # Prioritize BUG and BLAME tags for immediate syncing
        critical_todos = [todo for todo in todos if todo.tag in [TagType.BLAME, TagType.BUG]]
        other_todos = [todo for todo in todos if todo.tag not in [TagType.BLAME, TagType.BUG]]

        # Sync critical todos first, then others
        todos_to_sync = (critical_todos + other_todos)[:max_count]

        results = []
        for todo in todos_to_sync:
            try:
                # Use descriptive title based on tag type
                if todo.tag.value == 'BLAME':
                    title_prefix = "BLAME: Security/Architecture Review Required"
                elif todo.tag.value == 'BUG':
                    title_prefix = "BUG: Bug Fix Required"
                else:
                    title_prefix = f"{todo.tag.value}: Code Review Required"

                # Include content but keep it concise
                content_preview = todo.content[:60] + ('...' if len(todo.content) > 60 else '')
                title = f"{title_prefix} - {content_preview}"

                body = self._generate_issue_body(todo)

                # Create appropriate labels based on tag type
                labels = ['astodojo', todo.tag.value.lower()]
                if todo.tag == TagType.BLAME:
                    labels.append('priority-high')
                elif todo.tag == TagType.BUG:
                    labels.append('priority-high')

                issue = self.client.create_issue(
                    title=title,
                    body=body,
                    labels=labels
                )

                results.append({
                    'action': 'created',
                    'todo': todo.to_dict(),
                    'issue_number': issue['number'],
                    'issue_url': issue['html_url']
                })

            except Exception as e:
                results.append({
                    'action': 'error',
                    'todo': todo.to_dict(),
                    'error': str(e)
                })

        return results

    def refresh_cache(self) -> None:
        """Refresh the GitHub cache with current issues."""
        try:
            issues = self.client.get_issues(labels=['astodojo'])
            self.cache.set_github_issues(issues)
        except Exception as e:
            print(f"Warning: Could not refresh GitHub cache: {e}")

    def _find_new_todos(self, current: List[TodoItem],
                        cached: List[TodoItem]) -> List[TodoItem]:
        """Find TODOs that are new compared to cache.

        Args:
            current: Current TODO items
            cached: Cached TODO items

        Returns:
            List of new TODO items
        """
        # Simple implementation: consider todo new if not in cache
        # In a real implementation, you'd do more sophisticated diffing
        cached_keys = {(t.file_path, t.line_number, t.tag.value, t.content)
                      for t in cached}
        return [todo for todo in current
                if (todo.file_path, todo.line_number, todo.tag.value, todo.content)
                not in cached_keys]

    def _find_changed_todos(self, current: List[TodoItem],
                           cached: List[TodoItem]) -> List[TodoItem]:
        """Find TODOs that have changed compared to cache.

        Args:
            current: Current TODO items
            cached: Cached TODO items

        Returns:
            List of changed TODO items
        """
        # For now, just return empty list
        # In a real implementation, you'd compare content changes
        return []

    def _map_todos_to_issues(self, todos: List[TodoItem],
                            issues: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """Map TODO items to existing GitHub issues.

        Args:
            todos: TODO items
            issues: GitHub issues

        Returns:
            Mapping from TODO key to issues
        """
        # Simple mapping based on file path and line number in issue body
        mapping = {}

        for issue in issues:
            body = issue.get('body', '')
            for todo in todos:
                key = f"{todo.file_path}:{todo.line_number}:{todo.tag.value}"
                if f"{todo.file_path}:{todo.line_number}" in body:
                    mapping[key] = issue
                    break

        return mapping

    def _generate_issue_body(self, todo: TodoItem) -> str:
        """Generate GitHub issue body for a TODO item.

        Args:
            todo: TODO item

        Returns:
            Formatted issue body
        """
        context = []
        if todo.parent_class:
            context.append(f"**Class:** {todo.parent_class}")
        if todo.parent_function:
            context.append(f"**Function:** {todo.parent_function}")

        # Check for test status information
        test_status_info = self._get_test_status_info(todo.file_path)

        # Create more informative title and description based on tag type
        if todo.tag.value == 'BLAME':
            title_desc = "Security/Architecture Review Required"
            issue_description = f"""
This code has been flagged with a BLAME tag, indicating it requires human review for one or more reasons:

- **Security implications**: The code may have security vulnerabilities or risks
- **Architectural decisions**: Important design choices that need expert review
- **Complex logic**: Code that may be difficult to maintain or understand
- **Critical functionality**: Core business logic requiring careful validation

**Please review this code carefully before approving or merging.**
"""
        elif todo.tag.value == 'BUG':
            title_desc = "Bug Fix Required"
            issue_description = """
This code contains a confirmed bug that needs to be fixed.

**Please investigate and implement the necessary fix.**
"""
        else:
            title_desc = "Code Review Required"
            issue_description = f"""
This code item requires attention.

**Please review and address this {todo.tag.value.lower()} item.**
"""

        body = f"""## {todo.tag.value}: {title_desc}

**File:** {todo.file_path}
**Line:** {todo.line_number}
{f"**Context:** {', '.join(context)}" if context else ''}

**Content:** {todo.content}

{f"**Test Status:** {test_status_info}" if test_status_info else ''}

**Source:** https://github.com/{self.client.owner}/{self.client.repo}/blob/main/{todo.file_path}#L{todo.line_number}

{issue_description}

---

*This issue was automatically created by ASTODOJO based on code analysis.*
"""

        return body

    def _get_test_status_info(self, file_path: str) -> Optional[str]:
        """Get test status information for a file.

        Args:
            file_path: Path to the file

        Returns:
            Test status string or None if not available
        """
        try:
            # Try to load the test status cache
            cache_file = Path('.astodojo/test_status_cache.json')
            if cache_file.exists():
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)

                if file_path in cache_data:
                    status_info = cache_data[file_path]
                    status = status_info['status']
                    test_count = status_info['test_count']
                    failures = status_info['failures']

                    if status == 'Passed':
                        return f"✅ All {test_count} tests passed"
                    else:
                        return f"❌ {failures} of {test_count} tests failed"

        except (IOError, OSError, json.JSONDecodeError, KeyError):
            pass

        return None
