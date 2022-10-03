import math

import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RED_LIGHT = (200, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GREEN = (104, 232, 138)
BLUE = (0, 0, 255)

DEG_TO_RAD = 0.017453292519943295

class Drawner:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 800
        self.ticks = pygame.time.get_ticks()
        self.last_frame_ticks = 0
        self.delta_time = (self.ticks - self.last_frame_ticks) / 1000.0

        self.ventilador_angle = 0

        self.ball_x = 0
        self.ball_y = 0

        self.update_func = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        pass

    def on_loop(self):
        self.ticks = pygame.time.get_ticks()
        self.delta_time = (self.ticks - self.last_frame_ticks) / 1000.0
        self.last_frame_ticks = self.ticks

        self.ventilador_angle += self.delta_time * 2

        if self.update_func:
            self.update_func()

    def on_render(self):
        self._display_surf.fill(WHITE)

        # DIBUJO EN RECTANGULO
        pygame.draw.rect(self._display_surf, LIGHT_BLUE, (
            self.width/2 - 50, self.height/2 - (450 / 2), 100, 450
        ))

        # DIBUJAR TARJET
        pygame.draw.circle(self._display_surf, GREEN, (self.width/2 - 10, self.height/2), 20)

        # DIBUJAR VENTILADOR
        offset_x = (self.width / 2)
        offset_y = (self.height / 2) + 270

        scale = 70

        x1 = math.cos(self.ventilador_angle) * scale
        y1 = math.sin(self.ventilador_angle) * scale

        x2 = math.cos((90 * DEG_TO_RAD) + self.ventilador_angle) * scale
        y2 = math.sin((90 * DEG_TO_RAD) + self.ventilador_angle) * scale

        x3 = math.cos((180 * DEG_TO_RAD) + self.ventilador_angle) * scale
        y3 = math.sin((180 * DEG_TO_RAD) + self.ventilador_angle) * scale

        x4 = math.cos((270 * DEG_TO_RAD) + self.ventilador_angle) * scale
        y4 = math.sin((270 * DEG_TO_RAD) + self.ventilador_angle) * scale

        pygame.draw.polygon(self._display_surf, RED, (
            (offset_x + x1, offset_y + y1),
            (offset_x + x2, offset_y + y2),
            (offset_x + x3, offset_y + y3),
            (offset_x + x4, offset_y + y4),
        ))

        # DIBUJAR BOLA
        pygame.draw.circle(self._display_surf, RED_LIGHT, ((self.width / 2 - 10) + self.ball_x,
                                                       (self.height / 2) - self.ball_y), 20)

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
