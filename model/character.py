class Character:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def setX(self, x: float):
        self.x = x
    def setY(self, y: float):
        self.y = y
        