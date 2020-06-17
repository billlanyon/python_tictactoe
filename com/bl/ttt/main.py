from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
import re


# Run the game in a loop until a player has won or there is a draw.
while True:
    try:
        new_game_input = str(input("Would you like to start a new game? Please enter 'y' or 'n': "))
        if new_game_input is not None and re.match("^[yn]$", new_game_input):
            new_game = new_game_input
        else:
            print("Please enter either a valid 'y' or a valid 'n'.")
            continue
    except (ValueError, TypeError):
        break
    if new_game == 'y':
        # Instantiate the game
        g = Tictactoe()
        try:
            # Ask for the player_id who will play first
            player_one_input = str(input("Who will play first? Enter 'X' or 'O' (that is a capital O, not a zero): "))
            if player_one_input is not None and re.match("^[XO]$", player_one_input):
                player_one = player_one_input
            else:
                print("Please enter either a valid 'X' or a valid 'O'.")
                break
        except (ValueError, TypeError):
            break
        # Display the board state
        print(g)
        players = ['X', 'O']
        if player_one == 'X':
            turn = 0
        else:
            turn = 1
        while True:
            # Flip player
            player = players[turn]
            try:
                # Ask for the player_two move
                player_move_cell = input(f'Player {player} enter a coordinate to play from 0 to 8: ')
                if player_move_cell is not None and re.match("^[0-8]{1}$", player_move_cell):
                    player_move_cell = int(player_move_cell)
                else:
                    print(f'Player {player} please enter a valid coordinate from 0 to 8!')
                    continue
            except (ValueError, TypeError):
                break
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
                    # Increment turn
                    turn = (turn + 1) % len(players)
                    continue
            else:
                print('That is an invalid move: please try again.')
    else:
        print('Thanks for playing and goodbye.')
        break
