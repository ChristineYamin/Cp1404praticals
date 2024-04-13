
import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Unreliable Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive (self,distance):
        """Drive the car if the reliability check passes"""
        if random.randint(0,100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
