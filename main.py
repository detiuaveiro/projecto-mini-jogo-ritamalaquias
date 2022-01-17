import pygame
import os #helps defining path for images in case it uses different operating systems
from character import Character
from player import Player

#window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Fight") #window name

BLACK = (0, 0, 0) 
FPS = 60


ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2


ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemySprite1.png'))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))

player = Player([100.0, 100.0], [0.01, 0.01])

#main program
def main():
    enemy = pygame.Rect(700, 200, ENEMY_WIDTH, ENEMY_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #runs the while loop at the frames defined
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #player.y += 1
        
        player.player_controls()
        player.apply_momentum()
        draw_window(player, enemy)

    pygame.quit()

#methods
def draw_window(player, enemy):
    WIN.fill(BLACK)
    #fazer sprite e depois update
    WIN.blit(player.image, (player.position[0], player.position[1])) #when you want to draw a surface onto a screen
    WIN.blit(ENEMY, (enemy.x, enemy.y))
    pygame.display.update() #refreshes the screen



if __name__ == "__main__": #main file to run
    main()