from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("T-rex", 90)
        dino_2 = Dinosaur("Raptor", 85)
        dino_3 = Dinosaur("Terodactyl", 70)

        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)


# herd = Herd()
# print("hello")
