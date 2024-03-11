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
        x = 20
        y = 5
        self.surface[y][x] = MovableSolid(x, y, color[1])

    def draw_surface(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.surface[i][j] == None:
                    pg.draw.rect(self.screen, self.color1,
                                 (j * self.square_size, i * self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.surface[i][j].color,
                                 (j * self.square_size, i * self.square_size, self.square_size, self.square_size))

    def move_elements(self, sr):
        for i in range(self.size - 1, -1, -1):
            for j in range(self.size):
                if self.surface[i][j] != None:
                    self.surface[i][j].move(sr)


