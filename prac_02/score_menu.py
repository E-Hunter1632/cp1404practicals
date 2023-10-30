"""Score calculator with menu"""

MENU = """Enter Selection: 
(G)et a valid score, (0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    selection = str(input("> "))
    while selection != 'Q':
        if selection == 'G':
            score = float(input("Enter score: "))
            print(score)
        elif selection == 'P':
            determine_result(score)
            print(determine_result(score))
        elif selection == 'S':
            print_stars(int(score))
        else:
            print("Invalid Selection.")
        print(MENU)
        selection = str(input("> "))
    print("Farewell.")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(length):
    """Convert score to stars"""
    print('*' * length)


main()

