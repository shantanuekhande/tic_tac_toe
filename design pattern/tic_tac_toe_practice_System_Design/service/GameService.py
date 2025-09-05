from tic_tac_toe_practice_System_Design.models.Game import Game
from tic_tac_toe_practice_System_Design.models.Board import Board

class GameService:
    def __init__(self,game,board,players,board_size,winning_strategy):

        self.board = board
        self.bord_size = board_size
        self.players = players
        self.winning_strategy = winning_strategy
        self.game = game
    def get_game(self):
        return self.game

    def display_board(self):
        self.board.display()

    def validate_move(self, row, col):
        if row < 0 or row >= self.bord_size or col < 0 or col >= self.bord_size:
            return False
        if self.board.grid[row][col].symbol is not None:
            return False
        return True

    def take_input(self, player):
        while True:
            if player.player_type == 'HUMAN':
                row = int(input(f"Player {player.name}, enter your move row (0-{self.bord_size - 1}): "))
                col = int(input(f"Player {player.name}, enter your move column (0-{self.bord_size - 1}): "))
                if self.validate_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            elif player.player_type == 'BOT':
                # will select next available cell
                while True:
                    for row in range(self.bord_size):
                        for col in range(self.bord_size):
                            if self.board.grid[row][col].symbol is None:
                                return row ,col


    def make_move(self, player, row, col):

        self.board.grid[row][col].symbol = player.symbol
        self.board.grid[row][col].cell_status = 'FILLED'

    def check_winner(self, player):
        if self.winning_strategy.check_winner(self.board.grid, player):
            self.game.game_status = 'ENDED'
            self.game.winner = player
            return True
        return False

    def take_turn(self):
        self.game.current_player_index = (self.game.current_player_index + 1) % len(self.players)

