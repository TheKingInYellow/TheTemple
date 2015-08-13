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


# TOOL CLASS  ############################################################
class Tool(Item):
    """
    The base class Tool that inherits from Item.

    name :: name of the tool
    desc :: describes the tool
    val :: monetary value of the tool
    action :: specific action that the tool possesses

    Possibility of adding expendability / broken attribute?
    """
    def __init__(self, name, desc, val, action, equip):
        self.action = action
        self.equipped = equip
        super().__init__(name, desc, val)

    def __str__(self):
        return "{}\n---------------\nValue: {}\nAction: {}\n{}\n".format( \
                self.name, self.value, self.action, self.description)

class Knife(Tool):
    def __init__(self):
        super().__init__(name="Knife",
                         desc="A large hunting knife. Near the hilt, the " \
                              "initials K.M.J. are engraved into the blade.",
                         val=50,
                         action="Cut")

class PickAxe(Tool):
    def __init__(self):
        super().__init__(name="Pickaxe",
                         desc="A rusty pickaxe.",
                         val=20,
                         action="Mine")

class Rake(Tool):
    def __init__(self):
        super().__init__(name="Rake",
                         desc="A simple gardening rake",
                         val=20,
                         action="Rake")

class Flint(Tool):
    def __init__(self):
        super().__init__(name="Flint",
                         desc="Careful! Don't play with fire!",
                         val=15,
                         action="Light")

class Oar(Tool):
    def __init__(self):
        super().__init__(name="Wooden Oar",
                         desc="This wooden oar looks like it's seen a few " \
                            + "storms in its day.",
                         val=15,
                         action="Paddle")
                         
class FishingRod(Tool):
    def __init__(self):
        super().__init__(name="Fishing Rod",
                         desc="Perfect for those lazy afternoons.",
                         val=20,
                         action="Fish")
        
# CLOTHING CLASS #########################################################
class Clothing(Item):
    """
    The base class Clothing that inherits from Item. You can equip clothing.

    name :: the name of the clothing article
    desc :: a description
    val :: value of the clothing
    chr :: charisma boost from wearing the clothing
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
                         chr=50)

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
                         desc="A handsome leather vest. It even comes " \
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
                         desc="A dressy pair of trousers goes well with " \
                            + "anything!",
                         val=60,
                         chr=40)

# FOOD CLASS #############################################################
class Food(Item):
    """
    The base class Food that inherits from Item. You can eat food.

    name :: name of the food item
    desc :: description of the food item
    val :: monetary value
    cal :: caloric content of the item

    Possibility of adding a way to poison / cook the item?
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
                         desc="Red wine in a glass bottle."
                         val=30,
                         cal=125)
    def eat(self):
        return "The wine is firm, with a subtle fruity aroma to it."
        
class Cheddar(Food):
    def __init__(self):
        super().__init__(name="Cheddar",
                         desc="A piece of aged cheddar.",
                         val=10,
                         cal=110)

    def eat(self):
        return "The cheddar has a sharp, but pleasant taste to it."
        
class Rice(Food):
    def __init__(self):
        super().__init__(name="Wild Rice",
                         desc="A bowl of wild rice.",
                         val=10,
                         cal=100)

    def eat(self):
        return "The rice could use some salt."

class Bread(Food):
    def __init__(self):
        super().__init__(name="Bread",
                         desc="A loaf of bread. You're not sure what kind.",
                         val=10,
                         cal=200)

    def eat(self):
        return "The bread is rough, but filling."

class Fish(Food):
    def __init__(self):
        super().__init__(name="Raw Fish",
                         desc="A small uncooked fish.",
                         val=20,
                         cal=200)

    def eat(self):
        return "You probably should have cooked that fish."

class Lettuce(Food):
    def __init__(self):
        super().__init__(name="Lettuce",
                         desc="A small head of lettuce.",
                         val=5,
                         cal=50)

    def eat(self):
        return "The lettuce is tasteless and unfilling."
        
class Apple(Food):
    def __init__(self):
        super().__init__(name="Apple",
                         desc="A bright, red, delicious apple.",
                         val=5,
                         cal=50)

    def eat(self):
        return "The apple is crisp and sweet."
        
