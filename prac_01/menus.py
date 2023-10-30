name = str(input("What is your name? "))
print("(H)ello\n(G)oodbye\n(Q)uit")
selection = str(input(">"))
while selection != 'Q':
    if selection == 'H':
        print("Hello", name)
    elif selection == 'G':
        print("Goodbye", name)
    else:
        print("Invalid selection.")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    selection = str(input(">"))
print("Finished.")
