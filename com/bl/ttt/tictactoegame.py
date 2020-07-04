from random import randrange


class TictactoeGame:
    # This class enables a main script to play the game of TicTacToe.
    # A human player can chose to play another human or a built in computer player.
    # Player 'X' always plays first.
    # A computer player is always 'O'.

    def __init__(self, is_computer_opponent=False):
        self._cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self._player_ids = ['X', 'O']
        self._is_computer_opponent = is_computer_opponent
        self._turn_counter = 0

    def __str__(self):
        board = f"""
    | {self._cells[0]} | {self._cells[1]} | {self._cells[2]} |
    | {self._cells[3]} | {self._cells[4]} | {self._cells[5]} |
    | {self._cells[6]} | {self._cells[7]} | {self._cells[8]} |
    """
        return board

    @staticmethod
    def initial_board_layout():
        return """The board coordinates are:
        
            | 0 | 1 | 2 |
            | 3 | 4 | 5 |
            | 6 | 7 | 8 |
            """

    def get_turn_player_id(self):
        return self._player_ids[
            self._turn_counter % len(self._player_ids)
            ]

    def is_valid_move(self, move):
        try:
            if self._is_valid_player(move) and \
               self._is_cell_in_range(move) and \
               self._is_cell_empty(move):
                return True
            else:
                return False

        except (ValueError, TypeError):
            return False

    def _is_valid_player(self, move):
        return move.get_player_id() in self._player_ids

    def _is_cell_in_range(self, move):
        return 8 >= move.get_cell_chosen() >= 0

    def _is_cell_empty(self, move):
        return self._cells[move.get_cell_chosen()] == ' '

    def make_valid_move(self, move):
        self._cells[move.get_cell_chosen()] = move.get_player_id()
        self._turn_counter += 1
        if self._is_computer_turn():
            self._make_computer_move()

    def _is_computer_turn(self):
        return self._is_computer_opponent and \
               self.get_turn_player_id() == 'O'

    def _make_computer_move(self):
        while True:
            computer_cell = randrange(len(self._cells) + 1)
            move = TictactoeMove(self.get_turn_player_id(), computer_cell)
            if self.is_valid_move(move):
                self.make_valid_move(move)
                break

    def is_game_over(self):
        is_a_draw = ' ' not in self._cells
        player_id_1_has_won = self._has_won(self._player_ids[0])
        player_id_2_has_won = self._has_won(self._player_ids[1])

        return is_a_draw or \
               player_id_1_has_won or \
               player_id_2_has_won

    def get_winner_player_id(self):
        for p in self._player_ids:
            if self._has_won(p):
                return p

    def _has_won(self, player_id):
        return self._is_any_row_complete(player_id) or \
               self._is_any_column_complete(player_id) or \
                self._is_any_diagonal_complete(player_id)

    def _is_any_row_complete(self, player_id):
        return self._cells[0] == self._cells[1] == self._cells[2] == player_id or \
                self._cells[3] == self._cells[4] == self._cells[5] == player_id or \
                self._cells[6] == self._cells[7] == self._cells[8] == player_id

    def _is_any_column_complete(self, player_id):
        return self._cells[0] == self._cells[3] == self._cells[6] == player_id or \
                self._cells[1] == self._cells[4] == self._cells[7] == player_id or \
                self._cells[2] == self._cells[5] == self._cells[8] == player_id

    def _is_any_diagonal_complete(self, player_id):
        return self._cells[0] == self._cells[4] == self._cells[8] == player_id or \
                self._cells[6] == self._cells[4] == self._cells[2] == player_id


class TictactoeMove:
    def __init__(self, player_id, cell_chosen):
        self.player_id = player_id
        self.cell_chosen = cell_chosen

    def get_player_id(self):
        return self.player_id

    def get_cell_chosen(self):
        return self.cell_chosen