class Egg(Food):
    def __init__(self):
        super().__init__(name="Brown Egg",
                         desc="A large, brown egg with speckles on it.",
                         val=10,
                         cal=75)

    def eat(self):
        return "That egg tasted...strange."
        
class Pie(Food):
    def __init__(self):
        super().__init__(name="Meat Pie",
                         desc="A hearty slice of delicious meat pie, " \
                            + "just like Mom used to make!",
                         val=25,
                         cal=250)

    def eat(self):
        return "The pie was not as good as Mom's..."
        
class Carrot(Food):
    def __init__(self):
        super().__init__(name="Carrot",
                         desc="A large orange carrot. Rabbit food!",
                         val=5,
                         cal=25)

    def eat(self):
        return "No wonder you couldn't stick to that diet."
        
class NadaBerry(Food):
    def __init__(self):
        super().__init__(name="Nadaberry",
                         desc="The island locals seem to love this berry.",
                         val=50,
                         cal=40)

    def eat(self):
        return "The berry is much too bitter for your liking."


# MISC ITEMS #############################################################

# TREASURE ##############################################################
class CopperHelm(Item):
    def __init__(self):
        super().__init__(name="Copper Helm"
                         desc="An old battle-helm from ages past.",
                         val=100)

class GoldenChalice(Item):
    def __init__(self):
        super().__init__(name="Golden Chalice",
                         desc="A golden chalice with rubies lining the rim.",
                         val=250)

class Amulet(Item):
    def __init__(self):
        super().__init__(name="Precious Amulet",
                         desc="A large, round, silver amulet embedded " \
                            + "with rubies, emeralds and sapphires.",
                         val=200)

class Diamond(Item):
    def __init__(self):
        super().__init__(name="Rough Diamond",
                         desc="A rough-cut sample that glitters and shines.",
                         val=250)

class GoldNugget(Item):
    def __init__(self):
        super().__init__(name="Gold Nugget",
                         desc="A small, gold nugget.",
                         val=100)

class Pearl(Item):
    def __init__(self):
        super().__init__(name="Pearl",
                         desc="This round pearl is so perfect, you can't " \
                            + "take your eyes off of it.",
                         val=150)

class BattleSword(Item):
    def __init__(self):
        super().__init__(name="Rustic Battle Sword",
                         desc="This sword is heavy and ancient. It is " \
                              "not worth using in a fight.",
                         val=200)

class SilverArrow(Item):
    def __init__(self):
        super().__init__(name="Silver Arrow",
                         desc="An old silver arrow with no feathers.",
                         val=100)

class GoldenRing(Item):
    def __init__(self):
        super().__init__(name="Golden Ring",
                         desc="A voice from within the ring seems to be " \
                            + "calling to you. Strange letters are engraved" \
                            + " along the body. It is too big to be worn.",
                         val=150)

class Ruby(Item):
    def __init__(self):
        super().__init__(name="Large Ruby",
                         desc="A cut and polished, blood-red ruby.",
                         val=200)

class GoldenIdol(Item):
    def __init__(self):
        super().__init__(name="Golden Idol",
                         desc="This golden idol has rubies for eyes, " \
                            + "sapphires for teeth, and emeralds for nails."\
                            + "It weighs about the same as a bag of sand."
                         val=300)

class JadeFigure(Item):
    def __init__(self):
        super().__init__(name="Jade Figurine",
                         desc="You're not quite sure what this figurine is "\
                            + "supposed to represent. A cat, maybe?",
                         val=150)
                         
# QUEST ITEMS ############################################################
class RareLily(Item):
class AncientScroll(Item):
class RustyKey(Item):
class Torch(Item):
class CrystalMirror(Item):
class SilverWare(Item):
class TigerSkull(Item):
class Vitriol(Item):
class Sulfur(Item):
class Saltpeter(Item):
class SmallGear(Item):
class Laudanum(Item):
class Oil(Item):
class BrokenLadder(Item):
class GunPowder(Item):
class TigerDust(Item):
class DarkGold(Item):
class Lever(Item):
class BucketOfWater(Item):
class Seed(Item)

class BrokenCompass(Item):
class Vase(Item):
class Rock(Item):
class Tea(Item):
class IronCastPot(Item):
class Cup(Item):
class Plate(Item):
class EmptyJar(Item):
class EmptyBucket(Item):
class String(Item):
class Rod(Item):
class Hook(Item):
class Bait(Item):
