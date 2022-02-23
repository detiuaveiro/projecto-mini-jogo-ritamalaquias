import pygame
from pygame import *
from pygame.sprite import Sprite
import os
from consts import Consts
from button import Button

const = Consts()

start_img = image.load(os.path.join('Assets', 'titleStartSprite.png'))
start_img = transform.scale(start_img, (const.START_WIDTH, const.START_HEIGHT))
exit_img = image.load(os.path.join('Assets', 'titleExitSprite.png'))
exit_img = transform.scale(exit_img, (const.EXIT_WIDTH, const.EXIT_HEIGHT))
logo_img = image.load(os.path.join('Assets', 'titleSprite.png'))
logo_img = transform.scale(logo_img, (const.LOGO_WIDTH, const.LOGO_HEIGHT))
nintendo_img = image.load (os.path.join('Assets', 'titleCreditSprite1.png'))
nintendo_img = transform.scale(nintendo_img, (const.NINTENDO_WIDTH, const.NINTENDO_HEIGHT))
my_name_img = image.load (os.path.join('Assets', 'titleCreditSprite2.png'))
my_name_img = transform.scale(my_name_img, (const.CREDIT_WIDTH, const.CREDIT_HEIGHT))

class TitleScreen(Sprite):
    def __init__(self):
        self.start_button = Button(start_img, [270.0, 300.0])
        self.exit_button = Button(exit_img, [270.0, 330.0])

    def draw(self):
        const.WIN.fill(const.BLACK)
        self.start_button.draw()
        self.exit_button.draw()
        self.draw_text()
        

    def draw_text(self):
        #logo
        self.logo_text = Button(logo_img, [100.0, 40.0])
        self.logo_text.draw()
        #credits
        self.nintendo_text = Button(nintendo_img, [190.0, 400.0])
        self.nintendo_text.draw()
        self.my_name_text = Button(my_name_img, [150.0, 430.0])
        self.my_name_text.draw()
