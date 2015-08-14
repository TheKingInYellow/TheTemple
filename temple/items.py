#! /usr/bin/python2.7

__filename__ = 'items.py'
__author__ = 'Kody Crowell'

"""
Describes all of the items in the game.
"""
from actionClass import *


class Item:
    """
    Base class for all items.
    """
    def __init__(self, name, desc, val, wt):
        self.name = name
        self.description = desc
        self.value = val
        self.weight = wt

    def __str__(self):
        return "{}\n---------------\nValue: {}\nWeight:{}\n{}\n".format( \
                    self.name, self.value, self.weight, self.description)


# TOOL CLASS  ############################################################
class Tool(Item):
    """
    The base class Tool that inherits from Item.

    name :: name of the tool
    desc :: describes the tool
    val :: monetary value of the tool
    action :: specific action that the tool possesses
    wt :: weight of the tool
    
    Possibility of adding expendability / broken attribute?
    """
    def __init__(self, name, desc, val, wt, action, equip=False):
        self.action = action
        self.equipped = equip
        super().__init__(name, desc, val, wt)

    def __str__(self):
        t_str =  "{}*Equipped*\n---------------\nValue: {}\nWeight: {}" \
                 + "\nAction: {}\n{}\n".format(self.name, self.value, \
                            self.weight, self.action, self.description)
                            
    def equip(self):
        self.equipped = True

    def unequip(self):
        self.equipped = False


class Knife(Tool):
    def __init__(self):
        super().__init__(name="Knife",
                         desc="A small hunting knife. Near the hilt, the " \
                              "initials K.M.J. are engraved into the blade.",
                         val=50,
                         wt=3,
                         action="Cut")

class PickAxe(Tool):
    def __init__(self):
        super().__init__(name="Pickaxe",
                         desc="A rusty pickaxe.",
                         val=20,
                         wt=10,
                         action="Mine")

class Rake(Tool):
    def __init__(self):
        super().__init__(name="Rake",
                         desc="A simple gardening rake",
                         val=20,
                         wt=7,
                         action="Rake")

class Flint(Tool):
    def __init__(self):
        super().__init__(name="Flint",
                         desc="Careful! Don't play with fire!",
                         val=15,
                         wt=5,
                         action="Light")

class Oar(Tool):
    def __init__(self):
        super().__init__(name="Wooden Oar",
                         desc="This wooden oar looks like it's seen a few " \
                            + "storms in its day.",
                         val=15,
                         wt=5,
                         action="Paddle")
                         
class FishingRod(Tool):
    def __init__(self):
        super().__init__(name="Fishing Rod",
                         desc="Perfect for those lazy afternoons.",
                         val=20,
                         wt=7,
                         action="Fish")


# WEAPON ##################################################################
class Weapon(Tool):
    """
    The base class Weapon inherits from Tool. You can attack with weapons.
    You can only carry one weapon at a time.

    name :: name of the weapon
    desc :: description of the weapon
    val :: value of the weapon
    wt :: weight of the weapon
    dmg :: damage value of the weapon
    """
    def __init__(self, name, desc, val, wt, dmg):
        self.damage = dmg
        super().__init__(name, desc, val, wt, action="Attack")

    def __str__(self):
        return "{}\n---------------\nValue: {}\nWeight: {}\nDamage: " \
             + "{}\n{}\n".format(self.name, self.value, self.weight, \
                                 self.damage, self.description)


class Dagger(Weapon):
    def __init__():
        super().__init__(name="Dagger",
                         desc="A sharp dagger with a wooden hilt.",
                         val=10,
                         wt=3,
                         dmg=5)
                         
