"""Core ASTODOJO scanner implementation."""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum


class TagType(Enum):
    """Enumeration of supported tag types."""
    TODO = "TODO"
    BLAME = "BLAME"
    DEV_CRUFT = "DEV-CRUFT"
    PAY_ATTENTION = "PAY-ATTENTION"
    BUG = "BUG"


@dataclass
class TodoItem:
    """Represents a single TODO item found in code."""
    file_path: str
    line_number: int
    tag: TagType
    content: str
    context: Optional[str] = None  # Function/method name or class
    parent_function: Optional[str] = None
    parent_class: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            **asdict(self),
            "tag": self.tag.value
        }


class ASTODOJO:
    """Main ASTODOJO scanner class."""

    # Tag patterns to look for in comments and docstrings
    # Only match lines that are actually comments (start with #) or docstrings
    TAG_PATTERNS = {
        TagType.TODO: re.compile(r'^\s*#.*TODO[:\s]*(.+)', re.IGNORECASE | re.MULTILINE),
        TagType.BLAME: re.compile(r'^\s*#.*BLAME[:\s]*(.+)', re.IGNORECASE | re.MULTILINE),
        TagType.DEV_CRUFT: re.compile(r'^\s*#.*DEV-CRUFT[:\s]*(.+)', re.IGNORECASE | re.MULTILINE),
        TagType.PAY_ATTENTION: re.compile(r'^\s*#.*PAY-ATTENTION[:\s]*(.+)', re.IGNORECASE | re.MULTILINE),
        TagType.BUG: re.compile(r'^\s*#.*BUG[:\s]*(.+)', re.IGNORECASE | re.MULTILINE),
    }

    def __init__(self, exclude_patterns: Optional[List[str]] = None):
        """Initialize the scanner.

        Args:
            exclude_patterns: List of glob patterns to exclude from scanning
        """
        self.exclude_patterns = exclude_patterns or []

    def should_exclude(self, path: str) -> bool:
        """Check if a path should be excluded from scanning.

        Args:
            path: File path to check

        Returns:
            True if the path should be excluded
        """
        from pathlib import Path
        path_obj = Path(path)

        for pattern in self.exclude_patterns:
            # Handle ** globstar patterns by checking path components
            if '**' in pattern:
                if self._matches_globstar_pattern(path_obj, pattern):
                    return True
            else:
                # Use pathlib.Path.match for simple patterns
                try:
                    if path_obj.match(pattern):
                        return True
                except ValueError:
                    # Fallback to fnmatch for patterns that Path.match doesn't support
                    from fnmatch import fnmatch
                    if fnmatch(str(path_obj), pattern):
                        return True
        return False

    def _matches_globstar_pattern(self, path_obj: Path, pattern: str) -> bool:
        """Check if path matches a globstar pattern like **/venv/**."""
        path_str = str(path_obj)
        path_parts = path_obj.parts

        # Common patterns we handle:
        # **/dirname/** -> check if dirname is anywhere in path
        # **/dirname/* -> check if dirname is in path
        # dirname/** -> check if path starts with dirname

        if pattern.startswith('**/') and pattern.endswith('/**'):
            # Pattern like **/dirname/**
            dirname = pattern[3:-3]  # Remove **/ and /**
            return dirname in path_parts
        elif pattern.startswith('**/') and pattern.endswith('/*'):
            # Pattern like **/dirname/*
            dirname = pattern[3:-2]  # Remove **/ and /*
            return dirname in path_parts
        elif pattern.endswith('/**'):
            # Pattern like dirname/**
            dirname = pattern[:-3]  # Remove /**
            return path_str.startswith(dirname + '/')
        else:
            # Fallback: check if any significant part matches
            return any(part in path_str for part in ['venv', '__pycache__', '.git', 'node_modules'])

    def scan_file(self, file_path: str) -> List[TodoItem]:
        """Scan a single Python file for TODO items.

        Args:
            file_path: Path to the Python file to scan

        Returns:
            List of TodoItem objects found in the file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()

            tree = ast.parse(source, filename=file_path)
            return self._extract_todos_from_ast(tree, source, file_path)

        except (SyntaxError, UnicodeDecodeError, IOError) as e:
            # Skip files that can't be parsed
            print(f"Warning: Could not parse {file_path}: {e}")
            return []

    def scan_directory(self, directory: str, recursive: bool = True) -> List[TodoItem]:
        """Scan a directory for Python files containing TODO items.

        Args:
            directory: Directory path to scan
            recursive: Whether to scan subdirectories

        Returns:
            List of TodoItem objects found
        """
        todos = []
        path_obj = Path(directory)

        if recursive:
            pattern = "**/*.py"
        else:
            pattern = "*.py"

        for py_file in path_obj.glob(pattern):
            if not self.should_exclude(str(py_file.relative_to(path_obj))):
                todos.extend(self.scan_file(str(py_file)))

        return todos

    def _extract_todos_from_ast(self, tree: ast.AST, source: str,
                               file_path: str) -> List[TodoItem]:
        """Extract TODO items from AST and source code.

        Args:
            tree: Parsed AST
            source: Source code as string
            file_path: Path to the file

        Returns:
            List of TodoItem objects
        """
        todos = []
        lines = source.splitlines()

        # First pass: scan all lines for TODO comments
        for line_num, line in enumerate(lines):
            todo = self._extract_todo_from_line(line, line_num + 1, file_path)
            if todo:
                todos.append(todo)

        # Second pass: use AST to add context information
        class ContextVisitor(ast.NodeVisitor):
            def __init__(self, todos_list):
                self.todos = todos_list

            def visit_FunctionDef(self, node):
                self._add_context_to_todos_in_range(node, 'function', node.name)
                self.generic_visit(node)

            def visit_AsyncFunctionDef(self, node):
                self._add_context_to_todos_in_range(node, 'function', node.name)
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                self._add_context_to_todos_in_range(node, 'class', node.name)
                self.generic_visit(node)

            def _add_context_to_todos_in_range(self, node, context_type, name):
                """Add context to TODOs within the node's line range."""
                start_line = node.lineno
                end_line = getattr(node, 'end_lineno', start_line)

                for todo in self.todos:
                    if start_line <= todo.line_number <= end_line:
                        if context_type == 'function' and not todo.parent_function:
                            todo.parent_function = name
                        elif context_type == 'class' and not todo.parent_class:
                            todo.parent_class = name

        # Also check docstrings
        class DocstringVisitor(ast.NodeVisitor):
            def __init__(self, todos_list, file_path, extract_method):
                self.todos = todos_list
                self.file_path = file_path
                self.context_stack = []
                self._extract_todo_from_line = extract_method

            def visit_FunctionDef(self, node):
                self.context_stack.append(('function', node.name))
                self._check_docstring(node)
                self.generic_visit(node)
                self.context_stack.pop()

            def visit_AsyncFunctionDef(self, node):
                self.context_stack.append(('function', node.name))
                self._check_docstring(node)
                self.generic_visit(node)
                self.context_stack.pop()

            def visit_ClassDef(self, node):
                self.context_stack.append(('class', node.name))
                self._check_docstring(node)
                self.generic_visit(node)
                self.context_stack.pop()

            def visit_Expr(self, node):
                # Docstrings are handled by visit_FunctionDef/visit_ClassDef
                # This visitor is here for future enhancements if needed
                self.generic_visit(node)

            def _check_docstring(self, node):
                """Check if node has a docstring."""
                if hasattr(node, 'body') and node.body:
                    first_stmt = node.body[0]
                    if isinstance(first_stmt, ast.Expr):
                        if isinstance(first_stmt.value, ast.Constant) and isinstance(first_stmt.value.value, str):
                            self._check_docstring_content(first_stmt, first_stmt.value.value)
                        elif isinstance(first_stmt.value, ast.Str):
                            self._check_docstring_content(first_stmt, first_stmt.value.s)

            def _check_docstring_content(self, node, docstring):
                """Check docstring for TODO items."""
                # Split docstring into lines and check each line for TODO items
                lines = docstring.splitlines()
                for line_num, line in enumerate(lines):
                    # Calculate the actual line number in the file
                    actual_line_num = node.lineno + line_num
                    # For docstrings, use a modified regex that doesn't require #
                    todo = self._extract_todo_from_docstring_line(line, actual_line_num, self.file_path)
                    if todo:
                        # Add context from the current stack
                        if self.context_stack:
                            context_type, name = self.context_stack[-1]
                            if context_type == 'function':
                                todo.parent_function = name
                            elif context_type == 'class':
                                todo.parent_class = name
                        self.todos.append(todo)

            def _extract_todo_from_docstring_line(self, line: str, line_num: int, file_path: str) -> Optional[TodoItem]:
                """Extract TODO item from a docstring line (no # required)."""
                # Similar to _extract_todo_from_line but without requiring # prefix
                for tag_type, pattern in ASTODOJO.TAG_PATTERNS.items():
                    # Modify pattern to not require # prefix for docstrings
                    docstring_pattern = re.compile(pattern.pattern.replace(r'^\s*#.*', r'^\s*'), re.IGNORECASE | re.MULTILINE)
                    match = docstring_pattern.search(line)
                    if match:
                        content = match.group(1).strip()
                        return TodoItem(
                            file_path=file_path,
                            line_number=line_num,
                            tag=tag_type,
                            content=content
                        )
                return None

        context_visitor = ContextVisitor(todos)
        context_visitor.visit(tree)

        docstring_visitor = DocstringVisitor(todos, file_path, self._extract_todo_from_line)
        docstring_visitor.visit(tree)

        return todos

    def _extract_todo_from_line(self, line: str, line_num: int, file_path: str) -> Optional[TodoItem]:
        """Extract TODO item from a single line."""
        for tag_type, pattern in ASTODOJO.TAG_PATTERNS.items():
            match = pattern.search(line)
            if match:
                content = match.group(1).strip()
                return TodoItem(
                    file_path=file_path,
                    line_number=line_num,
                    tag=tag_type,
                    content=content
                )
        return None

    def format_tree_output(self, todos: List[TodoItem]) -> str:
        """Format TODO items as a tree structure.

        Args:
            todos: List of TodoItem objects

        Returns:
            Formatted tree string
        """
        from io import StringIO
        from rich.console import Console
        from rich.tree import Tree
        from rich.text import Text

        console = Console(file=StringIO(), width=80)
        tree = Tree("📋 ASTODOJO Scan Results", style="bold blue")

        # Group by file
        files = {}
        for todo in todos:
            if todo.file_path not in files:
                files[todo.file_path] = []
            files[todo.file_path].append(todo)

        # Colors for different tags
        tag_colors = {
            TagType.TODO: "blue",
            TagType.BLAME: "red",
            TagType.DEV_CRUFT: "yellow",
            TagType.PAY_ATTENTION: "purple",
            TagType.BUG: "red"
        }

        for file_path, file_todos in files.items():
            file_node = tree.add(f"📄 {file_path}")

            for todo in file_todos:
                context = ""
                if todo.parent_class:
                    context += f" in class {todo.parent_class}"
                if todo.parent_function:
                    context += f" in function {todo.parent_function}"

                tag_text = Text(f"[{todo.tag.value}]", style=f"bold {tag_colors[todo.tag]}")
                content_text = Text(f" {todo.content}", style="white")
                line_text = Text(f" (line {todo.line_number})", style="dim")

                item_node = file_node.add("")
                item_node.add(tag_text)
                item_node.add(content_text)
                item_node.add(line_text)
                if context:
                    item_node.add(Text(context, style="dim italic"))

        console.print(tree)
        return console.file.getvalue()

    def format_json_output(self, todos: List[TodoItem]) -> str:
        """Format TODO items as JSON.

        Args:
            todos: List of TodoItem objects

        Returns:
            JSON string
        """
        import json
        return json.dumps([todo.to_dict() for todo in todos], indent=2)

    def format_report_output(self, todos: List[TodoItem]) -> str:
        """Format TODO items as a summary report.

        Args:
            todos: List of TodoItem objects

        Returns:
            Report string
        """
        from collections import Counter

        if not todos:
            return "🎉 No TODO items found! Your codebase is clean."

        # Count by tag type
        tag_counts = Counter(todo.tag for todo in todos)

        # Group by file
        file_counts = Counter(todo.file_path for todo in todos)

        report = f"""📊 ASTODOJO Report
{'='*50}

📈 Summary:
- Total TODO items: {len(todos)}
- Files with TODOs: {len(file_counts)}

🏷️  By Tag Type:
"""

        for tag, count in tag_counts.items():
            report += f"  {tag.value}: {count}\n"

        report += "\n📁 Files with most TODOs:\n"
        for file_path, count in file_counts.most_common(10):
            report += f"  {file_path}: {count}\n"

        return report
