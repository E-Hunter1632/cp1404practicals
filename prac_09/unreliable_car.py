"""Unreliable car subclass. """
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        """Initialise the UnreliableCar class object"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car as normal but with added random reliability factor. """
        number = randint(0, 100)
        if number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
