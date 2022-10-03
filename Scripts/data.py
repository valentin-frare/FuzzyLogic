import random


class Data:
    def __init__(self, const_y):
        self.gravedad = 9.81
        self.pos_y = const_y
        self.vel_y = 0
        self.x = 400
        self.y = const_y
        self.obj_y = 0
        self.ventilador = random.randrange(1, 120)
        self.caos = 0