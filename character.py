from pygame import *
from pygame.sprite import Sprite
import os
class Character(Sprite):
    def __init__(self, character_image, width, height, position = [0.0, 0.0], momentum = [0.0, 0.0]):      
        self.position = position
        self.momentum = momentum
        self.character_image = image.load(os.path.join('Assets', character_image)) 
        self.image = transform.scale(self.character_image, (width, height))
        self.rect = self.image.get_rect() 
        
    def apply_momentum(self):
        self.position[0] += self.momentum[0] #position x and momentum x
        self.position[1] += self.momentum[1]
        #rect is where the sprite position is defined in x and y
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        
    def add_gravity(self):
        self.momentum[1] += 0.05 #momentum y, gravity
    
    def apply_window_collision(self, height):
        #colli sion window bottom
        if self.rect.bottom > height and self.momentum[1] > 0.0:
            self.rect.bottom = height
            self.momentum[1] = 0.0  
        #collision window top
        if self.rect.top < 0 and self.momentum[1] < 0.0:
            self.rect.top = height
            self.momentum[1] = 0.0