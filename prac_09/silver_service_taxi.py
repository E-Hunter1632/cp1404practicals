"""SilverService taxi subclass of Taxi class. """
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise the SilverServiceTaxi class object"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip plus the additional flagfall charge."""
        return self.flagfall + super().get_fare()