# CLOTHING CLASS ##########################################################
class Clothing(Item):
    """
    The base class Clothing that inherits from Item. You can equip clothing.

    name :: the name of the clothing article
    desc :: a description
    val :: value of the clothing
    chr :: charisma boost from wearing the clothing
    wt :: weight of the article
    """
    
    def __init__(self, name, desc, val, chr, wt, equip=False):
        self.charisma = chr
        self.equipped = equip
        super().__init__(name, desc, val, wt)

    def __str__(self):
        if self.equipped:
            c_str = "{} *Equipped*\n--------------\nValue: {}\nWeight: " \
                  + "{}\nCharisma: {}\n{}\n".format(self.name, self.value,\
                    self.weight, self.charisma, self.description)
        else:
            c_str = "{}\n--------------\nValue: {}\nWeight: " \
                  + "{}\nCharisma: {}\n{}\n".format(self.name, self.value,\
                    self.weight, self.charisma, self.description)
                    
        return c_str
        
    def equip(self):
        self.equipped = True

    def unequip(self):
        self.equipped = False

class GoldRing(Clothing):
    def __init__(self):
        super().__init__(name="Ring",
                         desc="A golden ring with a sapphire embedded in it.",
                         val=150,
                         chr=50,
                         wt=0)

class Hat(Clothing):
    def __init__(self):
        super().__init__(name="Hat",
                         desc="A simple hat that serves its purpose.",
                         val=10,
                         chr=25,
                         wt=2)

class Shoes(Clothing):
    def __init__(self):
        super().__init__(name="Shoes",
                         desc="A nice pair of shoes - simple and well-worn",
                         val=25,
                         chr=50,
                         wt=3)

class LeatherVest(Clothing):
    def __init__(self):
        super().__init__(name="Vest",
                         desc="A handsome leather vest. It even comes " \
                                 + "with a breast pocket.",
                         val=50,
                         chr=60,
                         wt=5)

class GreyCloak(Clothing):
    def __init__(self):
        super().__init__(name="Grey Cloak",
                         desc="A light grey hooded cloak lined with satin.",
                         val=55,
                         chr=75,
                         wt=7)

class FancyTrousers(Clothing):
    def __init__(self):
        super().__init__(name="Fancy Trousers",
                         desc="A dressy pair of trousers goes well with " \
                            + "anything!",
                         val=60,
                         chr=40,
                         wt=5)

# FOOD CLASS ##############################################################
class Food(Item):
    """
    The base class Food that inherits from Item. You can eat food.

    name :: name of the food item
    desc :: description of the food item
    val :: monetary value
    cal :: caloric content of the item
    wt :: weight
    
    Possibility of adding a way to poison / cook the item?
    """
    def __init__(self, name, desc, val, cal, wt):
        self.calories = cal
        super().__init__(name, desc, val, wt)

    def __str__(self):
        return "{}\n---------------\nValue: {}\nWeight: {}\nCalories: {}\n" \
             + "{}\n".format(self.name, self.value, self.weight, \
                             self.calories, self.description)

class Wine(Food):
    def __init__(self):
        super().__init__(name="Wine",
                         desc="Red wine in a glass bottle.",
                         val=30,
                         cal=125,
                         wt=3)
    def eat(self):
        return "The wine is firm, with a subtle fruity aroma to it."
        
class Cheddar(Food):
    def __init__(self):
        super().__init__(name="Cheddar",
                         desc="A piece of aged cheddar.",
                         val=10,
                         cal=110,
                         wt=2)

    def eat(self):
        return "The cheddar has a sharp, but pleasant taste to it."
        
class Rice(Food):
    def __init__(self):
        super().__init__(name="Wild Rice",
                         desc="A bowl of wild rice.",
                         val=10,
                         cal=100,
                         wt=3)

    def eat(self):
        return "The rice could use some salt."

class Bread(Food):
    def __init__(self):
        super().__init__(name="Bread",
                         desc="A loaf of bread. You're not sure what kind.",
                         val=10,
                         cal=200,
                         wt=3)

    def eat(self):
        return "The bread is rough, but filling."

