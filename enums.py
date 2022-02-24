from enum import Enum

class EnemyState(Enum): #to use in enemy state machine
    chasing = 1 
    dying = 2
    defeated = 3

class EnemyType(Enum): #to use to define an enemy type
    easy = 1
    normal = 2
    hard = 3

class MainState(Enum):
    menu = 1
    running = 2
    game_over = 3
    victory = 4
    pause = 5
    exit = 6