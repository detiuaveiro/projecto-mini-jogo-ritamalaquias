from pygame import *
from character import Character
from enums import PlayerState

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2 #image size with 200% scale
MAX_MOMENTUM = 2.5
class Player(Character):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0], score = 0):
        self.score = score
        self.state = PlayerState.normal
        super().__init__('playerSprite1.png', PLAYER_WIDTH, PLAYER_HEIGHT, position, momentum) #from Character class

    #adds momentum according to key pressed
    def player_controls(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.momentum[0] -= 0.1
        if keys_pressed[K_RIGHT]:
            self.momentum[0] += 0.1
        if keys_pressed[K_SPACE]:
            self.momentum[1] -= 0.3