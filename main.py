from inventory import Inventar
from crafting import Crafting
from exceptions import InventarPun
from persistency import spremi_stanje, ucitaj_stanje
from stats import Stats
from items import Blok, Hrana, Alat

def pokreni_igru():
    print("""
██████╗███████╗██╗  ██╗████████╗███╗   ███╗ ██████╗
╚═██╔═╝██╔════╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔════╝
  ██║  █████╗   ╚███╔╝    ██║   ██╔████╔██║██║     
  ██║  ██╔══╝   ██╔██╗    ██║   ██║╚██╔╝██║██║     
  ██║  ███████╗██╔╝ ██╗   ██║   ██║ ╚═╝ ██║╚██████╗
  ╚═╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝
""")
    
    inventar = Inventar()
    stats = Stats(inventar)
    crafting = Crafting()
    
    print("1. Ucitaj igru")
    print("2. Zapocni novu")
    izbor = input("Izbor: ")
    if izbor == "1":
        ucitaj_stanje(stats, inventar)
    elif izbor == "2":
        pass
    else:
        print("Nepoznat izbor...")
    
    while True:
        print("\n1. Prikazi inventar")
        print("2. Craftaj predmet")
        print("3. Pojedi hranu")
        print("4. Koristi alat")
        print("5. Prikazi stats")
        print("6. Stack Test")
        print("7. Spremi i izadji")
        izbor = input("Izbor: ")
        
        if izbor == "1":
            inventar.prikazi_inventar()
        elif izbor == "2":
            predmet = input("Izaberi predmet za napravit: ")   
            try:   
                crafting.craft(inventar, predmet) 
            except Exception as e:
                print(f"Greška: {e}")    
        elif izbor == "3":
            hrana = input("Izaberi sto pojesti: ")
            try:
                inventar.pojedi(hrana, stats)
            except Exception as e:
                print(f"Greška {e}")
        elif izbor == "4":
            alat = input("Izaberi alat za koristenje: ")
            try:
                inventar.koristi_alat(alat)
            except Exception as e:
                print(f"Greška: {e}")           
        elif izbor == "5":
            print(stats)
        elif izbor == "6":
            try:
                inventar.dodaj_predmet(Blok("Drvo", 30, 1))
                inventar.dodaj_predmet(Blok("Drvo", 50, 1))
                inventar.dodaj_predmet(Blok("Kamen", 140, 2))
                inventar.prikazi_inventar()
            except InventarPun as e:
                print(f"Greška: {e}")

        elif izbor == "7":
            spremi_stanje(stats, inventar)
            break
        else:
            print("Nepoznat izbor...")

#Start
if __name__ == "__main__":
    pokreni_igru()
    
    

