class Vehicle:
    def __init__(self, name, milesage):
        self.name = name
        self.milesage = milesage


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f"Seatng capacity of {self.name} is {capacity} passengers"


class SchoolBus(Bus):
    def bus_name(self, school):
        return f"{self.name} is assigned to {school} school"
    

school_bus = SchoolBus("School volovo", 12)
print(school_bus.seating_capacity(50))
print(school_bus.bus_name("ABC International"))
print(SchoolBus.__mro__)
