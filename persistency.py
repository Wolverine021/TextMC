import json
from items import Predmet, Blok, Alat, Hrana

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