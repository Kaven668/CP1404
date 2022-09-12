from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Create a class called SilverServiceTaxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string to show SilverServiceTaxi"""
        return "{} plus ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Calculate the fare"""
        return self.flagfall + super().get_fare()
