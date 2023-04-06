from pygame import Surface
from pygame.sprite import Sprite
import pygame
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE
from dino_runner.utils.text import draw_message

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    POS_Y_DUCK = 345
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING[0]
        self.step = 0
        self.action = DINO_RUNNING
        self.position()
        self.jump_velocity = self.JUMP_VELOCITY
        self.power_up_time_up = 0
        self.img_run = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.img_duck = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.img_jump = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}

    def position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()
        
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_SPACE]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def run(self):
        #self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.image = self.img_run[self.type][self.step // 5]
        self.position()
        self.step += 1

    def jump(self):
        self.image = self.img_jump[self.type]
        self.rect.y -= self.jump_velocity * 4 #in this line we are subtracting at speed by 4
        self.jump_velocity -= 0.8 #control it up and down

        if self.jump_velocity < -self.JUMP_VELOCITY:    #when it is less than -8.5 be updated 
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = self.img_duck[self.type][self.step // 5]
        self.position()
        self.rect.y = self.POS_Y_DUCK
        self.step += 1
        
    def dead(self, image):
        self.image = image

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = (power_up.start_time + power_up.duration / 1000)

    #def draw_power_up(self, screen):
        #if self.type != DEFAULT_TYPE:
            #time_up_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            #if time_up_show >= 0:
                #draw_message(f"{self.type.capitalize()} enabled for {time_up_show} seconds.", screen, font_size=18, pos_y_center=40)
            #else:
                #self.type = DEFAULT_TYPE
                #self.power_up_time_up = 0
