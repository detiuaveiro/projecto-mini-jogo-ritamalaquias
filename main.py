import pygame
import os #helps defining path for images in case it uses different operating systems

#window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Fight") #window name

BLACK = (0, 0, 0) 
FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 19*2, 27*2
ENEMY_WIDTH, ENEMY_HEIGHT = 17*2, 25*2

PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'playerSprite1.png')) 
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemySprite1.png'))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))

momentum_x, momentum_y = 0.0, 0.0
position_x, position_y = 100.0, 200.0 #float positions to help with physics calc

#main program
def main():
    player = pygame.Rect(position_x, position_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy = pygame.Rect(700, 200, ENEMY_WIDTH, ENEMY_HEIGHT)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #runs the while loop at the frames defined
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #player.y += 1
        
        player_controls()
        apply_momentum(player)
        draw_window(player, enemy)

    pygame.quit()

#methods
def draw_window(player, enemy):
    WIN.fill(BLACK)
    #fazer sprite e depois update
    WIN.blit(PLAYER, (player.x, player.y)) #when you want to draw a surface onto a screen
    WIN.blit(ENEMY, (enemy.x, enemy.y))
    pygame.display.update() #refreshes the screen

def player_controls():
    global momentum_x, momentum_y
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        momentum_x -= 0.1
    if keys_pressed[pygame.K_RIGHT]:
        momentum_x += 0.1
    if keys_pressed[pygame.K_SPACE]:
        momentum_y -= 0.3

def apply_momentum(player):
    global momentum_x, momentum_y, position_x, position_y

    momentum_y += 0.05

    position_x += momentum_x
    position_y += momentum_y
    player.x = position_x
    player.y = position_y

if __name__ == "__main__": #main file to run
    main()