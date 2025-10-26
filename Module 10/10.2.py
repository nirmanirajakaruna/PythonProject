class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        else:
            print("Olet ylin kerros — ei voi mennä ylemmäs.")
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        else:
            print("Olet alin kerros — ei voi mennä alemmas.")
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        # Tarkistetaan, että kohde on sallittu välillä
        if not (self.alin_kerros <= kohdekerros <= self.ylin_kerros):
            print(f"Virhe: kohdekerros {kohdekerros} ei ole välillä "
                  f"{self.alin_kerros}-{self.ylin_kerros}.")
            return

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

    def aja_hissia(self, hissin_numero, kohdekerros):
        # Käytetään oikeaa len-funktiota
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissin_numero + 1}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print("Virheellinen hissinumero!")


# --- Main program ---
talo = Talo(1, 10, 2)
talo.aja_hissia(0, 5)   # ensimmäinen hissi, siirrytään kerrokseen 5
talo.aja_hissia(1, 8)   # toinen hissi, siirrytään kerrokseen 8