import pygame as pg

class Element:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Solid(Element):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

class MovableSolid(Solid):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, sr):
        if self.y + 1 < sr.size:
            if sr.surface[self.y + 1][self.x] == None:
                sr.surface[self.y][self.x] = None
                self.y += 1
                sr.surface[self.y][self.x] = self


