from pygame import *
from pygame.sprite import Sprite

class Character(Sprite):
    def __init__(self, position = [0.0, 0.0], momentum = [0.0, 0.0]):      
        self.position = position
        self.momentum = momentum
        self.rect = self.image.get_rect() 
    
    def apply_momentum(self):
        self.momentum[1] += 0.05 #momentum y, gravity
        self.position[0] += self.momentum[0] #position x and momentum x
        self.position[1] += self.momentum[1]
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        
   