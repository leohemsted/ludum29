import pygame
import math
from entity import Entity


class Background(Entity):
    def __init__(self, screen_dimensions):
        super().__init__()

        self.collisions_on = False
        image = pygame.image.load(self.resource_dir + 'sea_background.png').convert()
        image_size = image.get_size()

        # get the next highest area that covers the screen
        width = screen_dimensions[0] + 1 + (math.ceil(screen_dimensions[0] / image_size[0]) *
                                            image_size[0])
        height = screen_dimensions[1] + 1 + (math.ceil(screen_dimensions[1] / image_size[1]) *
                                             image_size[1])

        self.surface = pygame.Surface((width, height))

        for y in range(0, width, image_size[0]):
            for x in range(0, width, image_size[0]):
                self.surface.blit(image, (x, y))

        self.texture_size = image_size
        self.top_left = (0 - round(image_size[0] / 2), 0 - round(image_size[1] / 2))

    def move(self, left=0, right=0, up=0, down=0):
        top_left = list(self.top_left)

        # flip round left and right deliberately here so it paralax's n shit
        top_left[0] += (left - right)
        top_left[1] += (down - up)

        if top_left[0] > 0:
            top_left[0] -= self.texture_size[0]
        if top_left[1] > 0:
            top_left[1] -= self.texture_size[1]
        if top_left[0] < (0 - self.texture_size[0]):
            top_left[0] += self.texture_size[0]
        if top_left[1] < (0 - self.texture_size[1]):
            top_left[1] += self.texture_size[1]

        self.top_left = tuple(top_left)

    def draw(self, surface):
        surface.blit(self.surface, self.top_left)
