# autocare_module.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Function 1: Register Customer
def register_customer(name, phone):
    return {
        "Name": name,
        "Phone": phone
    }


# Function 2: Register Vehicle
def register_vehicle(number, model):
    return {
        "Vehicle Number": number,
        "Model": model
    }


# Function 3: Calculate Service Charge
def calculate_service_charge(services):

    price = {
        "Oil Change": 80,
        "Car Wash": 30,
        "Engine Repair": 250,
        "Tyre Change": 150
    }

    total = 0

    for service in services:
        total += price[service]

    return total



# OOP Class

class Vehicle:

    def __init__(self, number, brand, model, year):
        self.number = number
        self.brand = brand
        self.model = model
        self.year = year


    def display_vehicle(self):
        return (
            self.brand + " "
            + self.model
            + " "
            + str(self.year)
        )


    def service_cost(self, basic=50):
        return basic



# Inheritance

class PremiumVehicle(Vehicle):

    def __init__(self, number, brand, model, year, membership):

        super().__init__(
            number,
            brand,
            model,
            year
        )

        self.membership = membership


    def display_vehicle(self):

        return (
            super().display_vehicle()
            + " Premium "
            + self.membership
        )



# Magic Methods

class Service:

    def __init__(self, name, charge):
        self.name = name
        self.charge = charge


    def __str__(self):
        return self.name


    def __add__(self, other):
        return self.charge + other.charge



# Data Analysis

def analysis():

    data = {

        "Vehicle": [
            "Honda",
            "Toyota",
            "BMW"
        ],

        "Charge": [
            100,
            150,
            300
        ]

    }


    df = pd.DataFrame(data)


    print(df)


    print(
        "Average:",
        np.mean(df["Charge"])
    )


    print(
        df.sort_values("Charge")
    )


    plt.bar(
        df["Vehicle"],
        df["Charge"]
    )

    plt.xlabel("Vehicle")
    plt.ylabel("Charge")

    plt.title(
        "Service Charge Analysis"
    )

    plt.show()