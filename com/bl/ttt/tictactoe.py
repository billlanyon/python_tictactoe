from random import randrange
import time


win_cell_tuples = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8},
                  {6, 4, 2}]


class Tictactoe:

    def __init__(self, is_computer_game=False):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.is_computer_game = is_computer_game
        self.players = ['X', 'O']
        self.player1 = self.players[0]
        self.player2 = self.players[1]
        self.human_player = self.player1
        self.computer_player = self.player2
        self.turn_counter = 1
        self.player_move_log = {'X': [], 'O': []}

    def __str__(self):
        board = f"""
    | {self.cells[0]} | {self.cells[1]} | {self.cells[2]} |
    | {self.cells[3]} | {self.cells[4]} | {self.cells[5]} |
    | {self.cells[6]} | {self.cells[7]} | {self.cells[8]} |
    """
        return board

    @staticmethod
    def initial_coordinates():
        coordinates = """The board coordinates are:
    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |
    """
        return coordinates

    def get_computer_game(self):
        return self.is_computer_game

    def get_turn_counter(self):
        return self.turn_counter

    def get_turn_player(self):
        if self.turn_counter % 2 == 0:
            return self.player2
        else:
            return self.player1

    def get_previous_turn_player(self):
        if self.get_turn_player() == self.player1:
            return self.player2
        else:
            return self.player1

    def get_empty_cells(self):
        empty_cell_indices = [i for i, x in enumerate(self.cells) if x == ' ']
        return empty_cell_indices

    def get_player_move_log(self):
        return self.player_move_log

    def get_game_status(self):
        print(
            f'TurnCounter = {self.get_turn_counter()} | '
            f'PlayerMoveLog = {self.get_player_move_log()}'
        )
        print(self)

    def get_computer_move(self):
        computer_cell = None
        while True:
            if self.get_turn_counter() == 2:
                if 4 in self.get_empty_cells():
                    computer_cell = 4
                else:
                    computer_cell = 0
            elif self.get_turn_counter() == 4:
                human_player_move_set = set(self.player_move_log[self.human_player])
                loss_list = []
                for loss in win_cell_tuples:
                    if human_player_move_set.issubset(loss):
                        loss_list.append(loss)
                        computer_cell_set = loss_list[0].difference(human_player_move_set)
                        computer_cell = computer_cell_set.pop()
            else:
                computer_cell = randrange(9)
            move = TictactoeMove(self.get_turn_player(), computer_cell)
            if self.is_valid_move(move):
                self.process_valid_move(move)
                time.sleep(2)
            else:
                continue
            return True

    def is_valid_move(self, move):
        try:
            if self._is_valid_player(move) and \
               self._is_cell_in_range(move) and \
               self._is_cell_empty(move):
                self.turn_counter += 1
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
