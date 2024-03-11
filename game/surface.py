import pygame as pg
import random
from game.element import *
from game.solid import *

class Surface:
    def __init__(self, size, color, screen):
        self.size = size
        self.color1 = color[0] #Color for background
        self.color2 = color[1] #Color for sand
        self.screen = screen
        self.square_size = screen.get_width() / size
        self.surface = [[None] * size for _ in range(size)]

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

    def paint_on_surface(self):
        pos = pg.mouse.get_pos()
        pos_x = pos[0] // 6
        pos_y = pos[1] // 6
        sand_colors = [(242, 194, 136), (242, 200, 121), (242, 208, 167)]
        self.surface[pos_y][pos_x] = MovableSolid(pos_x, pos_y, random.choice(sand_colors))


