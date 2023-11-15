import random
from sorts import Sortable, SelectionSort
import pygame as pg
pg.init()

ELEMENTS = 16
WINDOW_SIZE = 800, 600
FILL_COLOR = 0, 0, 0

display = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Sorting Algorithm Visualizer")

data_length = 128
starting_data = list(range(2, data_length + 2))
sortable = Sortable.generate_random(starting_data)
sort = SelectionSort().run(sortable)

stepping = True

clock = pg.time.Clock()
run = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
    
    if stepping:
        step = next(sort, None)

        colored = {}
        for position, color in sortable.colored:
            colored[position] = color

    elif step is None:
        stepping = False
        step = "Done"

    
    if not run:break

    display.fill(FILL_COLOR)
    
    for position, value in enumerate(sortable.data):
        color = colored[position] if position in colored else (255, 255, 255)
        color = (0, 255, 0) if step is None else color
        pg.draw.rect(display, color, pg.Rect((5 * position + 50, WINDOW_SIZE[1] - 100 - 3 * value), (4, 3 * value)))

    pg.display.update()
    #clock.tick(120)
pg.quit()