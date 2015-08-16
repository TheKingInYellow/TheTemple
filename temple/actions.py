"""
ACTION CLASS

Describes all of the actions a player can make in the game.
"""

from player import Player

class Action:
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
        return "{}".format(self.name)


class mo
        
