from abc import ABC

class Vheicle(ABC):

    spped = {
        'car': 50,
        'byke': 60,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate


class Car(Vheicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

class Byke(Vheicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)