import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.components.sun import Sun

from dino_runner.utils.constants import BG, CLOUD, DEAD, GAME_OVER, HAMMER_TYPE, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, START, TITLE, FPS
from dino_runner.utils.text import draw_message


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.sun = Sun()
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def play(self):
        self.playing = True
        self.reset()
        self.obstacle_manager.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.obstacle_manager.reset()
        self.power_up_manager.reset()
        self.score.reset()
        self.game_speed = 20

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.score.score, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.color()
        self.draw_background()
        self.player.draw(self.screen)
        self.score.draw(self.screen)
        self.sun.draw(self.screen)
        self.cloud()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.draw_power_up(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count:
            self.screen.fill((215, 189, 226))
            self.screen.blit(GAME_OVER, (360,180))
            self.screen.blit(RESET, (500,240))
            draw_message("PRESS ANT KEY RESTART", self.screen, pos_y_center= half_screen_height + 50)
            draw_message(f"Your score: {self.score.score}", self.screen, pos_y_center= half_screen_height + 100)
            draw_message(f"Death count: {self.death_count}", self.screen, pos_y_center= half_screen_height + 150)
        else:
            self.screen.fill((215, 189, 226))
            draw_message("START", self.screen, pos_y_center= half_screen_height + 200)
            self.screen.blit(START, (300, 225))

        pygame.display.flip()
        self.menu_events()

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()

    def on_death(self):
        if self.player.type != SHIELD_TYPE or HAMMER_TYPE:
            self.player.dead(DEAD)
            self.draw()
            self.playing = False
            self.death_count += 1
            pygame.time.delay(500)

    def cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1020, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1070, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2030, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +900, self.y_pos_bg -120))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3000, self.y_pos_bg -189))

    def color(self):
        if self.score.score == 1:
            self.colors = 0
        self.colors += 1

        if self.colors >= 200:
            self.screen.fill((252, 243, 207))
            if self.colors >= 400:
                self.colors = 0
        else:
            self.screen.fill((208, 236, 231))