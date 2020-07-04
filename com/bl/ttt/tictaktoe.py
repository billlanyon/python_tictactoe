from com.bl.ttt.tictactoegame import TictactoeGame, TictactoeMove

continue_game = False


def main():
    while True:
        if play_another_game() != 'Y':
            print('Thanks for playing and goodbye.')
            break
        if get_opponent_type() == 'C':
            game = TictactoeGame(True)
            print('OK, you will play first and the computer will play second.')
        else:
            game = TictactoeGame()

        print(game.initial_board_layout())

        play_the_game(game)
        display_outcome(game)


def play_another_game():
    return get_input("Would you like to start a game of Tic Tac Toe? Please enter 'y' or 'n': ",
                     valid_responses=['Y', 'N'])


def get_opponent_type():
    return get_input("What kind of game will you play: enter 'h' for human or 'c' for computer: ",
                     valid_responses=['H', 'C'])


def get_input(prompt, valid_responses):
    while True:
        try:
            i = input(prompt).upper()
            if i in valid_responses:
                return i
            else:
                print('That was an invalid input: please try again.\n')
                continue
        except (Exception, ValueError):
            print('That was an invalid input: please try again.\n')
            continue


def play_the_game(game):
    print(game)
    while not game.is_game_over():
        process_another_move(game)
        print(game)


def process_another_move(game):
    current_player_id = game.get_turn_player_id()
    cell = input(f'Player {current_player_id}: please enter a cell from 0 to 8: ')
    move = TictactoeMove(current_player_id, int(cell))

    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {current_player_id}, please try again.')


def display_outcome(game):
    winner = game.get_winner_player_id()
    if not winner:
        print('Game Over - DRAW\n\n')
    else:
        print(f'Game Over - Player {game.get_winner_player_id()} WINS.\n\n')


if __name__ == "__main__":
    main()
