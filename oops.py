class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")  # Adding a display method in Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.__fuel_type = fuel_type

    def display_info(self):
        super().display_info()  # Now it will print the basic vehicle info
        print(f"Fuel: {self.__fuel_type}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity  # Correct attribute name

    def display_info(self):
        super().display_info()  # Now it will print the basic vehicle info
        print(f"Engine: {self.engine_capacity}")

# Creating instances
my_car = Car("Toyota", "Corolla", 2022, "Petrol")
my_bike = Bike("Yamaha", "R15", 2021, "150cc")

# Displaying information
my_car.display_info()
print()  # Adding a space for better readability
my_bike.display_info()
