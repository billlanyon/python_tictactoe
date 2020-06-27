from unittest import mock
from com.bl.ttt.tictactoe import Tictactoe, TictactoeMove
from com.bl.ttt.main import get_first_move


def test_01_main_get_first_move_valid_input_player_x():
    with mock.patch('builtins.input', side_effect=['X 0']):
        g = Tictactoe()
        get_first_move(g)
        assert g.player1 == 'X'
        assert g.player2 == 'O'


def test_02_main_get_first_move_valid_input_player_y():
    with mock.patch('builtins.input', side_effect=['O 7']):
        g = Tictactoe()
        get_first_move(g)
        assert g.player1 == 'O'
        assert g.player2 == 'X'


def test_03_main_get_first_move_valid_input_move():
    with mock.patch('builtins.input', side_effect=['O 7']):
        g = Tictactoe()
        get_first_move(g)
        assert g.player1 == 'O'
        assert g.player2 == 'X'
