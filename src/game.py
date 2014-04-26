import pygame


class Game(object):
    def __init__(self):
        self.display = pygame.display
        self.clock = pygame.clock
        self.fps = 50
        self.quit = False

    def tick(self):
        self.display.update()
        self.clock.tick(self.fps)

    def keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            # go fuckin mental
            pass
        elif event.type == pygame.KEYUP:
            # stop goin fuckin mental
            pass

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                self.keyboard_event(event)

    def game_running(self):
        return self.quit