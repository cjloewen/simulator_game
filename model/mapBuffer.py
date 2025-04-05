from model.map import Map, Region, Tile
from model.game import Game
from model.character import Character
from typing import List, Tuple, Dict
import math

'''
File:       mapBuffer.py
Purpose:    Holds buffers to streamline/optimize what amount of the game is actively being updated and viewed.

TODO: put all the common annoying index/coordinate math somewhere else, like a library
Maybe make a class for x,y coordinates to also have logic for translating to and from global stuff.

Essentially a buffer of what part of the map is actually "loaded"
For now, this is just for displaying the map (I think it should just be the whole buffer?)
Later, it should either also update everything within it, or have a sister class that deals with that
IMPORTANT: MAP BUFFER SHOULD NOT BE ALLOWED TO CHANGE THE MAP/REGION/TILE DATA

Units are scarce, so they are accessed and then their x,y is gotten
Tiles are are dense, so they are accessed by x,y
So the generation will be maps, then characters ontop. Tiles should also know when a building is on them

NOTE: The controller/view will actually be getting tile and character data, so when something changes, we do not need 
to regenerate, the reference will update all the way up to the view.
This is potentially bad because the view can change the game data, try to find a way to make it view only.
'''


'''
Name:       Buffer
Purpose:    Runs a small window of the game to decide which things need to actively be updated
            This hopefully allows the game to run and transition smoothly as the user navigates the world.
Usage:      Used with the controller, the controller will create and use buffers to update portions of the world
            as well as return pertinent data to the view.
'''
class Buffer:
    def __init__(self, x: int, y: int, size: int, game: Game):
        self.centerX: int = 0
        self.centerY: int = 0
        self.size = size

        self.game = game
        self.unit: UnitBuffer = UnitBuffer(game.characters, size)
        self.map: MapBuffer = MapBuffer(game.map, size)
    

    def setCenter(self, centerX: int, centerY: int):
        self.centerX = centerX
        self.centerY = centerY 

    '''
    Usage:  Call whenever main character is approaching the bounds of the buffer
            It may be smart to have a secondary buffer loading in when it is probable
            that the user may leave, that way, when the user does leave, it can seamlessly
            transition to the other buffer
    '''
    def regenerateBuffer(self):
        self.unit.regenerateBuffer(self.centerX, self.centerY)
        self.map.regenerateBuffer(self.centerX, self.centerY)

    '''
    Usage:  Call to give out orders to 'active' objects in the buffer
            The rate is in hz, and the default is 1 (very slow)
    '''
    def tick(self, rate: float = 1):
        self.unit.tick(rate)

    def getMapView(self):
        return self.map.grid
    
    def getCharOverlay(self):
        return self.unit.buffer


'''
Name:       UnitBuffer
Purpose:    The unit specific portion of the buffer
Usage:      Used by the main buffer class in this file
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
    
    '''
    Usage: Called each refresh to give orders to 'active' characters
    '''
    def tick(self, rate: float=1):
        for char in self.characters:
            pass
            # eventually this will run each characters script


'''
Name:       MapBuffer
Purpose:    The map/tile specific portion of the buffer
Usage:      Used by the main buffer class in this file
'''
class MapBuffer:
    def __init__(self, map: Map, size: int):
        self.map = map
        self.size = size
        self.grid: List[List[Tile]] = []
        for _ in range(self.size):
            self.grid.append([])

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