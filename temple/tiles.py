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
            moves.append(actions.MoveFore())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveAstern())
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


class HoldingCell(MapTile):
    def intro_text(self):
        return """
        You awake in a cell...
        """

    def modify_player(self, the_player):
        # room has no action on player
        pass


        
class Corridor(MapTile):
    def intro_text(self):
        return """
        You are in an unremarkable corridor. Dim lights guide the pathway
        along the floor.
        """

    def modify_player(self, the_player):
        pass

class Brig(MapTile):
    def intro_text(self)

class ControlCentre(MapTile):

class Communications(MapTile):

class AstroMetrics(MapTile):

class StasisRoom(MapTile):

class OfficersMess(MapTile):

class Galley(MapTile):

class MessHall(MapTile):

class Showers(MapTile):

class CargoHold(MapTile):

class Library(MapTile):

class ObservationDeck(MapTile):

class Barracks(MapTile):

class LivingQuarters(MapTile):

class Armoury(MapTile):

class WarRoom(MapTile):

class RecreationRoom(MapTile):

class Infirmary(MapTile):

class MedicalBay(MapTile):

class ShieldControl(MapTile):

class Morgue(MapTile):

class WasteManagement(MapTile):

class WeaponSystems(MapTile):

class PodHangar(MapTile):

class FusionStudies(MapTile):

class Laboratory(MapTile):

class BioTechStudies(MapTile):

class TurretDeck(MapTile):

class Airlock(MapTile):

class Hydroponics(MapTile):

class GravityControl(MapTile):

class EngineeringDeck(MapTile):

class EnviroSysems(MapTile):

class WaterTreatment(MapTile):

class PowerSystems(MapTile):

class EngineRoom(MapTile):
