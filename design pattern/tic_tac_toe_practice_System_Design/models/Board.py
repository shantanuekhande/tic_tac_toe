from tic_tac_toe_practice_System_Design.models.Cell import Cell
class Board:
    def __init__(self,board_size):
        self.board_size = board_size
        self.grid = [[Cell(row, col) for col in range(board_size)] for row in range(board_size)]

    def display(self):
        for row in self.grid:
            row_display = ' | '.join([cell.symbol if cell.symbol else ' ' for cell in row])
            print(row_display)
            print('-' * (self.board_size * 4 - 3))