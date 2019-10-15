import pygame
from pygame.locals import *
from play import GamePlay

WIDTH = 640
HEIGHT = 400

STATE_START = 1
STATE_PLAYING = 2
STATE_GAMEOVER = 3

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class TypingTutor():
    def __init__(self):
        self.state = STATE_START
        self._running = True
        self.disp_surf = None
        self.size = self.width, self.height = WIDTH, HEIGHT
        

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Typing Tutor')
        self.disp_surf = pygame.display.set_mode(self.size)
        self.bigfont = pygame.font.Font('Consolas Bold.ttf', 32)
        return True if self.disp_surf else False

    def on_execute(self):
        if not self.on_init():
            self._running = False
        while self._running:
            self.on_render()
            self.on_check_event()
            self.on_loop()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def on_loop(self):
        if (self.state == STATE_PLAYING):
            # start game
            self.score = GamePlay(self.disp_surf).on_execute()
            if (self.score == -1):
                self._running = False
            self.state = STATE_GAMEOVER
        return

    def draw_text(self, text, color, coord):
        surf = self.bigfont.render("Typing Tutor", True, RED)
        rect = surf.get_rect()
        rect.center = (int(self.width/2), int(self.height/2))
        self.disp_surf.blit(surf, rect)

    def on_check_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False
                self.state = STATE_GAMEOVER
            elif event.type ==  pygame.locals.KEYUP:
                if self.state == STATE_GAMEOVER:
                    self.state = 1
                else:
                    self.state += 1

    def on_render(self):
        self.disp_surf.fill(BLACK)

        if self.state == STATE_START:
            text = "Typing Tutor"
        elif self.state == STATE_GAMEOVER:
            text = "Game Over"
        else:
            text = "Playing"

        self.draw_text(text, RED, (int(self.width/2), int(self.height/2)))
        pygame.display.flip()
        


if __name__ == "__main__":
    game = TypingTutor()
    game.on_execute()
