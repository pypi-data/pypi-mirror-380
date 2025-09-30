"""
Edge cases and boundary conditions for ASTODOJO testing.
"""

# Empty file with no TODOs

# File with TODOs at different indentation levels
def function_with_indented_todos():
    # TODO: Normal indentation
    if True:
        # TODO: Nested indentation
        for i in range(10):
            # TODO: Deeply nested
            if i % 2 == 0:
                # TODO: Very deep nesting
                pass

# Case variations
def case_variations():
    # todo: lowercase
    # Todo: mixed case
    # TODO: uppercase
    # BLAME: normal blame
    # blame: lowercase blame
    # Blame: mixed case blame
    pass

# Tags with different separators
def different_separators():
    # TODO: colon separator
    # TODO- dash separator
    # TODO= equals separator
    # BLAME: normal
    # BLAME- dash
    # BLAME= equals
    pass

# Tags with no content
def empty_content():
    # TODO:
    # BLAME
    # DEV-CRUFT:
    # PAY-ATTENTION
    # BUG:
    pass

# Tags with special characters
def special_characters():
    # TODO: Special chars: @#$%^&*()[]{}
    # BLAME: Unicode: 你好世界 🌍
    # BUG: Emojis: 🚀💥🔥
    pass

# Tags in different comment styles (though Python only supports #)
def comment_styles():
    # TODO: Standard comment
    # This is not a TODO
    # TODO: Another TODO
    pass

# Tags spanning multiple lines
def multiline_tags():
    # TODO: This is a very long TODO comment that might span
    # multiple lines in the source code and should still be
    # captured as a single TODO item

    # BLAME: Another multiline
    # comment that continues
    # on several lines
    pass

# Tags in various string contexts (should NOT be detected)
def string_contexts():
    todo_string = "This is a TODO in a string"
    blame_string = 'This is a BLAME in a string'
    code = """
    # This is code inside a string
    # TODO: This should NOT be detected
    """

    # This should be detected
    # TODO: But this should
    pass

# Class with complex inheritance
class ComplexClass(BaseException, object):
    """
    Class docstring.

    TODO: Class-level documentation
    BLAME: Inheritance pattern review needed
    """

    def method(self):
        # TODO: Method implementation
        pass

# Tags near function boundaries
def function_boundary_test():
    # TODO: Before function
    pass

    # TODO: Between functions
    pass

def another_function():
    # TODO: Inside second function
    pass
# TODO: After last function
