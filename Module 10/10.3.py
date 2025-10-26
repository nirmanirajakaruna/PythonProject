class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        print(f"Siirrytään kerrokseen {kohdekerros}")
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
        self.alin_kerros = alin_kerros

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero + 1}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero!")

    def palohalytys(self):
        print("\n🔥 Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen! 🔥")
        for i, hissi in enumerate(self.hissit):
            print(f"\nHissi {i + 1}:")
            hissi.siirry_kerrokseen(self.alin_kerros)

talo = Talo(1, 10, 3)
talo.aja_hissia(0, 7)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 9)
talo.palohalytys()