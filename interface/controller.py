# so the controller will have a game object (can be null)
from creation_settings import CreationSettings
from game_settings import GameSettings
import math
 

from typing import Any, List
from model.character import Character
from model.map import Map, Region, Tile
from model.game import Game

class Controller:
    def __init__(self) -> None:
        self.game: Game = Game()
        self.map: Map = self.game.map

    @classmethod
    def load_game(cls, game: Game):
        return Controller()

    @classmethod
    def new_game(cls, game_settings: GameSettings, creation_settings: CreationSettings):
        return Controller()
    
    '''
    Map functions
    '''
    def getRegion(self, x: float, y: float):
        return Region()

    def getTile(self, x: float, y: float) -> Tile:
        return Tile()

    def isAvailable(self, x: float, y: float):
        return self.map.isPassable(x, y)

    '''
    Character functions
    '''
    def moveCharacter(self, toMove: Character, direction: float, hertz: float = 1) -> bool:
        x = math.cos(2*math.pi * direction)
        y = math.sin(2*math.pi * direction)

        curX: float = toMove.getX()
        curY: float = toMove.getY()

        tempX: float = x * 1 / hertz + curX
        tempY: float = y * 1 / hertz + curY

        if self.isAvailable(tempX, tempY):
            toMove.setX(tempX)
            toMove.setY(tempY)
            return True
        return False
    
        