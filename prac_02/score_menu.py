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
            from score import determine_result
            determine_result(score)
            print(determine_result(score))
        elif selection == 'S':
            from password_stars import print_stars
            print_stars(score)
        else:
            print("Invalid Selection.")
        print(MENU)
        selection = str(input("> "))
    print("Farewell.")


main()











main()