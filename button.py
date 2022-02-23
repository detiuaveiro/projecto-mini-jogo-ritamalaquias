from msilib.schema import Class
from tkinter import Button
from pygame import *
from pygame.sprite import Sprite
import os

class Button(Sprite):
    def __init__(self, image, position): 
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.clicked = False

    def draw(self):
        #draws button
        #screen.blit(self.image, self.rect)
        pass