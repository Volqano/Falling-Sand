import random

from game.solid import *
from game.element import *


class Liquid(Element):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    # def move(self, sr):
    #     if self.y + 1 < sr.size:
    #         if not sr.surface[self.y + 1][self.x]:
    #             self.change_position(sr, self.x, self.y, self.x, self.y + 1)
    #         else:
    #             x1 = self.x - 1
    #             x2 = self.x + 1
    #             while x1 != 0 and x2 != sr.size - 1:
    #                 if isinstance(sr.surface[self.y][x1], Element):
    #                     self.change_position(sr, self.x, self.y, self.x + 1, self.y)
    #                     return
    #                 elif isinstance(sr.surface[self.y][x2], Element):
    #                     self.change_position(sr, self.x, self.y, self.x - 1, self.y)
    #                     return
    #                 elif not sr.surface[self.y + 1][x1]:
    #                     self.change_position(sr, self.x, self.y, self.x - 1, self.y)
    #                     return
    #                 elif not sr.surface[self.y + 1][x2]:
    #                     self.change_position(sr, self.x, self.y, self.x + 1, self.y)
    #                     return
    #                 x1 -= 1
    #                 x2 += 1
    #             if x2 == sr.size - 1:
    #                 self.change_position(sr, self.x, self.y, self.x - 1, self.y)
    #             # elif x1 == 0:
    #             else:
    #                 self.change_position(sr, self.x, self.y, self.x + 1, self.y)

    def move(self, sr):
        if self.y + 1 < sr.size:
            if not sr.surface[self.y + 1][self.x]:
                self.change_position(sr, self.x, self.y, self.x, self.y + 1)
            else:
                choice = [(self.x + 1 < sr.size and (not sr.surface[self.y][self.x + 1]), 1),
                          (self.x > 0 and not sr.surface[self.y][self.x - 1], -1)]
                random.shuffle(choice)
                condition1, direction1 = choice[1]
                condition2, direction2 = choice[0]
                if condition1:
                    self.change_position(sr, self.x, self.y, self.x + direction1, self.y)
                elif condition2:
                    self.change_position(sr, self.x, self.y, self.x + direction2, self.y)
