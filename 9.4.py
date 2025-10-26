import random

class Auto:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def kiihdyta(self, speed_change):
        # Change speed by given amount, but stay within [0, top_speed]
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def kulje(self, hours):
        # Distance = speed × time
        self.distance_traveled += self.current_speed * hours



cars = []

# Create 10 cars
for i in range(1, 11):
    top_speed = random.randint(100, 200)
    license_plate = f"ABC-{i}"
    cars.append(Auto(license_plate, top_speed))

race_over = False
hours = 0

# Race simulation
while not race_over:
    hours += 1
    for car in cars:
        # Random speed change between -10 and +15
        speed_change = random.randint(-10, 15)
        car.kiihdyta(speed_change)
        car.kulje(1)

        # Check if any car has traveled at least 10,000 km
        if car.distance_traveled >= 10000:
            race_over = True
            break

print("\nRACE FINISHED!")
print(f"Total hours raced: {hours}\n")
print(f"{'License':<10} {'TopSpeed(km/h)':<15} {'Current(km/h)':<15} {'Distance(km)':<15}")
print("-" * 55)

for car in cars:
    print(f"{car.license_plate:<10} {car.top_speed:<15} {car.current_speed:<15} {car.distance_traveled:<15.1f}")