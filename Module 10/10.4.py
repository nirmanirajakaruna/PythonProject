import random

# Car class
class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kulje(self, tunti):
        """Increase the distance traveled based on current speed."""
        self.matka += self.nopeus * tunti

# Race class
class Kilpailu:
    def __init__(self, nimi, matka, autot):
        self.nimi = nimi
        self.matka = matka
        self.autot = autot

    def tunti_kuluu(self):
        """Simulate one hour of the race."""
        for auto in self.autot:
            nopeus_muutos = random.randint(-10, 15)
            auto.nopeus += nopeus_muutos

            if auto.nopeus < 0:
                auto.nopeus = 0
            elif auto.nopeus > auto.huippunopeus:
                auto.nopeus = auto.huippunopeus
            auto.kulje(1)

    def tulosta_tilanne(self):
        """Print current status of all cars."""
        print(f"{'Rekisteri':<10} {'Matka':>6} km {'Nopeus':>6} km/h")
        print("-" * 26)
        for auto in self.autot:
            print(f"{auto.rekisteri:<10} {auto.matka:6.1f} {auto.nopeus:6}")

    def kilpailu_ohi(self):
        """Return True if any car has finished the race."""
        for auto in self.autot:
            if auto.matka >= self.matka:
                return True
        return False

def main():
    # Create 10 cars
    autot = [
        Auto("ABC-123", 142),
        Auto("DEF-456", 135),
        Auto("GHI-789", 148),
        Auto("JKL-012", 138),
        Auto("MNO-345", 150),
        Auto("PQR-678", 140),
        Auto("STU-901", 145),
        Auto("VWX-234", 132),
        Auto("YZA-567", 137),
        Auto("BCD-890", 144),
    ]

    # Create race
    kilpailu = Kilpailu("The Great Junkyard Rally", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:  # Print every 10 hours
            print(f"\n--- Tilanne tunnin {tunnit} jälkeen ---")
            kilpailu.tulosta_tilanne()

    print(f"\n--- Kilpailu ohi tunnin {tunnit} jälkeen ---")
    kilpailu.tulosta_tilanne()

if __name__ == "_main_":
    main()