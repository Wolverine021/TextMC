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


class Inventar:
    def __init__(self, max_slotova=36):
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
                    print(
                        f"{predmet.naziv} - preostala izdržljivost: {predmet.izdrzljivost}"
                    )
                return
        print("Alat ne postoji...")

    def pojedi(self, naziv):
        for predmet in self.predmeti:
            if predmet.naziv == naziv and isinstance(predmet, Hrana):
                predmet.kolicina -= 1
                print(
                    f"{predmet.naziv} je pojeden, sitost je napunjena za {predmet.siti}"
                )
                if predmet.kolicina <= 0:
                    self.predmeti.remove(predmet)
                    print(f"{predmet.naziv} su potrošeni!")
                return
        print("Hrana ne postoji...")


class Crafting:
    def __init__(self):
        self.recepti = {
    "Pijuk": {
        "materijali": {"drvo": 2, "kamen": 3},
        "tip": "alat",
        "izdrzljivost": 100
    },
    "Sjekira": {
        "materijali": {"drvo": 3, "kamen": 2},
        "tip": "alat",
        "izdrzljivost": 80
    },
    "Kruh": {
        "materijali": {"psenica": 3},
        "tip": "hrana",
        "siti": 5
    },
    "Cigla": {
        "materijali": {"glina": 4},
        "tip": "blok",
        "tvrdoca": 2
    }
}

    def craft(self, inventar, naziv_predmeta):
        if naziv_predmeta not in self.recepti:
            print("Recept ne postoji...")
            return        
         
        if len(inventar.predmeti) == inventar.max_slotova:
            print("Inventar je pun, ne mozes craftat!")
            return
        
        
        
        recept = self.recepti[naziv_predmeta]
        materijali = recept["materijali"]
        
        for materijal, broj in materijali.items():
            pronadeno = False
            for predmet in inventar.predmeti:
                if predmet.naziv == materijal:
                    pronadeno = True
                    if predmet.kolicina < broj:
                        print(f"Nemas dovoljno materijala: {materijal}")
                        return
            if not pronadeno:
                print(f"Nemas materijal: {materijal}")
                return
            
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
moj_inventar.dodaj_predmet(Blok("drvo", kolicina=5, tvrdoca=1))
moj_inventar.dodaj_predmet(Blok("kamen", kolicina=5, tvrdoca=2))
moj_inventar.dodaj_predmet(Hrana("psenica", kolicina=5, siti=1))
moj_inventar.dodaj_predmet(Blok("glina", kolicina=5, tvrdoca=1))

crafting = Crafting()
crafting.craft(moj_inventar, "Pijuk")
crafting.craft(moj_inventar, "Kruh")
crafting.craft(moj_inventar, "Cigla")

moj_inventar.prikazi_inventar()