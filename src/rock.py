import pygame
from entity import Entity


class Rock(Entity):
    # actually this class is all rocks on screen. i think

    def __init__(self, screen_dimensions):
        super().__init__()

        image = pygame.image.load(self.resource_dir + 'rock_background.png').convert()
        image_size = image.get_size()

        # get the next highest area that covers the screen

        self.texture = pygame.Surfaces(screen_dimensions)

        for y in range(0, screen_dimensions[0], image_size[0]):
            for x in range(0, screen_dimensions[1], image_size[0]):
                self.texture.blit(image, (x, y))

        self.mask = pygame.mask.Mask(screen_dimensions)

    def add_area(self, surface):
        self.mask.draw(pygame.mask.from_surface(surface))
        # adds area as rock

    def remove_area(self, surface):
        # removes area as rock
        self.mask.erase(pygame.mask.from_surface(surface))

    def draw(self, surface):
        surface.blit()
        pass
