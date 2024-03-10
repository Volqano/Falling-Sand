import pygame as pg
from game.map import *

pg.init()

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Falling sand simulator")

def main():

    BACKGROUND_COLOR = (0, 0, 0)
    SAND_COLOR = (217, 170, 85)
    colors = [BACKGROUND_COLOR, SAND_COLOR]
    map = Map(64, colors, screen)

    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        map.draw_map()
        pg.display.flip()
        pg.time.Clock().tick(60)

    pg.quit()

main()
