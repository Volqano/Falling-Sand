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
        if self.x != 0:
            if sr[self.y + 1][self.x] == None:
                self.y += 1


