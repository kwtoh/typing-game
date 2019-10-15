import pygame
from pygame.locals import *
from objects import Objects

START = 1
PLAYING = 2
GAMEOVER = 3

class GamePlay():
    def __init__(self, disp_surf):
        self._disp_surf = disp_surf
        self.game_objects = None
        self.last_add = 0
        self.add_timeout = 2000 # start with 2 seconds
        self.state = PLAYING

    def on_init(self):
        self.game_objects = Objects(self.width, self.height)

    def on_execute(self):
        self.on_init()
        while (self.state == PLAYING):
            self.on_loop()
            self.on_render()
            self.on_check_event()
            self.check_keyhit()
            self.fpsclock.tick(self.fps)
        pygame.event.clear()
        return self.score if self.state else -1

