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
        except (Exception, ValueError):
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
        cell = input(f'Player {game.get_turn_player()}: please enter a cell from 0 to 8: ')
        move = TictactoeMove(game.get_turn_player(), int(cell))
        if game.is_valid_move(move):
            game.process_valid_move(move)
        else:
            print(f'Sorry, that is not a valid move for Player {game.get_turn_player()}, please try again.')
            continue

        if game.is_game_over():
            game.get_game_status()
            print(game.inform_game_over())
            return game_over
        else:
            if game.get_computer_game() and game.is_computer_turn():
                game.get_computer_move()
                game.get_game_status()
                return get_next_move
        return get_next_move


if __name__ == "__main__":
    main()
