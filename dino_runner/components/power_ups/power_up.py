import random
from pygame import Surface
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image: Surface, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(150, 200)

        self.duration = random.randint(3, 6)
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()
    
    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))