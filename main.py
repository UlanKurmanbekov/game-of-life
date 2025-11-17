import numpy as np
import matplotlib.pyplot as plt

import patterns


class GameOfLife:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height), dtype=np.uint8)

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

    def spawn_cell(self, x: int, y: int) -> None:
        self.grid[x][y] = 1

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


width, height = list(map(int, input('Enter the field size (separated by a space): ').split())) or [50, 50]
while width < 50 or height < 50:
    print("The width and height can't be less than 50 cells")
    width, height = list(map(int, input('Enter the field size (separated by a space): ').split()))

xticks = [i - 0.5 for i in range(width + 1)]
yticks = [i - 0.5 for i in range(height + 1)]

g = GameOfLife(width, height)

for x, y in patterns.GLIDER:
    g.spawn_cell(x, y)

plt.ion()
fig, ax = plt.subplots()

for generation in range(1000):
    ax.clear()
    ax.set_xticks(xticks, [])
    ax.set_yticks(yticks, [])
    ax.grid(color='black', linestyle='-', linewidth=0.5)
    ax.set_title(f'Generation: {generation}')
    ax.imshow(g.grid, cmap='binary')
    plt.pause(0.1)
    g.update()
plt.ioff()
plt.show()
