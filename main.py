import sorts
from sorts import Sortable
from handler import VisualHandler, WINDOW_SIZE
import pygame as pg
pg.init()

handler = VisualHandler(sorts.MergeSort())

# Pygame Initializing
display = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption(f"Sorting Algorithm Visualizer - {handler.algorithm_name}")

img = pg.image.load("sorting_window_icon.png")
pg.display.set_icon(img)

clock = pg.time.Clock()
run = True
while True:

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:handler.paused = not handler.paused
            elif event.key == pg.K_r:handler.reset()
    
    if not run:break

    handler.update(display)
    clock.tick(10)
pg.quit()