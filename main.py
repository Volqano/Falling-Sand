import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Falling sand simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def main():
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.fill(WHITE)
        pg.time.Clock().tick(60)

    pg.quit()

main()