import pygame
import os
import json
from pygame import *
from pygame.locals import *
from player import Player
from enemy import Enemy, EnemyState, EnemyType
from level import Level
from layer import Layer

#window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Fight") #window name

BLACK = (0, 0, 0) #color for window fill defined here so it can be easier to change it if needed
FPS = 60 #fps defined here so it can be easier to change if needed

#using dictionaries to correlate grid numbers to the image file names for sprites
background_img_dict = {2: 'bgSprite1.png', 3: 'bgSprite2.png', 4: 'bgSprite3.png', 5: 'bgSprite4.png', 6: 'bgSprite5.png'}
platform_img_dict = {2: 'tileSprite1.png'}

#TO DO: read grid from file
###TEST
f = open(os.path.join('levelmaps', 'level1.json'))
level_test = json.load(f)
print(level_test["background"])

#background
grid_background = level_test["background"]
#foreground
grid_platform = level_test["foreground"]

#classes are instanciated here so that they can be used in other functions besides main()
background = Layer(grid_background, background_img_dict) #creates background layer using its sprites dictionary
platforms = Layer(grid_platform, platform_img_dict, True) #creates foreground layer using its sprites dictionary with collision
level = Level() #creates the level where the layers and enemies lists are going to reside
player = Player([100.0, 100.0])

#main program
def main():  
    clock = pygame.time.Clock()
    level.layer_list.append(background)
    level.layer_list.append(platforms)
    level.enemy_list.append(Enemy(EnemyType.easy, [100.0, 200.0])) 
    level.enemy_list.append(Enemy(EnemyType.normal, [500.0, 100.0])) 

    #game loop
    run = True
    while run:
        clock.tick(FPS) #runs the while loop at the frames defined
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.add_gravity()

        for tile in level.get_collidable_tiles():
            collide = tile[1].colliderect(player.rect)
            if collide:
                player.rect.bottom = tile[1].top
                player.bounce_vertical()
                player.bounce_horizontal()

        player.player_controls()
        player.apply_window_collision(HEIGHT, WIDTH)
        player.apply_momentum()       
        update_enemies()
        draw_window()

    pygame.quit()

#methods
def update_enemies():
    for enemy in level.enemy_list:
        enemy.add_gravity()
        #state machine
        if enemy.state == EnemyState.chasing:
            enemy.apply_window_collision(HEIGHT, WIDTH)
            enemy.apply_ai(player)
        enemy.apply_momentum()
        
        if player.rect.colliderect(enemy.rect) and enemy.state == EnemyState.chasing:
            if player.rect.bottom < enemy.rect.top+2:
                enemy.state = EnemyState.dying
                player.score += Enemy.enemy_type_score_value[enemy.enemy_type]
            enemy.bounce_horizontal()
            enemy.bounce_vertical()
            player.bounce_horizontal()
            player.bounce_vertical()

        for tile in level.get_collidable_tiles():
            if tile[1].colliderect(enemy.rect) and enemy.state == EnemyState.chasing:
                enemy.rect.bottom = tile[1].top
                enemy.bounce_vertical()
        
        if enemy.rect.top > HEIGHT: #to remove dead enemy after it drops from screen
            level.enemy_list.remove(enemy)

def draw_window():
    WIN.fill(BLACK)
    for tile in level.get_all_tiles():
        WIN.blit(tile[0], tile[1]) #0 = tile_sprite, 1 = rect
    WIN.blit(player.image, (player.position[0], player.position[1])) 
    for enemy in level.enemy_list:
        WIN.blit(enemy.image, (enemy.position[0], enemy.position[1])) #0 = x, 1 = y

    pygame.display.update() #refreshes the screen

if __name__ == "__main__": #main file to run
    main()