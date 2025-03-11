from model.map import Map, Region, Tile
from model.character import Character
from typing import List

class Game:
    def __init__(self):
        self.characters: List[Character] = []
        self.map: Map = Map()

    def addCharacter(self, character: Character):
        self.characters.append(character)

    def __str__(self):
        return "U"