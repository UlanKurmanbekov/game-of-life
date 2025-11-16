import matplotlib.pyplot as plt

import patterns


class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]

    def update(self):
        current_gen = [row[:] for row in self.grid]
        next_gen = [row[:] for row in self.grid]

        for i in range(self.height):
            for j in range(self.width):
                cnt = self.counter(i, j, current_gen)

                if cnt == 3:
                    next_gen[i][j] = 1
                elif cnt < 2 or cnt > 3:
                    next_gen[i][j] = 0

        self.grid = next_gen

    def get_grid(self):
        for vector in self.grid:
            print(vector)

        print('\n\n\n\n')

    def seed(self, x, y):
        self.grid[x][y] = 1

    def counter(self, x, y, curr_gen: list[list[int]]):
        cnt = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor_x = (x + i) % self.height
                neighbor_y = (y + j) % self.width
                cnt += curr_gen[neighbor_x][neighbor_y]
        return cnt


width, height = list(map(int, input('Enter the field size (separated by a space): ').split())) or [50, 50]
while width < 50 or height < 50:
    print("The width and height can't be less than 50 cells")
    width, height = list(map(int, input('Enter the field size (separated by a space): ').split()))

xticks = [i - 0.5 for i in range(width + 1)]
yticks = [i - 0.5 for i in range(height + 1)]

g = GameOfLife(width, height)

for x, y in patterns.GLIDER:
    g.seed(x, y)

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
