class Tictactoe:

    """ Cell coordinate:
    0	1	2
    3	4	5
    6	7	8
    """
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_valid_move(self, move):
        try:
            if self.is_valid_player(move) and \
               self.is_cell_in_range(move) and \
               self.is_cell_empty(move):
                return True
            else:
                return False

        except (ValueError, TypeError):
            return False

    def is_valid_player(self, move):
        return move.player_id == 'X' or move.player_id == 'O'

    def is_cell_in_range(self, move):
        return 8 >= move.cell_chosen >= 0

    def is_cell_empty(self, move):
        return self.cells[move.cell_chosen] == ' '

    def make_valid_move(self, move):
        self.cells[move.cell_chosen] = move.player_id

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
    def __init__(self, player_id, cell_chosen):
        self.player_id = player_id  # TODO Orchestrator to return as str
        self.cell_chosen = cell_chosen  # TODO Orchestrator to return as int

    def get_player_id(self):
        return self.player_id

    def cell_chosen(self):
        return self.cell_chosen
