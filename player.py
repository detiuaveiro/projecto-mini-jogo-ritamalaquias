from pygame import *
from character import Character
from enums import PlayerState

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2 #image size with 200% scale
MAX_MOMENTUM = 2.5

class Player(Character):
    player_instance = None
    #singleton implementation
    @staticmethod
    def get_instance(position = [0.0, 0.0], momentum = [0.0, 0.0], score = 0):
        if Player.player_instance is None:
            Player(position, momentum, score)
        return Player.player_instance

    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0], score = 0):
        self.score = score
        self.state = PlayerState.normal
        Player.player_instance = self 
        super().__init__('playerSprite1.png', PLAYER_WIDTH, PLAYER_HEIGHT, position, momentum) #from Character class

    #adds momentum according to key pressed
    def jump(self):
        self.momentum[1] -= 0.3
    def right(self):
        self.momentum[0] += 0.1
    def left(self):
        self.momentum[0] -= 0.1

   