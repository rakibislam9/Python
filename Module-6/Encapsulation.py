class Vehicle:
    def __init__(self, name, mileage, capacity):
        self. name = name
        self._mileage = mileage
        self.__capacity = capacity


    def get_capacity(self):
        return self.__capacity
    
car = Vehicle("Sedan", 15, 5)

print(car.name)

print(car._mileage)

print(car.get_capacity())