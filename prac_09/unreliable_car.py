"""UnreliableCar Class"""

import random
from prac_09.car import Car

LOW_RANDOM_NUMBER = 0
HIGH_RANDOM_NUMBER = 100


class UnreliableCar(Car):
    """An unreliability version of car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car when random number is less than car's reliability. """
        random_number = random.uniform(LOW_RANDOM_NUMBER, HIGH_RANDOM_NUMBER)

        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven