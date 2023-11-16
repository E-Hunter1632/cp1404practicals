"""SilverService taxi subclass of Taxi class. """
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class"""

    def __init__(self, name, fuel):
        """Initialise the SilverServiceTaxi class object"""
        super().__init__(name, fuel)
