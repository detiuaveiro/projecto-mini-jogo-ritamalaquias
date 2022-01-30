from enum import Enum
from pygame import *
from character import Character
from enums import EnemyType, EnemyState

ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2 #image size with 200% scale

class Enemy(Character):

    enemy_type_score_value = {EnemyType.easy: 100, EnemyType.normal: 200, EnemyType.hard: 500}

    def __init__(self, enemy_type, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        self.state = EnemyState.chasing
        #self.score_value = score_value
        self.enemy_type = enemy_type
        super().__init__('enemySprite1.png', ENEMY_WIDTH, ENEMY_HEIGHT, position, momentum) #from Character class

    #enemy tries to reach player by checking his position relative to the player, using the rect coordinates
    def apply_ai(self, player):
        if self.rect.centerx < player.rect.centerx:
            self.momentum[0] += 0.05
        if self.rect.centerx > player.rect.centerx:
            self.momentum[0] -= 0.05
        if self.rect.centery > player.rect.centery:
            self.momentum[1] -= 0.1
   