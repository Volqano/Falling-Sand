import pygame as pg


class Element:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def change_position(self, sr, x1, y1, x2, y2):
        sr.surface[y1][x1] = sr.surface[y2][x2]
        sr.surface[y2][x2] = self
        if isinstance(sr.surface[y1][x1], Element):
            sr.surface[y1][x1].x = x1
            sr.surface[y1][x1].y = y1
        self.y = y2
        self.x = x2


