"""
ITEM CLASS

Describes all of the items in the game.
"""

import string
from random import choice


class Item:
    """
    Base class for all items.

    name :: name of the item
    desc :: description of the item
    """
    def __init__(self, name, desc):
        self.name = name
        self.description = desc

    def __str__(self):
        return "{}\n---------------\n{}\n".format(self.name, self.description)


# WEAPON ##################################################################
class Weapon(Item):
    """
    The base class Weapon inherits from Tool. You can attack with weapons.
    You can only carry one weapon at a time.

    dmg :: damage value of the weapon
    """
    def __init__(self, name, desc, dmg):
        self.damage = dmg
        super().__init__(name, desc)

    def __str__(self):
        return "{}\n---------------\nDamage: " \
             + "{}\n{}\n".format(self.name, self.damage, self.description)


class VoidKnuckles(Weapon):
    def __init__():
        super().__init__(name="Void Knuckles",
                         desc="These knuckledusters remove enemies from " \
                            + "this dimension and throw them into the Void.")


class LaserKnife(Weapon):
    def __init__():
        super().__init__(name="YAD Laser Knife",
                         desc="This knife is made from a yttrium-aluminium-" \
                            + "diamond alloy. It gives a soft green glow.",
                         dmg=5)


class DiscretizationPistol(Weapon):
    def __init__():
        super().__init__(name="Discretization Pistol",
                         desc="A phase-modulated weapon that discharges "\
                            + "energy in the form of a pulse, discretizing "\
                            + "attackers into their component particles.",
                         dmg=10)
                                
                         
class BifurcationRifle(Weapon):
    def __init__(self):
        super().__init__(name="Bifurcation Rifle",
                         desc="A large, heavy, rifle that rips enemies " \
                            + "into two pieces. Near the butt, the " \
                              "initials K.M.J. are engraved.",
                         dmg=20)


class HeteroskedasticSpear(Weapon):
    def __init__(self):
        super().__init__(name="Heteroskedastic Spear",
                         desc="This polearm disperses enemies with unequal " \
                            + "variance thrroughout the cosmos.",
                         dmg=15)


# MISC ######################################################################
class HotGloves(Item):
    def __init__(self):
        super().__init__(name="Heat Resistant Industrial Gloves",
                         desc="Great for handling objects with temperatures "\
                            + "reaching up to 1700 K.")

class MedPack(Item):
    def __init__(self):
        super().__init__(name="Temp-Steal Med-Pack",
                         desc="These med-packs use complicated technology " \
                            + "to steal perfectly healthy tissue from the " \
                            + "future in order to heal wounds in the present")

class SwipeCard(Item):
    def __init__(self, color):
        self.color = color
        itl = string.ascii_uppercase
        name = self.color.capitalize + " Key Card"
        desc = "A " + self.color + " key card. The initials on the back say "\
        choice(itl) + "." + choice(itl) + "." + choice(itl) + "."
        super().__init__(name, desc)


class OxyMask(Item):
    def __init__(self):
        super().__init__(name="Oxy-Filtration Mask",
                         desc="This mask filters any element into Earth-01-"\
                            + "like air: 78.09% N, 20.95% O, 0.93% Ar, " \
                            + "0.039% CO2, trace amounts of other elements." \
                            + "Also added is the faint smell of marijuana.")

class LaserWireCutters(Item):
    def __init__(self):
        super().__init__(name="Laser Wire Cutters",
                         desc="A nice pair of wire cutters, a must-have for "\
                            + "every practical person.")


class IvyCrysantheum(Item):
    def __init__(self):
        super().__init__(name="Ivy Crysantheum",
                         desc="A rar hybrid that is Super Poisonous. " \
                            + "It also adds a bit of a kick to any " \
                            + "Asian Confederate Tuna-Skunk stir-fry. But " \
                            + "everyone who has ever tried it has died."


class Vitriol(Item):
    def __init__(self):
        super().__init__(name="Tincture of Vitriol",
                         desc="Vitriolic Oil is used to feed many types " \
                            + "of toxic plant and animal hybrids. Also used "\
                            + "to get rid of Tongue Fungus.")


class Spspork(Item):
    def __init__(self):
        super().__init__(name="Space Spork",
                         desc="Self explanatory. Made from an impenetrable " \
                            + "superconducting vibranium-adamantium alloy.")


class BrokenLever(Item):
    def __init__(self):
        super().__init__(name="Broken Lever",
                         desc="A lever that connects to something..."\
                            + "but what?")


class CoordinateChip(Item):
    def __init__(self):
        super().__init__(name="Coordinate Chip",
                         desc="This chip can hold galactic coordinates " \
                            + "in both Euclidean space and Minkowski space")


class FuelCell(Item):
    def __init__(self):
        super().__init__(name="Fuse-X Fuel Cell",
                         desc="This third generation fuel cell is a true " \
                            + "sun-in-a-can. Once iron is fused in the " \
                            + "core, the cell politely removes itself from "\
                            + "spacetime and implodes.")


# FOOD ####################################################################
class Food(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)


class FoodPack(Food):
    def __init__(self):
        super().__init__(name="Food Ration",
                         desc="High quality space-food packed with a month's"\
                            + " worth of protein, carbohydrates and other " \
                            + "essential nutrients.")

    def eat(self):
        print "Your food ration tasted...strange. It probably needs salt."

        
class CoffeePack(Food):
    def __init__(self):
        super().__init__(name="Antimicrobial Coffee",
                         desc="This genetically-modified coffee supposedly " \
                            + "has the ability to keep astronauts awake for "\
                            + "more than 72 hours while fighting infections.")

    def eat(self):
        print "You begin to feel the effects of the caffeine immediately."

        
class WineSupplement(Food):
    def __init__(self):
        super().__init__(name="Wine Supplement",
                         desc="A wine-flavoured, nutrient-filled jelly. " \
                            + "Just add water!")

    def eat(self):
        print "The alcohol by volume on the package says 16%, but you're "\
            + "not convinced."

            
class SandwichCube(Food):
    def __init__(self):
        super().__init__(name="Sandwich Cube",
                         desc="After the destruction of Earth-03, these " \
                            + "treats are a delicacy among rarified circles.")

    def eat(self):
        print "An aftertaste of ham and cheese lingers in your mouth."

        
class SpaceOkra(Food):
    def __init__(self):
        super().__init__(name="Space Okra",
                         desc="Nobody is sure what this is. A vegetable? A "\
                            + "fruit? How do you even eat it?")

    def eat(self):
         print "The okra is soft with a flat taste; very tough to eat."
