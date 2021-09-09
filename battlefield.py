from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self, name):
        self.name = name
        self.display_welcome()

        fleet = Fleet()
        print(fleet)
        print("hello")

    def run_game(self):
        # Master function. Will call other functions here.
        pass

    def display_welcome(self):
        user_input = input(
            "Welcome to Back to the Future. Are you ready to begin? type: 'yes or no'")
        if(user_input.upper() == "yes".upper()):
            self.run_game()
        else:
            self.display_welcome()

    def battle(self):
        # logic for game goes here
        pass

    def display_fleet(self, list):
        for object in list:
            self.dino_turn(object)

    def dino_turn(self, robot):
        self.show_dino_opponents(robot)

    def show_dino_opponents(self):

        print(object.name + "Current Health: " + object.health)

    def show_robo_opponents(self):
        # display dinos
        pass

    def display_winner(self):
        pass
