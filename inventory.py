from exceptions import InventarPun, HranaNePostoji, AlatNePostoji
from items import Blok, Alat, Hrana


class Inventar:
    def __init__(self, max_slotova=36, max_stack=64):
        self.max_slotova = max_slotova
        self.max_stack = max_stack
        self.predmeti = []

    def dodaj_predmet(self, predmet):
        if isinstance(predmet, Alat):
            if len(self.predmeti) < self.max_slotova:
                self.predmeti.append(predmet)
                print(f"Dodan je {predmet.naziv}")
            else:
                raise InventarPun("Inventar je pun!")

        elif isinstance(predmet, (Hrana, Blok)):
            pocetna_kolicina = predmet.kolicina
            preostalo = predmet.kolicina

            for item in self.predmeti:
                if (
                    item.naziv == predmet.naziv
                    and item.kolicina < self.max_stack
                ):
                    slobodno = self.max_stack - item.kolicina
                    dodat = min(preostalo, slobodno)

                    item.kolicina += dodat
                    preostalo -= dodat

                    if preostalo == 0:
                        print(
                            f"Dodano je x{pocetna_kolicina} "
                            f"{predmet.naziv}"
                        )
                        return

            while preostalo > 0:
                if len(self.predmeti) >= self.max_slotova:
                    raise InventarPun(
                        f"Inventar je pun, nije dodano "
                        f"x{preostalo} {predmet.naziv}."
                    )

                novi_stack = min(preostalo, self.max_stack)

                if isinstance(predmet, Blok):
                    novi_predmet = Blok(
                        predmet.naziv,
                        novi_stack,
                        predmet.tvrdoca,
                    )

                elif isinstance(predmet, Hrana):
                    novi_predmet = Hrana(
                        predmet.naziv,
                        novi_stack,
                        predmet.siti,
                    )

                self.predmeti.append(novi_predmet)
                preostalo -= novi_stack

            print(
                f"Dodano je x{pocetna_kolicina} "
                f"{predmet.naziv}"
            )

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
            if (
                predmet.naziv == naziv
                and isinstance(predmet, Alat)
            ):
                predmet.izdrzljivost -= 1

                if predmet.izdrzljivost <= 0:
                    self.predmeti.remove(predmet)
                    print(f"{predmet.naziv} je puknuo!")
                else:
                    print(
                        f"{predmet.naziv} - preostala izdržljivost: "
                        f"{predmet.izdrzljivost}"
                    )

                return

        raise AlatNePostoji(
            f"Alat {naziv} ne postoji..."
        )

    def pojedi(self, naziv, stats):
        for predmet in self.predmeti:
            if (
                predmet.naziv == naziv
                and isinstance(predmet, Hrana)
            ):
                predmet.kolicina -= 1
                stats.dodaj_hunger(predmet.siti)

                print(
                    f"{predmet.naziv} je pojeden, sitost je "
                    f"napunjena za {predmet.siti}"
                )

                if predmet.kolicina <= 0:
                    self.predmeti.remove(predmet)
                    print(
                        f"{predmet.naziv} su potrošeni!"
                    )

                return

        raise HranaNePostoji(
            f"Hrana {naziv} ne postoji..."
        )

