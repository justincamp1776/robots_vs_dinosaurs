from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.run_game()

    # This initiates the battle.

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to robots vs dinosaurs!")

    #  The blocks of code below are responsible for keeping the attacks
    #  going until the battle is complete.

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

    # This displays the winner

    def display_winner(self):
        if len(self.fleet.robots) != 0:
            print("Robots win again!")
        else:
            print("Dinosaurs with the come back!")
