from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("T-rex", 92)
        dino_2 = Dinosaur("Raptor", 79)
        dino_3 = Dinosaur("Terodactyl", 65)

        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)


# herd = Herd()
# print("hello")
