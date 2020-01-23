import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[""] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.players = ["krest", "circle"]
        self.current = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                pygame.draw.rect(screen, pygame.Color('white'), (
                    self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                 1)

    def color(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                col = self.board[y][x]
                # if col == "":
                #     pygame.draw.rect(screen, pygame.Color('Black'), (
                #         (self.left + x * self.cell_size) + 1, (self.top + y * self.cell_size) + 1, self.cell_size - 2,
                #         self.cell_size - 2), )
                if col == "krest":
                    pygame.draw.line(screen, pygame.Color("Blue"),
                                     ((self.left + x * self.cell_size) + 3, (self.top + y * self.cell_size) + 3),
                                     ((self.left + x * self.cell_size) + self.cell_size - 4,
                                      (self.top + y * self.cell_size) + self.cell_size - 4), 2)
                    pygame.draw.line(screen, pygame.Color("Blue"),
                                     ((self.left + x * self.cell_size) + self.cell_size - 4,
                                      (self.top + y * self.cell_size) + 3),
                                     ((self.left + x * self.cell_size) + 3,
                                      (self.top + y * self.cell_size) + self.cell_size - 4), 2)

                elif col == "circle":
                    pygame.draw.circle(screen, pygame.Color("Red"),
                                       ((self.left + x * self.cell_size) + int(self.cell_size / 2),
                                        (self.top + y * self.cell_size) + int(self.cell_size / 2)),
                                       int(self.cell_size / 2) - 4,
                                       2)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if 0 <= cell[0] < self.height and 0 <= cell[1] < self.width:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        return [y, x]

    def on_click(self, cell):
        x = cell[1]
        y = cell[0]

        if self.board[y][x] == "":
            self.board[y][x] = self.players[self.current]
            self.current = abs(self.current - 1)


pygame.init()
board = Board(10, 7)
board.set_view(20, 20, 50)
screen = pygame.display.set_mode((540, 390))
board.render()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    board.color()
    pygame.display.flip()
