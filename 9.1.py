class Auto:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

def main():
    car = Auto("ABC-123", 142)
    print("Car details:")
    print(f"License Plate: {car.license_plate}")
    print(f"Top Speed: {car.top_speed} km/h")
    print(f"Current Speed: {car.current_speed} km/h")
    print(f"Distance Traveled: {car.distance_traveled} km")

if __name__ == "__main__":
    main()