from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_process_another_move_valid_move():
    game = Tictactoe()
    with mock.patch('builtins.input', side_effect=['X 0']):
        process_another_move(game)
        assert game.cells[0] == 'X'


def test_02_main_process_another_move_valid_move():
    game = Tictactoe()
    with mock.patch('builtins.input', side_effect=['O 8']):
        process_another_move(game)
        assert game.cells[8] == 'O'
