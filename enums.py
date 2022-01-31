from enum import Enum

class EnemyState(Enum): #to use in enemy state machine
    chasing = 1 
    dying = 2

class EnemyType(Enum): #to use to define an enemy type
    easy = 1
    normal = 2
    hard = 3