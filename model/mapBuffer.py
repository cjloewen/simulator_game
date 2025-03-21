from model.map import Map, Region, Tile
from model.character import Character
from typing import List, Tuple, Dict
import math

'''
TODO: put all the common annoying index/coordinate math somewhere else, like a library
Maybe make a class for x,y coordinates to also have logic for translating to and from global stuff.
'''
'''
Essentially a buffer of what part of the map is actually "loaded"
For now, this is just for displaying the map (I think it should just be the whole buffer?)
Later, it should either also update everything within it, or have a sister class that deals with that
IMPORTANT: MAP BUFFER SHOULD NOT BE ALLOWED TO CHANGE THE MAP/REGION/TILE DATA
'''

class Buffer:
    def __init__(self, size: int, characters: List[Character], map: Map):
        self.centerX: int = 0
        self.centerY: int = 0
        self.unit: UnitBuffer = UnitBuffer(characters, size)
        self.map: MapBuffer = MapBuffer(map, size)
    

    def setCenter(self, centerX: int, centerY: int):
        self.centerX = centerX
        self.centerY = centerY 

    def regenerateBuffer(self):
        self.unit.regenerateBuffer(self.centerX, self.centerY)
        self.map.regenerateBuffer(self.centerX, self.centerY)
        
    '''
    Units are scarce, so they are accessed and then their x,y is gotten
    Tiles are are dense, so they are accessed by x,y
    So the generation will be maps, then characters ontop. Tiles should also know when a building is on them
    '''

'''
For now, just use all characters in the game for this, there shouldn't be enough for it to be a problem yet
'''
class UnitBuffer:
    def __init__(self, characters: List[Character], size: int):
        self.characters: List[Character] = characters
        self.buffer: List[Character] = []
        self.size = size

    def regenerateBuffer(self, centerX: int, centerY: int):
        characters = self.characters
        size = self.size
        minX = centerX - math.floor(size / 2)
        maxX = centerX + math.ceil(size / 2)
        maxY = centerY + math.ceil(size / 2)
        minY = centerY - math.floor(size / 2)

        for character in characters:
            x, y = character.getX(), character.getY()
            
            if x > minX and x < maxX and y < maxY and y > minY:
                self.buffer.append(character)


        

class MapBuffer:
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