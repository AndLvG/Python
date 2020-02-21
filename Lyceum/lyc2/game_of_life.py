import numpy
import copy
import pygame
from pygame.locals import *
import random

pygame.init()

height = 400
width = 400
block_size = 4
window = pygame.display.set_mode((height, width), DOUBLEBUF)
window.set_alpha(None)
alive = (255, 255, 255)
dead = (0, 0, 0)


def check(y_axis, x_axis, grid):
    tmp_grid = copy.copy(grid)
    for y in range(1, y_axis - 1):
        for x in range(1, x_axis - 1):
            a = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if grid[y + i][x + j] == 1:
                        a += 1
            if grid[y][x] == 1:
                a -= 1
                if a < 2 or a > 3:
                    tmp_grid[y][x] = 0
            elif grid[y][x] == 0:
                if a == 3:
                    tmp_grid[y][x] = 1
    grid = tmp_grid
    return grid


def display(y_axis, x_axis, grid):
    rects = []
    for y in range(1, y_axis - 1):
        for x in range(1, x_axis - 1):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            if grid[x][y] == 1:
                rects.append(pygame.draw.rect(window, alive, rect))
            elif grid[x][y] == 0:
                rects.append(pygame.draw.rect(window, dead, rect))
    pygame.display.update(rects)


def generate(y_axis, x_axis, grid):
    for y in range(1, y_axis - 1):
        for x in range(1, x_axis - 1):
            alive_or_dead = random.randint(0, 1)
            if alive_or_dead:
                grid[y][x] = 1
            else:
                grid[y][x] = 0


def main():
    y_axis = height // block_size
    x_axis = width // block_size
    grid = numpy.zeros((y_axis, x_axis))
    generate(y_axis, x_axis, grid)
    while True:
        display(y_axis, x_axis, grid)
        grid = check(y_axis, x_axis, grid)


if __name__ == '__main__':
    main()
