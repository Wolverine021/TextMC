from inventory import Inventar
from main import nova_igra
from stats import Stats

def test_new_game():
    inventar = Inventar()
    stats = Stats(inventar)
    
    nova_igra(inventar, stats)
    
    assert stats.health == stats.max_health
    assert stats.hunger == stats.max_hunger

    assert inventar.predmeti