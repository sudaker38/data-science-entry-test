# -*- coding: utf-8 -*-
"""q7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/106E6TEkYznUNRiXrIhbesnWtdNGdAUyB
"""

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()