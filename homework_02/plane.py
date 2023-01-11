"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, weight):
        result = self.cargo + weight
        have_overload = result > self.max_cargo

        if have_overload:
            raise CargoOverload()

        self.cargo = result

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
