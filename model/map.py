from typing import List

"""
Class: Map
More info later
"""


class Terrain:
    def __init__(self, geo: str = "grassy"):
        self.geography: str = geo


class Tile:
    def __init__(self):
        self.rows: int = 100
        self.cols: int = 100
        self.grid: List[List[Terrain]] = []
        for _ in range(self.rows):
            self.grid.append([])


class Map:
    def __init__(self, x: int = 1, y: int = 1):
        self.grid: List[List[Tile]] = []
        self.rows: int = x
        self.cols: int = y
