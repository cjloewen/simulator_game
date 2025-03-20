from typing import List
from map import Map, Region, Tile
from biomes import terrains, biomes
import random

def chooseRandomTerrain():
    return terrains[random.randint(0, len(terrains) - 1)]

def chooseWeightedRandomTerrain():
    map = biomes["grassland"]
    weights = [map[terrain] for terrain in terrains]
    ter = random.choices(terrains, weights = weights, k = 1)
    return ter[0]

terrainGenerator = chooseWeightedRandomTerrain

def generateMap(mapSize: int, regionSize: int):
    map: Map = Map(mapSize, mapSize, regionSize)
    tempGrid: List[List[Region]] = []
    for row in range(0, mapSize):
        tempRow: List[Region] = []
        for region in range(0, mapSize):
            tempRow.append(generateRegion(regionSize))
        tempGrid.append(tempRow)
    map.grid = tempGrid
    
    return map

def generateRegion(size: int):
    region: Region = Region(size)
    tempGrid: List[List[Tile]] = []
    for row in range(0, size):
        tempRow: List[Tile] = []
        for tile in range(0, size):
            tempRow.append(Tile(terrainGenerator()))
        tempGrid.append(tempRow)
    region.grid = tempGrid

    return region

def printMap(map: Map):
    for row in range(0, map.rows):
        for col in range(0, map.cols):
            printRegion(map.grid[row][col])
    return

def printRegion(region: Region):
    for row in range(0, region.rows):
        for col in range(0, region.cols):
            print(region.grid[row][col], end = "")
        print()
    print()





def main():
    map = generateMap(1, 100)
    printMap(map)

if __name__ == "__main__":
    main()