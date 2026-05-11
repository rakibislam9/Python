from distro import name


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    

class Bus(Vehicle):
    pass



school_bus = Bus('School bus', 10, 50)

print(f'Name: {school_bus.name}, Fare: {school_bus.fare()}')