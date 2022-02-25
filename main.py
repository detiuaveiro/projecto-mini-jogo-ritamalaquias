import pygame
import os
import json
from pygame import *
from pygame.locals import *
from command import InputHandler, Command
from player import Player, PlayerState
from enemy import Enemy, EnemyState, EnemyType
from level import Level
from layer import Layer
from consts import Consts
from titlescreen import TitleScreen, MainState
from ui import GameUI

#using dictionaries to correlate grid numbers to the image file names for sprites
background_img_dict = {2: 'bgSprite1.png', 3: 'bgSprite2.png', 4: 'bgSprite3.png', 5: 'bgSprite4.png', 6: 'bgSprite5.png', 7: 'bgSpriteWater1.png', 8: 'bgSpriteWater2.png'}
platform_img_dict = {2: 'tileSprite1.png', 3: 'tileSprite2.png'}

###TEST
f = open(os.path.join('levelmaps', 'level1.json'))
level = json.load(f)
#print(level_test["background"])

#background
grid_background = level["background"]
#foreground
grid_platform = level["foreground"]

#classes are instanciated here so that they can be used in other functions besides main()
const = Consts()
title_screen = TitleScreen()
game_ui = GameUI()
background = Layer(grid_background, background_img_dict) #creates background layer using its sprites dictionary
platforms = Layer(grid_platform, platform_img_dict, True) #creates foreground layer using its sprites dictionary with collision
level = Level() #creates the level where the layers and enemies lists are going to reside
player = Player.get_instance([100.0, 100.0])
current_game_state = MainState.menu

#main program

def main():  
    global current_game_state
    clock = pygame.time.Clock()
    level.layer_list.append(background)
    level.layer_list.append(platforms)
    level.enemy_list.append(Enemy(EnemyType.easy, [500.0, 400.0])) 
    level.enemy_list.append(Enemy(EnemyType.normal, [500.0, 100.0])) 
        
    #game loop
    run = True
    while run:
        clock.tick(const.FPS) #runs the while loop at the frames defined

        #pause menu appears
        key_pressed = key.get_pressed()
        if key_pressed[K_p]: 
            if current_game_state == MainState.pause:
                current_game_state = MainState.running
            else:
                current_game_state = MainState.pause

        #counts amount of enemies remaining
        remaining_enemies = 0
        for enemy in level.enemy_list:
            if enemy.state != EnemyState.defeated:
                remaining_enemies += 1

        #checks if game over screen should appear
        if remaining_enemies == 0 or player.state == PlayerState.dead:
            current_game_state = MainState.game_over
        #checks click on start button in title screen, which starts the game
        if title_screen.start_button.on_click():
            current_game_state = MainState.running
        #checks click on exit button in title screen
        if title_screen.exit_button.on_click():
            current_game_state = MainState.exit
        #checks click on quit button in game over screen
        if game_ui.quit_button.on_click():
            current_game_state = MainState.exit
        #when user clicks on the X button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        #checks if game is in exit state - if so, the game closes
        if current_game_state == MainState.exit:
            run = False

        player.add_gravity()
        player.add_friction()

        #checks if player is colliding with platforms 
        for tile in level.get_collidable_tiles():
            #the rect coordinates are on the tile's second value. tile is a surface which contains an image as its first value, then rect as its second value. rect is [1]
            collide = tile[1].colliderect(player.rect)
            if collide:
                player.rect.bottom = tile[1].top #positions player on top of the platform, which makes sure the player cannot go through it
                player.bounce_vertical()
                player.bounce_horizontal()

        #command pattern
        input_handler = InputHandler() #needs to be inside main loop to get button presses each frame
        command_list = input_handler.handleInput()
        for command in command_list:
            command.execute(player)

        player.apply_window_collision(const.HEIGHT, const.WIDTH)
        player.apply_momentum()
        update_enemies()
        draw_window()

    pygame.quit()

#methods
def update_enemies():
    if current_game_state == MainState.running:
        for enemy in level.enemy_list:
            enemy.add_gravity()
            #state machine
            if enemy.state == EnemyState.chasing:
                enemy.apply_window_collision(const.HEIGHT, const.WIDTH)
                enemy.apply_ai(player)
            enemy.apply_momentum()
            
            #enemies collide with player
            if player.rect.colliderect(enemy.rect) and enemy.state == EnemyState.chasing:
                if player.rect.bottom <= enemy.rect.top+2:
                    enemy.state = EnemyState.dying
                    player.score += Enemy.enemy_type_score_value[enemy.enemy_type]
                if enemy.rect.bottom <= player.rect.top+2:
                    player.state = PlayerState.dead
                enemy.bounce_horizontal()
                enemy.bounce_vertical()
                player.bounce_horizontal()
                player.bounce_vertical()

            for tile in level.get_collidable_tiles():
                if tile[1].colliderect(enemy.rect) and enemy.state == EnemyState.chasing:
                    enemy.rect.bottom = tile[1].top
                    enemy.bounce_vertical()
            
            if enemy.rect.top > const.HEIGHT: #to remove dead enemy after it drops from screen
                level.enemy_list.remove(enemy)

def draw_window():
    if current_game_state == MainState.menu:
        title_screen.draw()
    if current_game_state == MainState.running:
        const.WIN.fill(const.BLACK)
        for tile in level.get_all_tiles():
            const.WIN.blit(tile[0], tile[1]) #0 = tile_sprite, 1 = rect
        const.WIN.blit(player.image, (player.position[0], player.position[1])) 
        for enemy in level.enemy_list:
            const.WIN.blit(enemy.image, (enemy.position[0], enemy.position[1])) #0 = x, 1 = y
    if current_game_state == MainState.pause:
        game_ui.draw_pause()
    if current_game_state == MainState.game_over:
        game_ui.draw_game_over()
    
    pygame.display.set_caption("Balloon Fight") #window name
    pygame.display.update() #refreshes the screen


if __name__ == "__main__": #main file to run
    main()