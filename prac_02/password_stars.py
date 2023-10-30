"""Password to stars"""


MIN_LENGTH = 8


def main():
    """Get user password and convert to stars. """
    password = get_password(MIN_LENGTH)
    print_stars(password)


def get_password(min_length):
    """Get user password and validate minimum length. """
    password = input("Enter 8-character password: ")
    while len(password) < min_length:
        print("Password length valid.")
        password = input("Enter 8-character password: ")
    return password


def print_stars(length):
    """Convert password to stars"""
    print('*' * len(length))


main()
