from pygame import *

#contains list of layers and enemies and methods related to them
class Level():
    def __init__(self):
        self.layer_list = []
        self.enemy_list = []

    def get_all_tiles(self): #joins tiles from all layers
        all_tiles = []
        for layer in self.layer_list:
            all_tiles += layer.tile_list
        return all_tiles

    def get_collidable_tiles(self): #joins tiles from all collidable layers
        collidable_tiles = []
        for layer in self.layer_list:
            if layer.collidable:
                collidable_tiles += layer.tile_list
        return collidable_tiles


    