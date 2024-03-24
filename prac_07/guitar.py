from datetime import datetime
CURRENT_YEAR = datetime.now().year
CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Details of a guitar in Guitar class"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representing of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage or not."""
        return self.get_age() >= VINTAGE_AGE

