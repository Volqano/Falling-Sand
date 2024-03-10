import pygame as pg

class Map:
    def __init__(self, size, color, screen):
        self.size = size
        self.color1 = color[0] #Color for background
        self.color2 = color[1] #Color for sand
        self.screen = screen
        self.square_size = screen.get_width() / size
        self.map = [[0] * 64 for _ in range(64)]
        self.map[5][4] = 1

    def draw_map(self):
        for i in range(64):
            for j in range(64):
                if self.map[i][j] == 0:
                    pg.draw.rect(self.screen, self.color1,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.color2,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))


