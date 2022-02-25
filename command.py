from pygame import *

class Command:
    def execute():
        raise NotImplemented

class Jump(Command):
    def execute(player):
        player.jump()
        
class Left(Command):
    def execute(player):
        player.left()

class Right(Command):
    def execute(player):
        player.right()

class InputHandler:
    def handleInput(self):
        command_list = [] #in order to allow multiple simultaneous commands a command is registered in a list for every input
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            command_list.append(Left)
        if keys_pressed[K_RIGHT]:
            command_list.append(Right)
        if keys_pressed[K_SPACE]:
            command_list.append(Jump) 
        return command_list