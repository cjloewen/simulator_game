from model.map import Map, Region, Tile


'''
Essentially a buffer of what part of the map is actually "loaded"
For now, this is just for displaying the map
Later, it should either also update everything within it, or have a sister class that deals with that
'''
class MapView:
    def __init__(self, map: Map, size: int):
        self.map = Map
        self.size = size
        self.centerX: float = 0
        self.centerY: float = 0

    def setCenter(self, x: float, y: float):
        self.centerX = x
        self.centerY = y

    '''
    If the map itself changes (for whatever reason)
    Or when the center moves too far away, and we get close to the edge of memory
    '''
    def regenerateBuffer(self):
        pass

    def getStringRep(self):
        pass

    # granularity of tiles?
    def getMapRange(self):
        pass