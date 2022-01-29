from pygame import *
from character import Character

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2 #image size with 200% scale
MAX_MOMENTUM = 2.5
class Player(Character):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        super().__init__('playerSprite1.png', PLAYER_WIDTH, PLAYER_HEIGHT, position, momentum) #from Character class

    def player_controls(self):
        keys_pressed = key.get_pressed()
        #limits maximum momentum so that the player won't get super sonic
        if keys_pressed[K_LEFT] and self.momentum[0] > (MAX_MOMENTUM*-1):
            self.momentum[0] -= 0.1
        if keys_pressed[K_RIGHT] and self.momentum[0] < MAX_MOMENTUM:
            self.momentum[0] += 0.1
        if keys_pressed[K_SPACE] and self.momentum[1] > (MAX_MOMENTUM*-1):
            self.momentum[1] -= 0.3