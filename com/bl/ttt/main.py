from bl.ttt import ttt_game

# Instantiate the game instance, which gets the initial board setup from the user
game = ttt_game.Tictactoe()
# Run the game in a loop
while True:
    game.display()
    current_status = game.status_check()
    if current_status == 'Game not finished':
        game.input_move()
        # Flip players between turns
        if game.player == "X":
            game.player = "O"
        elif game.player == "O":
            game.player = "X"
    else:
        print(current_status)
        break


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