from prac_06.guitar import Guitar

CURRENT_YEAR = 2024

def run_tests():
    """Run tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {CURRENT_YEAR - year}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {CURRENT_YEAR - 2012}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

if __name__ == '__main__':
    run_tests()