class Fish(Food):
    def __init__(self):
        super().__init__(name="Raw Fish",
                         desc="A small uncooked fish.",
                         val=20,
                         cal=200,
                         wt=2)

    def eat(self):
        return "You probably should have cooked that fish."

class Lettuce(Food):
    def __init__(self):
        super().__init__(name="Lettuce",
                         desc="A small head of lettuce.",
                         val=5,
                         cal=50,
                         wt=2)

    def eat(self):
        return "The lettuce is tasteless and unfilling."
        
class Apple(Food):
    def __init__(self):
        super().__init__(name="Apple",
                         desc="A bright, red, delicious apple.",
                         val=5,
                         cal=50,
                         wt=1)

    def eat(self):
        return "The apple is crisp and sweet."
        
class Egg(Food):
    def __init__(self):
        super().__init__(name="Brown Egg",
                         desc="A large, brown egg with speckles on it.",
                         val=10,
                         cal=75,
                         wt=1)

    def eat(self):
        return "That egg tasted...strange."
        
class Pie(Food):
    def __init__(self):
        super().__init__(name="Meat Pie",
                         desc="A hearty slice of delicious meat pie, " \
                            + "just like Mom used to make!",
                         val=25,
                         cal=250,
                         wt=3)

    def eat(self):
        return "The pie was not as good as Mom's..."
        
class Carrot(Food):
    def __init__(self):
        super().__init__(name="Carrot",
                         desc="A large orange carrot. Rabbit food!",
                         val=5,
                         cal=25,
                         wt=2)

    def eat(self):
        return "No wonder you couldn't stick to that diet."
        
class NadaBerry(Food):
    def __init__(self):
        super().__init__(name="Nadaberry",
                         desc="The island locals seem to love this berry.",
                         val=50,
                         cal=40,
                         wt=1)

    def eat(self):
        return "The berry is much too bitter for your liking."


# TREASURE ##############################################################
class CopperHelm(Item):
    def __init__(self):
        super().__init__(name="Copper Helm",
                         desc="An old battle-helm from ages past.",
                         val=100,
                         wt=5)

class GoldenChalice(Item):
    def __init__(self):
        super().__init__(name="Golden Chalice",
                         desc="A golden chalice with rubies lining the rim.",
                         val=250,
                         wt=5)

class Amulet(Item):
    def __init__(self):
        super().__init__(name="Precious Amulet",
                         desc="A large, round, silver amulet embedded " \
                            + "with rubies, emeralds and sapphires.",
                         val=200,
                         wt=3)

class Diamond(Item):
    def __init__(self):
        super().__init__(name="Rough Diamond",
                         desc="A rough-cut sample that glitters and shines.",
                         val=250,
                         wt=1)

class GoldNugget(Item):
    def __init__(self):
        super().__init__(name="Gold Nugget",
                         desc="A small, gold nugget.",
                         val=100,
                         wt=1)

class Pearl(Item):
    def __init__(self):
        super().__init__(name="Pearl",
                         desc="This round pearl is so perfect, you can't " \
                            + "take your eyes off of it.",
                         val=150,
                         wt=1)

class BattleSword(Item):
    def __init__(self):
        super().__init__(name="Rustic Battle Sword",
                         desc="This sword is heavy and ancient. It is " \
                              "not worth using in a fight.",
                         val=200,
                         wt=20)

class SilverArrow(Item):
    def __init__(self):
        super().__init__(name="Silver Arrow",
                         desc="An old silver arrow with no feathers.",
                         val=100,
                         wt=2)

class GoldenRing(Item):
    def __init__(self):
        super().__init__(name="Golden Ring",
                         desc="A voice from within the ring seems to be " \
                            + "calling to you. Strange letters are engraved" \
                            + " along the body. It is too big to be worn.",
                         val=150,
                         wt=0)

class Ruby(Item):
    def __init__(self):
        super().__init__(name="Large Ruby",
                         desc="A cut and polished, blood-red ruby.",
                         val=200,
                         wt=1)

