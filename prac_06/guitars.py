"""
Program that uses the guitar class object
Estimated completion time: 40-50 minutes (start 6:10)
Actual completion time:
"""
from prac_06.guitar import Guitar

guitars = []

guitar_name = input("Guitar Name: ")
year = input()
cost = input()
guitar = Guitar(guitar_name, year, cost)
guitars.append(guitar)
