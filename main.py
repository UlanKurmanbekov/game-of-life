import matplotlib.pyplot as plt


class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[*([0] * width)] for _ in range(height)]

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
        for i in range(self.height):
            for j in range(self.width):
                if i == x and j == y:
                    self.grid[i][j] = 1

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


g = GameOfLife(70, 70)

for q in range(0, 3):
    g.seed(q, 2)

g.seed(2, 1)
g.seed(1, 0)

plt.ion()
fig, ax = plt.subplots()

for _ in range(1000):
    ax.clear()
    ax.imshow(g.grid, cmap='binary')
    plt.pause(0.1)
    g.update()
plt.ioff()
plt.show()
