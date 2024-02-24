MINIMUM_LENGTH = 8


def main():
    """Get and print password using functions."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a password from the user that is at least 8 characters long."""
    password = input("Enter a password at least 8 characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password must be at least 8 characters long.")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print a string of asterisks that is the same length as the password."""
    asterisks = "*" * len(password)
    print(asterisks)


main()
