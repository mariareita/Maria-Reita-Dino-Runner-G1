import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.kamel import Kamel
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import HAMMER_TYPE


class ObstacleManager:
    generate_obstacles =[Cactus, Bird, Kamel]

    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:    #len(self.obstacles) == 0
            obstacle = random.choice(self.generate_obstacles)
            self.obstacles.append(obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect):
                if player.type == HAMMER_TYPE:
                    self.obstacles.pop()
                else:
                    on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles = []