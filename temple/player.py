"""
PLAYER CLASS

Class holding all information about the player.
"""

from random import randint
import items, tiles


class Player:
    inventory = [items.VoidKnuckles()]
    hp = 100
    maxhp = 100
    loc_x, loc_y = (2, 11)
    victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        print 'Player Inventory\n---------------'
        for item in self.inventory:
            print item
        print '\n'


    def move(self, dx, dy):
        self.loc_x += dx
        self.loc_y += dy

    def move_astern(self):
        self.move(dx=-1, dy=0)

    def move_aport(self):
        self.move(dx=0, dy=-1)

    def move_fore(self):
        self.move(dx=1, dy=0)

    def move_astar(self):
        self.move(dx=0, dy=1)


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
            if not best_weapon:
                best_weapon = 
            
        print "You attack with the {}.".format(best_weapon.name)
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print "You killed the {}!".format(enemy.name)
        else:
            print "You hit the {}!\n\tYour HP is {}\n\t" \
                + "Enemy's HP is {}\n".format(enemy.name, self.hp, enemy.hp)


    def flee(self, tile):
        """
        Moves player to a randomly adjacent tile.
        """
        available_moves = tile.adjacent_moves()
        r = randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
        print "You have fled."


    def eat(self, food):
        if isinstance(food, items.Food):
            food.eat()
            self.inventory.remove(food)


    def heal(self):
        num = 0
        for i in self.inventory:
            if isinstance(i, items.MedPack):
               num += 1

        if num > 0:
            self.hp += 20
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            self.inventory.remove(items.MedPack)


    def unlock(self, tile):
        tile.unlock()


    
