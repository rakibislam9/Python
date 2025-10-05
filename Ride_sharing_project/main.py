from rider import Ridesharing, RideRequast, RideMatching, Ride
from ride_shair_user_part import Rider, Driver
from vehical import Car, Byke


niye_jao = Ridesharing("Niy jao")
Rahim = Rider('Rahim','rhim@gmail.com',376543,'Mohakhali',1200)
niye_jao.add_rider(Rahim)
Korim = Driver('Korim','korim@gmail.com',2345432,'Gulshan')
niye_jao.add_driver(Korim)
Rahim.request_ride(niye_jao,'Uttora','car')
Rahim.show_current_ride()
Korim.reach_distination(Rahim.current_ride)

print(niye_jao)