class Emerald(Item):
    def __init__(self):
        super().__init__(name="Large Emerald",
                         desc="A beautiful, green emerald.",
                         val=200,
                         wt=1)

class Sapphire(Item):
    def __init__(self):
        super().__init__(name="Large Sapphire",
                         desc="A gorgeous gemstone, blue within blue within "\
                            + "blue...",
                         val=200,
                         wt=1)

class GoldenIdol(Item):
    def __init__(self):
        super().__init__(name="Golden Idol",
                         desc="This golden idol has rubies for eyes, " \
                            + "sapphires for teeth, and emeralds for nails."\
                            + "It weighs about the same as a bag of sand.",
                         val=300,
                         wt=15)

class JadeFigure(Item):
    def __init__(self):
        super().__init__(name="Jade Figurine",
                         desc="You're not quite sure what this figurine is "\
                            + "supposed to represent. A cat, maybe?",
                         val=100,
                         wt=5)

class SilverWare(Item):
    def __init__(self):
        super().__init__(name="Assorted Silverware",
                         desc="A tarnished silverware collection.",
                         val=50,
                         wt=10)

# QUEST ITEMS ############################################################
class RareLily(Item):
    def __init__(self):
        super().__init__(name="Rare Tiger Lily",
                         desc="This bright, orange flower is a rare variant "\
                            + "that only blooms every 78 years.",
                         val=0,
                         wt=0)
                         
class AncientScroll(Item):
    def __init__(self):
        super().__init__(name="Papyrus Scroll",
                         desc="This scroll has strange runes written on it.",
                         val=0,
                         wt=5)
                         
class RustyKey(Item):
    def __init__(self):
        super().__init__(name="Rusty Key",
                         desc="A rusty key. What does it open?",
                         val=0,
                         wt=0)

class GoldenKey(Item):
    def __init__(self):
        super().__init__(name="Golden Key",
                         desc="An ornate golden key. What does it open?",
                         val=0,
                         wt=0)
                         
class Torch(Item):
    def __init__(self):
        super().__init__(name="Torch",
                         desc="This torch is too heavy to walk around with. "\
                            + "Maybe it could be mounted on something?",
                         val=0,
                         wt=2)
                         
                         
class CrystalMirror(Item):
    def __init__(self):
        super().__init__(name="Crystal Mirror",
                         desc="For some reason, you cannot see your own " \
                            + "reflection.",
                         val=0,
                         wt=5)

class TigerSkull(Item):
    def __init__(self):
        super().__init__(name="Tiger Skull",
                         desc="The skull of a once-great beast.",
                         val=0,
                         wt=7)
                         
class Vitriol(Item):
    def __init__(self):
        super().__init__(name="Oil of Vitriol",
                         desc="The jar emits a strong, pungent odour.",
                         val=0,
                         wt=5)
                         
class Sulfur(Item):
    def __init__(self):
        super().__init__(name="Sulfur",
                         desc="A large yellow mineral.",
                         val=0,
                         wt=3)
                         
class Saltpeter(Item):
    def __init__(self):
        super().__init__(name="Saltpeter",
                         desc="A small vial of powder.",
                         val=0,
                         wt=0)
                         
class SmallGear(Item):
    def __init__(self):
        super().__init__(name="Wooden Gear",
                         desc="A small wooden gear.",
                         val=0,
                         wt=3)
                         
class Laudanum(Item):
    def __init__(self):
        super().__init__(name="Laudanum",
                         desc="Tincture of opium - a powerful narcotic.",
                         val=0,
                         wt=0)
                         
class Oil(Item):
    def __init__(self):
        super().__init__(name="Oil",
                         desc="Some black, smelly oil.",
                         val=0,
                         wt=2)
                         
class BrokenLadder(Item):
    def __init__(self):
        super().__init__(name="Broken Ladder",
                         desc="This appears to be part of a larger ladder, "\
                            + "but where is it?",
                         val=0,
                         wt=2)
                         
