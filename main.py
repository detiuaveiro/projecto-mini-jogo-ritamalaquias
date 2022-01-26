import pygame
import os #helps defining path for images in case it uses different operating systems
#from character import Character
from player import Player
from tile import Tile

#window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Fight") #window name

BLACK = (0, 0, 0) 
FPS = 60


ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2

#for stars in background
# TO DO: stars_img = pygame.image.load()
#make a class for platform, load image and define where tiles should go

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemySprite1.png'))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))

player = Player([100.0, 100.0], [0.01, 0.01])
tile = Tile([10.0, 10.0])

#main program
def main():
    enemy = pygame.Rect(700, 200, ENEMY_WIDTH, ENEMY_HEIGHT)
    
    clock = pygame.time.Clock()
    #game loop
    run = True
    while run:
        clock.tick(FPS) #runs the while loop at the frames defined
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #player.y += 1
        
        player.player_controls()
        player.apply_momentum()
        draw_window(player, enemy, tile)

    pygame.quit()

#methods
def draw_window(player, enemy, tile):
    WIN.fill(BLACK)
    WIN.blit(player.image, (player.position[0], player.position[1])) #when you want to draw a surface onto a screen
    WIN.blit(ENEMY, (enemy.x, enemy.y))
    WIN.blit(tile.image, (tile.position[0], tile.position[1]))
    pygame.display.update() #refreshes the screen



if __name__ == "__main__": #main file to run
    main()