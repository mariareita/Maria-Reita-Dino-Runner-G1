from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import SUN  


class Sun(Obstacle):
    def __init__(self):
        self.image = SUN
        self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (920, 30))