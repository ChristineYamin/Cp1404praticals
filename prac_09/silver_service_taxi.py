from taxi import Taxi
class SilverServiceTaxi(Taxi):
    """ SilverServiceTaxi that include fare cost"""
    flagfall=4.5
    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate the fare"""
        return self.flagfall + super().get_fare()

    def __str__(self):
       return super().__str__() + f"plus flagfall of ${self.flagfall:.2f}"





