import numpy as np


class GameOfLife:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=np.uint8)

    def update(self) -> None:
        current_gen = self.grid

        neighbors = self._count_neighbors(current_gen)
        birth_mask = (current_gen == 0) & (neighbors == 3)
        underpopulation_mask = (current_gen == 1) & (neighbors < 2)
        overpopulation_mask = (current_gen == 1) & (neighbors > 3)

        next_gen = self.grid.copy()
        next_gen[birth_mask] = 1
        next_gen[underpopulation_mask | overpopulation_mask] = 0
        self.grid = next_gen

    def set_cell(self, x: int, y: int, state: int) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y, x] = state

    @staticmethod
    def _count_neighbors(grid: np.ndarray) -> np.ndarray:

        neighbors = (
            np.roll(grid, 1, axis=0) +
            np.roll(grid, 1, axis=1) +
            np.roll(grid, -1, axis=0) +
            np.roll(grid, -1, axis=1) +
            np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
            np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
            np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
            np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
        )
        return neighbors

    def clear(self) -> None:
        self.grid.fill(0)


