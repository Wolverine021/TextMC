import json

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

    assert path.exists()

    with open(path, "r", encoding="utf-8") as f:
        podaci = json.load(f)

    ocekivano = {
        "health": 20,
        "hunger": 15,
        "inventar": [
            {
                "tip": "blok",
                "naziv": "drvo",
                "kolicina": 10,
                "tvrdoca": 1,
            }
        ],
    }

    assert podaci == ocekivano


def test_ucitavanje(tmp_path):
    inventar1 = Inventar()
    stats1 = Stats(inventar1)

    inventar1.dodaj_predmet(Blok("drvo", 10, 1))
    stats1.health = 20
    stats1.hunger = 15

    path = tmp_path / "test_user.json"
    spremi_stanje(stats1, inventar1, path)

    inventar2 = Inventar()
    stats2 = Stats(inventar2)

    ucitaj_stanje(stats2, inventar2, path)

    assert stats2.health == stats1.health
    assert stats2.hunger == stats1.hunger

    assert len(inventar2.predmeti) == len(inventar1.predmeti)

    predmet1 = inventar1.predmeti[0]
    predmet2 = inventar2.predmeti[0]

    assert predmet2.naziv == predmet1.naziv
    assert predmet2.kolicina == predmet1.kolicina
    assert predmet2.tvrdoca == predmet1.tvrdoca