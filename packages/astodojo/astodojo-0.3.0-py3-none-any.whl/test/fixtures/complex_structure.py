"""
Complex test file with nested structures, docstrings, and edge cases.
"""

import os
import sys


def outer_function():
    """
    This function does something important.

    TODO: Add comprehensive error handling
    BLAME: Security review required for input validation
    """
    # BUG: Race condition in file operations
    def inner_function():
        # DEV-CRUFT: Remove temporary logging
        return "nested"

    return inner_function()


class BaseClass:
    """Base class for testing."""

    def __init__(self):
        # PAY-ATTENTION: Thread safety considerations
        pass

    def method_one(self):
        """
        Method with docstring.

        TODO: Implement caching mechanism
        """
        # BLAME: Performance bottleneck here
        return True


class DerivedClass(BaseClass):
    """Derived class with more complexity."""

    def __init__(self):
        super().__init__()
        # DEV-CRUFT: Remove after migration
        self.temp_attr = None

    def complex_method(self, param):
        """
        Complex method with multiple issues.

        BUG: Memory leak in loop
        PAY-ATTENTION: Database connection pooling
        """
        if param is None:
            # TODO: Handle None case gracefully
            return None

        # BLAME: SQL injection vulnerability
        query = f"SELECT * FROM table WHERE id = {param}"
        return query

    class NestedClass:
        """Nested class inside method."""

        def nested_method(self):
            # DEV-CRUFT: Legacy compatibility code
            # BUG: Incorrect calculation
            return 42


# Module-level TODOs
# TODO: Add module documentation
# BLAME: Review entire module for security issues

# Multi-line TODO
# TODO: This is a multi-line comment
# that spans several lines and should
# still be captured properly

# TODO: Another task
