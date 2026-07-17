class Predmet:
    def __init__(self, naziv, kolicina = 1):
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
    
class Inventar:
    def __init__(self, max_slotova = 36):
        self.max_slotova = max_slotova
        self.predmeti = []
        
    def dodaj_predmet(self, predmet):
        if len(self.predmeti) < self.max_slotova:
            self.predmeti.append(predmet)
            print(f"{predmet.naziv} je dodan!")
        else:
            print("Inventar je pun!")
            
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
                    print(f"{predmet.naziv} - preostala izdržljivost: {predmet.izdrzljivost}")
                return
        print("Alat ne postoji...")
    
    def pojedi(self, naziv):
        for predmet in self.predmeti:
            if predmet.naziv == naziv and isinstance(predmet, Hrana):
                predmet.kolicina -= 1
                print(f"{predmet.naziv} je pojeden, sitost je napunjena za {predmet.siti}")
                if predmet.kolicina <= 0:
                    self.predmeti.remove(predmet)
                    print(f"{predmet.naziv} su potrošeni!")
                return
        print("Hrana ne postoji...")

class Craft:
    def __init__(self,):
        recepti = {}
        
