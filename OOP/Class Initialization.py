class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You start driving the {self.color} {self.model}")

    def stop(self):
        print(f"You stop driving the {self.color} {self.model}")

    def describe(self):
        print(f"{self.model} {self.color} {self.year}")

car1 = Car("BMW", 2012, "Red", True)
car2 = Car("Audi", 2025, "Blue", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.describe()
car1.drive()
car2.describe()
car2.stop()