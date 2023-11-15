import sorts
from sorts import Sortable
import pygame as pg
pg.init()

ELEMENTS = 16
WINDOW_SIZE = 1200, 800
FILL_COLOR = 0, 0, 0

display = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Sorting Algorithm Visualizer - Merge Sort")

img = pg.image.load("sorting_window_icon.png")
pg.display.set_icon(img)

font = pg.font.SysFont("Arial", 24)

data_length = 1024
starting_data = list(range(2, data_length + 2))
sortable = Sortable.generate_random(starting_data)
sort = sorts.MergeSort().run(sortable)

rectangle_width = 1
rectangle_margin = 0
rectangle_scale = 0.6
rectangle_floor = 50

stepping = False
step = False
colored = {}

clock = pg.time.Clock()
run = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                stepping = not stepping
    
    if stepping:
        step = next(sort, None)

        colored = {}
        for position, color in sortable.colored:
            colored[position] = color


    if step is None:
        stepping = False
        step = "Done"
    
    if not run:break

    display.fill(FILL_COLOR)

    text_surface = font.render(f"{data_length} Element List", True, (255, 255, 255))
    display.blit(text_surface, (25, 25))

    text_surface = font.render(f"Timestep: {sortable.steps}", True, (255, 255, 255))
    display.blit(text_surface, (25, 50))
    
    for position, value in enumerate(sortable.data):
        color = colored[position] if position in colored else (255, 255, 255)
        color = (0, 255, 0) if step == "Done" else color
        pg.draw.rect(display, color, pg.Rect(((rectangle_width + rectangle_margin) * position + 50, WINDOW_SIZE[1] - rectangle_floor - rectangle_scale * value), (rectangle_width, rectangle_scale * value)))

    pg.display.update()
    #clock.tick(120)
pg.quit()