from dinosaur import Dinosaur
from fleet import Fleet
from weapon import Weapon

# why is fleet imported?


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Scar-XL", 82)

    def attack(self, dinosaur):
        self.damage = (self.weapon.attack_power / 10) * 2
        dinosaur.health = dinosaur.health - self.damage
