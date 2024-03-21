from dataclasses import dataclass, field

from curs_python.sesiunea13.vehicule import VEHICLES


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Vehicle:
    type: str
    capacity: int
    power: int
    owner: Person

    def ride(self):
        print(f'{self.owner} rides a {self.type}')


@dataclass
class UtilityVehicle(Vehicle):
    type: str = field(init=False, default='utility vehicle')
    load_capacity: int


@dataclass
class Car(Vehicle):
    type: str = field(init=False, default='car')
    fuel_type: str


@dataclass
class Bike(Vehicle):
    type: str = field(init=False, default='bike')


@dataclass
class Bus(Car):
    passengers_type: str


@dataclass
class MotorBike(Bike):
    engine_capacity: int


def find_vehicles_with_capacity_than_2(vehicles):
    result = []
    for x in vehicles:
        if x.capacity > 2:
            result.append(x)
    return result

print(find_vehicles_with_capacity_than_2(VEHICLES))

# 2.
def find_bike_owners(vehicules):
    result = set()
    for x in vehicules:
        if isinstance(x, Bike):
            result.add(x.owner.name)
    return list(result)