import pygame as pg
import random
from game.element import *
from game.solid import *
from game.liquid import *
from game.colors import colors


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
                if not self.surface[i][j]:
                    pg.draw.rect(self.screen, self.color1,
                                 (j * self.square_size, i * self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.surface[i][j].color,
                                 (j * self.square_size, i * self.square_size, self.square_size, self.square_size))

    def move_elements(self, sr):
        for i in range(self.size - 1, -1, -1):
            decide = [True, False]
            random.shuffle(decide)
            if decide[0]:
                for j in range(self.size):
                    if self.surface[i][j]:
                        self.surface[i][j].move(sr)
            else:
                for j in range(self.size - 1, -1, -1):
                    if self.surface[i][j]:
                        self.surface[i][j].move(sr)

    def paint_on_surface(self, res, element):
        pos = pg.mouse.get_pos()
        pos_x = pos[0] // (res // self.size)
        pos_y = pos[1] // (res // self.size)
        if not self.surface[pos_y][pos_x]:
            if element == "sand":
                self.surface[pos_y][pos_x] = MovableSolid(pos_x, pos_y, random.choice(colors[element]))
            elif element == "water":
                self.surface[pos_y][pos_x] = Liquid(pos_x, pos_y, random.choice(colors[element]))
            elif element == "stone":
                self.surface[pos_y][pos_x] = ImmovableSolid(pos_x, pos_y, random.choice(colors[element]))
        if element == "eraser":
            self.surface[pos_y][pos_x] = None

    def reset(self):
        self.surface = [[None] * self.size for _ in range(self.size)]


