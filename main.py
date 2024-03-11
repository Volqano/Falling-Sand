import pygame as pg
from game.surface import *

pg.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Falling sand simulator")

def main():

    BACKGROUND_COLOR = (0, 0, 0)
    SAND_COLOR = (217, 170, 85)
    size = 128
    colors = [BACKGROUND_COLOR, SAND_COLOR]
    sr = Surface(size, colors, screen)

    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        sr.draw_surface()
        pg.display.flip()
        pg.time.Clock().tick(60)

    pg.quit()

main()
