import re

class Tictactoe:
    """
    Concrete class for instantiating specific games based on a single list of nine position strings.
    0	1	2
    3	4	5
    6	7	8
    """
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __repr__(self):
        return self.cells

    def is_any_row_complete(self, player_id):
        """
        Check for three of a kind in the rows
        @param player_id:
        @return: True if yes
        """
        if self.cells[0] == self.cells[1] == self.cells[2] == player_id or \
                self.cells[3] == self.cells[4] == self.cells[5] == player_id or \
                self.cells[6] == self.cells[7] == self.cells[8] == player_id:
            return True

    def is_any_column_complete(self, player_id):
        """
        Check for three of a kind in columns
        @param player_id:
        @return: True if yes
        """
        if self.cells[0] == self.cells[3] == self.cells[6] == player_id or \
                self.cells[1] == self.cells[4] == self.cells[7] == player_id or \
                self.cells[2] == self.cells[5] == self.cells[8] == player_id:
                return True

    def is_any_diagonal_complete(self, player_id):
        """
        Check for three of a kind in diagonals
        @param player_id:
        @return: True if yes
        """
        if self.cells[0] == self.cells[4] == self.cells[8] == player_id or \
                self.cells[6] == self.cells[4] == self.cells[2] == player_id:
            return True

    def player_win(self, player_id):
        """
        Check if a player has a three of a kind
        @param player_id:
        @return: True if yes, False if not
        """
        if self.is_any_diagonal_complete(player_id) or self.is_any_row_complete(player_id) or self.is_any_column_complete(player_id):
            return self

    #     def display(self):
    #         """
    #         Print the current board
    #         """
    #         print('---------')
    #         for row in self.cells:
    #             print('| ', end='')
    #             print(' '.join(row), end='')
    #             print(' |')
    #         print('---------')
    #
    #     def get_first_player(self):
    #         global player
    #         while True:
    #             try:
    #                 player = input('Enter who plays first, X or O: > ')
    #                 player = player.upper()
    #                 if re.match("^[XO]$", player):
    #                     break
    #                 print('Please enter either an X or an O')
    #             except ValueError as error:
    #                 print(error)
    #                 continue
    #         return player
    #
    #     def input_move(self):
    #         """
    #         Get the next move
    #         """
    #         while True:
    #             try:
    #                 x, y = [int(a) for a in input("Enter the coordinates (eg. 1 3): > ").split()]
    #             except ValueError:
    #                 print("You should enter numbers!")
    #                 continue
    #             if not isinstance(x, int) or not isinstance(y, int):
    #                 print("You should enter numbers!")
    #                 continue
    #             if x > 3 or y > 3 or x < 1 or y < 1:
    #                 print("Coordinates should be from 1 to 3!")
    #                 continue
    #             if self.cells[3 - y][x - 1] != "_":
    #                 print("This cell is occupied! Choose another one!")
    #                 continue
    #             else:
    #                 self.cells[3 - y][x - 1] = self.player
    #                 break
    #
    #     def board_status(self):
    #         """
    #         Get current game state
    #         @return: current board status
    #         """
    #         return [self.cells[x][y] for x in range(3) for y in range(3)]
    #
    #     def status_check(self):
    #         board = self.board_status()
    #         total_o = len([element for element in board if element == "O"])
    #         total_x = len([element for element in board if element == "X"])
    #
    #         if not (-1 <= (total_o - total_x) <= 1):
    #             return "Impossible"
    #         if self.player_status("X") and self.player_status("O"):
    #             return "Impossible"
    #         if self.player_status("X"):
    #             return "X wins"
    #         if self.player_status("O"):
    #             return "O wins"
    #         if len([element for element in board if element == "_"]) == 0:
    #             return "Draw"
    #         return "Game not finished"


class TictactoeMove:
    """
    Concrete class for handling moves
    """
    def __init__(self, init_player_id, init_move_cell):
        self.player_id = str(init_player_id)
        self.move_cell = int(init_move_cell)

    def get_player_id(self):
        return self.player_id

    def get_move_cell(self):
        return self.move_cell

