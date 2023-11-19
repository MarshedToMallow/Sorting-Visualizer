import pygame as pg
import sorts

from config import ELEMENTS, CANVAS_WIDTH, CANVAS_HEIGHT, WINDOW_SIZE, bar_width, filled_height

class VisualHandler:
    """Handles the sorting rendering.
    """
    def __init__(self, sorting_algorithm):

        # Initialize Sorting
        self.sortable = sorts.Sortable.generate_random(list(range(1, ELEMENTS + 1)))
        self.sorting_algorithm = sorting_algorithm
        self.algorithm_name = type(sorting_algorithm).__name__
        self.sort = sorting_algorithm.run(self.sortable)

        self.font = pg.font.SysFont("Arial", 24)

        self.paused = True
        self.new = True

    def update(self, display):

        if self.new:self.new = False # Allows rendering of the initial random state
        elif self.paused:return None # Ignores while paused

        # Pauses when sorted
        step = next(self.sort, None)
        if step is None:self.paused = True

        # Gets the colors for the active positions of the sortable
        colored = {}
        for position, color in self.sortable.colored:
            colored[position] = color

        display.fill((0, 0, 0))

        # Text Rendering
        element_count_text = self.font.render(f"{ELEMENTS} Element List", True, (255, 255, 255))
        display.blit(element_count_text, (25, 25))

        timestep_text = self.font.render(f"Timestep: {self.sortable.steps}", True, (255, 255, 255))
        display.blit(timestep_text, (25, 50))

        # Render each bar
        for position, value in enumerate(self.sortable.data):

            # Priority (High to Low): Solved (Green), Active (Depends), Default (White)
            color = colored[position] if position in colored else (255, 255, 255)
            color = (0, 255, 0) if step is None else color

            # Bar coordinates (Top Left)
            x = (bar_width * position) + (CANVAS_WIDTH[0] * WINDOW_SIZE[0])
            y = (WINDOW_SIZE[1] * CANVAS_HEIGHT[1]) - (filled_height * value)

            # Bar size
            width = bar_width + 1
            height = filled_height * value

            pg.draw.rect(display, color, pg.Rect((x, y), (width, height)))
        
        pg.display.update()

    def reset(self):
        self.paused = True
        self.new = True
        self.sortable = sorts.Sortable.generate_random(list(range(1, ELEMENTS + 1)))
        self.sort = self.sorting_algorithm.run(self.sortable)