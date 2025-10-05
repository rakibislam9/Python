from abc import ABC, abstractmethod
from rider import RideRequast, RideMatching
class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0


    @abstractmethod
    def display_profil(self):
        raise NotImplementedError
    


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.wallet = initial_amount
        self.current_location = current_location


    def display_profil(self):
        print(f"Rider {self.name} and Email {self.email}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print(f"Amount less then 0")


    def update_location(self,current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_requast = RideRequast(self, destination)
        ride_Matching = RideMatching(ride_sharing.drivers)
        ride = ride_Matching.find_driver(ride_requast,vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("YAY!! we got a Ride")

    def show_current_ride(self):
        print(self.current_ride)
        print(self.load_cash())


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0


    def display_profil(self):
        print(f"Deiver {self.name}")

    def eccept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)


    def reach_distination(self, ride):
        ride.end_ride()

