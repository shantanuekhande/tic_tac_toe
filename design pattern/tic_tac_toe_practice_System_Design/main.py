from debugpy.common.timestamp import current

from tic_tac_toe_practice_System_Design.models.Game import Game
from tic_tac_toe_practice_System_Design.models.Player import Player
from tic_tac_toe_practice_System_Design.models.Board import Board
from tic_tac_toe_practice_System_Design.models.GameStatus import GameStatus
from tic_tac_toe_practice_System_Design.service.GameService import GameService
from tic_tac_toe_practice_System_Design.service.WinningStrategy import WinnerStrategy
from tic_tac_toe_practice_System_Design.controller.GameController import GameController


if __name__ == '__main__':


    player1 = Player("Alice", "X", "HUMAN")
    player2 = Player("Bot", "O", "BOT")
    players = [player1, player2]
    board_size = 3
    board = Board(board_size)
    winning_strategy = WinnerStrategy.RowWinner
    game = Game(board,players,board_size,winning_strategy)
    game_service = GameService(game,board,players,board_size,winning_strategy)
    game_controller = GameController(game_service)

    game_controller.start_game()


    while game.game_status == GameStatus.IN_PROGRESS:
        game_controller.display_game()
        row,col = game_controller.take_input(players[game.current_player_index])
        game_controller.make_move(players[game.current_player_index],row,col)

        if game_controller.check_winner(players[game.current_player_index]):
            print(f"Congratulations {players[game.current_player_index].name}! You have won the game.")
            game.game_status = GameStatus.WIN

        game_controller.take_turn()



