import pygame as pg

class Surface:
    def __init__(self, size, color, screen):
        self.size = size
        self.color1 = color[0] #Color for background
        self.color2 = color[1] #Color for sand
        self.screen = screen
        self.square_size = screen.get_width() / size
        self.surface = [[0] * size for _ in range(size)]
        self.surface[5][4] = 1

    def draw_surface(self, size):
        for i in range(size):
            for j in range(size):
                if self.surface[i][j] == 0:
                    pg.draw.rect(self.screen, self.color1,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))
                else:
                    pg.draw.rect(self.screen, self.color2,
                                 (i * self.square_size, j * self.square_size, self.square_size, self.square_size))


