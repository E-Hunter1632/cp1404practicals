"""Project class"""


class Project:
    """Represent a Project class object"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise the Project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return formatted string of project details. """
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}")

# Be able to sort/compare projects based on date/priority order - using '<'
