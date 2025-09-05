from tic_tac_toe_practice_System_Design.models.GameStatus import GameStatus
class Game:
    def __init__(self,board, players, board_size, winning_strategy):
        self.board_size = board_size
        self.board = board  # done
        self.players = players # done
        self.game_status = GameStatus.IN_PROGRESS # done
        self.winner = None
        self.winning_strategy = winning_strategy
        self.current_player_index = 0
