from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove

# Run the game in a loop until a player has won or there is a draw.
while True:
    try:
        new_game = str(input("Would you like to start a new game? Please enter 'y' or 'n': "))
        if new_game == 'y':
            # Instantiate the game
            g = Tictactoe()
            # Display the board state
            print(g)
            # Ask for the player_id who will play first
            first_player = str(input("Who will play first? Enter 'X' or 'O' (that is a capital O, not a zero): "))
            # Ask for the first player move
            first_player_move = int(input(f'{first_player} enter a coordinate to play from 0 to 8: '))
            # Create a TicTacToeMove with player input
            m = TictactoeMove(first_player, first_player_move)
            # Check that the input is a valid move
            if g.is_valid_move(m):
                # Make the valid move
                g.make_valid_move(m)
                # Check if player has won, or there is a draw: announce it and ask if the players want to play again.
                print(g)
                # Flip players and request move
            else:
                break
        else:
            break
    except (ValueError, TypeError):
        break
