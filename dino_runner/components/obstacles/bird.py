

import random
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        random_img = random.randint(0, 1)
        super().__init__(BIRD[random_img], pos_y= random.randint(100,300))
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = BIRD[0] if self.step <= 4 else BIRD[1]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 8:
            self.step = 0