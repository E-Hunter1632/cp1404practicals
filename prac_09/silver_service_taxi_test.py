""" SilverServiceTaxi testing program. """
from prac_09.silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
silver_taxi_2 = SilverServiceTaxi("Another", 200, 2)

silver_taxi.drive(50)
print(silver_taxi)
print(silver_taxi.get_fare())

silver_taxi.start_fare()
silver_taxi.drive(100)
print(silver_taxi)
print(silver_taxi.get_fare())

silver_taxi_2.drive(18)
print(silver_taxi_2)
print(silver_taxi_2.get_fare())
