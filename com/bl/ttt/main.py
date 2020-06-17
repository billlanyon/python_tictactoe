from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove

# Run the game in a loop until a player has won or there is a draw.
while True:
    new_game = str(input("Would you like to start a new game? Please enter 'y' or 'n': "))
    if new_game == 'y':
        # Instantiate the game
        g = Tictactoe()
        # Ask for the player_id who will play first
        player_one = str(input("Who will play first? Enter 'X' or 'O' (that is a capital O, not a zero): "))
        # Display the board state
        print(g)
        # Ask for the first player move
        player_one_move_cell = int(input(f'Player {player_one} enter a coordinate to play from 0 to 8: '))
        # Create a TicTacToeMove with player input
        first_move = TictactoeMove(player_one, player_one_move_cell)
        # Check that first move is valid
        if g.is_valid_move(first_move):
            # Make the first valid move
            g.make_valid_move(first_move)
            print(g)
            # Set the second player
            players = ['X', 'O']
            if player_one == 'X':
                turn = 1
            else:
                turn = 0
            while True:
                # Flip player
                player = players[turn]
                turn = (turn + 1) % len(players)
                # Ask for the player_two move
                player_move_cell = int(input(f'Player {player} enter a coordinate to play from 0 to 8: '))
                # Create a TicTacToeMove with player input
                move = TictactoeMove(player, player_move_cell)
                # Check that move is valid
                if g.is_valid_move(move):
                    g.make_valid_move(move)
                    # Check if player has won
                    if g.has_won(player):
                        print(g)
                        print(f'Player {move.player_id} has won.')
                        break
                    # Check if there is a draw
                    elif g.is_draw():
                        print(g)
                        print('This game is over: it is a draw.')
                        break
                    else:
                        print(g)
                        continue
                else:
                    print('That is an invalid move: please try again.')
        else:
            print('That is an invalid first move: please try again.')
    else:
        print('Thanks for playing and goodbye.')
        break
