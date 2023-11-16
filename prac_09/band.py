"""
Band class
- Initially Worked with / collaboration with Sachh Moka during Tuesday's Lecture (14/11)
- The Rest / Further Commits by Me (Eric Wagner)
"""

from musician import Musician


class Band:
    """Initialise the band class"""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        """Print a string list of musicians. """
        # return f"{self.name} is playing: {self.musicians}"
        if not self.musicians:
            return f"{self.name} needs an instrument!"
        return f"{self.name} ({self.musicians[0]})"

    def add(self, musician_name):
        """Add musicians to band. """
        new_musician = Musician(musician_name)
        self.musicians.append(new_musician)

    def play(self):
        """Play the band. """
        for musician in self.musicians:
            musician.play()

