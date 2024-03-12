from game.element import *
import random


class Solid(Element):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class MovableSolid(Solid):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, sr):
        if self.y + 1 < sr.size:
            direction = random.choice([-1, 1])
            if not sr.surface[self.y + 1][self.x]:
                self.change_position(sr, self.x, self.y, self.x, self.y + 1)
            elif self.x + 1 < sr.size and not sr.surface[self.y + 1][self.x + direction]:
                self.change_position(sr, self.x, self.y, self.x + direction, self.y + 1)
            elif self.x + 1 < sr.size and not sr.surface[self.y + 1][self.x - direction]:
                self.change_position(sr, self.x, self.y, self.x - direction, self.y + 1)

