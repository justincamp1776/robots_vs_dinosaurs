from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Scar-XL", 82)

    def attack(self, dinosaur):
        damage = (dinosaur.attack_power / 10) * 2
        dinosaur.health = dinosaur.health - damage
        print(f"{dinosaur.name}'s health is {dinosaur.health}")
