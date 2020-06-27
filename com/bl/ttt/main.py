from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
from random import randrange

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
    game.player1 = player_id
    if game.player1 == 'X':
        game.player2 = 'O'
    else:
        game.player2 = 'X'
    move = TictactoeMove(player_id, int(cell))
    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {move.player_id}, please try again.')
        return player_tries_again
    game.turn_player = player_id
    game.turn_counter = 1
    return move


def process_another_move(game):
    game.turn_counter += 1
    if game.turn_player == 'X':
        game.turn_player = 'O'
    else:
        game.turn_player = 'X'
    player_id = game.turn_player
    print(f'GP1: {game.player1}. GP2: {game.player2}. GTP: {game.turn_player}. GCP: {game.computer_player}. GTC: {game.turn_counter}.')
    if game.computer_player is not None and game.turn_counter % 2 == 0:
        while True:
            computer_move = randrange(9)
            if game.cells[computer_move] == ' ':
                cell = computer_move
                print(f'The computer player {game.player2} played cell {computer_move}.')
            else:
                continue
            break
    else:
        cell = input(f'Player {player_id} please enter a cell from 0 to 8: ')
    move = TictactoeMove(player_id, int(cell))
    if game.is_valid_move(move):
        game.make_valid_move(move)
    else:
        print(f'Sorry, that is not a valid move for Player {move.player_id}, please try again.')
        return player_tries_again
    if game.has_won(move.player_id):
        print(game)
        print(f'Player {move.player_id} has won.')
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
            game.computer_player = 2
        print("""The board coordinates are:

    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |
    """)
        process_player_turns(game)


if __name__ == "__main__":
    main()
