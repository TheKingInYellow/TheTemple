#! /usr/bin/python2.7


__filename__ = 'itemClass.py'
__author__ = 'Kody Crowell'

"""
Describes all of the items in the game.
"""
from actionClass import *


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


#### TOOL CLASS  #################################################################
class Tool(Item):
    """
    The base class Tool that inherits from Item.
    """
    def __init__(self, name, desc, val, action):
        self.action = action
        super().__init__(name, desc, val)

    def __str__(self):
        return "{}\n---------------\nValue: {}\nAction: {}\n{}\n".format( \
                self.name, self.value, self.action, self.description)


#### CLOTHING CLASS ##############################################################
class Clothing(Item):
    """
    The base class Clothing that inherits from Item.
    """
    def __init__(self, name, desc, val, chr):
        self.charisma = chr
        super().__init__(name, desc, val)

    def __str__(self):
        return "{}\n--------------\nValue: {}\nCharisma: {}\n{}\n".format( \
                self.name, self.value, self.charisma, self.description)

    def is_equipped(self):
        return self.charisma

class GoldRing(Clothing):
    def __init__(self):
        super().__init__(name="Ring",
                         desc="A golden ring with a sapphire embedded in it.",
                         val=150,
                         chr=10)

class Hat(Clothing):
    def __init__(self):
        super().__init__(name="Hat",
                         desc="A simple hat that serves its purpose.",
                         val=10,
                         chr=25)

class Shoes(Clothing):
    def __init__(self):
        super().__init__(name="Shoes",
                         desc="A nice pair of shoes - simple and well-worn",
                         val=25,
                         chr=50)

class LeatherVest(Clothing):
    def __init__(self):
        super().__init__(name="Vest",
                         desc="A very handsome leather vest. It even comes " \
                                 + "with a breast pocket.",
                         val=50,
                         chr=60)

class GreyCloak(Clothing):
    def __init__(self):
        super().__init__(name="Grey Cloak",
                         desc="A grey hooded cloak lined with satin.",
                         val=55,
                         chr=75)

class FancyTrousers(Clothing):
    def __init__(self):
        super().__init__(name="Fancy Trousers",
                         desc="A dressy pair of trousers goes well with anything!",
                         val=60,
                         chr=40)

#### FOOD CLASS ##################################################################
class Food(Item):
    """
    The base class Food that inherits from Item.
    """
    def __init__(self, name, desc, val, cal):
        self.calories = cal
        super().__init__(name, desc, val)

    def __str__(self):
        return "{}\n---------------\nValue: {}\nCalories: {}\n{}\n".format( \
                self.name, self.value, self.calories, self.description)

class Wine(Food):
    def __init__(self):
        super().__init__(name="Wine",
                         desc="Red wine that is firm, with a subtle fruity " \
                                + "aroma to it.",
                         val=30,
                         cal=125)

class Cheddar(Food):
    def __init__(self):
        super().__init__(name="Cheddar",
                         desc="A piece of aged cheddar with a sharp flavour.",
                         val=10,
                         cal=110)

class Rice(Food):
    def __init__(self):
        super().__init__(name="Wild Rice",
                         desc="A bowl of wild rice. It could use some salt.",
                         val=10,
                         cal=100)

class Bread(Food):
    def __init__(self):
        super().__init__(name="Bread",
                         desc="A loaf of bread. You're not sure what kind.",
                         val=10,
                         cal=200)

class Fish(Food):
    def __init__(self):
        super().__init__(name="Raw Fish",
                         desc="A small uncooked fish.",
                         val=20,
                         cal=200)

class Lettuce(Food):
    def __init__(self):
        super().__init__(name="Lettuce",
                         desc="A small head of lettuce.",
                         val=5,
                         cal=50)

class Apple(Food):
class Egg(Food):
class Pie(Food):
class Carrot(Food):
# Add option to get sick / cook?
