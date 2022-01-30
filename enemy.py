from pygame import *
from character import Character

ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2 #image size with 200% scale
class Enemy(Character):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):
        super().__init__('enemySprite1.png', ENEMY_WIDTH, ENEMY_HEIGHT, position, momentum) #from Character class

    #enemy tries to reach player by checking his position relative to the player, using the rect coordinates
    def apply_ai(self, player):
        if self.rect.centerx < player.rect.centerx:
            self.momentum[0] += 0.05
        if self.rect.centerx > player.rect.centerx:
            self.momentum[0] -= 0.05
        if self.rect.centery > player.rect.centery:
            self.momentum[1] -= 0.1        
        

    # def player_controls(self):
    #     keys_pressed = key.get_pressed()
    #     #limits maximum momentum so that the player won't get super sonic
    #     if keys_pressed[K_LEFT] and self.momentum[0] > (MAX_MOMENTUM*-1):
    #         self.momentum[0] -= 0.1
    #     if keys_pressed[K_RIGHT] and self.momentum[0] < MAX_MOMENTUM:
    #         self.momentum[0] += 0.1
    #     if keys_pressed[K_SPACE] and self.momentum[1] > (MAX_MOMENTUM*-1):
    #         self.momentum[1] -= 0.3