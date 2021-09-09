from robot import Robot
from dinosaur import Dinosaur
from battlefield import Battlefield


test_dino = Dinosaur("dino", 80)

test_robo = Robot("robo")


print(test_robo.health)
test_dino.attack(test_robo)
