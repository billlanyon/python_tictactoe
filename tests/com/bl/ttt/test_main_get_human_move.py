from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_get_human_move():
    g = Tictactoe()
    g._turn_counter = 1
    with mock.patch('builtins.input', side_effect=['0 0']):
        process_another_move(g)
        assert g._cells == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
