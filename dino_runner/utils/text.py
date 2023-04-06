import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0, 0, 0)
half_screen_height = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2

def get_score_element(poins):
    font = pygame.font.Font("freesansbold.ttf", 22)
    text = font.render(f"score: {poins}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (860, 35)
    return text, text_rect

FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30
FONT_STYLE = "freesansbold.ttf"

def draw_message(message, screen, font_color = FONT_COLOR, font_size = FONT_SIZE, pos_y_center = SCREEN_HEIGHT // 2, pos_x_center = SCREEN_WIDTH // 2,):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text,text_rect)