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

    # def __str__(self):
    #     """Return formatted string of project details. """
    #     return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
    #             f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}")

    def __repr__(self):
        """Return formatted string/list of project details"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}")

    def __gt__(self, other):
        """Compare priority - Sort the highest priority -> the lowest priority"""
        return self.priority > other.priority

    def __lt__(self, other):
        """Compare start dates - Sort the oldest start_date -> the newest start date"""
        return self.start_date < other.start_date

# Be able to sort/compare projects based on date/priority order - using '<'
