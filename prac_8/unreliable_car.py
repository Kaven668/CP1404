import random
from car import Car


class UnreliableCar(Car):
    """Initialise an UnreliableCar"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a car base on reliability"""
        random_num = random.randint(1, 100)
        if random_num > self.reliability:
            distance = 0
        return super().drive(distance)
