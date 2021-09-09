

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        damage = robot.health - (self.weapon.attack_power / 10) * 1.5
