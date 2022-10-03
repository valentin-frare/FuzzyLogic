import random
import threading

from Scripts.data import Data
from Scripts.utils import Utils


class System:
    def __init__(self, game):
        self.const_y = random.randrange(150, 450)
        self.data = Data(self.const_y)
        self.game = game

        self.game.update_func = self.update

    def set_caos(self):
        self.data.caos = random.randrange(-3, 3)

    def update(self):
        self.data = Utils.fuzzification(self.data)
        self.set_caos()
        self.data.vel_y += ((self.data.gravedad - self.data.ventilador + self.data.caos) * .01)
        self.data.pos_y += self.data.vel_y
        self.data.y = self.data.pos_y

        self.game.ball_y = self.data.y

