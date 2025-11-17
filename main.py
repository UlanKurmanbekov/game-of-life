import pygame
import sys
from game import GameOfLife
from renderer import Renderer

CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 75

SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 10

COLOR_BG = (0, 0, 0)
COLOR_CELL = (255, 255, 255)
COLOR_GRID = (40, 40, 40)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    game = GameOfLife(GRID_WIDTH, GRID_HEIGHT)
    renderer = Renderer(screen, CELL_SIZE, COLOR_CELL, COLOR_GRID, COLOR_BG)

    running = True
    paused = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_c:
                    game.clear()

            if paused:
                if pygame.mouse.get_pressed()[0]:
                    x, y = renderer.get_grid_coords_from_mouse(pygame.mouse.get_pos())
                    game.set_cell(x, y, 1)
                elif pygame.mouse.get_pressed()[2]:
                    x, y = renderer.get_grid_coords_from_mouse(pygame.mouse.get_pos())
                    game.set_cell(x, y, 0)

        if not paused:
            game.update()

        renderer.draw(game)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
