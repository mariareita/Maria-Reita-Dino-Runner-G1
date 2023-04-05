import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0, 0, 0)
half_screen_height = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2

def get_start_message(message):
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (half_screen_width, half_screen_height)
    return text, text_rect

def get_score_element(poins):
    font = pygame.font.Font("freesansbold.ttf", 22)
    text = font.render(f"score: {poins}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (1010, 35)
    return text, text_rect

def get_score(score):
    font = pygame.font.Font("freesansbold.ttf", 22)
    text = font.render(f"score: {score}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (600, 400)
    return text, text_rect

def get_final_message(message):
    font = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (550, 300)
    return text, text_rect

def get_number_deaths(deaths):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Deaths Count: {deaths}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (550, 350)
    return text, text_rect