import pygame as pg
from game.surface import *

pg.init()

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Falling sand simulator")


def main():

    BACKGROUND_COLOR = (0, 0, 0)
    SAND_COLOR = (217, 170, 85)
    size = 128
    colors = [BACKGROUND_COLOR, SAND_COLOR]
    sr = Surface(size, colors, screen)

    run = True
    is_mouse_down = False

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                is_mouse_down = True
            elif event.type == pg.MOUSEBUTTONUP:
                is_mouse_down = False
        sr.draw_surface()
        if is_mouse_down:
            sr.paint_on_surface(SCREEN_HEIGHT)
        sr.move_elements(sr)
        pg.display.flip()
        pg.time.Clock().tick()

    pg.quit()

main()
