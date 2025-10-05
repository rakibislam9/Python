from datetime import datetime
from vehical import Car, Byke
class Ridesharing:
    def __init__(self, compani_name):
        self.compani_name = compani_name
        self.drivers = []
        self.riders = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"Compani Name: {self.compani_name} with Rider: {len(self.riders)} and Driver: {len(self.drivers)}"


class Ride:
    def __init__(self, start_location, end_location,vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculet_fere(vehicle.vehicle_type)
        self.vehicle = vehicle


    def set_driver(self, diver):
        self.driver = diver


    def start_ride(self):
        self.start_time = datetime.now()


    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def calculet_fere(self, vehicle):
        distance = 10
        print(vehicle)
        fere_per_km = {
            'car' : 30,
            'bike' : 40,
            'cng' : 25
        }
        return distance*fere_per_km.get(vehicle)

    def __repr__(self):
        return f"Rider details. started {self.start_location} to {self.end_location}"



class RideRequast:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers):
        self.availabel_driver = drivers

    def find_driver(self, ride_requast, vehicle_type):
        if len(self.availabel_driver) > 0:
            print("Looking for divers........")
            driver = self.availabel_driver[0]
            if vehicle_type == 'car':
                vehicl = Car("car",'D23483A',300)
            elif vehicle_type == 'Byke':
                vehicl = Byke("Bike",'D1214CA', 200)
            ride = Ride(ride_requast.rider.current_location, ride_requast.end_location, vehicl)
            driver.eccept_ride(ride)
            return ride