from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to robots vs dinosaurs!")

    def battle(self):
        while len(self.fleet.robots) != 0 and len(self.herd.dinosaurs) != 0:
            self.dino_turn(
                self.herd.dinosaurs[0], self.fleet.robots[0], self.fleet.robots)
            self.robo_turn(
                self.fleet.robots[0], self.herd.dinosaurs[0], self.herd.dinosaurs)
        self.display_winner()

    def dino_turn(self, dino, robot, list_of_robos):
        dino.attack(robot, list_of_robos)

    def robo_turn(self, robot, dino, list_of_dinos):
        robot.attack(dino, list_of_dinos)

    def display_winner(self):
        if len(self.fleet.robots) != 0:
            print("Robots win again!")
        else:
            print("Dinosaurs with the come back!")
