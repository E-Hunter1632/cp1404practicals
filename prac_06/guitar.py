"""
Guitar class
Estimated completion time: 30-40 minutes
Actual completion time:
"""


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
