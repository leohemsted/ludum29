import pygame
from entity import Entity


class Diver(Entity):
    def __init__(self, start_loc):
        super().__init__()

        # multiplier of speed falling off when
        self.speed_degradation = 0.1
        self.halt_val = 0.1

        # how far your speed changes in one tick
        self.speed_modifier = 1

        self.centre_coords = start_loc

        # image = pygame.image.load(self.resource_dir + 'diver.png').convert()
        # image_size = image.get_size()

        self.surface = pygame.Surface((60, 40))
        self.surface.fill(pygame.Color('red'))

        self.x_speed = 0
        self.y_speed = 0

    def move(self, left=False, right=False, up=False, down=False):
        # call this once per tick! Always!

        # degrade speed
        self.x_speed = self.x_speed * (1 - self.speed_degradation)
        self.y_speed = self.y_speed * (1 - self.speed_degradation)

        if abs(self.x_speed) < self.halt_val:
            self.x_speed = 0
        if abs(self.y_speed) < self.halt_val:
            self.y_speed = 0

        self.x_speed += self.speed_modifier * (int(right) - int(left))
        self.y_speed += self.speed_modifier * (int(down) - int(up))

        self._move(self.x_speed, self.y_speed)

    def _move(self, x, y):
        self.centre_coords = tuple([self.centre_coords[0] + x, self.centre_coords[1] + y])

    def draw(self, surface):
        top_left = (self.centre_coords[0] - (self.surface.get_width() / 2),
                    self.centre_coords[1] - (self.surface.get_height() / 2))
        surface.blit(self.surface, top_left)
