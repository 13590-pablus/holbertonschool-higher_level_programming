#!/usr/bin/env python3
"""
Module defining CountedIterator class to track iteration count.
"""


class CountedIterator:
    """An iterator that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initializes the iterator and the counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current iteration count."""
        return self.count

    def __next__(self):
        """Overrides the __next__ method to increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
