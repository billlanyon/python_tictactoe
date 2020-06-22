from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove

game_over = False
player_tries_again = True
get_next_move = True


def process_another_move(game):
    player_id, cell = input('Please enter player X or O, a space, and then a cell from 0 to 8: ').split(' ')
    move = TictactoeMove(player_id, int(cell))
    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {player_id}, please try again.')
        return player_tries_again
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


def get_game_start():
    while True:
        try:
            new_game_input = input("Would you like to start a game of Tic Tac Toe? Please enter 'y' or 'n': ").upper()
            if new_game_input is not None and (new_game_input == 'N' or new_game_input == 'Y'):
                return new_game_input
            else:
                print('That was an invalid input: please try again.')
                continue
        except (Exception, ValueError):
            break


def main():
    while True:
        if get_game_start() != 'Y':
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
