from pygame import *
from character import Character

ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2 #image size with 200% scale
class Enemy(Character):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        super().__init__('enemySprite1.png', ENEMY_WIDTH, ENEMY_HEIGHT, position, momentum) #from Character class
