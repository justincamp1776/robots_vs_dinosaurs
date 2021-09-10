from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Scar-XL", 80)

    #  This method decrements opponents health and keeps the object
    # in battle until the object is out of health.

    def attack(self, dinosaur, list_of_dinos):
        damage = (dinosaur.attack_power / 4)
        dinosaur.health = dinosaur.health - damage
        if dinosaur.health <= 0:
            list_of_dinos.pop(0)
        print(f"{dinosaur.name}'s health is {dinosaur.health}")
