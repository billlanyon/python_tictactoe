from unittest import mock
from com.bl.ttt.main import process_another_move
from com.bl.ttt.tictactoe import Tictactoe


def test_01_main_process_another_move_valid_move():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=[0]):
        process_another_move(g)
        process_another_move.player_id = 'X'
        assert g.cells[0] == 'X'


def test_02_main_process_another_move_valid_move():
    g = Tictactoe()
    with mock.patch('builtins.input', side_effect=[8]):
        process_another_move(g)
        process_another_move.player_id = 'O'
        assert not g.cells[8] == 'O'

