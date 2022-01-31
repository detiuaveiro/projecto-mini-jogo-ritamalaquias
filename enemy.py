from pygame import *
from character import Character
from enums import EnemyType, EnemyState

ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2 #image size with 200% scale

class Enemy(Character):
    #Dictionary with scores defined for each enemy type
    enemy_type_score_value = {EnemyType.easy: 100, EnemyType.normal: 200, EnemyType.hard: 500} 
    #Enemy class takes enemy type and position arguments
    def __init__(self, enemy_type, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        self.state = EnemyState.chasing
        self.enemy_type = enemy_type
        super().__init__('enemySprite1.png', ENEMY_WIDTH, ENEMY_HEIGHT, position, momentum) #from Character class

    #enemy tries to reach player by checking his position relative to the player, using the rect coordinates
    def apply_ai(self, player):
        if self.rect.centerx < player.rect.centerx: 
            self.momentum[0] += 0.05 #right
        if self.rect.centerx > player.rect.centerx:
            self.momentum[0] -= 0.05 #left
        if self.rect.centery > player.rect.centery: 
            self.momentum[1] -= 0.1 #up
   