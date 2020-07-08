from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove

game_over = False
player_tries_again = True
get_next_move = True


def main():
    while True:
        if get_game_start() != 'Y':
            print('Thanks for playing and goodbye.')
            return game_over

        if get_game_type() == 'C':
            game = Tictactoe(is_computer_game=True)
            print('OK, you will play first as Player X, and the computer will play second.')
        else:
            game = Tictactoe()
            print('Player X will play first')
        print(game.initial_coordinates())
        process_player_turns(game)


def get_user_input(prompt, valid_input):
    while True:
        try:
            i = input(prompt).upper()
            if i is not None and i in valid_input:
                return i
            else:
                print('That was an invalid input: please try again.')
                continue
        except (Exception, ValueError):
            break


def get_game_start():
    return get_user_input("Would you like to start a game of Tic Tac Toe? Please enter 'y' or 'n': ", ['Y', 'N'])


def get_game_type():
    return get_user_input("What kind of game will you play: enter 'h' for human or 'c' for computer: ", ['H', 'C'])


def get_human_move(game):
    while True:
        cell = input(f'Player {game.get_turn_player()}: please enter a cell from 0 to 8: ')
        move = TictactoeMove(game.get_turn_player(), int(cell))
        if game.is_valid_move(move):
            game.process_valid_move(move)
        else:
            print(f'Sorry, that is not a valid move for Player {game.get_turn_player()}, please try again.')
            continue
        return get_next_move


def process_another_move(game):
    if game.get_computer_game() is True and game.get_turn_counter() % 2 == 0:
        game.get_computer_move()
    else:
        get_human_move(game)
    if game.has_won('X') or game.has_won('O'):
        game.get_game_status()
        print(f'Player {game.get_previous_turn_player()} has won.')
        return game_over
    elif game.is_draw():
        game.get_game_status()
        print(f'This game is over: it is a draw and neither player has won.')
        return game_over
    else:
        return get_next_move


def process_player_turns(game):
    while process_another_move(game):
        game.get_game_status()


if __name__ == "__main__":
    main()
