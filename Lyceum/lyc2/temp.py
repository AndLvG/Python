import pygame
<<<<<<< Updated upstream
import math
from pygame.locals import *
SIZE = 800, 800
pygame.init()
screen = pygame.display.set_mode(SIZE)
FPSCLOCK = pygame.time.Clock()
done = False
screen.fill((0, 0, 0))
degree=0
while not done:
    screen.fill(0)
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            done = True
            break
    for x in range(1,400,10):
        pygame.draw.circle(screen,(255,255,255),(400,400),x,1)
    radar = (400,400)
    radar_len = 400
    x = radar[0] + math.cos(math.radians(degree)) * radar_len
    y = radar[1] + math.sin(math.radians(degree)) * radar_len

    # then render the line radar->(x,y)
    pygame.draw.line(screen, Color("red"), radar, (x,y), 1)
    pygame.display.flip()
    degree+=2
    FPSCLOCK.tick(60)
=======


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.left, self.width * self.cell_size +self.left, self.cell_size):
            for y in range(self.top, self.height * self.cell_size+self.top, self.cell_size):
                pygame.draw.rect(screen, (0, 255, 0), (x, y, self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
board = Board(4, 3)
board.set_view(40,40, 30)
screen = pygame.display.set_mode((501, 501))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
>>>>>>> Stashed changes
