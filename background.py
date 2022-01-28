from pygame import *
from pygame.sprite import Sprite
import os

TILE_SIZE = 8*2

class Background(Sprite):
    def __init__(self, grid): 
        self.tile_list = []
        #images for background
        big_yellow_star = image.load(os.path.join('Assets', 'bgSprite1.png'))
        yellow_star = image.load(os.path.join('Assets', 'bgSprite2.png'))
        medium_blue_star = image.load(os.path.join('Assets', 'bgSprite3.png'))
        small_yellow_star = image.load(os.path.join('Assets', 'bgSprite4.png'))
        blue_star = image.load(os.path.join('Assets', 'bgSprite5.png'))
        
        row_count = 0
        for row in grid:
            column_count = 0
            for background_tile in row:
                #could use a match-case statement, but it's only available in py 3.10+
                if background_tile == 0:
                    tile_sprite = Surface((TILE_SIZE, TILE_SIZE))
                    tile_sprite.fill((0,0,0)) #black
                if background_tile == 1:
                    tile_sprite = transform.scale(big_yellow_star, (TILE_SIZE, TILE_SIZE))
                if background_tile == 2:
                    tile_sprite = transform.scale(yellow_star, (TILE_SIZE, TILE_SIZE))
                if background_tile == 3:
                    tile_sprite = transform.scale(medium_blue_star, (TILE_SIZE, TILE_SIZE))
                if background_tile == 4:
                    tile_sprite = transform.scale(small_yellow_star, (TILE_SIZE, TILE_SIZE))
                if background_tile == 5: 
                    tile_sprite = transform.scale(blue_star, (TILE_SIZE, TILE_SIZE)) 
                                   
                self.build_tile(tile_sprite, column_count, row_count)
                column_count +=1
            row_count+=1

    def build_tile(self, tile_sprite, column, row_count):
        rect = tile_sprite.get_rect()
        rect.x = column * TILE_SIZE
        rect.y = row_count * TILE_SIZE
        background_tile = (tile_sprite, rect)
        self.tile_list.append(background_tile)


