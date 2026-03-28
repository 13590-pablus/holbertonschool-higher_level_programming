#!/usr/bin/env python3
"""
Module demonstrating the use of Mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """Mixin to add swimming functionality."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying functionality."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that gains abilities from SwimMixin and FlyMixin.
    """
    def roar(self):
        print("The dragon roars!")
