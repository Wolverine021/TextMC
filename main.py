from inventory import Inventar
from crafting import Crafting
from items import Blok, Hrana
from persistency import spremi_stanje, ucitaj_stanje
from stats import Stats

def nova_igra(inventar, stats):
    inventar.predmeti.clear()

    stats.health = stats.max_health
    stats.hunger = stats.max_hunger

    inventar.dodaj_predmet(Blok("drvo", 10, 1))
    inventar.dodaj_predmet(Blok("kamen", 10, 2))
    inventar.dodaj_predmet(Blok("psenica", 5, 1))
    inventar.dodaj_predmet(Hrana("jabuka", 3, 1))

    inventar.dodaj_predmet(Blok("glina", 5, 1))
    inventar.dodaj_predmet(Blok("zeljezo", 5, 4))
    inventar.dodaj_predmet(Hrana("sirova_svinjetina", 3, 1))

    print("Nova igra je zapoceta!")
    
       
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
        nova_igra(inventar, stats)
    else:
        print("Nepoznat izbor...")
    
    while True:
        print("\n1. Prikazi inventar")
        print("2. Craftaj predmet")
        print("3. Pojedi hranu")
        print("4. Koristi alat")
        print("5. Prikazi stats")
        print("6. Spremi i izadji")
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
            spremi_stanje(stats, inventar)
            break
        
        else:
            print("Nepoznat izbor...")

#Start
if __name__ == "__main__":
    pokreni_igru()
    
    

