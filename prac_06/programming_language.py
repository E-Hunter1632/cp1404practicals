class ProgrammingLanguage:
    """New class for categorising programming languages."""

    def __init__(self, name="", typing="", reflection=False, year=""):
        """Initialise ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return true if self.typing is dynamic"""
        # if self.typing == "Dynamic": - NOT NEEDED, EXPERIMENTATION ONLY
        #     self.typing = "Dynamic"
        return self.typing == "Dynamic"
