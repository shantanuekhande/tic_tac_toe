class GameController:
    def __init__(self, game_service):
        self.game_service = game_service

    def start_game(self):
        self.game_service.get_game()

    def take_input(self, player):
        return self.game_service.take_input(player)

    def make_move(self, player, row, col):
        self.game_service.make_move(player, row, col )

    def check_winner(self,player):
        return self.game_service.check_winner(player)

    def display_game(self):
        self.game_service.display_board()

    def take_turn(self):
        self.game_service.take_turn()