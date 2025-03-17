from model.map import Map, Region, Tile
from model.character import Character
from typing import List, Tuple, Dict
import math

'''
Essentially a buffer of what part of the map is actually "loaded"
For now, this is just for displaying the map (I think it should just be the whole buffer?)
Later, it should either also update everything within it, or have a sister class that deals with that
IMPORTANT: MAP BUFFER SHOULD NOT BE ALLOWED TO CHANGE THE MAP/REGION/TILE DATA
'''

class Buffer:
    def __init__(self):
            self.centerX: int = 0
            self.centerY: int = 0

class unitBuffer:
    def __init__(self):
        self.characters: List[Character] = []
        self.positions: Dict[Character, Tuple[int, int]] = {}

class MapView:
    def __init__(self, map: Map, size: int):
        self.map = map
        self.size = size
        self.grid: List[List[Tile]] = []
        for _ in range(self.size):
            self.grid.append([])


    '''
    If the map itself changes (for whatever reason)
    Or when the center moves too far away, and we get close to the edge of memory
    '''
    def regenerateBuffer(self, centerX: int, centerY: int):
        map = self.map
        size = self.size
        counterY = 0
        for x in range(centerX - math.floor(size / 2), centerX + math.ceil(size / 2)):
            for y in range(centerY + math.ceil(size / 2), centerY - math.floor(size / 2), -1):
                curTile = map.getTile(x, y)
                self.grid[counterY].append(curTile)
            counterY += 1

    def getStringRep(self):
        pass

    # granularity of tiles?
    def getMapRange(self):
        pass