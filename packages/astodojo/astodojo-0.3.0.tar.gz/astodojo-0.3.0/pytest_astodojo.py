# pytest_astodojo.py
import pytest
import json
import os
from pathlib import Path
from astodojo.core import ASTODOJO
from astodojo.config import load_config

# Global storage for TODOs by file path
_todos_cache = {}

# Track test outcomes by file
_file_test_outcomes = {}

# Test status cache file
_test_status_cache_file = '.astodojo/test_status_cache.json'


def _save_test_status_cache():
    """Save test status cache to file."""
    try:
        cache_dir = Path(_test_status_cache_file).parent
        cache_dir.mkdir(parents=True, exist_ok=True)

        # Convert test outcomes to a serializable format
        cache_data = {}
        for file_path, outcomes in _file_test_outcomes.items():
            # If any test failed, overall status is "Failed", otherwise "Passed"
            overall_status = "Failed" if any(outcomes) else "Passed"
            cache_data[file_path] = {
                'status': overall_status,
                'test_count': len(outcomes),
                'failures': sum(outcomes)
            }

        with open(_test_status_cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, indent=2)

    except (IOError, OSError) as e:
        print(f"Warning: Could not save test status cache: {e}")


def _load_test_status_cache():
    """Load test status cache from file.

    Returns:
        Dict mapping file paths to test status info
    """
    try:
        if os.path.exists(_test_status_cache_file):
            with open(_test_status_cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    except (IOError, OSError, json.JSONDecodeError) as e:
        print(f"Warning: Could not load test status cache: {e}")

    return {}


@pytest.fixture
def astodojo_todos(request):
    """Fixture that provides TODOs for the current test file.

    Returns:
        List[TodoItem]: TODO items found in the current test file
    """
    file_path = str(request.fspath)
    return _todos_cache.get(file_path, [])

def pytest_runtest_protocol(item, nextitem):
    """Hook to run ASTODOJO scans before/after tests."""
    # Load ASTODOJO config
    config = load_config()
    # Initialize scanner with exclude patterns
    scanner = ASTODOJO(exclude_patterns=config.exclude_patterns)
    # Scan the file being tested
    file_path = str(item.fspath)
    if file_path not in _todos_cache:
        todos = scanner.scan_file(file_path)
        _todos_cache[file_path] = todos
    return None

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Hook to report ASTODOJO TODO-related insights and update docstrings."""
    terminalreporter.write("\n📋 ASTODOJO Test Summary\n")

    # Update docstrings based on test outcomes
    for file_path, test_results in _file_test_outcomes.items():
        if file_path in _todos_cache:
            # If any test in the file failed, mark all docstring TODOs as Failed
            # Otherwise, mark them as Passed
            overall_status = "Failed" if any(test_results) else "Passed"
            todos = _todos_cache[file_path]
            update_docstring_todos(file_path, todos, overall_status)

    # Save test status cache for GitHub integration
    _save_test_status_cache()

    if _todos_cache:
        for file_path, todos in _todos_cache.items():
            if todos:
                terminalreporter.write(f"\nFile: {file_path}")
                for todo in todos:
                    terminalreporter.write(
                        f"  {todo.tag.value}: {todo.content} (line {todo.line_number})"
                    )
    else:
        terminalreporter.write("No TODO items found in test files.")


def pytest_runtest_makereport(item, call):
    """Hook to capture test outcomes for later docstring updates."""
    if call.when == "call":  # After the test function has been executed
        # Track test outcomes by file
        file_path = str(item.fspath)
        if file_path not in _file_test_outcomes:
            _file_test_outcomes[file_path] = []

        # Record if this test failed
        test_failed = call.excinfo is not None
        _file_test_outcomes[file_path].append(test_failed)


def update_docstring_todos(file_path, todos, test_status):
    """Update TODO items in docstrings with test status.

    Args:
        file_path: Path to the Python file
        todos: List of TodoItem objects from ASTODOJO scan
        test_status: "Passed" or "Failed"
    """
    # Only update docstring TODOs (those with parent_function or parent_class set)
    docstring_todos = [todo for todo in todos if todo.parent_function or todo.parent_class]

    if not docstring_todos:
        return  # No docstring TODOs to update

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.splitlines()
        modified = False

        for todo in docstring_todos:
            line_num = todo.line_number - 1  # Convert to 0-based indexing

            if 0 <= line_num < len(lines):
                line = lines[line_num]

                # Only update if "Tested:" is not already present
                if "Tested:" not in line:
                    # Find the TODO content in the line and append test status
                    # We need to be careful to only modify the actual TODO line in the docstring
                    stripped_line = line.strip()
                    if todo.content in stripped_line:
                        # Append the test status to the line
                        lines[line_num] = line.rstrip() + f" [Tested: {test_status}]"
                        modified = True

        if modified:
            # Write back the modified content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n')

    except (IOError, UnicodeDecodeError) as e:
        # Don't fail the test if we can't update the file
        print(f"Warning: Could not update docstring TODOs in {file_path}: {e}")


# Smart Assertions API
def assert_no_critical_todos(todos, tags=None):
    """Assert that no critical TODO tags are present in the given todos.

    Args:
        todos: List of TodoItem objects from ASTODOJO scan
        tags: List of tag types to consider critical (default: ["BLAME", "BUG"])

    Raises:
        AssertionError: If critical TODOs are found
    """
    if tags is None:
        tags = ["BLAME", "BUG"]

    # Convert tag strings to TagType enums for comparison
    from astodojo.core import TagType
    critical_tag_types = []
    for tag in tags:
        enum_name = tag.replace('-', '_')
        if enum_name not in TagType.__members__:
            raise ValueError(f"Unknown tag type: {tag}. Valid types: {list(TagType.__members__.keys())}")
        critical_tag_types.append(TagType[enum_name])

    critical_todos = [todo for todo in todos if todo.tag in critical_tag_types]

    if critical_todos:
        error_msg = f"Critical TODOs found: {[f'{t.tag.value}: {t.content} (line {t.line_number})' for t in critical_todos]}"
        raise AssertionError(error_msg)


def assert_no_todos_of_type(todos, tag_type):
    """Assert that no TODOs of a specific type are present.

    Args:
        todos: List of TodoItem objects from ASTODOJO scan
        tag_type: String tag type to check for (e.g., "TODO", "DEV_CRUFT")

    Raises:
        AssertionError: If TODOs of the specified type are found
    """
    from astodojo.core import TagType

    # Handle enum name mapping (DEV-CRUFT becomes DEV_CRUFT)
    enum_name = tag_type.replace('-', '_')
    if enum_name not in TagType.__members__:
        raise ValueError(f"Unknown tag type: {tag_type}. Valid types: {list(TagType.__members__.keys())}")

    target_tag = TagType[enum_name]

    matching_todos = [todo for todo in todos if todo.tag == target_tag]

    if matching_todos:
        error_msg = f"{tag_type} TODOs found: {[f'{t.content} (line {t.line_number})' for t in matching_todos]}"
        raise AssertionError(error_msg)


def assert_max_todos_per_file(todos, max_count, tag_type=None):
    """Assert that no file exceeds the maximum number of TODOs.

    Args:
        todos: List of TodoItem objects from ASTODOJO scan
        max_count: Maximum number of TODOs allowed per file
        tag_type: Optional tag type to filter by (e.g., "TODO")

    Raises:
        AssertionError: If any file exceeds the maximum
    """
    # Group todos by file
    from collections import defaultdict
    todos_by_file = defaultdict(list)

    for todo in todos:
        if tag_type is None or todo.tag.value == tag_type:
            todos_by_file[todo.file_path].append(todo)

    # Check each file
    violations = []
    for file_path, file_todos in todos_by_file.items():
        if len(file_todos) > max_count:
            tag_desc = f" {tag_type}" if tag_type else ""
            violations.append(f"{file_path}: {len(file_todos)}{tag_desc} TODOs (max: {max_count})")

    if violations:
        error_msg = f"Files exceed maximum TODO limit: {violations}"
        raise AssertionError(error_msg)


def pytest_assertrepr_compare(config, op, left, right):
    """Custom assertion representation for ASTODOJO assertions."""
    if op == "no_critical_todos":
        return [
            "Critical TODOs detected in codebase:",
            left,  # The assertion error message
        ]
    elif op == "no_todos_of_type":
        return [
            f"TODOs of type '{right}' detected:",
            left,  # The assertion error message
        ]
    elif op == "max_todos_per_file":
        return [
            "Files exceed maximum TODO limits:",
            left,  # The assertion error message
        ]
    return None
