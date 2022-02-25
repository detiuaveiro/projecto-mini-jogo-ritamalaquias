from pygame import *
from pygame.sprite import Sprite
import os
from button import Button
from consts import Consts

const = Consts()

#game ui
pause_img = image.load(os.path.join('Assets', 'titleStartSprite.png')) #mudar imagem
pause_img = transform.scale(pause_img, (const.START_WIDTH, const.START_HEIGHT))
retry_img = image.load(os.path.join('Assets', 'titleRetrySprite.png')) 
retry_img = transform.scale(retry_img, (const.RETRY_WIDTH, const.RETRY_HEIGHT))
quit_img = image.load(os.path.join('Assets', 'titleQuitSprite.png'))
quit_img = transform.scale(quit_img, (const.QUIT_WIDTH, const.QUIT_HEIGHT))

class GameUI(Sprite):
    def __init__(self):
        self.pause_button = Button(pause_img, [270.0, 300.0])
        #self.retry_button = Button(retry_img, [270.0, 300.0])
        self.quit_button = Button(quit_img, [270.0, 330.0])

    def draw_pause(self):
        self.pause_button.draw()

    def draw_game_over(self):
        const.WIN.fill(const.BLACK)
        #self.retry_button.draw()
        self.quit_button.draw()
    
