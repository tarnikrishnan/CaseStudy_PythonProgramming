# autocare_system.py

from autocare_module import *


# Main Program


customer = register_customer(
    "Ali",
    "0123456789"
)


vehicle = register_vehicle(
    "ABC123",
    "Honda Civic"
)


services = [
    "Oil Change",
    "Car Wash"
]


charge = calculate_service_charge(
    services
)


print("====================")
print("AUTOCARE SERVICE CENTRE")
print("====================")


print(customer)

print(vehicle)


print("\nSelected Services:")

for s in services:
    print(s)


print(
    "Total Charge RM:",
    charge
)



# Object Creation

car1 = Vehicle(
    "ABC123",
    "Honda",
    "Civic",
    2024
)


premium = PremiumVehicle(
    "BMW001",
    "BMW",
    "X5",
    2025,
    "Gold"
)



print("\nVehicle Object:")
print(car1.display_vehicle())


print("\nPremium Vehicle Object:")
print(premium.display_vehicle())



# Magic Method

service1 = Service(
    "Oil Change",
    80
)

service2 = Service(
    "Car Wash",
    30
)


print(
    "\nMagic Method Output:"
)

print(service1)

print(
    "Total:",
    service1 + service2
)



# Data Analysis

analysis()