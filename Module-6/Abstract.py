from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fule_capacity(self):
        pass

    @ abstractmethod
    def seating_capacity(self):
        pass


class Bus(Vehicle):
    def fule_capacity(self):
        return "The fule capacity is 200 liters"
    

    def seating_capacity(self):
        return "The seating capacity is 50 passengers"
    
school_bus = Bus()
print(school_bus.fule_capacity())
print(school_bus.seating_capacity())

