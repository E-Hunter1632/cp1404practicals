"""Unreliable car class testing file. """
from prac_09.unreliable_car import UnreliableCar


my_reliable_car = UnreliableCar("New-car", 100, 75)
my_unreliable_car = UnreliableCar("Old-car", 100, 25)

my_reliable_car.drive(50)
print(my_reliable_car)

my_unreliable_car.drive(50)
print(my_unreliable_car)

