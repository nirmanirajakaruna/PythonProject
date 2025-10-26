class Kilidytis:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.nopeus = 0  # initial speed

    def Auta(self, speed_change):
        # Update speed with speed_change
        new_speed = self.nopeus + speed_change

        # Ensure speed does not go below 0 or above top speed
        if new_speed > self.top_speed:
            self.nopeus = self.top_speed
        elif new_speed < 0:
            self.nopeus = 0
        else:
            self.nopeus = new_speed

# Main program
car = Kilidytis(top_speed=150)  # example top speed 150 km/h

car.Auta(30)   # increase speed by 30 km/h
car.Auta(70)   # increase speed by 70 km/h
car.Auta(50)   # increase speed by 50 km/h

print(f"Current speed: {car.nopeus} km/h")  # print current speed

car.Auta(-200)  # emergency braking