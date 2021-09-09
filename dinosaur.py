

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot, list_of_robos):
        damage = (robot.weapon.attack_power / 4)
        robot.health = robot.health - damage
        if robot.health <= 0:
            list_of_robos.pop(0)
        print(f"{robot.name}'s health is {robot.health}")
