from inventory import Inventar
from stats import Stats

def test_promjena_healtha():
    inventar = Inventar()
    stats = Stats(inventar)

    stats.health = 10

    stats.dodaj_health(5)
    assert stats.health == 15

    stats.oduzmi_health(10)
    assert stats.health == 5

def test_promjena_hungera():
    inventar = Inventar()
    stats = Stats(inventar)

    stats.hunger = 10

    stats.dodaj_hunger(5)
    assert stats.hunger == 15