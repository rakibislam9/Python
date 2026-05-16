class Vehicle:
    def vehicle_info(self):
        return "This is a vehicle"
    

class Bus(Vehicle):
    def vehicle_info(self):
        return "this is a school bus with 50 seats"
    
class Car(Vehicle):
    def vehicle_info(self):
        return "This is a sports car with 2 seats"
    
vehicle = [Bus(), Car()]


for V in vehicle:
    print(V.vehicle_info())
    