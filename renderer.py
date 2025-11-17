import pygame
import numpy as np


class Renderer:
    def __init__(
            self,
            screen: pygame.Surface,
            cell_size: int,
            cell_color: tuple,
            grid_color: tuple,
            bg_color: tuple,
    ):
        self.screen = screen
        self.cell_size = cell_size
        self.width, self.height = screen.get_size()

        self.colors = {
            "cell": cell_color,
            "grid": grid_color,
            "bg": bg_color
        }

    def draw(self, game: 'GameOfLife', draw_grid_lines: bool = True):
        self.screen.fill(self.colors["bg"])

        self._draw_cells(game.grid)

        if draw_grid_lines and self.cell_size > 4:
            self._draw_grid_lines()

    def _draw_cells(self, grid: np.ndarray):
        for y, x in np.argwhere(grid == 1):
            rect = pygame.Rect(
                x * self.cell_size,
                y * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, self.colors["cell"], rect)

    def _draw_grid_lines(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.colors["grid"], (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.colors["grid"], (0, y), (self.width, y))

    def get_grid_coords_from_mouse(self, mouse_pos: tuple[int, int]) -> tuple[int, int]:
        x_pixel, y_pixel = mouse_pos
        x_grid = x_pixel // self.cell_size
        y_grid = y_pixel // self.cell_size
        return x_grid, y_grid
