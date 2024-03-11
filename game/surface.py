import pygame as pg
from game.element import *


class Surface:
    def __init__(self, size, color, screen):
        self.size = size
        self.color1 = color[0] #Color for background
        self.color2 = color[1] #Color for sand
        self.screen = screen
        self.square_size = screen.get_width() / size
        self.surface = [[None] * size for _ in range(size)]
        self.surface[5][4] = Element(5, 4, color[1])

    def draw_surface(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.surface[i][j] == None:
                    pg.draw.rect(self.screen, self.color1,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.surface[i][j].color,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))


