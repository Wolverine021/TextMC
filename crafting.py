import json
from exceptions import RecepNePostoji, MaterijalNepostoji, NedovoljnoMaterijala, InventarPun, HealingError, HranaNePostoji, AlatNePostoji
from items import Predmet, Blok, Alat, Hrana

class Crafting:
    def __init__(self):
        with open("recipes.json", "r") as f:
            self.recipes = json.load(f)

    def craft(self, inventar, naziv_predmeta):
        if naziv_predmeta not in self.recipes:
            raise RecepNePostoji(f"Recept za '{naziv_predmeta}' ne postoji.")        
         
        if len(inventar.predmeti) >= inventar.max_slotova:
            raise InventarPun("Inventar je pun, ne mozes craftat!")
        
        recept = self.recipes[naziv_predmeta]
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