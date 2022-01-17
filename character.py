from pygame import *
from pygame.sprite import Sprite
import os

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2

class Character(Sprite):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):

        player_image = image.load(os.path.join('Assets', 'playerSprite1.png')) 
        self.image = transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.position = position
        self.momentum = momentum
        self.rect = self.image.get_rect() 
    
    def apply_momentum(self):
        self.momentum[1] += 0.05 #momentum y, gravity
        self.position[0] += self.momentum[0] #position x and momentum x
        self.position[1] += self.momentum[1]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        
    def player_controls(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.momentum[0] -= 0.1
        if keys_pressed[K_RIGHT]:
            self.momentum[0] += 0.1
        if keys_pressed[K_SPACE]:
            self.momentum[1] -= 0.3