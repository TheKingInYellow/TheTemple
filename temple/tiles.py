"""
TILES CLASS

Describes all of the of the tiles in the map.
"""

import characters
import items
import actions
import world

class MapTile:
    """
    The base class for a tile within the world space.
    """
    def __init__(self, x, y):
        """
        Creates a new tile.

        x :: x-coordinate of the tile.
        y :: y-coordinate of the tile.
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """
        Information to be displayed when the player moves onto this tile.
        """
        raise NotImplementedError()

    def alter_player(self, the_player):
        """
        Processes actions that change the state of the player.
        """
        raise NotImplementedError()

    def possible_moves(self):
        """
        Returns all possible move actions for adjacent tiles.
        """
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveAstern())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveFore())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveAstarboard())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveAport())
        return moves

    def available_actions(self):
        """
        Returns all available actions in the room.
        """
        moves = self.possible_moves()
        moves.append(actions.ViewInventory())

        return moves

    def look_around(self):
        """
        Opportunity to provide a more in-depth description of the room.
        """
        raise NotImplementedError()

    def help(self):
        """
        Returns a basic help dialogue.
        """
        return """
        Use commands like 'move _____' to move a particular direction. Note
        that directions are given relative to the ship's bearing; that is,
        to move one room towards the stern, the command 'go astern' would 
        work. Likewise for bow, port, and starboard, the directional words
        are 'fore / foreward', 'aport' and 'astarboard'. Type 'look around'
        in a room to get a better look at at your environment. 'Look at _____'
        will give a description of a particular object. Special rooms or items
        trigger special action keywords. For example, if you have a piece of
        food in your inventory, typing 'eat _____' would consume the piece of
        food and add a small bit of health. To pick up a piece of food, simply
        type 'take _____' or 'pick up _____'. Type 'view inventory' to view 
        what items you are currently carrying. Other common keywords include:
         - interaction with environment - 'push', 'pull', 'press', 'turn'
         - combat - 'attack', 'fight'
         - interaction with doors - 'unlock', 'open'
         - interaction with self - 'heal', 'equip', 'wear', 'eat'
         - interaction with other items - 'eat', 'read', 'cut'
         - interaction with inventory - 'view', 'pick up', 'take', 'drop'
         - directional movement - 'go', 'walk', 'travel', 'move'
        """


class HoldingCell(MapTile):
    def intro_text(self):
        return """
        You awake in a cold, glass cell. You're slightly hungover and your
        fatigues smell funny. Nearby, the cell door is ajar.
        """

    def alter_player(self, the_player):
        # room has no action on player
        pass

    def look_around(self):
        return """
        A small cot with a single pillow sits in the corner of the cell.
        Nearby, a small sink and vacuum toilet are attached to the walls. 
        The entrance of the cell is unlocked and open, but looking
        through the glass, you don't see any guard posted.
        """

class Corridor(MapTile):
    def intro_text(self):
        return """
        You are in an unremarkable corridor. Dim lights guide the pathway
        along the floor.
        """

    def alter_player(self, the_player):
        pass

class Brig(MapTile):
    def intro_text(self):
        return """
        You are in the Brig. A small desk is nearby. Atop it, a console.
        """

    def alter_player(self, the_player):
        pass

        
class CommandCentre(MapTile):
    pass
class CollapsedCorridor(MapTile):
    pass
class Communications(MapTile):
    pass
class Astrometrics(MapTile):
    pass
class StasisRoom(MapTile):
    pass
class CaptainsQuarters(MapTile):
    pass
class OfficersMessHall(MapTile):
    pass
class Galley(MapTile):
    pass
class MessHall(MapTile):
    pass
class Showers(MapTile):
    pass
class CargoHold(MapTile):
    pass
class Library(MapTile):
    pass
class ObservationDeck(MapTile):
    pass
class Barracks(MapTile):
    pass
class LivingQuarters(MapTile):
    pass
class Armoury(MapTile):
    pass
class WarRoom(MapTile):
    pass
class RecreationRoom(MapTile):
    pass
class Infirmary(MapTile):
    pass
class MedicalBay(MapTile):
    pass
class ShieldControl(MapTile):
    pass
class Morgue(MapTile):
    pass
class WasteManagement(MapTile):
    pass
class WeaponSystems(MapTile):
    pass
class PodHangar(MapTile):
    pass
class FusionStudies(MapTile):
    pass
class Laboratory(MapTile):
    pass
class BiotechStudies(MapTile):
    pass
class TurretDeck(MapTile):
    pass
class Airlock(MapTile):
    pass
class Hydroponics(MapTile):
    pass
class GravityControl(MapTile):
    pass
class EngineeringDeck(MapTile):
    pass
class EnvironmentalSystems(MapTile):
    pass
class WaterTreatment(MapTile):
    pass
class PowerSystems(MapTile):
    pass
class EngineRoom(MapTile):
    pass
