from pygame import *
from pygame.sprite import Sprite
import os

TILE_WIDTH, TILE_HEIGHT = 8*2, 8*2

class Tile(Sprite):
    def __init__(self, position = [0.0, 0.0]):
        tile_image =  image.load(os.path.join('Assets', 'tileSprite1.png'))
        self.image = transform.scale(tile_image, (TILE_WIDTH, TILE_HEIGHT)) 
        self.position = position
        #self.rect = self.image.get_rect()

