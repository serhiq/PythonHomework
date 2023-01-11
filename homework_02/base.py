from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

VEHICLE_DEFAULT_WEIGHT = 1
VEHICLE_DEFAULT_STARTED = False
VEHICLE_DEFAULT_FUEL = 40
VEHICLE_DEFAULT_FUEL_CONSUMPTION = 10


class Vehicle(ABC):
    def __init__(self, weight=VEHICLE_DEFAULT_WEIGHT, fuel=VEHICLE_DEFAULT_FUEL,
                 fuel_consumption=VEHICLE_DEFAULT_FUEL_CONSUMPTION):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started:
            return

        if self.fuel <= 0:
            raise LowFuelError()

        self.started = True

    def move(self, distance):
        fuel_consumption = self.fuel_consumption * distance

        can_move = fuel_consumption <= self.fuel

        if can_move:
            self.fuel -= fuel_consumption
        else:
            raise NotEnoughFuel()
