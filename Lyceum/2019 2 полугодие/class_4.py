WHITE = 1

BLACK = 2


def opponent(color):
       if color == WHITE:

           return BLACK

        else:

           return WHITE


def correct_coords(row, col):
       return 0 <= row < 8 and 0 <= col < 8



class Rook:
       
    def __init__(self, row, col, color):
           self.row = row
           self.col = col
           self.color = color
       
    def set_position(self, row, col):
           self.row = row
           self.col = col
       
    def char(self):
           return 'R'
       
    def get_color(self):
           return self.color
       
    def can_move(self, row, col):
           if not (0 <= row < 8 and 0 <= col < 8):
               return False
           if self.row != row and self.col != col:
               return False
           return True


class Bishop:

       

    def __init__(self, row, col, color):

           self.row = row

           self.col = col

           self.color = color

       

    def set_position(self, row, col):

           self.row = row

           self.col = col

       

    def char(self):

           return 'B'

       

    def get_color(self):

           return self.color

       

    def can_move(self, row, col):

           if not (0 <= row < 8 and 0 <= col < 8):

               return False

           if abs(self.row - row) == abs(self.col - col):

               return True

           return False


class Board:

       

    def __init__(self):

           self.field = []

           for row in range(8):

               self.field.append([None] * 8)

       

    def current_player_color(self):

           return self.color

       

    def cell(self, row, col):

           piece = self.field[row][col]

           if piece is None:

               return '  '

           color = piece.get_color()

           c = 'w' if color == WHITE else 'b'

           return c + piece.char()

       

    def move_piece(self, row, col, row1, col1):

           if not correct_coords(row, col) or not correct_coords(row1, col1):

               return False

           if row == row1 and col == col1:

               return False

           piece = self.field[row][col]

           if piece is None:

               return False

           if piece.get_color() != self.color:

               return False

           if not piece.can_move(row1, col1):

               return False

           self.field[row][col] = None

           self.field[row1][col1] = piece

           piece.set_position(row1, col1)

           self.color = opponent(self.color)

           return True

       

    def is_under_attack(self, row, col, color):

           for i in range(8):

               for j in range(8):

                   if self.field[i][j] is not None:

                       piece = self.field[i][j]

                       if piece.get_color() == color:

                           if piece.can_move(row, col):

                               return True

           return False


Подробнее - на
Znanija.com - https: // znanija.com / task / 32164656  # readmore
