import pytest
from exceptions import RecepNePostoji, InventarPun, NedovoljnoMaterijala, MaterijalNepostoji
from crafting import Crafting
from inventory import Inventar
from items import Blok, Alat

def test_uspjesan_craft():
    crafting = Crafting()
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("kamen", 3, 1))
    inventar.dodaj_predmet(Blok("drvo", 2, 1))
    
    crafting.craft(inventar, "Pijuk")
    
    assert any(predmet.naziv == "Pijuk" for predmet in inventar.predmeti)
    
def test_recept_ne_postoji():
    crafting = Crafting()
    inventar = Inventar()
    
    with pytest.raises(RecepNePostoji):
        crafting.craft(inventar, "Gijuk")

def test_nedovoljno_materijala():
    crafting = Crafting()
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("kamen", 2, 1))
    inventar.dodaj_predmet(Blok("drvo", 2, 1))
    
    with pytest.raises(NedovoljnoMaterijala):
        crafting.craft(inventar, "Pijuk")
    
def test_materijal_ne_postoji():
    crafting = Crafting()
    inventar = Inventar()
    
    with pytest.raises(MaterijalNepostoji):
        crafting.craft(inventar, "Pijuk")