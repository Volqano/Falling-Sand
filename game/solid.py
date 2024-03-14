from game.element import *
from game.liquid import *
import random


class Solid(Element):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class MovableSolid(Solid):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, sr):
        if self.y + 1 < sr.size:
            # Checking if a potentially empty place contains liquid or free space
            if not sr.surface[self.y + 1][self.x] or isinstance(sr.surface[self.y + 1][self.x], Liquid):
                self.change_position(sr, self.x, self.y, self.x, self.y + 1)
            else:
                choice = [((self.x + 1 < sr.size and (not sr.surface[self.y + 1][self.x + 1]
                            or isinstance(sr.surface[self.y + 1][self.x + 1], Liquid))), 1),
                          (self.x > 0 and (not sr.surface[self.y + 1][self.x - 1]
                            or isinstance(sr.surface[self.y + 1][self.x - 1], Liquid)), -1)]
                random.shuffle(choice)
                condition1, direction1 = choice[0]
                condition2, direction2 = choice[1]
                if condition1:
                    self.change_position(sr, self.x, self.y, self.x + direction1, self.y + 1)
                elif condition2:
                    self.change_position(sr, self.x, self.y, self.x + direction2, self.y + 1)


class ImmovableSolid(Solid):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def move(self, sr):
        return
