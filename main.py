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

        x2 = x
        y2 = y
        for i in range(3):
            if i == 0:
                x -= 1
            elif i == 1:
                x += 1
            else:
                if self.height <= x + 1:
                    x -= x
                else:
                    x += 1

            y1 = y
            for j in range(3):
                if j == 0:
                    y1 -= 1
                elif j == 1:
                    y1 += 1
                else:
                    if self.width <= y1 + 1:
                        y1 -= y
                    else:
                        y1 += 1

                if x == x2 and y1 == y2:
                    continue
                cnt += curr_gen[x][y1]
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