class GunPowder(Item):
    def __init__(self):
        super().__init__(name="Gunpowder",
                         desc="A small charge of gunpowder.",
                         val=0,
                         wt=0)
                         
class TigerDust(Item):
    def __init__(self):
        super().__init__(name="Tiger Dust",
                         desc="Nobody knows what this dust does, exactly, " \
                            + "but it seems to be important.",
                         val=0,
                         wt=0)
                         
class DarkGold(Item):
    def __init__(self):
        super().__init__(name="Dark Gold Ore",
                         desc="This ore has hints of black swirling within.",
                         val=0,
                         wt=4)
                         
class Lever(Item):
    def __init__(self):
        super().__init__(name="Lever",
                         desc="This lever should be attached to something.",
                         val=0,
                         wt=0)
                         
class BucketOfWater(Item):
    def __init__(self):
        super().__init__(name="Bucket of Water",
                         desc="A bucket of water. It doesn't look potable.",
                         val=0,
                         wt=4)
                         
class Seed(Item):
    def __init__(self):
        super().__init__(name="Bag of Seeds",
                         desc="An assortment of seeds that you can't seem " \
                            + "to identify.",
                         val=0,
                         wt=1)


# MISC ITEMS ###########################################################
class BrokenCompass(Item):
    def __init__(self):
        super().__init__(name="Broken Compass",
                         desc="The needle on this compass keeps changing " \
                            + "direction randomly!",
                         val=10,
                         wt=2)
                         
class Vase(Item):
    def __init__(self):
        super().__init__(name="Vase",
                         desc="A beautiful glass vase. Maybe a flower " \
                            + "brighten it up?",
                         val=10,
                         wt=3)
                         
class Coal(Item):
    def __init__(self):
        super().__init__(name="Coal",
                         desc="A chunk blacker than a dark steer on a " \
                            + "moonless night.",
                         val=10,
                         wt=2)
                         
class TeaPot(Item):
    def __init__(self):
        super().__init__(name="Old Teapot",
                         desc="This beautiful, porcelain teapot can make " \
                            + "the perfect cup.",
                         val=25,
                         wt=4)
                         
class IronCastPot(Item):
    def __init__(self):
        super().__init__(name="Iron Cast Pot",
                         desc="The pot is old, but it seems to be resilient.",
                         val=20,
                         wt=6)
                         
class Cup(Item):
    def __init__(self):
        super().__init__(name="Cup",
                         desc="An clay cup.",
                         val=5,
                         wt=2)
                         
class Plate(Item):
    def __init__(self):
        super().__init__(name="Plate",
                         desc="A brown plate. There is something from its " \
                            + "last meal stuck to the surface.",
                         val=10,
                         wt=2)
                         
class EmptyJar(Item):
    def __init__(self):
        super().__init__(name="Empty Jar",
                         desc="A vessel for liquids or dry goods.",
                         val=10,
                         wt=1)
                         
class EmptyBucket(Item):
    def __init__(self):
        super().__init__(name="Empty Bucket",
                         desc="An empty metal bucket.",
                         val=5,
                         wt=1)
                         
class Twine(Item):
    def __init__(self):
        super().__init__(name="Twine",
                         desc="A long coil of slim wire.",
                         val=3,
                         wt=0)
                         
class Rod(Item):
    def __init__(self):
        super().__init__(name="Rod",
                         desc="A wooden rod. Maybe it could be used with " \
                            + "another item.",
                         val=2,
                         wt=1)
                         
class Hook(Item):
    def __init__(self):
        super().__init__(name="Hook",
                         desc="A shiny, metal hook.",
                         val=1,
                         wt=1)
                         
class Bait(Item):
    def __init__(self):
        super().__init__(name="Bait",
                         desc="Fishing bait. Probably for fishing?",
                         val=3,
                         wt=0)

