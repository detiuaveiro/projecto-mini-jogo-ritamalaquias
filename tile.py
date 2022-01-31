from pygame import *
from pygame.sprite import Sprite
import os

TILE_SIZE = 8*2

class Tile(Sprite):
    def __init__(self, image_file, position = (0.0, 0.0)):
        tile_image =  image.load(os.path.join('Assets', image_file))
        self.image = transform.scale(tile_image, (TILE_SIZE, TILE_SIZE)) 
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]