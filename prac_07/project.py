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

# Be able to sort/compare projects based on date/priority order - using '<'
#
