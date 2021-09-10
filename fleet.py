from robot import Robot


class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()

    # Below is where 3 Robots were instantiated and added to a list.

    def create_fleet(self):
        robot_1 = Robot("Dak")
        robot_2 = Robot("Greaser")
        robot_3 = Robot("Mugsy")

        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)
