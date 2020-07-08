import pytest
from unittest import mock
from com.bl.ttt.main import main
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_main_exits_game(capsys):
    with mock.patch('builtins.input', side_effect=['n']):
        main()
        out, err = capsys.readouterr()
        assert out == 'Thanks for playing and goodbye.\n'


def test_02_main_main_starts_game():
    main()
    game = Tictactoe()
    with mock.patch('builtins.input', side_effect=['y']):
        assert game.cells == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']