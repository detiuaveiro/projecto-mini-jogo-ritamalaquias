from enum import Enum

class EnemyState(Enum):
    chasing = 1 
    dying = 2
class EnemyType(Enum):
    easy = 1
    normal = 2
    hard = 3