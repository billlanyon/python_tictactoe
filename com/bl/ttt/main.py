from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
import re

game_over = False
player_retakes_move = True
get_next_move = True


def process_another_move(game):
    player_id, cell = input("Please enter player 'X' or 'O' and select a cell to play from 0 to 8: ").split(' ')
    move = TictactoeMove(player_id, int(cell))
    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {player_id}, please try again.')
        return player_retakes_move
    if game.has_won(player_id):
        print(game)
        print(f'Player {player_id} has won.')
        return game_over
    elif game.is_draw():
        print(game)
        print(f'This game is over: it is a draw and neither player has won.')
        return game_over
    else:
        return get_next_move


def process_player_turns(game):
    while process_another_move(game):
        print(game)


def main():
    while True:
        if input("Would you like to start a new game of Tic Tac Toe? Please enter 'y' or 'n': ") != 'y':
            print('Thanks for playing and goodbye.')
            return game_over
        game = Tictactoe()
        print("""The board coordinates are:

    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |
    """)
        process_player_turns(game)


if __name__ == "__main__":
    main()
