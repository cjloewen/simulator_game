from typing import Dict
from typing import List

terrains: List[str] = ["grass", "river", "tree", "mountain"]
impassable: List[str] = ["river", "mountain"]
biomes: Dict[str, Dict[str, float]] = {}

biomes["grassland"] = {
        "grass": .85,
        "river": .05,
        "tree": .1,
        "mountain": 0,
}

biomes["forest"] = {
        "grass": .4,
        "river": .2,
        "tree": .4,
        "mountain": 0.,
}

biomes["mountain"] = {
        "grass": 0,
        "river": 0,
        "tree": 0,
        "mountain": 0,
}