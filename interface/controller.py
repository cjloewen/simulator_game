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
        game: Game = Game()

    @classmethod
    def load_game(cls, game: Game):
        return Controller()

    @classmethod
    def new_game(cls, game_settings: GameSettings, creation_settings: CreationSettings):
        return Controller()
    
    '''
    Map functions
    '''
    def getRegion(self, x: int, y: int):
        return Region()

    def getTile(self, x: int, y: int) -> Tile:
        return Tile()

    def isAvailable(self, x: float, y: float):
        globalX = math.floor(x + .5)
        globalY: int = math.floor( y + .5)
        tile = self.getTile(globalX, globalY)
        return True

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
    
        