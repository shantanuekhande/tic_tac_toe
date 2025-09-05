from tic_tac_toe_practice_System_Design.models.absPlayer import AbsPlayer
class Player(AbsPlayer):
    def __init__(self, name, symbol,player_type):
        self.player_type = player_type
        super().__init__(name, symbol)
