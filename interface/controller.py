# so the controller will have a game object (can be null)
from creation_settings import CreationSettings
from game_settings import GameSettings
from typing import Any, List
class Controller:
    def __init__(self) -> None:
        pass

    @classmethod
    def load_game(cls, game):
        return Controller()

    @classmethod
    def new_game(cls, game_settings: GameSettings, creation_settings: CreationSettings):
        return Controller()