"""Tests for the core ASTODOJO scanner."""

import tempfile
import os
from pathlib import Path

import pytest

from astodojo.core import ASTODOJO, TodoItem, TagType


class TestASTODOJO:
    """Test the main ASTODOJO scanner."""

    def test_init_default_excludes(self):
        """Test that scanner initializes with default exclude patterns."""
        scanner = ASTODOJO()
        assert scanner.exclude_patterns == []

    def test_init_custom_excludes(self):
        """Test that scanner accepts custom exclude patterns."""
        excludes = ["*.pyc", "**/__pycache__/**"]
        scanner = ASTODOJO(exclude_patterns=excludes)
        assert scanner.exclude_patterns == excludes

    def test_should_exclude(self):
        """Test the exclude pattern matching."""
        scanner = ASTODOJO(exclude_patterns=["*.pyc", "**/__pycache__/**"])

        assert scanner.should_exclude("test.pyc")
        assert scanner.should_exclude("__pycache__/module.pyc")
        assert not scanner.should_exclude("test.py")

    def test_scan_file_with_todo_comments(self):
        """Test scanning a file with TODO comments."""
        code = '''
def function_one():
    # TODO: Implement this function
    pass

class MyClass:
    def method(self):
        # BLAME: This logic is wrong and needs review
        return None

# DEV-CRUFT: Remove this temporary code
temp_var = 42

# PAY-ATTENTION: Critical security check here
if user_input:
    process(user_input)

# BUG: This will cause a division by zero
result = 1 / 0
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            scanner = ASTODOJO()
            todos = scanner.scan_file(temp_file)

            assert len(todos) == 5

            # Check TODO
            todo_items = {todo.tag: todo for todo in todos}
            assert TagType.TODO in todo_items
            assert "Implement this function" in todo_items[TagType.TODO].content

            # Check BLAME
            assert TagType.BLAME in todo_items
            assert "This logic is wrong" in todo_items[TagType.BLAME].content

            # Check DEV-CRUFT
            assert TagType.DEV_CRUFT in todo_items
            assert "Remove this temporary code" in todo_items[TagType.DEV_CRUFT].content

            # Check PAY-ATTENTION
            assert TagType.PAY_ATTENTION in todo_items
            assert "Critical security check" in todo_items[TagType.PAY_ATTENTION].content

            # Check BUG
            assert TagType.BUG in todo_items
            assert "division by zero" in todo_items[TagType.BUG].content

        finally:
            os.unlink(temp_file)

    def test_scan_file_with_docstring_todos(self):
        """Test scanning docstrings for TODO items."""
        code = '''
def function_with_docstring():
    """
    This function does something.

    TODO: Add proper error handling
    BLAME: Review this implementation
    """
    pass
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            scanner = ASTODOJO()
            todos = scanner.scan_file(temp_file)

            assert len(todos) == 2

            todo_items = {todo.tag: todo for todo in todos}
            assert TagType.TODO in todo_items
            assert "Add proper error handling" in todo_items[TagType.TODO].content

            assert TagType.BLAME in todo_items
            assert "Review this implementation" in todo_items[TagType.BLAME].content

        finally:
            os.unlink(temp_file)

    def test_scan_file_context_tracking(self):
        """Test that scanner tracks function and class context."""
        code = '''
class MyClass:
    def my_method(self):
        # TODO: Implement this method
        pass

def standalone_function():
    # BLAME: This needs review
    pass
'''

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name

        try:
            scanner = ASTODOJO()
            todos = scanner.scan_file(temp_file)

            assert len(todos) == 2

            # Find todos by content
            method_todo = next(t for t in todos if "Implement this method" in t.content)
            function_todo = next(t for t in todos if "This needs review" in t.content)

            assert method_todo.parent_class == "MyClass"
            assert method_todo.parent_function == "my_method"

            assert function_todo.parent_class is None
            assert function_todo.parent_function == "standalone_function"

        finally:
            os.unlink(temp_file)

    def test_scan_directory(self):
        """Test scanning a directory of Python files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files
            file1_content = '''
def func1():
    # TODO: Task in file1
    pass
'''
            file2_content = '''
def func2():
    # BLAME: Issue in file2
    pass
'''

            file1_path = Path(temp_dir) / "file1.py"
            file2_path = Path(temp_dir) / "file2.py"
            non_py_path = Path(temp_dir) / "not_python.txt"

            file1_path.write_text(file1_content)
            file2_path.write_text(file2_content)
            non_py_path.write_text("not python")

            scanner = ASTODOJO()
            todos = scanner.scan_directory(temp_dir)

            assert len(todos) == 2

            # Check that both files were scanned
            file_paths = {todo.file_path for todo in todos}
            assert any("file1.py" in path for path in file_paths)
            assert any("file2.py" in path for path in file_paths)

    def test_scan_directory_with_excludes(self):
        """Test scanning directory with exclude patterns."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files
            included_content = '''
def func():
    # TODO: This should be found
    pass
'''

            excluded_content = '''
def func():
    # BLAME: This should be excluded
    pass
'''

            included_path = Path(temp_dir) / "included.py"
            excluded_path = Path(temp_dir) / "excluded.py"

            included_path.write_text(included_content)
            excluded_path.write_text(excluded_content)

            # Exclude the excluded.py file
            scanner = ASTODOJO(exclude_patterns=["excluded.py"])
            todos = scanner.scan_directory(temp_dir)

            assert len(todos) == 1
            assert "This should be found" in todos[0].content

    def test_format_json_output(self):
        """Test JSON output formatting."""
        todos = [
            TodoItem(
                file_path="test.py",
                line_number=10,
                tag=TagType.TODO,
                content="Test todo",
                parent_function="test_func"
            )
        ]

        scanner = ASTODOJO()
        json_output = scanner.format_json_output(todos)

        import json
        parsed = json.loads(json_output)

        assert len(parsed) == 1
        assert parsed[0]["file_path"] == "test.py"
        assert parsed[0]["line_number"] == 10
        assert parsed[0]["tag"] == "TODO"
        assert parsed[0]["content"] == "Test todo"
        assert parsed[0]["parent_function"] == "test_func"

    def test_format_report_output_no_todos(self):
        """Test report output when no TODOs found."""
        scanner = ASTODOJO()
        report = scanner.format_report_output([])

        assert "No TODO items found" in report
        assert "clean" in report

    def test_format_report_output_with_todos(self):
        """Test report output with TODOs."""
        todos = [
            TodoItem("file1.py", 1, TagType.TODO, "Task 1"),
            TodoItem("file1.py", 2, TagType.BLAME, "Issue 1"),
            TodoItem("file2.py", 1, TagType.TODO, "Task 2"),
        ]

        scanner = ASTODOJO()
        report = scanner.format_report_output(todos)

        assert "Total TODO items: 3" in report
        assert "Files with TODOs: 2" in report
        assert "TODO: 2" in report
        assert "BLAME: 1" in report


class TestTodoItem:
    """Test the TodoItem dataclass."""

    def test_to_dict(self):
        """Test TodoItem to_dict conversion."""
        todo = TodoItem(
            file_path="test.py",
            line_number=42,
            tag=TagType.TODO,
            content="Test content",
            parent_function="test_func",
            parent_class="TestClass"
        )

        data = todo.to_dict()

        assert data["file_path"] == "test.py"
        assert data["line_number"] == 42
        assert data["tag"] == "TODO"
        assert data["content"] == "Test content"
        assert data["parent_function"] == "test_func"
        assert data["parent_class"] == "TestClass"
