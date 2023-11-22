"""
Band class
- Initially Worked with / collaboration with Sachh Moka during Tuesday's Lecture (14/11)
- The Rest / Further Commits by Me (Eric Wagner)
"""

from musician import Musician


class Band:
    """Initialise the band class"""

    def __init__(self, name=""):
        """Initialise a Band object. """
        self.name = name
        self.musicians = []

    def __str__(self):
        """Print a string list of musicians. """
        return f"{self.name} ({self.musicians})"

        # for musician in self.musicians:
        #     return f"{musician} ({self.musicians})"

    def add(self, musician):
        """Add musicians to band. """
        self.musicians.append(musician)

    def play(self):
        """Play the band. """
        for musician in self.musicians:
            print(f"{musician} is playing {self.musicians[1]}")

        # if not self.musicians:
        #     return f"{self.musicians[0]} needs an instrument!"
        # return f"{self.musicians[0]} is playing: {self.musicians[1]}"
