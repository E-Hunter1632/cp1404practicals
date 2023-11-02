"""
Program to read guitars and store them in a list of Guitar objects, displayed using a loop.
Sorting guitars by year, from oldest to newest.
Estimated completion time: 20-40 minutes
Actual completion time: 26 minutes
"""
from prac_07.guitar import Guitar

guitars = []
in_file = open(" guitars.csv", 'r')
# File format is Name,Year,Cost
for line in in_file:
    parts = line.strip().split(',')
    # Year is an int, Cost should be a float.
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
    guitars.sort()
in_file.close()

# Printing the guitar list objects.
for guitar in guitars:
    print(guitar)
