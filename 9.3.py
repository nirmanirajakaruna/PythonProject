class Kilidytis:
    def _init_(self, top_speed):
        self.top_speed = top_speed
        self.nopeus = 0  # current speed in km/h
        self.matka = 0   # distance traveled in km

    def auta(self, speed_change):
        new_speed = self.nopeus + speed_change

        if new_speed > self.top_speed:
            self.nopeus = self.top_speed
        elif new_speed < 0:
            self.nopeus = 0
        else:
            self.nopeus = new_speed

    def kuljea(self, hours):
        # Increase distance traveled by speed * hours
        self.matka += self.nopeus * hours

# Example usage:
auto = Kilidytis()
auto.nopeus = 60
auto.matka = 2000

auto.kuljea(1.5)
print(f"Distance traveled: {auto.matka} km")  # Output: 2090 km