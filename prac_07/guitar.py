"""Guitar class"""
YEAR = 2023


class Guitar:
    """Represent a Guitar class object."""

    def __init__(self, name='', year=0, cost=0):
        """Initialise the Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string of guitar details."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare and return guitar less than guitar to be able to be sorted, by year. """
        return self.year < other.year

    def get_age(self):
        """Get age from current year minus the year of the guitar."""
        return YEAR - self.year

    def is_vintage(self):
        """Return whether the guitar is vintage based on if it is older than 50 years."""
        return self.get_age() >= 50
