from pygame import Surface
from pygame.sprite import Sprite
import pygame
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.step = 0
        self.action = DINO_RUNNING
        self.position()
        self.jump_velocity = self.JUMP_VELOCITY

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
            self.image = RUNNING[self.step // 5]
            self.position()
            self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4 #in this line we are subtracting at speed by 4
        self.jump_velocity -= 0.8 #control it up and down

        if self.jump_velocity < -self.JUMP_VELOCITY:    #when it is less than -8.5 be updated 
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.position()
        self.rect.y = self.POS_Y + 35
        self.step += 1
        

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))
