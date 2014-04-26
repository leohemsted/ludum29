class Entity(object):
    def __init__(self):
        self.collisions_on = True
        self.resource_dir = '../resources/'
        pass

    def is_collidable(self):
        return self.collisions_on
        
    def draw(self, surface):
        pass