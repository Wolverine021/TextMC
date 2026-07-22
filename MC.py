import json

class RecepNePostoji(Exception):
    pass

class MaterijalNepostoji(Exception):
    pass

class NedovoljnoMaterijala(Exception):
    pass

class InventarPun(Exception):
    pass

class HealingError(Exception):
    pass
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

class Stats:
    def __init__(self, inventar, max_health=20, max_hunger=20):
        self.inventar = inventar
        self.max_health = max_health
        self.max_hunger = max_hunger
        self.health = max_health
        self.hunger = max_hunger
        
    def __str__(self):
        return f"Health: {self.health}/{self.max_health}\nHunger: {self.hunger}/{self.max_hunger}"
        
    def dodaj_health(self, kolicina):
        if self.health <= 0:
            raise HealingError("Healing nemoguć, mrtav si!")     
         
        self.health += kolicina
        if self.health >= self.max_health:
            print("Health je na max")
            self.health = self.max_health
        else:
            print(f"Health je povećan za {kolicina}")
        
    def oduzmi_health(self, kolicina):
        self.health -= kolicina
        if self.health <= 0:
            self.health = 0
            print("You died!")
       
    def dodaj_hunger(self, kolicina):
        self.hunger += kolicina
        if self.hunger >= self.max_hunger:
            print("Hunger je na max")
            self.hunger = self.max_hunger
        else:
            print(f"Hunger je povećan za {kolicina}")

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
        print("Alat ne postoji...")

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
        print("Hrana ne postoji...")


class Crafting:
    def __init__(self):
        with open("recepti.json", "r") as f:
            self.recepti = json.load(f)

    def craft(self, inventar, naziv_predmeta):
        if naziv_predmeta not in self.recepti:
            raise RecepNePostoji(f"Recept za '{naziv_predmeta}' ne postoji.")        
         
        if len(inventar.predmeti) >= inventar.max_slotova:
            raise InventarPun("Inventar je pun, ne mozes craftat!")
        
        recept = self.recepti[naziv_predmeta]
        materijali = recept["materijali"]
        
        for materijal, broj in materijali.items():
            pronadeno = False
            for predmet in inventar.predmeti:
                if predmet.naziv == materijal:
                    pronadeno = True
                    if predmet.kolicina < broj:
                        raise NedovoljnoMaterijala(f"Nemas dovoljno materijala: {materijal}")
            if not pronadeno:
                raise MaterijalNepostoji(f"Materijal ne postoji: {materijal}")
            
        for materijal, broj in materijali.items():
            for predmet in inventar.predmeti:
                if predmet.naziv == materijal:
                    predmet.kolicina -= broj
                    if predmet.kolicina == 0:
                        inventar.ukloni_predmet(materijal)
                    break
        
        if recept["tip"] == "alat":
            novi_predmet = Alat(naziv_predmeta, kolicina=1, izdrzljivost=recept["izdrzljivost"])
        elif recept["tip"] == "hrana":
            novi_predmet = Hrana(naziv_predmeta, kolicina=1, siti=recept["siti"])
        elif recept["tip"] == "blok":
            novi_predmet = Blok(naziv_predmeta, kolicina=1, tvrdoca=recept["tvrdoca"])
        
        inventar.dodaj_predmet(novi_predmet)  
    
        print(f"{naziv_predmeta} je uspjesno napravljen!")   

#Test
moj_inventar = Inventar()
moj_stats = Stats(moj_inventar)
moj_stats.hunger = 10

moj_inventar.dodaj_predmet(Hrana("Kruh", kolicina = 1, siti = 5))
moj_inventar.pojedi("Kruh", moj_stats)

print(moj_stats)