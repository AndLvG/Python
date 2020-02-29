import pygame
from random import *

PLAYERS = {0: pygame.Color("Blue"), 1: pygame.Color("Red")}
PLAYERS_NAMES = {0: 'Играет СИНИЙ игрок', 1: 'Играет КРАСНЫЙ игрок'}

pygame.init()

screen = pygame.display.set_mode((300, 400))
screen.fill((0, 0, 0))
pygame.display.set_caption("Игра Недореверси")


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[sample(PLAYERS.keys(), 1)[0] for _ in range(width)] for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.current_player = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.draw_text(screen, PLAYERS_NAMES[self.current_player])

    def render(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                 1)

    def color(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                pygame.draw.circle(screen, PLAYERS[self.board[y][x]],
                                   ((self.left + x * self.cell_size) + int(self.cell_size / 2),
                                    (self.top + y * self.cell_size) + int(self.cell_size / 2)),
                                   int(self.cell_size / 2) - 4)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        # self.three_colors(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= y <= self.height - 1 and 0 <= x <= self.width - 1:
            return (y, x)
        else:
            return None

    def draw_text(self, surf, text):
        font_name = pygame.font.match_font('Arial')
        font = pygame.font.Font(font_name, 16)
        text_surface = font.render(text, True, pygame.Color('yellow'))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (150, 5)
        surf.blit(text_surface, text_rect)

    def check_victory(self):
        t = self.board[0][0]
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] != t:
                    return False
        return True

    def on_click(self, cell):
        if not cell:
            return
        col = self.board[cell[0]][cell[1]]
        for x in range(self.width):
            self.board[cell[0]][x] = col
        for y in range(self.height):
            self.board[y][cell[1]] = col
        self.current_player = abs(self.current_player - 1)
        screen.fill((0, 0, 0))
        board.render()
        if self.check_victory():
            self.draw_text(screen, 'Игра окончена')
        else:
            self.draw_text(screen, PLAYERS_NAMES[self.current_player])


board = Board(5, 7)
board.set_view(20, 40, 50)
board.render()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.check_victory():
                screen.fill((0, 0, 0))
                board = Board(5, 7)
                board.set_view(20, 40, 50)
                board.render()
            else:
                board.get_click(event.pos)
    board.color()

    pygame.display.flip()
pygame.quit()
