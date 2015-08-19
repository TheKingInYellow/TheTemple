"""
ACTION CLASS

Describes all of the actions a player can make in the game.
"""

from player import Player
import tiles

class Action(object):
    """
    The base class for all actions.
    """
    def __init__(self, name, method, **kwargs):
        """
        Defines a new action.

        name :: name of the action
        method :: function that is executed upon call
        """
        self.name = name
        self.method = method

        def __str__(self):
            return "\t{}".format(self.name)


# MOVEMENT #################################################################
class MoveFore(Action):
    def __init__(self):
        super(MoveFore, self).__init__(name='Move Fore', 
                                       method=Player.move_fore)

class MoveAstern(Action):
    def __init__(self):
        super(MoveAstern, self).__init__(name='Move Astern', 
                                         method=Player.move_astern)

class MoveAstarboard(Action):
    def __init__(self):
        super(MoveAstarboard, self).__init__(name='Move Astarboard', 
                                             method=Player.move_astar)

class MoveAport(Action):
    def __init__(self):
        super(MoveAport, self).__init__(name='Move Aport', 
                                        method=Player.move_aport)

class ViewInventory(Action):
    """
    Prints the Player's inventory.
    """
    def __init__(self):
        super(ViewInventory, self).__init__(name="View Inventory", 
                                            method=Player.print_inventory)


class Attack(Action):
    def __init__(self, enemy):
        super(Attack, self).__init__(name='Attack', 
                                     method=Player.attack, enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super(Flee, self).__init__(name='Flee', 
                                   method=Player.flee, tile=tile)


class Eat(Action):
    def __init__(self, food):
        super(Eat, self).__init__(name='Eat', 
                                  method=Player.eat, food=food)


class UnlockDoor(Action):
    def __init__(self, tile):
        super(UnlockDoor, self).__init__(name='Unlock Door', 
                                         method=Player.unlock, tile=tile)
