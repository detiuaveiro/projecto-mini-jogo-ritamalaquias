from pygame import *
from pygame.sprite import Sprite
import os #helps defining path for images in case it uses different operating systems

BOUNCE_INTENSITY = 1.0
MAX_MOMENTUM = 2.5

class Character(Sprite):
    def __init__(self, character_image, width, height, position = [0.0, 0.0], momentum = [0.0, 0.0]):      
        self.position = position
        self.momentum = [momentum[0], momentum[1]] #necessary to force momentum to be a instance variable: alternative (self.momentum = momentum) won't work 
        self.character_image = image.load(os.path.join('Assets', character_image)) 
        self.image = transform.scale(self.character_image, (width, height))
        self.rect = self.image.get_rect()

        self.apply_momentum() #to apply initial position so that we can use the x and y rect coordinates
        
    #limits maximum momentum so that the character won't get super sonic
    def apply_momentum(self):
        if self.momentum[0] > MAX_MOMENTUM: #right
            self.momentum[0] = MAX_MOMENTUM
        if self.momentum[0] < MAX_MOMENTUM*-1: #left
            self.momentum[0] = MAX_MOMENTUM*-1
        if self.momentum[1] < MAX_MOMENTUM*-1: #up
            self.momentum[1] = MAX_MOMENTUM*-1

        self.position[0] += self.momentum[0] #position x and momentum x
        self.position[1] += self.momentum[1]
        #rect is where the sprite position is defined in x and y
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    #TO DO: fix bounce
    def bounce_horizontal(self):
        self.momentum[0] *= -BOUNCE_INTENSITY

    def bounce_vertical(self):
        self.momentum[1] *= -BOUNCE_INTENSITY

    def add_friction(self):
        self.momentum[0] -= 0.03
        self.momentum[1] -= 0.03

    def add_gravity(self):
        self.momentum[1] += 0.05 #momentum y, gravity
    
    def apply_window_collision(self, height, width):
        #collision window bottom
        if self.rect.bottom > height and self.momentum[1] > 0.0:
            self.rect.bottom = height
            self.momentum[1] = 0.0  
        #collision window top
        if self.rect.top < 0 and self.momentum[1] < 0.0:
            self.rect.top = height
            self.momentum[1] = 0.0

        #to left
        if self.rect.left > width and self.position[0] > width:
            self.position[0] = 0.0

        #to right
        if self.rect.right < 0 and self.position[0] < 0.0:
            self.position[0] = width

    