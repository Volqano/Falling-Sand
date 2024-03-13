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
            choice = [((self.x + 1 < sr.size and not sr.surface[self.y + 1][self.x + 1]), 1),
                      ((not sr.surface[self.y + 1][self.x - 1]), -1)]
            random.shuffle(choice)
            condition1, direction1 = choice[0]
            condition2, direction2 = choice[1]
            if not sr.surface[self.y + 1][self.x]:
                self.change_position(sr, self.x, self.y, self.x, self.y + 1)
            elif condition1:
                self.change_position(sr, self.x, self.y, self.x + direction1, self.y + 1)
            elif condition2:
                self.change_position(sr, self.x, self.y, self.x + direction2, self.y + 1)

