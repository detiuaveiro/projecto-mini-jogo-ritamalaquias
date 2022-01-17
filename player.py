from turtle import position
from pygame import *
from pygame.sprite import Sprite
import os

from character import Character

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2 #image size with 200% scale


class Player(Character):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        player_image = image.load(os.path.join('Assets', 'playerSprite1.png')) 
        self.image = transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        super().__init__(position, momentum) #from Character class

    def player_controls(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.momentum[0] -= 0.1
        if keys_pressed[K_RIGHT]:
            self.momentum[0] += 0.1
        if keys_pressed[K_SPACE]:
            self.momentum[1] -= 0.3