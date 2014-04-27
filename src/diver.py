import pygame


class Diver(pygame.sprite.Sprite):
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
        self.mask = pygame.mask.from_surface(self.surface)
        self.mask.fill()
        print(self.mask.count())

        self.x_speed = 0
        self.y_speed = 0

        # set up self.rect
        self._move(0, 0)

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
        self.rect = (int(self.centre_coords[0] - (self.surface.get_width() / 2)),
                     int(self.centre_coords[1] - (self.surface.get_height() / 2)))

    def bounce(self, collision_mask):
        # bounce off a given collision mask

        # simplistic approach: reverse speed completely and move one tick
        self.x_speed *= -1
        self.y_speed *= -1

        self.move()

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
