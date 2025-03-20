from typing import List
import math
from biomes import impassable

"""
Class: Map
More info later
Grid XY is actually rows columns, not cartesian (x,y), eventually can resolve this, maybe with the map buffer?
"""


class Tile:
    def __init__(self, terr: str = "grass"):
        self.terrain: str = terr

    def isPassable(self):
        return self.terrain not in impassable
    
    def __str__(self):
        terr = self.terrain
        if terr == "grass":
            return " "
        elif terr == "river":
            return "~"
        elif terr == "mountain":
            return "^"
        else:
            return terr[0]
    
    @classmethod
    def convertChar(cls, terr: str):
        if terr == " ":
            return Tile("grass")
        elif terr == "~":
            return Tile("river")
        elif terr == "^":
            return Tile("mountain")
        else:
            return Tile()

class Region:
    def __init__(self, x: int):
        self.rows: int = x
        self.cols: int = x
        self.grid: List[List[Tile]] = []
        for _ in range(self.rows):
            self.grid.append([])

    def getTile(self, x: int, y: int):
        return self.grid[y][x]

class Map:
    def __init__(self, x: int = 1, y: int = 1, regionSize: int = 1):
        self.grid: List[List[Region]] = []
        self.rows: int = x
        self.cols: int = y
        self.regionSize: int = regionSize

        #self.importMap()

    def getTile(self, x: float, y: float):
        x1,x2,y1,y2 = self.convertToIndices(x, y)
        return self.grid[y1][x1].getTile(x2, y2)


    def convertToIndices(self, x: float, y: float):
        size = self.regionSize
        globalX = math.floor(x + .5)
        globalY: int = math.floor( y + .5)
        blockSize = self.regionSize
        block_x = math.floor(globalX / blockSize)
        block_y = math.floor(globalY / blockSize)
        tile_x = globalX % blockSize
        tile_y = globalY % blockSize

        # convert global coordinates to actual array indices, index(0,0) is the top left of the map
        # also, x corresponds to the inner index, so it is indexed like array[y][x]
        block_x += self.rows // 2
        block_y = self.cols // 2 - block_y
        tile_x += size // 2 + tile_y
        tile_y = size // 2 - tile_y

        return (block_x, block_y, tile_x, tile_y)
    
    def isPassable(self, globalX: float, globalY: float):
        x, y, t_x, t_y = self.convertToIndices(globalX, globalY)
        region = self.grid[x][y]
        return region.grid[t_x][t_y].isPassable()

    def importMap(self):
        path = input("Enter map path: ")
        # path = ..\\maps\\test.txt

        with open(path, "r") as file:
            self.rows = int(file.readline())
            self.cols = int(file.readline())
            self.regionSize = int(file.readline())       
            lines = file.readlines()
            counter = 0
            curRegion = Region(self.regionSize)
            tempList = [curRegion]
            for line in lines:
                for char in line:
                    curTile: Tile = Tile.convertChar(char)
                    curRegion.grid[counter].append(curTile)
                counter += 1
                if counter == self.regionSize:
                    curRegion = Region(self.regionSize)
                    tempList.append(curRegion)
                    counter = 0

