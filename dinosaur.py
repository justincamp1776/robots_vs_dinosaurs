

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        damage = (robot.weapon.attack_power / 10) * 2
        robot.health = robot.health - damage
        print(f"{robot.name}'s health is {robot.health}")
