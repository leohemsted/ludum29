import pygame
import random


def create_rocks(bg):
    min_rocks = 10
    max_rocks = 12
    min_radius = 30
    max_radius = 100

    add_chance = 0.5

    remove_chance = 1 - add_chance

    options = [bg.add_area] * int(100 * add_chance) + [bg.remove_area] * int(100 * remove_chance)

    # constructs a random load of rocks or something
    bg_size = bg.get_size()

    # between 10 and 20 shapes
    for i in range(0, random.randint(min_rocks, max_rocks), 1):
        surface = pygame.Surface(bg.get_size())
        surface.fill(pygame.Color('black'))

        x = random.randint(0, bg_size[0])
        y = random.randint(0, bg_size[1])
        radius = random.randint(min_radius, max_radius)
        pygame.draw.circle(surface, pygame.Color('white'), (x, y), radius)
        random.choice(options)(surface)
    bg.recompute_alpha()


class Rock(pygame.sprite.Sprite):
    # actually this class is all rocks on screen. i think

    def __init__(self, screen_dimensions):
        super().__init__()

        image = pygame.image.load('../resources/rock_background.png').convert()
        image_size = image.get_size()

        # get the next highest area that covers the screen

        self.texture = pygame.Surface(screen_dimensions)

        for x in range(0, screen_dimensions[0], image_size[0]):
            for y in range(0, screen_dimensions[1], image_size[1]):
                self.texture.blit(image, (x, y))

        self.mask = pygame.mask.Mask(screen_dimensions)  # empty
        self.texture_mask = pygame.Surface(screen_dimensions)
        self.texture_mask.fill(pygame.Color('black'))

        # we'll want to move this if we do any scrolling of any sort later on, also
        # then we'd probably need to do some mental shit involving the marks and
        # the shapes etc etc, lets just leave that alone for a while
        self.rect = (0, 0)

    def get_size(self):
        return self.texture.get_size()

    def add_area(self, surface):
        # removes area as rock, based on greyscale value of surface provided
        self.texture_mask.blit(surface, (0, 0), None, pygame.BLEND_MAX)

    def remove_area(self, surface):
        # removes area as rock, based on greyscale value of surface provided (white is kept)
        # (filled in on surface = gone on Rock)
        self.texture_mask.blit(surface, (0, 0), None, pygame.BLEND_SUB)

    def recompute_alpha(self):
        self.surface = self.texture.copy()
        # self.surface.set_colorkey(pygame.Color('black'))
        self.surface.blit(self.texture_mask, (0, 0), None, pygame.BLEND_MULT)
        self.surface.set_colorkey(pygame.Color('black'))
        self.mask = pygame.mask.from_surface(self.surface)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
