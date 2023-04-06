from pygame.sprite import Sprite
from dino_runner.utils.text import get_score_element

class Score(Sprite):
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        score, score_rect = get_score_element(self.score)
        screen.blit(score, score_rect)

    def reset(self):
        self.score = 0