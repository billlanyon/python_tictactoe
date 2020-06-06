import re

class Tictactoe:
    """
    Concrete class for instantiating specific games based on a single list of nine position strings.
    """
    def __init__(self):
        self.cells = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def board(self):
        """
        0	1	2
        3	4	5
        6	7	8
        Return a board status visualisation
        """
        print('–––––––––')
        print(f'| {self.cells[0]} {self.cells[1]} {self.cells[2]} |')
        print(f'| {self.cells[3]} {self.cells[4]} {self.cells[5]} |')
        print(f'| {self.cells[6]} {self.cells[7]} {self.cells[8]} |')
        print('–––––––––')


class Game:
    """
    This class attempts to manage games for ttt_main.py
    Game class attributes: Are there any?
    Game instance attributes: variety (eg. human vs human); first player; start; moves; end; initial_board; outcome;
    """
    def __init__(self):
        # self.variety = variety
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        # while True:
        #     try:
        #         self.initial_setup = input('Enter cells: > ')
        #         if re.match("^[XO_]*$", self.initial_setup) and len(self.initial_setup) == 9:
        #             break
        #         print('Please enter a 9 character string containing only X, O or _')
        #     except ValueError as error:
        #         print(error)
        #         continue
        # while True:
        #     try:
        #         self.player = input('Enter who plays first, X or O: > ')
        #         self.player = self.player.upper()
        #         if re.match("^[XO]$", self.player):
        #             break
        #         print('Please enter either an X or an O')
        #     except ValueError as error:
        #         print(error)
        #         continue
        # self.player = self.player.upper()
        # for x in range(3):
        #     for y in range(3):
        #         self.board[x][y] = self.initial_setup[x * 3 + y]

    def display(self):
        """
        Print the current board
        """
        print('---------')
        for row in self.board:
            print('| ', end='')
            print(' '.join(row), end='')
            print(' |')
        print('---------')

    def get_first_player(self):
        global player
        while True:
            try:
                player = input('Enter who plays first, X or O: > ')
                player = player.upper()
                if re.match("^[XO]$", player):
                    break
                print('Please enter either an X or an O')
            except ValueError as error:
                print(error)
                continue
        return player

    def input_move(self):
        """
        Get the next move
        """
        while True:
            try:
                x, y = [int(a) for a in input("Enter the coordinates (eg. 1 3): > ").split()]
            except ValueError:
                print("You should enter numbers!")
                continue
            if not isinstance(x, int) or not isinstance(y, int):
                print("You should enter numbers!")
                continue
            if x > 3 or y > 3 or x < 1 or y < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            if self.board[3 - y][x - 1] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                self.board[3 - y][x - 1] = self.player
                break

    def board_status(self):
        """
        Get current game state
        @return: current board status
        """
        return [self.board[x][y] for x in range(3) for y in range(3)]

    # Single game status testing function?
    def is_any_row_complete(self, player):
        """
        Check for three of a kind in the rows
        @param player:
        @return: True if yes
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True

    def is_any_column_complete(self, player):
        """
        Check for three of a kind in columns
        @param player:
        @return: True if yes
        """
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

    def is_any_diagonal_complete(self, player):
        """
        Check for three of a kind in diagonals
        @param player:
        @return: True if yes
        """
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player \
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

    def player_status(self, player):
        """
        Check if a player has a three of a kind
        @param player:
        @return: True if yes, False if not
        """
        if self.is_any_diagonal_complete(player) or self.is_any_row_complete(player) or self.is_any_column_complete(player):
            return True

    def status_check(self):
        board = self.board_status()
        total_o = len([element for element in board if element == "O"])
        total_x = len([element for element in board if element == "X"])

        if not (-1 <= (total_o - total_x) <= 1):
            return "Impossible"
        if self.player_status("X") and self.player_status("O"):
            return "Impossible"
        if self.player_status("X"):
            return "X wins"
        if self.player_status("O"):
            return "O wins"
        if len([element for element in board if element == "_"]) == 0:
            return "Draw"
        return "Game not finished"
