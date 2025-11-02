class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.kilometer_counter = 0  # starts at 0

    def drive(self, hours):
        # Distance = speed * time
        distance = self.maximum_speed * hours
        self.kilometer_counter += distance

    def print_info(self):
        print(f"Car {self.registration_number}:")
        print(f"  Max Speed: {self.maximum_speed} km/h")
        print(f"  Kilometer Counter: {self.kilometer_counter} km")

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity  # in kWh

    def print_info(self):
        super().print_info()
        print(f"  Battery Capacity: {self.battery_capacity} kWh")

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume  # in liters

    def print_info(self):
        super().print_info()
        print(f"  Tank Volume: {self.tank_volume} liters")

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.drive(3)
gasoline_car.drive(3)

electric_car.print_info()
print()
gasoline_car.print_info()