import pygame
import diver
import background
import rock


class Game(object):
    def __init__(self):
        self.display = pygame.display
        self.clock = pygame.time.Clock()
        self.fps = 50
        self.quit = False
        self.pause = False
        self.dimensions = (500, 700)

        self.display.set_mode(self.dimensions)

        self.entities = []
        self.init_entities()
        self.surface = self.display.get_surface()

    def init_entities(self):
        self.diver = diver.Diver((self.dimensions[0] / 2, self.dimensions[1] / 2))
        self.bg = background.Background(self.dimensions)
        self.rocks = rock.Rock(self.dimensions)

        rock.create_rocks(self.rocks)

        self.entities = [self.bg, self.diver, self.rocks]

    def redraw_entities(self):
        for entity in self.entities:
            entity.draw(self.surface)

    def move_diver(self):
        pressed_keys = pygame.key.get_pressed()

        self.diver.move(left=pressed_keys[pygame.K_a],
                        right=pressed_keys[pygame.K_d],
                        up=pressed_keys[pygame.K_w],
                        down=pressed_keys[pygame.K_s])

        if self.rocks.mask.overlap(self.diver.mask, self.diver.rect):
            self.diver.bounce(self.rocks.mask, overlap_point)

    def background_scrolling(self):
        pressed_keys = pygame.key.get_pressed()
        left, right, up, down = 0, 0, 0, 0

        if pressed_keys[pygame.K_w]:
            up = 1
        if pressed_keys[pygame.K_s]:
            down = 1
        if pressed_keys[pygame.K_a]:
            left = 1
        if pressed_keys[pygame.K_d]:
            right = 1

        self.bg.move(left=left, right=right, up=up, down=down)

    def tick(self):
        self.process_events()

        self.background_scrolling()
        self.move_diver()

        self.redraw_entities()

        self.display.update()
        self.clock.tick(self.fps)

    def keyboard_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            self.quit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.pause = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                self.keyboard_event(event)

    def running(self):
        return not self.quit
