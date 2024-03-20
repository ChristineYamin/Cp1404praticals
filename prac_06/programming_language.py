"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self,name="",typing="",reflection="",year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Initialise a programming instance."""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, first appeared in {self.year}"

    def is_dynamic(self):

        if self.typing == "Dynamic":
            return True
        else:
            return False



