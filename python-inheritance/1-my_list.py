#!/usr/bin/python3
"""This module defines a custom list class that adds a method to display its elements in sorted order."""

class MyList(list):
    """This class extends the built-in list type with additional behavior for sorted display."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order without modifying the original list."""
        print(sorted(self))
