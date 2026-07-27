from exceptions import InventarPun, HranaNePostoji, AlatNePostoji
from items import Predmet, Blok, Alat, Hrana

class Inventar:
    def __init__(self, max_slotova=36):
        self.max_slotova = max_slotova
        self.predmeti = []

    def dodaj_predmet(self, predmet):
        if len(self.predmeti) < self.max_slotova:
            self.predmeti.append(predmet)
            print(f"{predmet.naziv} je dodan!")
        else:
            raise InventarPun("Inventar je pun, ne mozes craftat!")

    def ukloni_predmet(self, naziv):
        for predmet in self.predmeti:
            if predmet.naziv == naziv:
                self.predmeti.remove(predmet)
                print(f"{predmet.naziv} je uklonjen!")
                return
        print("Taj predmet ne postoji...")

    def prikazi_inventar(self):
        for predmet in self.predmeti:
            print(predmet)

    def koristi_alat(self, naziv):
        for predmet in self.predmeti:
            if predmet.naziv == naziv and isinstance(predmet, Alat):
                predmet.izdrzljivost -= 1
                if predmet.izdrzljivost <= 0:
                    self.predmeti.remove(predmet)
                    print(f"{predmet.naziv} je puknuo!")
                else:
                    print(
                        f"{predmet.naziv} - preostala izdržljivost: {predmet.izdrzljivost}"
                    )
                return
        raise AlatNePostoji(f"Alat {naziv} ne postoji...")

    def pojedi(self, naziv, stats):
        for predmet in self.predmeti:
            if predmet.naziv == naziv and isinstance(predmet, Hrana):
                predmet.kolicina -= 1
                stats.dodaj_hunger(predmet.siti)
                print(f"{predmet.naziv} je pojeden, sitost je napunjena za {predmet.siti}")
                if predmet.kolicina <= 0:
                    self.predmeti.remove(predmet)
                    print(f"{predmet.naziv} su potrošeni!")
                return
        raise HranaNePostoji(f"Hrana {naziv} ne postoji...")