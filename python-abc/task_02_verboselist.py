#!/usr/bin/env python3
"""
Module defining VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        count = len(x)
        super().extend(x)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
