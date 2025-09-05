from tic_tac_toe_practice_System_Design.models.CellStatus import CellStatus
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.symbol = None  # Can be 'X', 'O', or ''
        self.cell_status = CellStatus.EMPTY
