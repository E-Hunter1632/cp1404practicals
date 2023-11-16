"""Taxi simulator program using taxi classes. """

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    selection = input(">>> ")
    while selection.lower() != 'q':
        if selection.lower() == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print("f Bill to date: {Current_Bill}")  # This is just a placeholder for me for later.
            else:
                drive()

        elif selection.lower() == 'c':
            view_taxis(taxis)
            try:
                choice = int(input("Choose taxi: "))
            except ValueError:
                print("Invalid choice")
                print("f Bill to date: {Current_Bill}")
            try:
                current_taxi = taxis[choice]
            except IndexError:
                print("Invalid taxi choice")
                print("f Bill to date: {Current_Bill}")

        else:
            print("Invalid option")
        print(MENU)
        selection = input(">>> ")
    print("ADD -> QUITTED")


def view_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive():
    print("DRIVE THE TAXI HERE - CALL THE TAXI DRIVE METHOD")


main()
