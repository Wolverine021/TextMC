from exceptions import RecepNePostoji, MaterijalNepostoji, NedovoljnoMaterijala, InventarPun, HealingError, HranaNePostoji, AlatNePostoji

class Stats:
    def __init__(self, inventar, max_health=20, max_hunger=20):
        self.inventar = inventar
        self.max_health = max_health
        self.max_hunger = max_hunger
        self.health = max_health
        self.hunger = max_hunger
        
    def __str__(self):
        return f"Health: {self.health}/{self.max_health}\nHunger: {self.hunger}/{self.max_hunger}"
        
    def dodaj_health(self, kolicina):
        if self.health <= 0:
            raise HealingError("Healing nemoguć, mrtav si!")     
         
        self.health += kolicina
        if self.health >= self.max_health:
            print("Health je na max")
            self.health = self.max_health
        else:
            print(f"Health je povećan za {kolicina}")
        
    def oduzmi_health(self, kolicina):
        self.health -= kolicina
        if self.health <= 0:
            self.health = 0
            print("You died!")
       
    def dodaj_hunger(self, kolicina):
        self.hunger += kolicina
        if self.hunger >= self.max_hunger:
            print("Hunger je na max")
            self.hunger = self.max_hunger
        else:
            print(f"Hunger je povećan za {kolicina}")