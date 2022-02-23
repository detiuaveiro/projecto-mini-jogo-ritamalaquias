import pygame

class Consts():
    WIDTH, HEIGHT = 640, 480 #4:3
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    BLACK = (0, 0, 0) #color for window fill
    FPS = 60 #for clock.tick

    #title screen image constants
    SCALE = 2
    LOGO_WIDTH, LOGO_HEIGHT = 223 * SCALE, 103 * SCALE
    START_WIDTH, START_HEIGHT = 38 * SCALE, 7 * SCALE
    EXIT_WIDTH, EXIT_HEIGHT = 31 * SCALE, 7 * SCALE
    NINTENDO_WIDTH, NINTENDO_HEIGHT = 113 * SCALE, 8 * SCALE
    CREDIT_WIDTH, CREDIT_HEIGHT = 158 * SCALE, 8 * SCALE