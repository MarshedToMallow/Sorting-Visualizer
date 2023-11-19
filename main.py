import sorts
from handler import VisualHandler
from config import WINDOW_SIZE, SORT
import pygame as pg
pg.init()

handler = VisualHandler(SORT())

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
            if event.key == pg.K_SPACE:handler.paused = not handler.paused # Pause/Play
            elif event.key == pg.K_r:handler.reset() # Reset (Start over from new random list)
    
    if not run:break

    handler.update(display)
    #clock.tick(60) # Steps per second
pg.quit()