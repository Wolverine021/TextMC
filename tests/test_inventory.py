import pytest
from exceptions import InventarPun
from inventory import Inventar
from items import Blok, Alat, Hrana
from stats import Stats


#Testovi za dodaj_predmet()
def test_dodaj_jedan_blok():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("Kamen",1,1))
    
    assert len(inventar.predmeti) == 1
    assert inventar.predmeti[0].naziv == "Kamen"
    assert inventar.predmeti[0].kolicina == 1

def test_dodaj_jednu_hranu():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Hrana("Kruh",1,1))
    
    assert len(inventar.predmeti) == 1
    assert inventar.predmeti[0].naziv == "Kruh"
    assert inventar.predmeti[0].kolicina == 1

def test_dodaj_jedan_alat():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Alat("Pijuk",1,100))
    
    assert len(inventar.predmeti) == 1
    assert inventar.predmeti[0].naziv == "Pijuk"
    assert inventar.predmeti[0].kolicina == 1

def test_stackanje_istih_blokova():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("Drvo",32,1))
    inventar.dodaj_predmet(Blok("Drvo",32,1))
    
    assert len(inventar.predmeti) == 1
    assert inventar.predmeti[0].kolicina == 64
    
def test_stackanje_preko_64():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("Drvo",73,1))
    
    assert len(inventar.predmeti) == 2
    assert inventar.predmeti[0].kolicina == inventar.max_stack
    assert inventar.predmeti[1].kolicina == 9

def test_vise_novih_stackova():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Blok("Drvo",150,1))

    assert len(inventar.predmeti) == 3
    assert inventar.predmeti[0].kolicina == inventar.max_stack
    assert inventar.predmeti[1].kolicina == inventar.max_stack
    assert inventar.predmeti[2].kolicina == 22

def test_alati_se_ne_stackaju():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Alat("Pijuk", 1, 100))
    inventar.dodaj_predmet(Alat("Pijuk", 1, 100))
    
    assert len(inventar.predmeti) == 2

def test_pun_inventar():
    inventar = Inventar(max_slotova=2)

    inventar.dodaj_predmet(Alat("Pijuk", 1, 100))
    inventar.dodaj_predmet(Alat("Sjekira", 1, 100))

    with pytest.raises(InventarPun):
        inventar.dodaj_predmet(Alat("Lopata", 1, 100)) 

#Ostali testovi
def test_pojedi_hranu():
    inventar = Inventar()
    stats = Stats(inventar)
    
    inventar.dodaj_predmet(Hrana("Kruh",2,1))
    inventar.pojedi("Kruh", stats)
    
    assert inventar.predmeti[0].kolicina == 1 

def test_koristi_alat():
    inventar = Inventar()
    
    inventar.dodaj_predmet(Alat("Pijuk",1,100))
    inventar.koristi_alat("Pijuk")
    
    assert inventar.predmeti[0].izdrzljivost == 99

def test_ukloni_predmet():
    inventar = Inventar()

    inventar.dodaj_predmet(Alat("Pijuk", 1, 100))
    inventar.dodaj_predmet(Hrana("Kruh", 2, 1))

    inventar.ukloni_predmet("Pijuk")

    assert len(inventar.predmeti) == 1
    assert inventar.predmeti[0].naziv == "Kruh"
    