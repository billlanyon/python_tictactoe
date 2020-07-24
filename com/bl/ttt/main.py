#!/usr/bin/env python3
from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
import logging
import logging.config
import os

game_over = False
player_tries_again = True
get_next_move = True
logger = logging.getLogger(__name__)


def set_logging_from_config_file():
    config_file = os.path.join(os.path.dirname(__file__), 'log.conf')
    logging.config.fileConfig(fname=config_file, disable_existing_loggers=False)


def main():
    set_logging_from_config_file()
    while True:
        if get_game_start() != 'Y':
            print('Thanks for playing and goodbye.')
            return game_over

        if get_game_type() == 'C':
            game = Tictactoe(is_computer_game=True)
            print('OK, you will play first as Player X, and the computer will play second as Player O.')
        else:
            game = Tictactoe()
            print('Player X will play first.')
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
        except (Exception, ValueError) as e:
            logger.error(e, exc_info=True)
            break


def get_game_start():
    return get_user_input("Would you like to start a game of Tic Tac Toe? Please enter 'y' or 'n': ", ['Y', 'N'])


def get_game_type():
    return get_user_input("What kind of game will you play: enter 'h' for human or 'c' for computer: ", ['H', 'C'])


def process_player_turns(game):
    while process_another_move(game):
        game.get_game_status()


def process_another_move(game):
    while True:
        try:
            cell = input(f'Player {game.get_turn_player()}: please enter a cell from 0 to 8: ')
            move = TictactoeMove(game.get_turn_player(), int(cell))
            logger.debug(f'process_another_move constructed: {move.__str__()}')
            if game.is_valid_move(move):
                game.process_valid_move(move)
            else:
                print(f'Sorry, that is not a valid move for Player {game.get_turn_player()}, please try again.')
                continue
        except ValueError as e:
            logger.error(e, exc_info=True)

        if game.is_game_over():
            game.get_game_status()
            print(game.inform_game_over())
            return game_over
        else:
            return get_next_move


if __name__ == "__main__":
    main()
