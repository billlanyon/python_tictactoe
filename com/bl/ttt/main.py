from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
import time

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
            print('OK, you will play first and the computer will play second.')
        else:
            game = Tictactoe()
        print(game.initial_coordinates())
        process_player_turns(game)


def get_first_move(game):
    first_player_id, cell = input('Please enter player X or O, a space, and then a cell from 0 to 8: ').split(' ')
    move = TictactoeMove(first_player_id, int(cell))
    if game.is_valid_move(move):
        game.process_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {move.player_id}, please try again.')
        return player_tries_again
    game.set_player_ids(first_player_id)
    return get_next_move


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
        human_cell = input(f'Player {game.get_turn_player()}: please enter a cell from 0 to 8: ')
        move = TictactoeMove(game.get_turn_player(), int(human_cell))
        if game.is_valid_move(move):
            game.process_valid_move(move)
        else:
            print(f'Sorry, that is not a valid move for Player {game.get_turn_player()}, please try again.')
            continue
        return get_next_move


def process_another_move(game):
    if game.get_computer_game() is True and game.get_turn_counter() % 2 == 0:
        time.sleep(2)
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
    get_first_move(game)
    game.get_game_status()
    game.get_computer_status()
    while process_another_move(game):
        game.get_game_status()
        game.get_computer_status()


if __name__ == "__main__":
    main()
