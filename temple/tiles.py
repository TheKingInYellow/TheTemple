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


class HoldingCell(MapTile):
    def intro_text(self):
        return """
        You awake in a cold, glass cell. You're slightly hungover and your
        fatigues smell funny. Nearby, the cell door is ajar.
        """

    def alter_player(self, the_player):
        # room has no action on player
        pass


class Corridor(MapTile):
    def intro_text(self):
        return """
        You are in an unremarkable corridor. Dim lights guide the pathway
        along the floor.
        """

    def alter_player(self, the_player):
        pass

class Brig(MapTile):
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
