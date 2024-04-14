from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the taxi."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate and return the total fare, including flagfall."""
        return super().get_fare() + self.flagfall

