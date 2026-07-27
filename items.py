class Predmet:
    def __init__(self, naziv, kolicina=1):
        self.naziv = naziv
        self.kolicina = kolicina


class Blok(Predmet):
    def __init__(self, naziv, kolicina=1, tvrdoca=1):
        super().__init__(naziv, kolicina)
        self.tvrdoca = tvrdoca

    def __str__(self):
        return f"{self.naziv} x{self.kolicina} (tvrdoća: {self.tvrdoca})"


class Alat(Predmet):
    def __init__(self, naziv, kolicina=1, izdrzljivost=100):
        super().__init__(naziv, kolicina)
        self.izdrzljivost = izdrzljivost

    def __str__(self):
        return f"{self.naziv} x{self.kolicina} (izdrzljivost: {self.izdrzljivost})"


class Hrana(Predmet):
    def __init__(self, naziv, kolicina=1, siti=4):
        super().__init__(naziv, kolicina)
        self.siti = siti

    def __str__(self):
        return f"{self.naziv} x{self.kolicina} (sitost: {self.siti})"