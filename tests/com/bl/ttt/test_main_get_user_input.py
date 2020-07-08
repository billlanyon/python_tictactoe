from unittest import mock
from com.bl.ttt.main import get_user_input, get_game_start, game_over
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_get_user_input_invalid_input(capsys):
    with mock.patch('builtins.input', side_effect=['dd']):
        get_user_input('bla', ['Y', 'N'])
        out, err = capsys.readouterr()
        assert out == 'That was an invalid input: please try again.\n'
