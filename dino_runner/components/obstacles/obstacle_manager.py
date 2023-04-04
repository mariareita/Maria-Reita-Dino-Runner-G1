import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus_large import LargeCactus
from dino_runner.components.obstacles.cactus_small import SmallCactus
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def generate_obstacles(self):
        obstacles = [LargeCactus(), SmallCactus(), Bird()]
        return obstacles[random.randint(0, 2)]

    def update(self, game):
        if not self.obstacles:    #len(self.obstacles) == 0
            self.obstacles.append(self.generate_obstacles())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)