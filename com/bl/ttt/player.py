from random import randrange


class TictactoeHumanPlayer:
    def __init__(self, player_id, player_number):
        self.player_id = player_id
        self.player_number = player_number


class TictactoeComputerPlayer:
    def __init__(self, player_id, player_number):
        self.player_id = player_id
        self.player_number = player_number

    def get_computer_move(self):
        computer_move = randrange(9)
        return computer_move
