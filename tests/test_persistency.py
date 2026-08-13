import json
from pathlib import Path
from inventory import Inventar
from stats import Stats
from items import Blok
from persistency import spremi_stanje, ucitaj_stanje

def test_spremanje(tmp_path):
    inventar = Inventar()
    stats = Stats(inventar)

    inventar.dodaj_predmet(Blok("drvo", 10, 1))
    stats.health = 20
    stats.hunger = 15

    path = tmp_path / "test_user.json"

    spremi_stanje(stats, inventar, path)

    with open(path, "r") as f:
        podaci = json.load(f)

    ocekivano = {
        "health": 20,
        "hunger": 15,
        "predmeti": [
            {
                "tip": "Blok",
                "naziv": "drvo",
                "kolicina": 10,
                "tvrdoca": 1
            }
        ]
    }

    assert podaci == ocekivano
    
def test_ucitavanje():
    inventar = Inventar()
    stats = Stats(inventar)
    
    pass

def test_roundtrip():
    pass