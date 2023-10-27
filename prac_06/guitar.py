"""Guitar class"""
YEAR = 2023


class Guitar:
    """Represent a Guitar class object"""

    def __init__(self, name='', year=0, cost=0):
        """Initialise the Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string of guitar details"""
        return f"{self.name} ({self.year}) : ${self.cost}.2f"

    def get_age(self):
        return YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50
