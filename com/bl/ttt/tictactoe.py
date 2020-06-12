import re


class Tictactoe:
    """ Cell coordinates are:
    0	1	2
    3	4	5
    6	7	8
    """
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_valid_move(self, player_id, move):
        try:
            if player_id == 'X' or player_id == 'O':
                coordinate = int(move)
                if 8 >= coordinate >= 0:
                    if self.cells[coordinate] == ' ':
                        valid_move_cell = coordinate
                        return True, valid_move_cell

            return False

        except (ValueError, TypeError):
            return False

    def make_valid_move(self, player_id, move):
        self.cells[move] = player_id

    def is_any_row_complete(self, player_id):
        if self.cells[0] == self.cells[1] == self.cells[2] == player_id or \
                self.cells[3] == self.cells[4] == self.cells[5] == player_id or \
                self.cells[6] == self.cells[7] == self.cells[8] == player_id:
            return True

    def is_any_column_complete(self, player_id):
        if self.cells[0] == self.cells[3] == self.cells[6] == player_id or \
                self.cells[1] == self.cells[4] == self.cells[7] == player_id or \
                self.cells[2] == self.cells[5] == self.cells[8] == player_id:
                return True

    def is_any_diagonal_complete(self, player_id):
        if self.cells[0] == self.cells[4] == self.cells[8] == player_id or \
                self.cells[6] == self.cells[4] == self.cells[2] == player_id:
            return True

    def has_won(self, player_id):
        if self.is_any_diagonal_complete(player_id) or self.is_any_row_complete(player_id) or self.is_any_column_complete(player_id):
            return self


class TictactoeMove:
    # Valid player_id are 'X' or 'O'
    def __init__(self, init_player_id, init_move_cell):
        self.player_id = str(init_player_id)
        self.move_cell = int(init_move_cell)

    def get_player_id(self):
        return self.player_id

    def get_move_cell(self):
        return self.move_cell
