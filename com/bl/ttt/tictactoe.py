from random import randrange
import time

class Tictactoe:

    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.is_computer_game = False
        self.player1 = None
        self.player2 = None
        self.human_player = None
        self.computer_player = None
        self.player_id = None
        self.turn_counter = 1
        self.player_move_log = {'X': [], 'O': []}

    def __str__(self):
        board = f"""
    | {self.cells[0]} | {self.cells[1]} | {self.cells[2]} |
    | {self.cells[3]} | {self.cells[4]} | {self.cells[5]} |
    | {self.cells[6]} | {self.cells[7]} | {self.cells[8]} |
    """
        return board

    def set_computer_game(self):
        self.is_computer_game = True

    def get_computer_game(self):
        return self.is_computer_game

    def get_board_size(self):
        pass

    def set_player_ids(self, first_player_id):
        self.player1 = first_player_id
        if self.player1 == 'X':
            self.player2 = 'O'
        else:
            self.player2 = 'X'
        if self.is_computer_game is True:
            self.computer_player = self.player2
            self.human_player = self.player1

    def increment_turn_counter(self):
        self.turn_counter += 1

    def get_turn_counter(self):
        return self.turn_counter

    def get_turn_player(self):
        if self.turn_counter % 2 == 0:
            return self.player2
        else:
            return self.player1

    def get_player1_id(self):
        player1_id = self.player1
        return player1_id

    def get_player2_id(self):
        player2_id = self.player2
        return player2_id

    def get_computer_move(self, move):
        pass

    def get_empty_cells(self):
        empty_cell_indices = [i for i, x in enumerate(self.cells) if x == ' ']
        return empty_cell_indices

    def get_player_move_log(self):
        return self.player_move_log

    def get_game_status(self):
        self.turn_counter += 1
        print(
            f'GP1 = {self.get_player1_id()} | '
            f'GP2 = {self.get_player2_id()} | '
            f'GTP = {self.get_turn_player()} | '
            f'GTC = {self.get_turn_counter()} | '
            f'PML = {self.get_player_move_log()}'
        )
        print(self)

    def get_computer_status(self):
        print(
            f'CPID = {self.computer_player} | '
            f'HPML = {self.player_move_log[self.human_player]} | '
            f'CPML = {self.player_move_log[self.computer_player]} | '
            f'UPC = {self.get_empty_cells()}'
        )

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

    def process_valid_move(self, move):
        self.cells[move.get_cell_chosen()] = move.get_player_id()
        if move.get_player_id() == 'X':
            self.player_move_log['X'].append(move.get_cell_chosen())
        else:
            self.player_move_log['O'].append(move.get_cell_chosen())

    def _is_valid_player(self, move):
        return move.get_player_id() == 'X' or move.get_player_id() == 'O'

    def _is_cell_in_range(self, move):
        return 8 >= move.get_cell_chosen() >= 0

    def _is_cell_empty(self, move):
        return self.cells[move.get_cell_chosen()] == ' '

    def has_won(self, player_id):
        return self._is_any_row_complete(player_id) or self._is_any_column_complete(player_id) or \
                self._is_any_diagonal_complete(player_id)

    def _is_any_row_complete(self, player_id):
        if self.cells[0] == self.cells[1] == self.cells[2] == player_id or \
                self.cells[3] == self.cells[4] == self.cells[5] == player_id or \
                self.cells[6] == self.cells[7] == self.cells[8] == player_id:
            return True

    def _is_any_column_complete(self, player_id):
        if self.cells[0] == self.cells[3] == self.cells[6] == player_id or \
                self.cells[1] == self.cells[4] == self.cells[7] == player_id or \
                self.cells[2] == self.cells[5] == self.cells[8] == player_id:
            return True

    def _is_any_diagonal_complete(self, player_id):
        if self.cells[0] == self.cells[4] == self.cells[8] == player_id or \
                self.cells[6] == self.cells[4] == self.cells[2] == player_id:
            return True

    def is_draw(self):
        return ' ' not in self.cells


class TictactoeMove:
    def __init__(self, player_id, cell_chosen):
        self.player_id = player_id
        self.cell_chosen = cell_chosen

    def get_player_id(self):
        return self.player_id

    def get_cell_chosen(self):
        return self.cell_chosen
