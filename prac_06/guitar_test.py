"""
Guitar test file for testing class object
Estimated completion time: 30-40 minutes (start 5:15)
Actual completion time:
"""
from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar1 = Guitar(name, year, cost)
guitar2 = Guitar("Another guitar", 1999, 6499.99)

print(f"{guitar1.name} get_age() - Expected 101. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 24. Got {guitar2.get_age()}")
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
