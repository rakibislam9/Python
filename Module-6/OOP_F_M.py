class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    
    def fare(self):
        return self.capacity * 100
    


bus = Vehicle('school bus', 15, 60)
print(f"Total Bus fare is: {bus.fare()}")


bike = Vehicle('Yamaha', 20, 40)
print(f"Total Bike fare is: {bike.fare()}")