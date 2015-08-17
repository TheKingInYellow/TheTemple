"""
WORLD CLASS

Loads all tiles in the world space.
"""
import csv
import tiles

_world = {}

def tile_exists(x, y):
    """
    Returns the tile at the given coordinates, or None if there is no tile.

    x :: x-coordinate in the world space
    y :: y-coordinate in the world space
    """
    return _world.get((x,y))


def load_tiles():
    """
    Parses a csv file that describes the world space into the _world object.
    """
    rdr = csv.reader(open('../resources/blueprint.csv', 'r'), delimiter=',')
    world = list(reader)

    for i, row in enumerate(world):
        for j, room in enumerate(row):
            if room == "":
                room = None
            else:
                room = getattr(tiles, room)(x,y)
            _world[(i,j)] = room
            
