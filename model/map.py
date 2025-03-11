from typing import List

"""
Class: Map
More info later
"""


class Tile:
    def __init__(self, terr: str = "grassy"):
        self.terrain: str = terr


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

    def importMap(self):
        path = input("Enter map path: ")
        # path = ..\\maps\\test.txt

        with open(path, "r") as file:
            self.rows = file.readline()
            self.cols = file.readline()
            self.regionSize = file.readline()        
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