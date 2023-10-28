"""
Program that uses the guitar class object
Estimated completion time: 40-50 minutes
Actual completion time: 55 minutes
"""
from prac_06.guitar import Guitar

guitars = []

print("My guitars! ")
guitar_name = input("Guitar Name: ")
while guitar_name != '':
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(guitar_name, year, cost)
    guitars.append(guitar)
    print(f"{guitar_name} ({year}) : ${cost:,.2f} added. ")
    guitar_name = input("Guitar Name: ")


guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
