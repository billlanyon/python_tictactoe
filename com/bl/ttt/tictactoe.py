from random import randrange
import logging
import itertools
import math


class Tictactoe:

    def __init__(self, is_computer_game=False, board_dims=3):
        self._board_dims = board_dims
        self._cells = [' ' for i in range(0, board_dims*board_dims)]
        self._is_computer_game = is_computer_game
        self._players = ['X', 'O']
        self._player1 = self._players[0]
        self._player2 = self._players[1]
        self._human_player = self._player1
        self._computer_player = self._player2
        self._turn_counter = 1
        self._player_move_log = {'X': [], 'O': []}
        self._logger = logging.getLogger(__name__)
        self._logger.debug(f'Game instantiated with self._players: {self._players} and turn_counter: {self._turn_counter}')

    def __str__(self):
        board = '\n'+'\n'.join(Tictactoe._delimited_rows( self._cells ))
        return board

    @staticmethod
    def _delimited_rows(cells):
        return ['|'.join(row) for row in Tictactoe._board_to_rows(cells)]

    @staticmethod
    def _board_to_rows(cells):
        dims = int(math.sqrt(len(cells)))
        return [
            cells[x: x + dims]
            for x in range(0, len(cells), dims)
        ]

    @staticmethod
    def initial_coordinates():
        coordinates = """The board coordinates are:
    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |"""
        return coordinates

    def get_computer_game(self):
        return self._is_computer_game

    def get_turn_counter(self):
        return self._turn_counter

    def get_turn_player(self):
        if self._turn_counter % 2 == 0:
            return self._player2
        else:
            return self._player1

    def get_previous_turn_player(self):
        if self.get_turn_player() == self._player1:
            return self._player2
        else:
            return self._player1

    def get_player_move_log(self, player_id='both'):
        if player_id == 'both':
            x_move_log = list(self._player_move_log.get('X'))
            o_move_log = list(self._player_move_log.get('O'))
            players_move_tuples = list(itertools.zip_longest(x_move_log, o_move_log))
            players_move_list = list(itertools.chain(*players_move_tuples))
            return [move for move in players_move_list if(move is not None)]
        else:
            player_move_list = list(self._player_move_log.get(player_id))
            return player_move_list

    def get_game_status(self):
        print(self)

    def get_game_summary(self):
        empty_cell_indices = [i for i, x in enumerate(self._cells) if x == ' ']
        return f'Played: {self.get_player_move_log()}. Unplayed: {empty_cell_indices}.'

    def _get_computer_move(self):
        while True:
            computer_cell = randrange(9)
            move = TictactoeMove(self.get_turn_player(), computer_cell)
            self._logger.debug(f'get_computer_move constructed: {move.__str__()}')
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
        self._logger.debug(f'process_valid_move: {move}')
        self._logger.debug(f'process_valid_move before: {self.__str__()}')
        self._cells[move.get_cell_chosen()] = move.get_player_id()
        self._logger.debug(f'process_valid_move after: {self.__str__()}')
        if move.get_player_id() == 'X':
            self._player_move_log['X'].append(move.get_cell_chosen())
        else:
            self._player_move_log['O'].append(move.get_cell_chosen())
        self._logger.debug(f'get_turn_counter: {self.get_turn_counter()}')
        self._logger.debug(f'get_player_move_log: {self.get_player_move_log()}')
        self._turn_counter += 1

        if self._is_computer_game and \
           self.is_computer_turn() and not \
           self.is_game_over():
            self._get_computer_move()

    def is_computer_turn(self):
        return self.get_turn_player() == 'O'

    def is_game_over(self):
        return self.has_won('X') or \
               self.has_won('O') or \
               self.is_draw()

    def inform_game_over(self):
        if self.has_won(self.get_previous_turn_player()):
            self._logger.debug('Game won')
            self._logger.debug(self.get_game_summary())
            return f'Player {self.get_previous_turn_player()} has won the game.'
        else:
            self._logger.debug('Game drawn')
            self._logger.debug(self.get_game_summary())
            return f'This game is over: it is a draw and neither player has won.'

    def _is_valid_player(self, move):
        return move.get_player_id() == 'X' or move.get_player_id() == 'O'

    def _is_cell_in_range(self, move):
        return self._board_dims*self._board_dims >= move.get_cell_chosen() >= 0

    def _is_cell_empty(self, move):
        return self._cells[move.get_cell_chosen()] == ' '

    def has_won(self, player_id):
        return self._is_any_row_complete(player_id) or \
               self._is_any_column_complete(player_id) or \
                self._is_any_diagonal_complete(player_id)

    def _is_any_row_complete(self, player_id):
        rows = self._board_to_rows(self._cells)
        return self._row_complete_checker(rows, player_id)

    def _is_any_column_complete(self, player_id):
        piv = self._pivot_cells(self._cells)
        cols = self._board_to_rows(piv)
        return self._row_complete_checker(cols, player_id)

    @staticmethod
    def _pivot_cells(cells):
        as_rows = Tictactoe._board_to_rows(cells)
        piv = [e for e in zip(*as_rows)]
        return Tictactoe._flatten_list(piv)

    @staticmethod
    def _flatten_list(l):
        return [item for sublist in l for item in sublist]

    def _row_complete_checker(self, rows, player_id):
        complete_rows = self._get_complete_rows(rows)
        return len(complete_rows) > 0 and set(player_id) in complete_rows

    def _get_complete_rows(self, rows):
        return [set(row) for row in rows if (len(set(row)) == 1)]

    def _is_any_diagonal_complete(self, player_id):
        back_slash_diag = self._get_diagonal(self._cells)
        is_backslash = set(player_id) == set(back_slash_diag)
        trans = self._horiz_flip_cells(self._cells)
        fwd_slash_diag = self._get_diagonal(trans)
        is_fwd_slash = set(player_id) == set(fwd_slash_diag)
        return is_backslash or is_fwd_slash

    @staticmethod
    def _horiz_flip_cells(cells):
        as_rows = Tictactoe._board_to_rows(cells)
        transposed = as_rows[::-1]
        return Tictactoe._flatten_list(transposed)

    def _get_diagonal(self, cells):
        dims = self._board_dims
        return [cells[a*dims+a] for a in range(0, dims)]

    def is_draw(self):
        return ' ' not in self._cells


class TictactoeMove:
    def __init__(self, player_id, cell_chosen):
        self.player_id = player_id
        self.cell_chosen = cell_chosen

    def __str__(self):
        player_move = f'{self.player_id}:{self.cell_chosen}'
        return player_move

    def get_player_id(self):
        return self.player_id

    def get_cell_chosen(self):
        return self.cell_chosen
