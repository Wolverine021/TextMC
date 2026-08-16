import json
from exceptions import RecepNePostoji, MaterijalNepostoji, NedovoljnoMaterijala, InventarPun
from items import Blok, Alat, Hrana

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
            ukupno = 0
            
            for predmet in inventar.predmeti:
                if predmet.naziv == materijal:
                    pronadeno = True
                    ukupno += predmet.kolicina
            
            if not pronadeno:
                raise MaterijalNepostoji(f"Materijal ne postoji: {materijal}")           
            
            if ukupno < broj:
                raise NedovoljnoMaterijala(f"Nemas dovoljno: {materijal}")
        
         
        for materijal, broj in materijali.items():
            preostalo = broj
            
            while preostalo > 0:
                stackovi = [
                    predmet
                    for predmet in inventar.predmeti
                    if predmet.naziv == materijal
                ]
                min_stack = min(stackovi, key=lambda predmet: predmet.kolicina)
                    
                if preostalo >= min_stack.kolicina:
                    preostalo -= min_stack.kolicina 
                    inventar.predmeti.remove(min_stack)
                
                else:
                    min_stack.kolicina -= preostalo
                    preostalo = 0
                            
        if recept["tip"] == "alat":
            novi_predmet = Alat(naziv_predmeta, kolicina=1, izdrzljivost=recept["izdrzljivost"])
        elif recept["tip"] == "hrana":
            novi_predmet = Hrana(naziv_predmeta, kolicina=1, siti=recept["siti"])
        elif recept["tip"] == "blok":
            novi_predmet = Blok(naziv_predmeta, kolicina=1, tvrdoca=recept["tvrdoca"])
        
        inventar.dodaj_predmet(novi_predmet)  
    
        print(f"{naziv_predmeta} je uspjesno napravljen!") 