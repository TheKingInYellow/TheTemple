#! /usr/bin/python2.7


__filename__ = 'itemClass.py'
__author__ = 'Kody Crowell'

"""
Describes all of the items in the game.
"""

class Item:
    """
    Base class for all items.
    """
    def __init__(self, name, desc, val):
        self.name = name
        self.description = desc
        self.value = val

    def __str__(self):
        return "{}\n---------------\nValue: {}\n{}\n".format(self.name, \
                self.value, self.description)

class Tool(Item):
    """
    The base class Tool that inherits from Item.
    """
    pass

class Armour(Item):
    """
    The base class Armour that inherits from Item.
    """
    pass

class Food(Item):
    """
    The base class Food that inherits from Item.
    """
    pass

