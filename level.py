from pygame import *
from pygame.sprite import Sprite
import os
from layer import Layer
class Level():
    def __init__(self):
        self.layer_list = []
        self.enemy_list = []

    def get_all_tiles(self):
        all_tiles = []
        for layer in self.layer_list:
            all_tiles += layer.tile_list
        return all_tiles

    def get_collidable_tiles(self):
        collidable_tiles = []
        for layer in self.layer_list:
            if layer.collidable:
                collidable_tiles += layer.tile_list
        return collidable_tiles


    