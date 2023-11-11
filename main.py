import pygame as pg
pg.init()

ELEMENTS = 16
WINDOW_SIZE = 800, 600
FILL_COLOR = 0, 0, 0

display = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Sorting Algorithm Visualizer")

clock = pg.time.Clock()
run = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
    
    if not run:break

    display.fill(FILL_COLOR)
    clock.tick(60)
pg.quit()