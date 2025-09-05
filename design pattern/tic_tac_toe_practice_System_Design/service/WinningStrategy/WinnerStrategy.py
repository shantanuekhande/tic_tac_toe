
class RowWinner:
    @staticmethod
    def check_winner(board, player):
        for row in board:
            if all(cell.symbol == player.symbol for cell in row):
                return True
        return False

class ColumnWinner:
    @staticmethod
    def check_winner(board, player):
        for col in range(len(board)):
            if all(board[row][col].symbol == player.symbol for row in range(len(board))):
                return True
        return False

class DiagonalWinner:
    @staticmethod
    def check_winner(board, player):
        # Check primary diagonal
        if all(board[i][i].symbol == player.symbol for i in range(len(board))):
            return True
        # Check secondary diagonal
        if all(board[i][len(board)-1-i].symbol == player.symbol for i in range(len(board))):
            return True
        return False