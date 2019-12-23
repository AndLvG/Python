import pygame


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
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + x * self.cell_size, self.height + y * self.cell_size, self.cell_size, self.cell_size),
                                 abs(self.board[y][x] - 1))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        # self.on_click(cell)
        self.three_colors(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= y <= self.height - 1 and 0 <= x <= self.width - 1:
            return (y, x)
        else:
            return None

    def on_click(self, cell):
        if not cell:
            return
        # print(cell)
        for x in range(self.width):
            self.board[cell[0]][x] = abs(self.board[cell[0]][x] - 1)
        for y in range(self.height):
            if y != cell[0]:
                self.board[y][cell[1]] = abs(self.board[y][cell[1]] - 1)

    def three_colors(self, cell):
        if not cell:
            return
        if self.board[cell[0]][cell[1]] == 2:
            self.board[cell[0]][cell[1]] = 0
        else:
            self.board[cell[0]][cell[1]] += 1


pygame.init()
board = Board(5, 7)
board.set_view(20, 20, 50)
screen = pygame.display.set_mode((500, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT  or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
