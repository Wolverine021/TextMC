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

class HranaNePostoji(Exception):
    pass

class AlatNePostoji(Exception):
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

def spremi_stanje(stats, inventar, path = "user.json"):
    inventar_lista = []
    
    for predmet in inventar.predmeti:
            if isinstance(predmet, Alat):
                stavka = {"tip": "alat", "naziv": predmet.naziv, "kolicina": predmet.kolicina, "izdrzljivost": predmet.izdrzljivost}
            elif isinstance(predmet, Hrana):
                stavka = {"tip": "hrana", "naziv": predmet.naziv, "kolicina": predmet.kolicina, "siti": predmet.siti}
            elif isinstance(predmet, Blok):
                stavka = {"tip": "blok", "naziv": predmet.naziv, "kolicina": predmet.kolicina, "tvrdoca": predmet.tvrdoca}
            inventar_lista.append(stavka)
            
    podaci = {
        "health": stats.health,
        "hunger": stats.hunger,
        "inventar": inventar_lista
    }
    
    with open(path, "w") as f:
        json.dump(podaci, f, indent = 4)
        
def ucitaj_stanje(stats, inventar, path="user.json"):
    with open(path, "r") as f:
        podaci = json.load(f)
    
    stats.health = podaci["health"]
    stats.hunger = podaci["hunger"]
    
    inventar.predmeti = []   
    
    for stavka in podaci["inventar"]:
        if stavka["tip"] == "alat":
            predmet = Alat(stavka["naziv"], kolicina=stavka["kolicina"], izdrzljivost=stavka["izdrzljivost"])
        elif stavka["tip"] == "hrana":
            predmet = Hrana(stavka["naziv"], kolicina=stavka["kolicina"], siti=stavka["siti"])
        elif stavka["tip"] == "blok":
            predmet = Blok(stavka["naziv"], kolicina=stavka["kolicina"], tvrdoca=stavka["tvrdoca"])
        
        inventar.predmeti.append(predmet)
    
def pokreni_igru():
    print("""
██████╗███████╗██╗  ██╗████████╗███╗   ███╗ ██████╗
╚═██╔═╝██╔════╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔════╝
  ██║  █████╗   ╚███╔╝    ██║   ██╔████╔██║██║     
  ██║  ██╔══╝   ██╔██╗    ██║   ██║╚██╔╝██║██║     
  ██║  ███████╗██╔╝ ██╗   ██║   ██║ ╚═╝ ██║╚██████╗
  ╚═╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝
""")
    
    inventar = Inventar()
    stats = Stats(inventar)
    crafting = Crafting()
    
    print("1. Ucitaj igru")
    print("2. Zapocni novu")
    izbor = input("Izbor: ")
    if izbor == "1":
        ucitaj_stanje(stats, inventar)
    elif izbor == "2":
        pass
    else:
        print("Nepoznat izbor...")
    
    while True:
        print("\n1. Prikazi inventar")
        print("2. Craftaj predmet")
        print("3. Pojedi hranu")
        print("4. Koristi alat")
        print("5. Prikazi stats")
        print("6. Spremi i izadji")
        izbor = input("Izbor: ")
        
        if izbor == "1":
            inventar.prikazi_inventar()
        elif izbor == "2":
            predmet = input("Izaberi predmet za napravit: ")   
            try:   
                crafting.craft(inventar, predmet) 
            except Exception as e:
                print(f"Greška: {e}")    
        elif izbor == "3":
            hrana = input("Izaberi sto pojesti: ")
            try:
                inventar.pojedi(hrana, stats)
            except Exception as e:
                print(f"Greška {e}")
        elif izbor == "4":
            alat = input("Izaberi alat za koristenje: ")
            try:
                inventar.koristi_alat(alat)
            except Exception as e:
                print(f"Greška: {e}")           
        elif izbor == "5":
            print(stats)
        elif izbor == "6":
            spremi_stanje(stats, inventar)
            break
        else:
            print("Nepoznat izbor...")

#Start
pokreni_igru()
    
    

