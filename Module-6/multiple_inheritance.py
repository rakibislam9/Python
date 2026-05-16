class Engine:
    def engine_info(self):
        return "Theis car has a 2.0l Turbo Engine"


class Body:
    def body_info(self):
        return "This car has a steel body"


class Car(Engine, Body):
    def car_info(self):
        return "This is a sports car"
    
car1 = Car()
print(car1.car_info())
print(car1.engine_info())
print(car1.body_info())