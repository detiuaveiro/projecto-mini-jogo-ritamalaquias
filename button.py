import pygame
from pygame import *
from pygame.sprite import Sprite
import os
from consts import Consts

const = Consts()
class Button(Sprite):
    def __init__(self, image, position): 
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.clicked = False
        
    def on_click(self):
        mouse_action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mousehover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #left click
                mouse_action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return mouse_action
    
    def draw(self): #need it separated in order to reuse button code for non interactive text
        #draws button
        const.WIN.blit(self.image, (self.position[0], self.position[1]))