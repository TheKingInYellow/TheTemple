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
            return "\t{}".format(self.name[0])


# MOVEMENT #################################################################
class MoveFore(Action):
    def __init__(self):
        super(MoveFore, self).__init__(name=['move fore',
                                             'move foreward',
                                             'go fore',
                                             'travel fore',
                                             'walk fore',
                                             'go forward',
                                             'travel forward',
                                             'walk forward'],
                                       method=Player.move_fore)

class MoveAstern(Action):
    def __init__(self):
        super(MoveAstern, self).__init__(name=['move astern',
                                               'go astern',
                                               'travel astern',
                                               'walk astern',
                                               'move aft',
                                               'walk aft',
                                               'go aft',
                                               'travel aft'],
                                         method=Player.move_astern)

class MoveAstarboard(Action):
    def __init__(self):
        super(MoveAstarboard, self).__init__(name=['move astarboard',
                                                   'go astarboard',
                                                   'walk astarboard',
                                                   'travel astarboard'],
                                             method=Player.move_astar)

class MoveAport(Action):
    def __init__(self):
        super(MoveAport, self).__init__(name=['move aport',
                                              'go aport',
                                              'travel aport',
                                              'walk aport'],
                                        method=Player.move_aport)

class ViewInventory(Action):
    """
    Prints the Player's inventory.
    """
    def __init__(self):
        super(ViewInventory, self).__init__(name=['view inventory',
                                                  'see inventory',
                                                  'inventory',
                                                  'items'],
                                            method=Player.print_inventory)


class Attack(Action):
    def __init__(self, enemy):
        super(Attack, self).__init__(name=['attack',
                                           'fight'],
                                     method=Player.attack, enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super(Flee, self).__init__(name=['flee',
                                         'run Away'],
                                   method=Player.flee, tile=tile)


class Eat(Action):
    def __init__(self, food):
        super(Eat, self).__init__(name=['eat',
                                        'consume'],
                                  method=Player.eat, food=food)


class Unlock(Action):
    def __init__(self, tile):
        super(Unlock, self).__init__(name=['unlock',
                                           'open'],
                                         method=Player.unlock, tile=tile)



class Interact(Action):
    def __init__(self, obj, tile):
        super(Interact, self).__init__(name=['adjust',
                                             'push',
                                             'pull',
                                             'turn',
                                             'press',
                                             'crank',
                                             'repair'],
                                       method=Player.interact, 
                                       obj=obj, 
                                       tile=tile)


class Use(Action):
    def __init__(self, item):
        super(Use, self).__init__(name['use',
                                       'cut',
                                       'mix',
                                       'read',
                                       'combine'],
                                  method=Player.use, item=item)


class Look(Action):
    def __init__(self, obj, tile):
        super(Look, self).__init__(name=['look',
                                         'look at',
                                         'view',
                                         'inspect'],
                                   method=Player.look, obj=obj, tile=tile)


class Equip(Action):
    def __init__(self, item):
        super(Equip, self).__init__(name=['equip',
                                          'wear',
                                          'put on'],
                                    method=Player.Equip, item=item)



class Heal(Action):
    def __init__(self):
        super(Heal, self).__init__(name=['heal'],
                                   method=Player.heal)



class Help(Action):
    def __init__(self):
        super(Help, self).__init__(name=['help'],
                                   method=Player.helpme)

