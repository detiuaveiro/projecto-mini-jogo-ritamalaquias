from pygame import *
from pygame.sprite import Sprite
from pygame.locals import *

from tile import Tile

TILE_SIZE = 8*2

class Layer(Sprite):
    def __init__(self, grid, assets_dict, collidable = False): 
        self.tile_list = []
        self.collidable = collidable

        #cycles through all rows and columns from the grid to build the tiles
        row_count = 0
        for row in grid:
            column_count = 0
            for tile in row:
                if tile == 0: #black tile
                    tile_sprite = Surface((TILE_SIZE, TILE_SIZE))
                    tile_sprite.fill((0,0,0))
                    self.tile_list.append((tile_sprite, tile_sprite.get_rect()))
                elif tile == 1: #alpha tile
                    tile_sprite = Surface((TILE_SIZE, TILE_SIZE))
                    tile_sprite.set_alpha(0)
                    self.tile_list.append((tile_sprite, tile_sprite.get_rect()))
                else:
                    tile_sprite = Tile(assets_dict[tile], (column_count * TILE_SIZE, row_count * TILE_SIZE))
                    self.tile_list.append((tile_sprite.image, tile_sprite.rect))

                column_count +=1
            row_count+=1
        