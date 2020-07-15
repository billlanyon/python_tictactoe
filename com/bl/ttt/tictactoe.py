from random import randrange
import itertools


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

    def get_player_move_log(self, player_id='both'):
        if player_id == 'both':
            x_move_log = list(self.player_move_log.get('X'))
            o_move_log = list(self.player_move_log.get('O'))
            players_move_tuples = list(itertools.zip_longest(x_move_log, o_move_log))
            players_move_list = list(itertools.chain(*players_move_tuples))
            return [move for move in players_move_list if(move is not None)]
        else:
            player_move_list = list(self.player_move_log.get(player_id))
            return player_move_list

    def get_game_status(self):
        print(self)

    def get_computer_move(self):
        while True:
            computer_cell = randrange(9)
            move = TictactoeMove(self.get_turn_player(), computer_cell)
            if self.is_valid_move(move):
                self.process_valid_move(move)
            else:
                continue
            return True

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

        self.turn_counter += 1

        if self.is_computer_game and \
           self.is_computer_turn() and not \
           self.is_game_over():
            self.get_computer_move()

    def is_computer_turn(self):
        return self.get_turn_player() == 'O'

    def is_game_over(self):
        return self.has_won('X') or \
               self.has_won('O') or \
               self.is_draw()

    def inform_game_over(self):
        if self.has_won(self.get_previous_turn_player()):
            return f'Player {self.get_previous_turn_player()} has won the game.'
        else:
            return f'This game is over: it is a draw and neither player has won.'

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
