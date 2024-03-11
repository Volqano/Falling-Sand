from game.element import *

class Solid(Element):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

class MovableSolid(Solid):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, sr):
        if self.y + 1 < sr.size:
            if sr.surface[self.y + 1][self.x] == None:
                self.change_position(sr, self.x, self.y, self.x, self.y + 1)
            elif self.x + 1 < sr.size and sr.surface[self.y + 1][self.x + 1] == None:
                self.change_position(sr, self.x, self.y, self.x + 1, self.y + 1)
            elif sr.surface[self.y + 1][self.x - 1] == None:
                self.change_position(sr, self.x, self.y, self.x - 1, self.y + 1)

