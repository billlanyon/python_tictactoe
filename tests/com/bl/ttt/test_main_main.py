from unittest import mock
from com.bl.ttt.tictaktoe import main


def test_01_main_main_exits_game(capsys):
    with mock.patch('builtins.input', side_effect=['n']):
        main()
        out, err = capsys.readouterr()
        assert out == 'Thanks for playing and goodbye.\n'
