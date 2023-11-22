"""Taxi simulator program using taxi classes. """

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    selection = input(">>> ")
    while selection.lower() != 'q':
        if selection.lower() == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${current_bill:.2f}")  # This is just a placeholder for me for later.
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                current_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
                current_bill += current_fare
                print(f"Bill to date: ${current_bill:.2f}")

        elif selection.lower() == 'c':
            view_taxis(taxis)
            try:
                choice = int(input("Choose taxi: "))
            except ValueError:
                print("Invalid choice")
                print(f"Bill to date: ${current_bill:.2f}")
            try:
                current_taxi = taxis[choice]
            except IndexError:
                print("Invalid taxi choice")

            print(f"Bill to date: ${current_bill:.2f}")

        else:
            print("Invalid option")
            print(f"Bill to date: ${current_bill:.2f}")
        print(MENU)
        selection = input(">>> ")
    print(f"Total trip cost: ${current_bill:.2f}")
    print("Taxis are now:")
    view_taxis(taxis)


def view_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
