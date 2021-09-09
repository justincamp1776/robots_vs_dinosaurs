from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_1 = Dinosaur("Rex", 90)
        dino_2 = Dinosaur("Velo", 79)
        dino_3 = Dinosaur("Tony", 75)

        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)
