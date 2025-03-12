from typing import List
import math

"""
Class: Map
More info later
"""


class Tile:
    impassable: List[str] = ["river", "mountain"]
    def __init__(self, terr: str = "grassy"):
        self.terrain: str = terr

    def isPassable(self):
        return self.terrain not in Tile.impassable
    
    def __str__(self):
        terr = self.terrain
        if terr == "grassy":
            return " "
        elif terr == "river":
            return "~"
        elif terr == "mountain":
            return "^"
        else:
            return terr[0]


class Region:
    def __init__(self):
        self.rows: int = 100
        self.cols: int = 100
        self.grid: List[List[Tile]] = []
        for _ in range(self.rows):
            self.grid.append([])


class Map:
    def __init__(self, x: int = 1, y: int = 1, z: int = 1):
        self.grid: List[List[Region]] = []
        self.rows: int = x
        self.cols: int = y
        self.regionSize: int = z

    def convertToIndices(self, x: float, y: float):
        globalX = math.floor(x + .5)
        globalY: int = math.floor( y + .5)
        blockSize = self.regionSize
        block_x = math.floor(globalX / blockSize)
        block_y = math.floor(globalY / blockSize)
        tile_x = globalX % blockSize
        tile_y = globalY % blockSize

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

            for line in lines:
                for char in line:
                    print(char, end = " ")
                print()
        return



def main():
    Map().importMap()

if __name__ == "__main__":
    main()