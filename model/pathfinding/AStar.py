from character import Character
from map import Tile
from typing import List, Tuple, Dict
from queue import Queue

def aStarPathfinding(moveDistance: int, grid: List[List[Tile]], start: Tuple[int, int], end: Tuple[int, int]):
    openList: List[Tuple[Tuple[int, int], int]] = [(start, 0)]
    closedList: List[Tuple[Tuple[int, int], int]] = []
    depth: int = 0
    prev: Dict[Tuple[int, int], Tuple[int, int]] = {}
    path: List[Tuple[int, int]] = []

    tempLowestFCostTile: Tuple[int, int] = start
    tempLowestFCost: int = getFCost(start, end, start)

    while len(openList) > 0:
        for tile in openList:
            curTileFCost: int = getFCost(start, end, tile[0])
            if curTileFCost < tempLowestFCost:
                tempLowestFCostTile = tile[0]
                tempLowestFCost = curTileFCost
        openList.remove((tempLowestFCostTile, openList))
        closedList.append((tempLowestFCostTile))

        if 



    return

def getNeighbors():

    return

def getFCost(start: Tuple[int, int], end: Tuple[int, int], curPos: Tuple[int, int]):
    gCost: int = calculateDistance(curPos[0], curPos[1], start[0], start[1])
    hCost: int = calculateDistance(curPos[0], curPos[1], end[0], end[1])

    return gCost + hCost

def calculateDistance(startX: int, startY: int, endX: int, endY: int):
    dstX: int = abs(endX - startX)
    dstY: int = abs(endY - startY)
    
    # 10 is horizontal / vertical unit distance; 14 is diagonal unit distance
    if(dstX > dstY):
        return 14 * dstY + 10 * (dstX - dstY)
    return 14 * dstX + 10 * (dstY - dstX)

def calculateDistance2(startX: int, startY: int, endX: int, endY: int):
    a: int = endX - startX
    b: int = endY - startY
    return a * a + b * b