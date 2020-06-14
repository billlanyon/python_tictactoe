import re


class Tictactoe:
    """ Cell coordinates are:
    0	1	2
    3	4	5
    6	7	8
    """
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_valid_move(self, cell_chosen):
        try:
            if 8 >= cell_chosen >= 0:
                if self.cells[cell_chosen] == ' ':
                    return True

            return False

        except (ValueError, TypeError):
            return False

    def make_valid_move(self, player_id, cell_chosen):
        self.cells[cell_chosen] = player_id

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
    def __init__(self, player_id, cell_chosen):
        self.player_id = str(player_id)
        self.cell_chosen = int(cell_chosen)

    def get_player_id(self):
        return self.player_id

    def cell_chosen(self):
        return self.cell_chosen
