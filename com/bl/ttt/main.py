from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
from random import randrange
import time

game_over = False
player_tries_again = True
get_next_move = True


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


def get_game_type():
    while True:
        try:
            game_type_input = input("What kind of game will you play: enter 'h' for human or 'c' for computer: ").upper()
            if game_type_input is not None and (game_type_input == 'H' or game_type_input == 'C'):
                return game_type_input
            else:
                print('That was an invalid input: please try again.')
                continue
        except (Exception, ValueError):
            break


def get_first_move(game):
    player_id, cell = input('Please enter player X or O, a space, and then a cell from 0 to 8: ').split(' ')
    game.set_player_order(player_id)
    move = TictactoeMove(game.player1, int(cell))
    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {move.player_id}, please try again.')
        return player_tries_again
    game.turn_counter = 1
    return move


def get_computer_move(game):
    while True:
        computer_cell = randrange(9)
        move = TictactoeMove(game.get_player_id(), computer_cell)
        if game.is_valid_move(move):
            game.make_valid_move(move)
            print(f'The computer player is going to play cell {computer_cell}.')
            time.sleep(2)
        else:
            continue
        game.turn_counter += 1
        return get_next_move


def get_human_move(game):
    while True:
        human_cell = input(f'Player {game.get_player_id()}: please enter a cell from 0 to 8: ')
        move = TictactoeMove(game.get_player_id(), int(human_cell))
        if game.is_valid_move(move):
            game.make_valid_move(move)
        else:
            print(f'Sorry, that is not a valid move for Player {move.player_id}, please try again.')
            continue
        game.turn_counter += 1
        return get_next_move


def process_another_move(game):
    game.turn_counter += 1
    print(f'GP1: {game.player1} | GP2: {game.player2} | GPID: {game.get_player_id()} | GTC: {game.turn_counter} | GICG: {game.is_computer_game}')
    if game.get_computer_game() is True and game.get_turn_count() % 2 == 0:
        get_computer_move(game)
    else:
        get_human_move(game)
    if game.has_won(game.get_player_id()):
        print(game)
        print(f'Player {game.get_player_id()} has won.')
        return game_over
    elif game.is_draw():
        print(game)
        print(f'This game is over: it is a draw and neither player has won.')
        return game_over
    else:
        return get_next_move


def process_player_turns(game):
    get_first_move(game)
    print(game)
    while process_another_move(game):
        print(game)


def main():
    while True:
        if get_game_start() != 'Y':
            print('Thanks for playing and goodbye.')
            return game_over
        game = Tictactoe()
        if get_game_type() == 'C':
            game.set_computer_game()
            print('OK, you will play first and the computer will play second.')
        print("""The board coordinates are:

    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |
    """)
        process_player_turns(game)


if __name__ == "__main__":
    main()
