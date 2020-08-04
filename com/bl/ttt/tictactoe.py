from random import randrange
import logging
import itertools


class Tictactoe:

    def __init__(self, is_computer_game=False, board_size=3):
        self._board_size = board_size
        self._cells = [[' '] * self._board_size for _ in range(self._board_size)]
        self._coordinates = (
                [[(x, y) for y in range(self._board_size)] for x in range(self._board_size)] +
                [[(x, y) for x in range(self._board_size)] for y in range(self._board_size)] +
                [[(d, d) for d in range(self._board_size)]] +
                [[(self._board_size - 1 - d, d) for d in range(self._board_size)]]
        )
        self._is_computer_game = is_computer_game
        self._players = ['X', 'O']
        self._player1 = self._players[0]
        self._player2 = self._players[1]
        self._human_player = self._player1
        self._computer_player = self._player2
        self._turn_counter = 1
        self._player_move_log = {'X': [], 'O': []}
        self._logger = logging.getLogger(__name__)
        self._logger.debug(f'{self._board_size}x{self._board_size} game instantiated with '
                           f'self._players:{self._players} and turn_counter: {self._turn_counter}')

    def __str__(self):
        row_counter = 0
        header_list = [str(i) for i in range(0, self._board_size)]
        header_string = f"  {'   '.join(header_list)}"
        board_list = [header_string]
        for row in self._cells:
            board_line = f"{row_counter} {' | '.join(row)}"
            board_list.append(board_line)
            row_counter += 1
        board = '\n'.join(board_list)
        return board

    def get_computer_game(self):
        return self._is_computer_game

    def get_turn_counter(self):
        return self._turn_counter

    def get_turn_player(self):
        if self._turn_counter % 2 == 0:
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

    def get_board_status(self):
        print(self)

    def get_game_summary(self):
        return f'Played: {self.get_player_move_log()}'

    def _get_computer_move(self):
        while True:
            computer_cell_x = randrange(0, self._board_size)
            computer_cell_y = randrange(0, self._board_size)
            move = TictactoeMove(self.get_turn_player(), computer_cell_x, computer_cell_y)
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
        self._logger.debug(f"""process_valid_move before:
{self.__str__()}""")

        self._cells[move.get_cell_chosen_y()][move.get_cell_chosen_x()] = move.get_player_id()
        self._logger.debug(f"""process_valid_move after: 
{self.__str__()}""")
        if move.get_player_id() == 'X':
            self._player_move_log['X'].append(move.get_cell_chosen())
        else:
            self._player_move_log['O'].append(move.get_cell_chosen())
        if not self.is_game_over():
            self._turn_counter += 1
        self._logger.debug(f'get_turn_counter: {self.get_turn_counter()}')
        self._logger.debug(f'get_player_move_log: {self.get_player_move_log()}')

        if self._is_computer_game and \
           self.is_computer_turn() and not \
           self.is_game_over():
            self._get_computer_move()

    def is_computer_turn(self):
        return self.get_turn_player() == 'O'

    def is_game_over(self):
        if self._is_draw() or self._has_won(self.get_turn_player()):
            return True

    def inform_game_over(self):
        if self._has_won(self.get_turn_player()):
            self._logger.debug(f'Game won by {self.get_turn_player()}')
            self._logger.debug(self.get_game_summary())
            return f'Player {self.get_turn_player()} has won the game.'
        elif self._is_draw():
            self._logger.debug('Game drawn')
            self._logger.debug(self.get_game_summary())
            return f'This game is over: it is a draw and neither player has won.'

    def _is_valid_player(self, move):
        return move.get_player_id() == 'X' or move.get_player_id() == 'O'

    def _is_cell_in_range(self, move):
        if (self._board_size - 1) >= move.get_cell_chosen_x() >= 0 and \
                (self._board_size - 1) >= move.get_cell_chosen_y() >= 0:
            return True

    def _is_cell_empty(self, move):
        return self._cells[move.get_cell_chosen_y()][move.get_cell_chosen_x()] == ' '

    def _has_won(self, player_id):
        for dimensions in self._coordinates:
            values = [self._cells[x][y] for (x, y) in dimensions]
            if len(set(values)) == 1 and \
                set(values) == {player_id} and \
                    ' ' not in values:
                return True

    def _is_draw(self):
        flat_cells_list = []
        for sublist in self._cells:
            for item in sublist:
                flat_cells_list.append(item)
        if not self._has_won(self.get_turn_player()) and ' ' not in flat_cells_list:
            return True


class TictactoeMove:
    def __init__(self, player_id, cell_chosen_x, cell_chosen_y):
        self.player_id = player_id
        self.cell_chosen_x = int(cell_chosen_x)
        self.cell_chosen_y = int(cell_chosen_y)

    def __str__(self):
        player_move = f'{self.player_id}:{self.cell_chosen_x}:{self.cell_chosen_y}'
        return player_move

    def get_player_id(self):
        return self.player_id

    def get_cell_chosen_x(self):
        return self.cell_chosen_x

    def get_cell_chosen_y(self):
        return self.cell_chosen_y

    def get_cell_chosen(self):
        cell_chosen = f'{self.cell_chosen_x}:{self.cell_chosen_y}'
        return cell_chosen
